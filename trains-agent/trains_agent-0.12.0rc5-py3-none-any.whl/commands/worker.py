from __future__ import print_function, division, unicode_literals

import errno
import json
import logging
import os.path
import re
import signal
import subprocess
import sys
import shutil
import traceback
from collections import defaultdict
from copy import copy, deepcopy
from datetime import datetime
from distutils.spawn import find_executable
from functools import partial
from itertools import chain
from os import environ, getpid
from tempfile import gettempdir, mkdtemp
from time import sleep, time
from typing import Text, Optional, Any, Tuple

import attr
import psutil
import six
from trains_agent.backend_api.services import queues as queues_api
from trains_agent.backend_api.services import tasks as tasks_api
from pathlib2 import Path
from pyhocon import ConfigTree, ConfigFactory
from requests import Session as HTTPSession
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from six.moves.urllib.parse import quote

from trains_agent.helper.check_update import start_check_update_daemon
from trains_agent.commands.base import resolve_names, ServiceCommandSection
from trains_agent.definitions import (
    WORKER_ALREADY_REGISTERED,
    ENVIRONMENT_SDK_PARAMS,
    INVALID_WORKER_ID,
    PROGRAM_NAME,
    DEFAULT_VENV_UPDATE_URL)
from trains_agent.definitions import WORKING_REPOSITORY_DIR, PIP_EXTRA_INDICES
from trains_agent.errors import APIError, CommandFailedError, Sigterm
from trains_agent.helper.base import (
    return_list,
    print_parameters,
    dump_yaml,
    warning,
    normalize_path,
    check_directory_path,
    select_for_platform,
    mkstemp as safe_mkstemp,
    print_table,
    safe_remove_file,
    is_windows_platform,
    rm_tree,
    is_conda,
    named_temporary_file,
    ExecutionInfo,
    HOCONEncoder, error)
from trains_agent.helper.console import ensure_text
from trains_agent.helper.package.base import PackageManager
from trains_agent.helper.package.conda_api import CondaAPI
from trains_agent.helper.package.horovod_req import HorovodRequirement
from trains_agent.helper.package.pip_api.system import SystemPip
from trains_agent.helper.package.pip_api.venv import VirtualenvPip
from trains_agent.helper.package.poetry_api import PoetryConfig, PoetryAPI
from trains_agent.helper.package.pytorch import PytorchRequirement
from trains_agent.helper.package.requirements import RequirementsManager
from trains_agent.helper.package.venv_update_api import VenvUpdateAPI
from trains_agent.helper.process import (
    kill_all_child_processes,
    check_if_command_exists,
    WorkerParams,
    ExitStatus,
    Argv,
    COMMAND_SUCCESS,
    Executable,
    get_bash_output)
from trains_agent.helper.package.cython_req import CythonRequirement
from trains_agent.helper.repo import clone_repository_cached, RepoInfo, VCS
from trains_agent.helper.resource_monitor import ResourceMonitor
from trains_agent.session import Session
from trains_agent.helper.singleton import Singleton

from .events import Events

log = logging.getLogger(__name__)


@attr.s
class LiteralScriptManager(object):
    """
    Manage notebook tasks
    """

    venv_folder = attr.ib(type=str)

    @staticmethod
    def is_literal_script(task):
        # type: (tasks_api.Task) -> bool
        """
        Returns whether a task object represents a notebook task
        """
        script = task.script
        if not script:
            return False
        diff = script.diff
        return diff and not diff.strip().lower().startswith("diff ")

    @staticmethod
    def write(task, directory, entry_point=None):
        # type: (tasks_api.Task, str, Optional[str]) -> str
        """
        Create notebook file for ``task`` in ``directory``
        """
        if entry_point:
            full_path = normalize_path(Text(directory), entry_point)
            if os.path.exists(full_path):
                return entry_point

            with open(full_path, "wt") as f:
                f.write(task.script.diff)
                return full_path

        with named_temporary_file(
            delete=False, prefix="script_", suffix=".py", dir=Text(directory), mode="wt"
        ) as f:
            f.write(task.script.diff)
            return f.name

    def create_notebook_file(self, task, execution, repo_info):
        # type: (tasks_api.Task, ExecutionInfo, Optional[RepoInfo]) -> Tuple[str, str]
        """
        Create notebook file in appropriate location
        :return: directory and script path
        """
        if repo_info and repo_info.root:
            location = Path(repo_info.root, execution.working_dir)
        else:
            if execution.working_dir:
                log.warning(
                    "found task with `script.working_dir` (`%s`) but without `script.repository`, ignoring",
                    execution.working_dir,
                )
            location = None
        location = location or (repo_info and repo_info.root)
        if not location:
            location = Path(self.venv_folder, "code")
            location.mkdir(exist_ok=True)
        log.debug("selected execution directory: %s", location)
        return Text(location), self.write(task, location, execution.entry_point)


def get_repo_auth_string(user, password):
    # type: (Text, Text) -> Text
    """
    Return user:password only if user and password are valid
    :param user: username
    :param password:
    :return: URL authentication string
    """
    if not (user and password):
        return ""
    return ":".join(map(quote, (user, password)))


CONCAT_CMD = select_for_platform(linux=" && ", windows=" & ")


class TaskStopReason(object):
    no_stop = 0         # type: TaskStopReason
    stopped = 1         # type: TaskStopReason
    reset = 2           # type: TaskStopReason
    status_changed = 3  # type: TaskStopReason


def get_task(session, task_id, *args, **kwargs):
    return session.api_client.tasks.get_all(id=[task_id], *args, **kwargs)[0]


class TaskStopSignal(object):
    """
    Follow task status and signals when it should be stopped
    """

    _number_of_consecutive_reset_tests = 4
    statuses = tasks_api.TaskStatusEnum
    unexpected_statuses = [
        statuses.closed,
        statuses.stopped,
        statuses.failed,
        statuses.published,
    ]
    default = TaskStopReason.no_stop
    stopping_message = "stopping"

    def __init__(self, command, session, events_service, task_id):
        # type: (Worker, Session, Events, Text) -> ()
        """
        :param command: workers command
        :param session: command session
        :param events_service: events service object
        :param task_id: followed task ID
        """
        self.command = command
        self.session = session
        self.events_service = events_service
        self.worker_id = command.worker_id
        self._task_reset_state_counter = 0
        self.task_id = task_id

    def test(self):
        # type: () -> TaskStopReason
        """
        Returns whether task should stop and for what reason,
        returns TaskStopReason.no_stop if task shouldn't stop.
        Catches and logs exceptions.
        """
        try:
            return self._test()
        except Exception as ex:
            self.command.log_traceback(ex)

    def _test(self):
        # type: () -> TaskStopReason
        """
        "Unsafe" version of test()
        """
        task_info = get_task(
            self.session, self.task_id, only_fields=["status", "status_message"]
        )
        status = task_info.status
        message = task_info.status_message

        if status == self.statuses.in_progress and self.stopping_message in message:
            self.command.log(
                "task status_message has '%s', task will terminate",
                self.stopping_message,
            )
            return TaskStopReason.stopped

        if status in self.unexpected_statuses and "worker" not in message:
            self.command.log("unexpected status change, task will terminate")
            return TaskStopReason.status_changed

        if status == self.statuses.created:
            if (
                self._task_reset_state_counter
                >= self._number_of_consecutive_reset_tests
            ):
                self.command.log("task was reset, task will terminate")
                return TaskStopReason.reset
            self._task_reset_state_counter += 1
            warning_msg = "Warning: Task {} was reset! if state is consistent we shall terminate ({}/{}).".format(
                self.task_id,
                self._task_reset_state_counter,
                self._number_of_consecutive_reset_tests,
            )
            if self.events_service:
                self.events_service.send_log_events(
                    self.worker_id,
                    task_id=self.task_id,
                    lines=[warning_msg],
                    level="WARNING",
                )
            print(warning_msg)
        else:
            self._task_reset_state_counter = 0

        return TaskStopReason.no_stop


