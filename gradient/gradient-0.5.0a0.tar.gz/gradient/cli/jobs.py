from functools import reduce

import click

from gradient import utils, logger
from gradient.cli import common
from gradient.cli.cli import cli
from gradient.cli.cli_types import json_string
from gradient.cli.common import api_key_option, del_if_value_is_none, ClickGroup, jsonify_dicts
from gradient.cli.experiments import \
    show_workspace_deprecation_warning_if_workspace_archive_or_workspace_archive_was_used
from gradient.commands import jobs as jobs_commands
from gradient.workspace import WorkspaceHandler


def get_workspace_handler():
    logger_ = logger.Logger()
    workspace_handler = WorkspaceHandler(logger_=logger_)
    return workspace_handler


@cli.group("jobs", help="Manage gradient jobs", cls=ClickGroup)
def jobs_group():
    pass


@jobs_group.command("delete", help="Delete job")
@click.option(
    "--jobId",
    "job_id",
    required=True,
    help="Delete job with given ID",
)
@api_key_option
def delete_job(job_id, api_key):
    command = jobs_commands.DeleteJobCommand(api_key=api_key)
    command.execute(job_id)


@jobs_group.command("stop", help="Stop running job")
@click.option(
    "--jobId",
    "job_id",
    required=True,
    help="Stop job with given ID",
)
@api_key_option
def stop_job(job_id, api_key=None):
    command = jobs_commands.StopJobCommand(api_key=api_key)
    command.execute(job_id)


@jobs_group.command("list", help="List jobs with optional filtering")
@click.option(
    "--project",
    "project",
    help="Use to filter jobs by project name",
    cls=common.GradientOption,
)
@click.option(
    "--projectId",
    "project_id",
    help="Use to filter jobs by project ID",
    cls=common.GradientOption,
)
@click.option(
    "--experimentId",
    "experiment_id",
    help="Use to filter jobs by experiment ID",
    cls=common.GradientOption,
)
@api_key_option
@common.options_file
def list_jobs(api_key, options_file, **filters):
    del_if_value_is_none(filters)

    command = jobs_commands.ListJobsCommand(api_key=api_key)
    command.execute(**filters)


def common_jobs_create_options(f):
    options = [
        click.option(
            "--name",
            "name",
            help="Job name",
            cls=common.GradientOption,
        ),
        click.option(
            "--machineType",
            "machine_type",
            help="Virtual machine type",
            required=True,
            cls=common.GradientOption,
        ),
        click.option(
            "--container",
            "container",
            default="paperspace/tensorflow-python",
            help="Docker container",
            required=True,
            cls=common.GradientOption,
        ),
        click.option(
            "--command",
            "command",
            help="Job command/entrypoint",
            cls=common.GradientOption,
        ),
        click.option(
            "--ports",
            "ports",
            help="Mapped ports",
            cls=common.GradientOption,
        ),
        # TODO: make it a flag
        click.option(
            "--isPublic",
            "is_public",
            help="Flag: is job public",
            cls=common.GradientOption,
        ),
        click.option(
            "--workspace",
            "workspace",
            help="Path to workspace directory",
            cls=common.GradientOption,
        ),
        click.option(
            "--workspaceArchive",
            "workspace_archive",
            help="Path to workspace archive",
            cls=common.GradientOption,
        ),
        click.option(
            "--workspaceUrl",
            "workspace_url",
            help="Project git repository url",
            cls=common.GradientOption,
        ),
        click.option(
            "--workingDirectory",
            "working_directory",
            help="Working directory for the experiment",
            cls=common.GradientOption,
        ),
        click.option(
            "--ignoreFiles",
            "ignore_files",
            help="Ignore certain files from uploading",
            cls=common.GradientOption,
        ),
        click.option(
            "--experimentId",
            "experiment_id",
            help="Experiment Id",
            cls=common.GradientOption,
        ),
        click.option(
            "--jobEnv",
            "job_env",
            type=json_string,
            help="Environmental variables ",
            cls=common.GradientOption,
        ),
        click.option(
            "--useDockerfile",
            "use_dockerfile",
            help="Flag: using Dockerfile",
            cls=common.GradientOption,
        ),
        # TODO: make it a flag
        click.option(
            "--isPreemptible",
            "is_preemptible",
            help="Flag: isPreemptible",
            cls=common.GradientOption,
        ),
        click.option(
            "--project",
            "project",
            help="Project name",
            cls=common.GradientOption,
        ),
        click.option(
            "--projectId",
            "project_id",
            help="Project ID",
            required=True,
            cls=common.GradientOption,
        ),
        click.option(
            "--startedByUserId",
            "started_by_user_id",
            help="User ID",
            cls=common.GradientOption,
        ),
        click.option(
            "--relDockerfilePath",
            "rel_dockerfile_path",
            help="Relative path to Dockerfile",
            cls=common.GradientOption,
        ),
        click.option(
            "--registryUsername",
            "registry_username",
            help="Docker registry username",
            cls=common.GradientOption,
        ),
        click.option(
            "--registryPassword",
            "registry_password",
            help="Docker registry password",
            cls=common.GradientOption,
        ),
        click.option(
            "--cluster",
            "cluster",
            help="Cluster name",
            cls=common.GradientOption,
        ),
        click.option(
            "--clusterId",
            "cluster_id",
            help="Cluster id",
            cls=common.GradientOption,
        ),
        click.option(
            "--nodeAttrs",
            "node_attrs",
            type=json_string,
            help="Cluster node details",
            cls=common.GradientOption,
        ),
        click.option(
            "--buildOnly",
            "build_only",
            type=bool,
            is_flag=True,
            help="Determines whether to only build and not run image (default false)",
            cls=common.GradientOption,
        ),
    ]
    return reduce(lambda x, opt: opt(x), reversed(options), f)


@jobs_group.command("create", help="Create job")
@common_jobs_create_options
@api_key_option
@common.options_file
@click.pass_context
def create_job(ctx, api_key, options_file, **kwargs):
    utils.validate_workspace_input(kwargs)
    show_workspace_deprecation_warning_if_workspace_archive_or_workspace_archive_was_used(kwargs)

    del_if_value_is_none(kwargs)
    jsonify_dicts(kwargs)

    command = jobs_commands.CreateJobCommand(api_key=api_key, workspace_handler=get_workspace_handler())
    job_handle = command.execute(kwargs)
    if job_handle is not None:
        ctx.invoke(list_logs, job_id=job_handle, line=0, limit=100, follow=True, api_key=api_key)


@jobs_group.command("logs", help="List job logs")
@click.option(
    "--jobId",
    "job_id",
    required=True,
    cls=common.GradientOption,
)
@click.option(
    "--line",
    "line",
    required=False,
    default=0,
    cls=common.GradientOption,
)
@click.option(
    "--limit",
    "limit",
    required=False,
    default=10000,
    cls=common.GradientOption,
)
@click.option(
    "--follow",
    "follow",
    required=False,
    default=False,
    cls=common.GradientOption,
)
@api_key_option
@common.options_file
def list_logs(job_id, line, limit, follow, options_file, api_key=None):
    command = jobs_commands.JobLogsCommand(api_key=api_key)
    command.execute(job_id, line, limit, follow)


@jobs_group.group("artifacts", help="Manage jobs' artifacts", cls=ClickGroup)
def artifacts():
    pass


@artifacts.command("destroy", help="Destroy job's artifacts")
@click.argument("job_id", cls=common.GradientArgument)
@click.option(
    "--files",
    "files",
    cls=common.GradientOption,
)
@api_key_option
@common.options_file
def destroy_artifacts(job_id, options_file, api_key=None, files=None):
    command = jobs_commands.ArtifactsDestroyCommand(api_key=api_key)
    command.execute(job_id, files=files)


@artifacts.command("get", help="Get job's artifacts")
@click.argument("job_id", cls=common.GradientArgument)
@api_key_option
@common.options_file
def get_artifacts(job_id, options_file, api_key=None):
    command = jobs_commands.ArtifactsGetCommand(api_key=api_key)
    command.execute(job_id)


@artifacts.command("list", help="List job's artifacts")
@click.argument("job_id", cls=common.GradientArgument)
@click.option(
    "--size",
    "-s",
    "size",
    help="Show file size",
    is_flag=True,
    cls=common.GradientOption,
)
@click.option(
    "--links",
    "-l",
    "links",
    help="Show file URL",
    is_flag=True,
    default=False,
    cls=common.GradientOption,
)
@click.option(
    "--files",
    "files",
    help="Get only given file (use at the end * as a wildcard)",
    cls=common.GradientOption,
)
@api_key_option
@common.options_file
def list_artifacts(job_id, size, links, files, options_file, api_key=None):
    command = jobs_commands.ArtifactsListCommand(api_key=api_key)
    command.execute(job_id=job_id, size=size, links=links, files=files)


@artifacts.command("download", help="List job's artifacts")
@click.option(
    "--jobId",
    "job_id",
    cls=common.GradientOption,
)
@click.option(
    "--destinationDir",
    "destination_directory",
    cls=common.GradientOption,
)
@api_key_option
@common.options_file
def download_artifacts(job_id, destination_directory, options_file, api_key=None):
    command = jobs_commands.DownloadArtifactsCommand(api_key=api_key)
    command.execute(job_id=job_id, destination_directory=destination_directory)