class Worker(ServiceCommandSection):
    _pip_extra_index_url = PIP_EXTRA_INDICES

    _default_pip = tuple()

    _requirement_substitutions = (
        PytorchRequirement,
        CythonRequirement,
        HorovodRequirement,
    )

    # poll queues every _polling_interval seconds
    _polling_interval = 5.0
    # machine status update intervals, seconds
    _machine_update_interval = 30.0

    @property
    def service(self):
        """ Worker command service endpoint """
        return "workers"

    @property
    def _task_status_change_message(self):
        return "Changed by {} {}".format(PROGRAM_NAME, self.worker_id)

    @staticmethod
    def register_signal_handler():
        def handler(*_):
            raise Sigterm()

        signal.signal(signal.SIGTERM, handler)

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.monitor = None
        self.log = self._session.get_logger(__name__)
        self.register_signal_handler()
        self._worker_registered = False
        self.is_conda = is_conda(self._session.config)  # type: bool
        # Add extra index url - system wide
        extra_url = None
        try:
            if self._session.config.get("agent.package_manager.extra_index_url", None):
                extra_url = self._session.config.get("agent.package_manager.extra_index_url", [])
                if not isinstance(extra_url, (tuple, list)):
                    extra_url = [extra_url]
                # put external pip url before default ones, so we first look for packages there
                for e in reversed(extra_url):
                    PIP_EXTRA_INDICES.insert(0, e)
        except Exception:
            self.log.warning('Failed adding extra-index-url to pip environment: {}'.format(extra_url))
        # update pip install command
        pip_install_cmd = ["pip", "install"]
        if self._pip_extra_index_url:
            pip_install_cmd.extend(
                chain.from_iterable(
                    ("--extra-index-url", x) for x in self._pip_extra_index_url
                )
            )
        self.pip_install_cmd = tuple(pip_install_cmd)
        self.worker_id = self._session.config["agent.worker_id"] or "{}:{}".format(
            self._session.config["agent.worker_name"], getpid()
        )
        self._last_stats = defaultdict(lambda: 0)
        self._last_report_timestamp = psutil.time.time()
        self.temp_config_path = None
        self.queues = ()
        self.venv_folder = None  # type: Optional[Text]
        self.package_api = None  # type: PackageManager

        self.is_venv_update = self._session.config.agent.venv_update.enabled
        self.poetry = PoetryConfig(self._session)
        self.poetry.initialize()
        self.docker_image_func = None
        self._docker_image = None
        self._docker_arguments = None
        self._daemon_foreground = None

    def _get_requirements_manager(self, os_override=None, base_interpreter=None):
        requirements_manager = RequirementsManager(
            self._session, base_interpreter=base_interpreter
        )
        for requirement_cls in self._requirement_substitutions:
            if os_override and issubclass(requirement_cls, PytorchRequirement):
                requirement_cls = partial(requirement_cls, os_override=os_override)
            requirements_manager.register(requirement_cls)
        if not requirements_manager.found_cuda:
            self.warning(
                "could not find installed CUDA/CuDNN version using original requirements file"
            )
        return requirements_manager

    def handle_user_abort(self, task_id):
        """
        Set task status to appropriate value on user abort.
        """
        try:
            task_status = self._session.send_api(
                tasks_api.GetByIdRequest(task_id)
            ).task.status
            if task_status == tasks_api.TaskStatusEnum.in_progress:
                print("\nUser abort - stopping task {}".format(task_id))
                self._session.send_api(tasks_api.StoppedRequest(task_id))
        except Exception:
            pass

    def run_one_task(self, queue, task_id, worker_args):
        # type: (Text, Text, WorkerParams) -> ()
        """
        Run one task pulled from queue.
        :param queue: ID of queue that task was pulled from
        :param task_id: ID of task to run
        :param worker_args: Worker command line arguments
        """
        # start new process and execute task id
        print("Running task '{}'".format(task_id))
        # set task status to in_progress so we know it was popped from the queue
        try:
            self._session.send_api(tasks_api.StartedRequest(task=task_id, force=True))
        except Exception:
            print("Warning: Could not start task id '{}', skipping".format(task_id))
            return
        # setup console log
        temp_stdout_name = safe_mkstemp(
            suffix=".txt", prefix=".trains_agent_out.", name_only=True
        )
        # temp_stderr_name = safe_mkstemp(suffix=".txt", prefix=".trains_agent_err.", name_only=True)
        temp_stderr_name = None
        print(
            "Storing stdout and stderr log to '{}', '{}'".format(
                temp_stdout_name, temp_stderr_name or temp_stdout_name
            )
        )

        if self.docker_image_func:
            try:
                response = get_task(self._session, task_id, only_fields=["execution.docker_cmd"])
                task_docker_cmd = response.execution.docker_cmd
                task_docker_cmd = task_docker_cmd.strip() if task_docker_cmd else None
            except Exception:
                task_docker_cmd = None

            if task_docker_cmd:
                self.send_logs(task_id=task_id,
                               lines=['Running Task {} inside docker: {}\n'.format(task_id, task_docker_cmd)],
                               level="INFO")
                task_docker_cmd = task_docker_cmd.split(' ')
                full_docker_cmd = self.docker_image_func(docker_image=task_docker_cmd[0],
                                                         docker_arguments=task_docker_cmd[1:])
            else:
                self.send_logs(task_id=task_id,
                               lines=['No docker image specified, running Task {} inside docker: {} {}\n'.format(
                                   task_id, self._docker_image, self._docker_arguments or '')],
                               level="INFO")
                full_docker_cmd = self.docker_image_func(docker_image=self._docker_image,
                                                         docker_arguments=self._docker_arguments)
                # Update docker command
                try:
                    docker_cmd = ' '.join([self._docker_image] + self._docker_arguments)
                    self._session.send_api(
                        tasks_api.EditRequest(task_id, execution=dict(docker_cmd=docker_cmd), force=True))
                except Exception:
                    pass

            full_docker_cmd[-1] = full_docker_cmd[-1] + 'execute --disable-monitoring --id ' + task_id
            cmd = Argv(*full_docker_cmd)
        else:
            cmd = worker_args.get_argv_for_command("execute") + (
                "--disable-monitoring",
                "--id",
                task_id,
            )

        events_service = self.get_service(Events)
        stop_signal = TaskStopSignal(
            command=self,
            session=self._session,
            events_service=events_service,
            task_id=task_id,
        )
        stop_signal_status = TaskStopSignal.default
        status = ExitStatus.failure
        try:
            # set WORKER ID
            os.environ['TRAINS_WORKER_ID'] = self.worker_id
            status, stop_signal_status = self._log_command_output(
                task_id=task_id,
                cmd=cmd,
                stdout_path=temp_stdout_name,
                stderr_path=temp_stderr_name,
                daemon=True,
                stop_signal=stop_signal,
            )
            errors = temp_stderr_name and Path(temp_stderr_name).read_text()
            if errors:
                print("\nEncountered errors:\n\n{}\n".format(errors))
            if status is None:
                print(
                    "DONE: Running task '{}' (user aborted)".format(task_id)
                )
            else:
                print("DONE: Running task '{}', exit status {}".format(task_id, status))
        except KeyboardInterrupt:
            self.handle_user_abort(task_id)
            status = ExitStatus.interrupted
        finally:
            self.handle_task_termination(task_id, status, stop_signal_status)
            # remove temp files after we sent everything to the backend
            safe_remove_file(temp_stdout_name)
            safe_remove_file(temp_stderr_name)

    def run_tasks_loop(self, queues, worker_params):
        """
        :summary: Pull and run tasks from queues.
        :description: 1. Go through ``queues`` by order.
                      2. Try getting the next task for each and run the first one that returns.
                      3. Go to step 1
        :param queues: IDs of queues to pull tasks from
        :type queues: list of ``Text``
        :param worker_params: Worker command line arguments
        :type worker_params: ``trains_agent.helper.process.WorkerParams``
        """

        if not self._daemon_foreground:
            print('Starting infinite task polling loop...')

        _last_machine_update_ts = 0
        while True:

            # iterate over queues (priority style, queues[0] is highest)
            for queue in queues:
                # get next task in queue
                try:
                    response = self._session.send_api(
                        queues_api.GetNextTaskRequest(queue=queue)
                    )
                except Exception as e:
                    print(
                        "Warning: Could not access task queue [{}], error: {}".format(
                            queue, e
                        )
                    )
                    continue
                else:
                    try:
                        task_id = response.entry.task
                    except AttributeError:
                        if self._daemon_foreground or worker_params.debug:
                            print("No tasks in queue {}".format(queue))
                        continue

                    self.send_logs(
                        task_id=task_id,
                        lines=["task {} pulled from {} by worker {}\n".format(task_id, queue, self.worker_id)],
                        level="INFO",
                    )
                    self.report_monitor(ResourceMonitor.StatusReport(queues=queues, queue=queue, task=task_id))
                    self.run_one_task(queue, task_id, worker_params)
                    self.report_monitor(ResourceMonitor.StatusReport(queues=self.queues))
                    break
            else:
                # sleep and retry polling
                if self._daemon_foreground or worker_params.debug:
                    print("No tasks in Queues, sleeping for {:.1f} seconds".format(self._polling_interval))
                sleep(self._polling_interval)

            if self._session.config["agent.reload_config"]:
                self.reload_config()

    def reload_config(self):
        try:
            reloaded = self._session.reload()
        except Exception as ex:
            self.log("Failed reloading config file")
            self.log_traceback(ex)
        else:
            if reloaded:
                self.log(
                    'Config file change detected, reloading and updating "{.temp_config_path}"'.format(
                        self
                    )
                )
                self.dump_config()

    def check(self, **_):
        try:
            check_directory_path(str(Path(".").resolve()))
        except OSError as e:
            if e.errno == errno.ENOENT:
                raise CommandFailedError("current working directory does not exist")
            raise

        for key in "agent.venvs_dir", "sdk.storage.cache.default_base_dir":
            try:
                value = self._session.config.get(key, None)
                if value:
                    check_directory_path(value)
            except CommandFailedError as e:
                raise CommandFailedError(
                    'Invalid config key "{}": {.message}'.format(key, e)
                )

        if is_windows_platform():
            if not self.is_conda:
                self.warning("Worker on Windows without Conda are not supported")
            if self._session.config.agent.venv_update:
                self.warning("venv-update is not supported on Windows")
                self.is_venv_update = False

        self._session.print_configuration()

    @resolve_names
    def daemon(self, queues, log_level, foreground=False, docker=False, **kwargs):
        # make sure we only have a single instance,
        # also make sure we set worker_id properly and cache folders
        self._singleton()

        # check if we have the latest version
        start_check_update_daemon()

        self.check(**kwargs)
        self.log.debug("starting resource monitor thread")
        print("Worker \"{}\" - ".format(self.worker_id), end='')

        if not queues:
            default_queue = self._session.send_api(queues_api.GetDefaultRequest())
            queues = [default_queue.id]

        queues = return_list(queues)
        queues_info = [
            self._session.send_api(
                queues_api.GetByIdRequest(queue)
            ).queue.to_dict()
            for queue in queues
        ]
        columns = ("id", "name", "tags")
        print("Listening to queues:")
        print_table(queues_info, columns=columns, titles=columns)

        # register worker
        self._register(queues)

        # create temp config file with current configuration
        self.temp_config_path = safe_mkstemp(
            suffix=".cfg", prefix=".trains_agent.", text=True, name_only=True
        )

        # print docker image
        if docker is not False and docker is not None:
            temp_config, docker_image_func = self.get_docker_config_cmd(docker)
            self.dump_config(temp_config)
            self.docker_image_func = docker_image_func
        else:
            self.dump_config()

        self._daemon_foreground = foreground
        if not foreground:
            out_file, name = safe_mkstemp(
                prefix=".trains_agent_daemon_out",
                suffix=".txt",
                open_kwargs={
                    "buffering": self._session.config.get("agent.log_files_buffering", 1)
                },
            )
            print(
                "Running TRAINS-AGENT daemon in background mode, writing stdout/stderr to {}".format(
                    name
                )
            )
            sys.stdout = sys.stderr = out_file

        try:
            while True:
                try:
                    self.new_monitor(ResourceMonitor.StatusReport(queues=queues))
                    self.run_tasks_loop(
                        queues,
                        worker_params=WorkerParams(
                            log_level=log_level,
                            config_file=self.temp_config_path,
                            debug=self._session.debug_mode,
                            trace=self._session.trace,
                        ),
                    )
                except Exception:
                    tb = six.text_type(traceback.format_exc())
                    print("FATAL ERROR:")
                    print(tb)
                    crash_file, name = safe_mkstemp(prefix=".trains_agent-crash", suffix=".log")
                    try:
                        with crash_file:
                            crash_file.write(tb)
                    except Exception:
                        print(
                            "Could not write crash log to {}\nException:\n{}".format(
                                name, tb
                            )
                        )
                    sleep(1)
        finally:
            self._unregister(queues)
            safe_remove_file(self.temp_config_path)

    def report_monitor(self, report):
        if not self.monitor:
            self.new_monitor(report=report)
        else:
            self.monitor.set_report(report)
        self.monitor.send_report()

    def stop_monitor(self):
        if self.monitor:
            self.monitor.stop()
            self.monitor = None

    def new_monitor(self, report=None):
        self.stop_monitor()
        self.monitor = ResourceMonitor(
            session=self._session, worker_id=self.worker_id,
            first_report_sec=3.0,
            report_frequency_sec=self._machine_update_interval)
        self.monitor.set_report(report)
        self.monitor.start()
        return self.monitor

    def dump_config(self, config=None):
        def to_json(config):
            return json.dumps(config.as_plain_ordered_dict(), cls=HOCONEncoder, indent=4)
        Path(self.temp_config_path).write_text(six.text_type(self._session.to_json()
                                                             if config is None else to_json(config)))

    def _log_command_output(
        self,
        task_id,  # type: Text
        cmd,  # type: Executable
        stdout_path=None,  # type: Text
        stderr_path=None,  # type: Optional[Text]
        daemon=False,  # type: bool
        cwd=None,  # type: Text
        stop_signal=None,  # type: Optional[TaskStopSignal]
        **kwargs  # type: Any
    ):
        # type: (...) -> Tuple[Optional[int], TaskStopReason]
        def _print_file(file_path, prev_line_count):
            with open(file_path, "rt") as f:
                # skip the previously printed lines,
                return f.readlines()[prev_line_count:]

        stdout = open(stdout_path, "wt")
        stderr = open(stderr_path, "wt") if stderr_path else stdout
        try:
            stdout_line_count, stdout_last_lines = 0, []
            stderr_line_count, stderr_last_lines = 0, []
            status = None
            stopping = False
            _last_machine_update_ts = time()
            stop_reason = None

            process = cmd.call_subprocess(
                subprocess.Popen,
                stdout=stdout,
                stderr=stderr,
                cwd=cwd and str(cwd),
                **kwargs
            )

            while status is None and not stopping:

                stop_reason = stop_signal.test() if stop_signal else TaskStopSignal.default
                if stop_reason != TaskStopSignal.default:
                    # mark quit loop
                    stopping = True
                    if daemon:
                        self.send_logs(
                            task_id=task_id,
                            lines=["User aborted: stopping task\n"],
                            level="ERROR",
                        )
                        kill_all_child_processes(process.pid)
                else:
                    sleep(self._polling_interval)
                    status = process.poll()
                # flush stdout and stderr buffers
                if stdout:
                    stdout.flush()
                if stderr:
                    stderr.flush()

                # get diff from previous poll
                stdout_line_count += self.send_logs(
                    task_id, _print_file(stdout_path, stdout_line_count)
                )
                if stderr_path:
                    stderr_line_count += self.send_logs(
                        task_id, _print_file(stderr_path, stderr_line_count)
                    )
        except subprocess.CalledProcessError as ex:
            # non zero return code
            stop_reason = 'Exception occurred'
            status = ex.returncode

        stdout.close()
        if stderr_path:
            stderr.close()

        # Send last lines
        stdout_line_count += self.send_logs(
            task_id, _print_file(stdout_path, stdout_line_count)
        )
        if stderr_path:
            stderr_line_count += self.send_logs(
                task_id, _print_file(stderr_path, stderr_line_count)
            )

        return status, stop_reason

    def send_logs(self, task_id, lines, level="DEBUG"):
        """
        Send output lines as log events to backend
        :param task_id: ID of task to send logs for
        :type task_id: Text
        :param lines: lines to send
        :type lines: [Text]
        :param str level: log level, default DEBUG
        :return: number of lines sent
        :rtype: int
        """
        if not lines:
            return 0
        print("".join(lines), end="")
        # remove backspaces from the text log, they look bad.
        for i, l in enumerate(lines):
            lines[i] = l.replace('\x08', '')

        events_service = self.get_service(Events)
        try:
            events_service.send_log_events(
                self.worker_id, task_id=task_id, lines=lines, level=level
            )
            return len(lines)
        except Exception as e:
            print("\n### Error sending log: %s ###\n" % e)
            # revert number of sent lines (we will try next time)
            return 0

    def _update_commit_id(self, task_id, execution, repo_info):
        """
        If commit ID is not set, set it to the currently running version of the repository
        """
        if not repo_info.commit or execution.version_num:
            return
        self.log("Updating task commit ID: %s", repo_info.commit)
        try:
            self._session.send_api(
                tasks_api.EditRequest(
                    task_id, script=dict(version_num=repo_info.commit), force=True
                )
            )
        except Exception:
            pass

    def apply_diff(self, task, vcs, execution_info, repo_info):
        # type: (Any, VCS, ExecutionInfo, RepoInfo) -> None
        """
        Apply task diff if present
        """
        diff = task.script and task.script.diff
        if not diff:
            return
        print("Applying uncommitted changes")
        try:
            success = vcs.patch(normalize_path(repo_info.root), diff)
        except Exception as ex:
            self.log.warning("could not apply diff: %s", ex)
            success = False

        if not success:
            raise ValueError("Failed applying git diff:\n{}\n\nERROR! Failed applying git diff, see diff above.".format(diff))

    @resolve_names
    def build(
        self,
        task_id,
        target_folder=None,
        python_version=None,
        **_
    ):
        if not task_id:
            raise CommandFailedError("Worker build must have valid task id")
        if not check_if_command_exists("virtualenv"):
            raise CommandFailedError("Worker must have virtualenv installed")
        self._session.print_configuration()
        current_task = self._session.api_client.tasks.get_by_id(task_id)

        execution = self.get_execution_info(current_task)

        try:
            requirements = current_task.script.requirements
        except AttributeError:
            requirements = None

        # TODO: make sure we pass the correct python_version
        venv_folder, requirements_manager = self.install_virtualenv(venv_dir=target_folder,
                                                                    requested_python_version=python_version)

        if self._default_pip:
            self.package_api.install_packages(*self._default_pip)

        directory, vcs, repo_info = self.get_repo_info(execution, current_task, venv_folder.as_posix())

        self.install_requirements(
            execution,
            repo_info,
            requirements_manager=requirements_manager,
            cached_requirements=requirements,
        )
        freeze = self.freeze_task_environment()
        script_dir = directory

        # Summary
        print("Restoring running environment of task id [%s]:" % task_id)
        if freeze:
            print("Summary - installed python packages:")
            print(dump_yaml(freeze))
        else:
            print("No freeze information available")

        print("Virtual environment: {}".format(venv_folder / 'bin'))
        print("Source code: {}".format(repo_info.root))
        print("Entry point: {}".format(Path(script_dir) / execution.entry_point))

        return 0

    @resolve_names
    def execute(
        self,
        task_id,
        log_level,
        optimization=0,
        disable_monitoring=False,
        full_monitoring=False,
        log_file=None,
        **_
    ):
        if not task_id:
            raise CommandFailedError("Worker execute must have valid task id")
        if not check_if_command_exists("virtualenv"):
            raise CommandFailedError("Worker must have virtualenv installed")
        if full_monitoring:
            worker_params = WorkerParams(
                log_level=log_level,
                config_file=self._session.config_file,
                debug=self._session.debug_mode,
                trace=self._session.trace,
            )
            self.report_monitor(ResourceMonitor.StatusReport(task=task_id))
            self.run_one_task(queue='', task_id=task_id, worker_args=worker_params)
            self.stop_monitor()
            self._unregister()
            return

        self._session.print_configuration()
        current_task = self._session.api_client.tasks.get_by_id(task_id)
        try:
            if not current_task.id:
                pass
        except Exception:
            raise ValueError("Could not find task id={}".format(task_id))

        self._session.api_client.tasks.started(
            task=current_task.id,
            status_reason="worker started execution",
            status_message=self._task_status_change_message,
        )

        if not disable_monitoring:
            self.log.debug("starting resource monitor")
            self.report_monitor(ResourceMonitor.StatusReport(task=task_id))

        execution = self.get_execution_info(current_task)

        try:
            requirements = current_task.script.requirements
        except AttributeError:
            requirements = None

        venv_folder, requirements_manager = self.install_virtualenv()

        if self._default_pip:
            self.package_api.install_packages(*self._default_pip)

        print("\n")

        directory, vcs, repo_info = self.get_repo_info(
            execution, current_task, venv_folder
        )

        print("\n")

        self.install_requirements(
            execution,
            repo_info,
            requirements_manager=requirements_manager,
            cached_requirements=requirements,
        )
        freeze = self.freeze_task_environment(current_task.id)
        script_dir = (directory if isinstance(directory, Path) else Path(directory)).absolute().as_posix()

        # run code
        print("Running task id [%s]:" % task_id)
        extra = ['-u', ]
        if optimization:
            extra.append(
                WorkerParams(optimization=optimization).get_optimization_flag()
            )
        extra.append(execution.entry_point)
        command = self.package_api.get_python_command(extra)
        print("[{}]$ {}".format(execution.working_dir, command.pretty()))

        if freeze:
            print("Summary - installed python packages:")
            print(dump_yaml(freeze))
        else:
            print("No freeze information available")

        print("Environment setup completed successfully\n")

        sdk_env = {
            # config_file updated in session.py
            "task_id": current_task.id,
            "log_level": log_level,
            "log_to_backend": "0",
            "config_file": self._session.config_file,  # The config file is the tmp file that trains_agent created
        }
        environ.update(
            {
                sdk_key: str(value)
                for key, value in sdk_env.items()
                for sdk_key in ENVIRONMENT_SDK_PARAMS[key]
            }
        )

        if repo_info:
            self._update_commit_id(task_id, execution, repo_info)

        print("Starting Task Execution:\n".format(task_id))
        exit_code = -1
        try:
            if disable_monitoring:
                try:
                    sys.stdout.flush()
                    sys.stderr.flush()
                    os.chdir(script_dir)
                    os.execv(command.argv[0].as_posix(), tuple([command.argv[0].as_posix()])+command.argv[1:])
                    # exit_code = command.check_call(cwd=script_dir)
                except subprocess.CalledProcessError as ex:
                    # non zero return code
                    exit_code = ex.returncode
            else:
                # store stdout/stderr into file, and send to backend
                temp_stdout_fname = log_file or safe_mkstemp(
                    suffix=".txt", prefix=".trains_agent_out.", name_only=True
                )
                print("Storing stdout and stderr log into [%s]" % temp_stdout_fname)
                exit_code, _ = self._log_command_output(
                    task_id=task_id,
                    cmd=command,
                    stdout_path=temp_stdout_fname,
                    cwd=script_dir,
                )
        except KeyboardInterrupt:
            self.handle_user_abort(task_id)
            raise
        except Exception as e:
            self.log.warning(str(e))
            self.log_traceback(e)
            exit_code = -1

        # kill leftover processes
        kill_all_child_processes()

        # if we return ExitStatus.interrupted==2,
        # it means user aborted, KeyboardInterrupt should have caught it,
        # that cannot happen when running with disable monitoring
        exit_code = exit_code if exit_code != ExitStatus.interrupted else -1

        if not disable_monitoring:
            # we need to change task status according to exit code
            self.handle_task_termination(task_id, exit_code, TaskStopReason.no_stop)
            self.stop_monitor()
            # unregister the worker
            self._unregister()

        return 1 if exit_code is None else exit_code

    def get_execution_info(self, current_task):
        # type: (...) -> ExecutionInfo
        try:
            execution = ExecutionInfo.from_task(current_task)
        except Exception as e:
            self.error("Could not parse task execution info: {}".format(e.args[0]))
            current_task.failed(
                status_reason=e.args[0], status_message=self._task_status_change_message
            )
            self.exit(e.args[0])
        if "\\" in execution.working_dir:
            warning(
                'Working dir "{}" contains backslashes. '
                "All path separators must be forward slashes.".format(
                    execution.working_dir
                )
            )
        print("Executing task id [%s]:" % current_task.id)
        for pair in attr.asdict(execution).items():
            print("{} = {}".format(*pair))
        print()
        return execution

    def get_repo_info(self, execution, task, venv_folder):
        # type: (ExecutionInfo, tasks_api.Task, str) -> Tuple[str, Optional[VCS], Optional[RepoInfo]]
        literal_script = LiteralScriptManager(venv_folder)
        has_repository = bool(execution.repository)
        is_literal_script = literal_script.is_literal_script(task)
        if not has_repository and not is_literal_script:
            raise CommandFailedError(
                "Can not run task without repository or literal script in `script.diff`"
            )
        repo_info = None
        directory = None
        vcs = None
        if has_repository:
            vcs, repo_info = self._get_repo_info(execution, task, venv_folder)
            directory = Path(repo_info.root, execution.working_dir or ".")

            for pair in attr.asdict(repo_info).items():
                print("{}: {}".format(*pair))
            if not is_literal_script:
                self.apply_diff(
                    task=task, vcs=vcs, execution_info=execution, repo_info=repo_info
                )
        if is_literal_script:
            self.log.info("found literal script in `script.diff`")
            directory, script = literal_script.create_notebook_file(
                task, execution, repo_info
            )
            execution.entry_point = script
            if not has_repository:
                return directory, None, None
        else:
            # in case of no literal script, there is not difference between empty working dir and `.`
            execution.working_dir = execution.working_dir or "."
        if not directory:
            assert False, "unreachable code"
        return directory, vcs, repo_info

    def _get_repo_info(self, execution, task, venv_folder):
        try:
            vcs, repo_info = clone_repository_cached(
                session=self._session,
                execution=execution,
                destination=Path(venv_folder) / WORKING_REPOSITORY_DIR,
            )
        except Exception:
            task.failed(
                status_reason="failed cloning repository",
                status_message=self._task_status_change_message,
            )
            if self._session.debug_mode:
                raise
            raise CommandFailedError(
                "Failed cloning repository. \n"
                "1) Make sure you pushed the requested commit:\n{}\n"
                "2) Check if remote-worker has valid credentials [see worker configuration file]".format(
                    str(execution).replace('ExecutionInfo', '', 1).replace('version_num', 'commit_id', 1))
            )
        return vcs, repo_info

    def handle_task_termination(self, task_id, exit_code, stop_reason):
        # type: (Text, int, TaskStopReason) -> None
        try:
            if stop_reason == TaskStopReason.stopped:
                self.log("Stopping - tasks.stop was called for task")
                self._session.api_client.tasks.stopped(
                    task=task_id,
                    status_reason="task was stopped by tasks.stop",
                    status_message=self._task_status_change_message,
                )

            elif stop_reason == TaskStopReason.status_changed:
                try:
                    task_status = get_task(
                        self._session, task_id, only_fields=["status"]
                    ).status
                    self.log(
                        "Task status changed unexpectedly (status: {}), "
                        "terminating task process.".format(task_status)
                    )
                except Exception as ex:
                    self.log(
                        "Task status changed unexpectedly. Was not able to obtain the current status: "
                        "{}: {}".format(type(ex), ex)
                    )
                    self.log_traceback(ex)

            elif stop_reason == TaskStopReason.reset:
                self.log("Task was reset unexpectedly")

            elif stop_reason == TaskStopReason.no_stop:
                self.handle_task_process_termination(task_id, exit_code)
            else:
                self.log(
                    "INTERNAL ERROR: unidentified task stop reason: {}".format(
                        stop_reason
                    )
                )

        except Exception as e:
            # task probably set its own status
            self.log(
                "Warning: could not update task id '{}' status. Task exit code {}".format(
                    task_id, exit_code
                )
            )
            self.log_traceback(e)

    def handle_task_process_termination(self, task_id, exit_code):
        # type: (Text, int) -> None
        self.log("Task process terminated")

        if exit_code == COMMAND_SUCCESS:
            self.log("Task success: completing")
            self._session.api_client.tasks.completed(
                task=task_id,
                status_reason="worker execution done",
                status_message=self._task_status_change_message,
            )
        elif exit_code == ExitStatus.interrupted:
            self.log("Task interrupted: stopping")
            self._session.api_client.tasks.stopped(
                task=task_id,
                status_reason="user abort",
                status_message=self._task_status_change_message,
            )
        else:
            self.log("Task failure: setting status to 'failed'")
            self._session.api_client.tasks.failed(
                task=task_id,
                status_reason="worker execution exit code {}".format(exit_code),
                status_message=self._task_status_change_message,
            )

    def freeze_task_environment(self, task_id=None):
        try:
            freeze = self.package_api.freeze()
        except Exception as e:
            print("Could not freeze installed packages")
            self.log_traceback(e)
            return None
        if not task_id:
            return freeze

        # get original requirements and update with the new frozen requirements
        try:
            current_task = get_task(self._session, task_id, only_fields=["script.requirements"])
            requirements = current_task.script.requirements
            requirements.update(freeze)
        except Exception:
            requirements = freeze

        request = tasks_api.SetRequirementsRequest(task=task_id, requirements=requirements)
        try:
            self._session.send_api(request)
        except APIError as e:
            print("Could not set task requirements")
            self.log_traceback(e)
        return freeze

    def _install_poetry_requirements(self, repo_info):
        # type: (Optional[RepoInfo]) -> Optional[PoetryAPI]
        if not repo_info:
            return None
        try:
            api = self.poetry.get_api(repo_info.root)
            if api.enabled:
                api.install()
                return api
        except Exception:
            self.log.error("failed installing poetry requirements:")
        return None

    def install_requirements(
        self, execution, repo_info, requirements_manager, cached_requirements=None
    ):
        # type: (ExecutionInfo, RepoInfo, RequirementsManager, Optional[dict]) -> None
        """
        :summary: Install requirements for task script using pip.
        :description: A file named "requirements.txt" is looked for in each containing folder between the
                      repository root and the directory containing the script.
                      For each such file, CUDA based packages are looked for and replaced if necessary.
        :param execution: task execution information
        :param repo_info: repository information
        :param requirements_manager: requirements manager for task
        :param cached_requirements: cached requirements from previous run
         """
        api = self._install_poetry_requirements(repo_info)
        if api:
            self.package_api = api
            return

        self.package_api.upgrade_pip()
        self.package_api.set_selected_package_manager()
        # always install cython,
        # if we have a specific version in the requirements,
        # the CythonRequirement(SimpleSubstitution) will reinstall cython with the specific version
        if not self.is_conda:
            self.package_api.out_of_scope_install_package('Cython')

        cached_requirements_failed = False
        if cached_requirements:
            self.log("Found cached requirements, trying to install")
            try:
                self.package_api.load_requirements(cached_requirements)
            except Exception as e:
                self.log_traceback(e)
                self.error("Could not install cached requirements, installing requirements from repository")
                cached_requirements_failed = True
            else:
                self.log("Cached requirements installation success")
                return

        if not repo_info:
            self.log("no repository to install requirements from")
            return

        repo_requirements_installed = False
        for parent in reversed(
            (Path(execution.working_dir) / execution.entry_point).parents
        ):
            requirements_file = (
                repo_info.root / parent / "requirements.txt"
            )  # type: Path
            if not requirements_file.is_file():
                continue
            print("Trying pip install: {}".format(requirements_file))
            requirements_text = requirements_file.read_text()
            new_requirements = requirements_manager.replace(requirements_text)

            temp_file = None
            try:
                with self.named_temporary_file(
                    mode="w", prefix="requirements_", suffix=".txt", delete=False
                ) as temp_file:
                    temp_file.write(new_requirements)
                    temp_file.flush()
                # close the file before reading in install_from_file for Windows compatibility
                self.package_api.install_from_file(temp_file.name)
            except Exception as e:
                print('ERROR: Failed installing requirements.txt:\n{}'.format(requirements_text))
                raise e
            finally:
                if self._session.debug_mode and temp_file:
                    try:
                        Path(temp_file.name).unlink()
                    except OSError:
                        pass
            # call post installation callback
            requirements_manager.post_install()
            # mark as successful installation
            repo_requirements_installed = True

        # if we reached here without installing anything, and
        # we failed installing from cached requirements, them this is an error
        if cached_requirements_failed and not repo_requirements_installed:
            raise ValueError("Could not install cached requirements or repository requirements")

    def named_temporary_file(self, *args, **kwargs):
        kwargs.setdefault("delete", not self._session.debug_mode)
        return named_temporary_file(*args, **kwargs)

    def list(self, **_):
        # display all registered working machines
        workers = self.get("get_all", last_seen=0)
        print_parameters(workers)

    def _register(self, queues=()):
        self.queues = queues
        try:
            self.get("register", worker=self.worker_id, queues=queues)
            # If we got here - we've registered
            self._worker_registered = True
        # except APIError as error:
        #     if error.codes != WORKER_ALREADY_REGISTERED:
        #         raise
        # except ValueError:
        #     raise ValueError("Worker cannot register itself with backend service")
        except Exception as e:
            self.log("Worker failed registering itself with backend service: {}".format(e))

    def _unregister(self, queues=()):
        self.queues = ()
        try:
            self.get("unregister", worker=self.worker_id, queues=queues)
            self._worker_registered = False
        except Exception as e:
            self.log("Worker failed unregistering itself with backend service: {}".format(e))

    def log_traceback(self, err):
        if isinstance(err, APIError):
            tb = err.get_traceback()
            if tb:
                print("Server traceback:\n{}".format(tb))
        if self._session.debug_mode:
            self.log(traceback.format_exc())

    def debug(self, message):
        if self._session.debug_mode:
            print("trains_agent: {}".format(message))

    def find_python_executable_for_version(self, config_version):
        # type: (Text) -> Tuple[Text, Text, Text]
        """
        Find python executable with version ``config_version``.
        The search starts with the executable named ``python<config_version>``.
        If not found in the path, increasingly major components of the semantic version are dropped
        with the last executable to be searched being a plain ``python``.
        A result is returned only if ``python --version``'s output matches config_version.
        For example: if config_version=3.6.5, the search order is:
        1. python3.6.5
        2. python3.6
        3. python3
        4. python
        if config_version=3.6, the search starts with ``python3.6`` and so on.
        :return: 3-tuple:
            1. Python executable version as reported by itself with ``--version``
            2. The version suffix of the executable name (e.g. ``python3`` -> ``3``)
            3. The executable name itself (e.g. ``python3``)
        """

        def suffixes(it):
            it = list(it)
            for i in range(len(it) + 1):
                yield it[:i]

        python_executables = [
            (version, "python{}".format(version))
            for version in map(
                ".".join, reversed(list(suffixes(config_version.split("."))))
            )
        ]
        for version, executable in python_executables:
            self.log.debug("Searching for {}".format(executable))
            if find_executable(executable):
                try:
                    output = Argv(executable, "--version").get_output(
                        stderr=subprocess.STDOUT
                    )
                except subprocess.CalledProcessError as ex:
                    self.log.warning("error getting %s version: %s", executable, ex)
                    continue
                match = re.search(
                    r"Python ({}(?:\.\d+)*)".format(config_version or r"\d+"), output
                )
                if match:
                    self.log.debug("Found: {}".format(executable))
                    return match.group(1), version, executable
        raise CommandFailedError(
            "Python executable with version {!r} defined in configuration file, "
            "key 'agent.default_python', not found in path, tried: {}".format(
                config_version, list(zip(*python_executables))[1]
            )
        )

    def install_virtualenv(self, venv_dir=None, requested_python_version=None):
        # type: (str, str) -> Tuple[Path, RequirementsManager]
        """
        Install a new python virtual environment, removing the old one if exists
        :return: virtualenv directory and requirements manager to use with task
        """
        requested_python_version = requested_python_version or Text(self._session.config["agent.default_python"])
        venv_dir = Path(venv_dir) if venv_dir else \
            Path(self._session.config["agent.venvs_dir"], requested_python_version)
        executable_version, executable_version_suffix, executable_name = self.find_python_executable_for_version(
            requested_python_version
        )
        self._session.config.put("agent.default_python", executable_version)
        first_time = (
            is_windows_platform()
            or self.is_conda
            or not venv_dir.is_dir()
            or not self.is_venv_update
        )

        requirements_manager = self._get_requirements_manager(
            base_interpreter=executable_name
        )

        rm_tree(normalize_path(venv_dir, WORKING_REPOSITORY_DIR))
        package_manager_params = dict(
            session=self._session,
            python=executable_version_suffix,
            path=venv_dir,
            requirements_manager=requirements_manager,
        )

        if not self.is_conda:
            if self.is_venv_update:
                self.package_api = VenvUpdateAPI(
                    url=self._session.config["agent.venv_update.url"] or DEFAULT_VENV_UPDATE_URL,
                    **package_manager_params
                )
            else:
                self.package_api = VirtualenvPip(**package_manager_params)
            if first_time:
                self.package_api.remove()
                self.package_api.create()
        else:

            get_conda = partial(CondaAPI, **package_manager_params)
            self.package_api = get_conda()
            # no support for reusing Conda environments
            self.package_api.remove()

            if venv_dir.exists():
                timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
                new_venv_folder = venv_dir.with_name(
                    "{}_{}".format(venv_dir.name, timestamp)
                )
                self.warning(
                    'Path "{}" exists, using "{}" instead'.format(
                        venv_dir, new_venv_folder
                    )
                )
                venv_dir = new_venv_folder
                self.package_api = get_conda(path=venv_dir)

            self.package_api.create()

        return venv_dir, requirements_manager

    def parse_requirements(self, reqs_file=None, overrides=None):
        os = None
        session = self._session
        if overrides:
            overrides = ConfigFactory.parse_string("\n".join(overrides))
            os = overrides.pop("os", None)
            ConfigTree.merge_configs(session.config, overrides)
        if reqs_file:
            contents = Path(reqs_file).read_text()
        else:
            contents = ensure_text(sys.stdin.read())
        session.finalize_config(session.config)
        requirements_manager = self._get_requirements_manager(os_override=os)
        requirements_manager.translator.enabled = False
        print(requirements_manager.replace(contents))

    def get_docker_config_cmd(self, docker_args):
        def docker_cmd_functor(default_kwargs, **kwargs):
            args = deepcopy(default_kwargs)
            args.update(kwargs)
            return self._get_docker_cmd(**args)

        docker_image = str(self._session.config.get("agent.default_docker.image", "nvidia/cuda")) \
            if not docker_args else docker_args[0]
        docker_arguments = docker_image.split(' ') if docker_image else []
        if len(docker_arguments) > 1:
            docker_image = docker_arguments[0]
            docker_arguments = docker_arguments[1:]
        else:
            docker_arguments = self._session.config.get("agent.default_docker.arguments", None) or []
            if isinstance(docker_arguments, six.string_types):
                docker_arguments = [docker_arguments]
        python_version = '3'
        if not python_version.startswith('python'):
            python_version = 'python'+python_version
        print("Running in Docker mode (v19.03 and above) - using default docker image: {} running {}\n".format(
            docker_image, python_version))
        temp_config = self._session.config.copy()
        mounted_cache_dir = '/root/.trains/cache'
        mounted_pip_dl_dir = '/root/.trains/pip-download-cache'
        mounted_vcs_cache = '/root/.trains/vcs-cache'
        mounted_venv_dir = '/root/.trains/venvs-builds'
        host_cache = Path(os.path.expandvars(self._session.config["sdk.storage.cache.default_base_dir"])).expanduser().as_posix()
        host_pip_dl = Path(os.path.expandvars(self._session.config["agent.pip_download_cache.path"])).expanduser().as_posix()
        host_vcs_cache = Path(os.path.expandvars(self._session.config["agent.vcs_cache.path"])).expanduser().as_posix()
        temp_config.put("sdk.storage.cache.default_base_dir", mounted_cache_dir)
        temp_config.put("agent.pip_download_cache.path", mounted_pip_dl_dir)
        temp_config.put("agent.vcs_cache.path", mounted_vcs_cache)
        temp_config.put("agent.package_manager.system_site_packages", True)
        temp_config.put("agent.default_python", "")
        temp_config.put("agent.venvs_dir", mounted_venv_dir)

        host_apt_cache = Path(os.path.expandvars(self._session.config.get(
            "agent.docker_apt_cache", '~/.trains/apt-cache'))).expanduser().as_posix()
        host_pip_cache = Path(os.path.expandvars(self._session.config.get(
            "agent.docker_pip_cache", '~/.trains/pip-cache'))).expanduser().as_posix()
        host_ssh_cache = mkdtemp(prefix='trains_agent.ssh.')

        # make sure all folders are valid
        Path(host_apt_cache).mkdir(parents=True, exist_ok=True)
        Path(host_pip_cache).mkdir(parents=True, exist_ok=True)
        Path(host_cache).mkdir(parents=True, exist_ok=True)
        Path(host_pip_dl).mkdir(parents=True, exist_ok=True)
        Path(host_vcs_cache).mkdir(parents=True, exist_ok=True)
        Path(host_ssh_cache).mkdir(parents=True, exist_ok=True)

        # copy the .ssh folder to a temp folder, to be mapped into docker
        try:
            src = Path(host_ssh_cache)
            if src.is_dir():
                src.rmdir()
            shutil.copytree(Path('~/.ssh').expanduser().as_posix(), host_ssh_cache)
        except Exception:
            host_ssh_cache = None
            log.warning('Failed creating temporary copy of ~/.ssh for git credential')
            pass

        # store docker arguments
        self._docker_image = docker_image
        self._docker_arguments = docker_arguments
        docker_cmd = dict(worker_id=self.worker_id,
                          # docker_image=docker_image,
                          # docker_arguments=docker_arguments,
                          python_version=python_version, conf_file=self.temp_config_path,
                          host_apt_cache=host_apt_cache,
                          host_pip_cache=host_pip_cache,
                          host_ssh_cache=host_ssh_cache,
                          host_cache=host_cache, mounted_cache=mounted_cache_dir,
                          host_pip_dl=host_pip_dl, mounted_pip_dl=mounted_pip_dl_dir,
                          host_vcs_cache=host_vcs_cache, mounted_vcs_cache=mounted_vcs_cache)
        return temp_config, partial(docker_cmd_functor, docker_cmd)

    @staticmethod
    def _get_docker_cmd(worker_id, docker_image, docker_arguments,
                        python_version, conf_file,
                        host_apt_cache,
                        host_pip_cache,
                        host_ssh_cache,
                        host_cache, mounted_cache,
                        host_pip_dl, mounted_pip_dl,
                        host_vcs_cache, mounted_vcs_cache):
        docker = 'docker'

        base_cmd = [docker, 'run', '-t']
        gpu_devices = os.environ.get('NVIDIA_VISIBLE_DEVICES', None)
        if gpu_devices is None:
            base_cmd += ['--gpus', 'all', ]
        elif gpu_devices.strip():
            base_cmd += ['--gpus', 'device='+gpu_devices, ]
            # We are using --gpu, so we should not pass NVIDIA_VISIBLE_DEVICES, I think.
            # base_cmd += ['-e', 'NVIDIA_VISIBLE_DEVICES=' + gpu_devices, ]

        if docker_arguments:
            docker_arguments = list(docker_arguments) \
                if isinstance(docker_arguments, (list, tuple)) else [docker_arguments]
            base_cmd += [a for a in docker_arguments if a]

        base_cmd += ['-e', 'TRAINS_WORKER_ID='+worker_id, ]

        if host_ssh_cache:
            base_cmd += ['-v', host_ssh_cache+':/root/.ssh', ]

        base_cmd += [
                    '-v', conf_file+':/root/trains.conf',
                    '-v', host_apt_cache+':/var/cache/apt/archives',
                    '-v', host_pip_cache+':/root/.cache/pip',
                    '-v', host_pip_dl+':'+mounted_pip_dl,
                    '-v', host_cache+':'+mounted_cache,
                    '-v', host_vcs_cache+':'+mounted_vcs_cache,
                    '--rm', docker_image, 'bash', '-c',
                    "echo 'Binary::apt::APT::Keep-Downloaded-Packages \"true\";' > /etc/apt/apt.conf.d/docker-clean ; "                    
                    "chown -R root /root/.cache/pip ; "
                    "apt-get update ; "
                    "apt-get install -y git libsm6 libxext6 libxrender-dev libglib2.0-0 {python_single_digit}-pip ; "
                    "{python} -m pip install -U pip ; "
                    "{python} -m pip install -U trains-agent ; "
                    "{python} -u -m trains_agent ".format(
                        python_single_digit=python_version.split('.')[0],
                        python=python_version)]

        return base_cmd

    def _singleton(self):
        # ensure singleton
        worker_id = self._session.config["agent.worker_id"]
        worker_name = self._session.config["agent.worker_name"]
        if not worker_id and os.environ.get('NVIDIA_VISIBLE_DEVICES'):
            worker_id = '{}:gpu{}'.format(worker_name, os.environ.get('NVIDIA_VISIBLE_DEVICES'))
        self.worker_id, worker_slot = Singleton.register_instance(unique_worker_id=worker_id, worker_name=worker_name)
        if self.worker_id is None:
            error('Instance with the same WORKER_ID [{}] is already running'.format(worker_id))
            exit(1)
        # update folders based on free slot
        self._session.create_cache_folders(slot_index=worker_slot)


if __name__ == "__main__":
    pass
