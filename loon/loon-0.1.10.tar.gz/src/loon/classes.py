# -*- coding: utf-8 -*-
"""Classes used in loon package"""

import sys
import os
import json
import socket
import glob
import re
import io
from getpass import getpass
from subprocess import run, PIPE
from datetime import datetime
from ssh2.session import Session
if __package__ == '' or __package__ is None:  # Use for test
    from __init__ import __host_file__
    from utils import create_parentdir, isfile, isdir, pretty_table, get_filelist
else:
    from loon import __host_file__
    from loon.utils import create_parentdir, isfile, isdir, pretty_table, get_filelist

this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
data_dir = os.path.join(this_dir, 'data')

class Host:
    """
    Representation of remote host
    """
    def __init__(self, hostfile = __host_file__):
        self.hostfile = hostfile
        self.load_hosts()
        return

    def load_hosts(self):
        """Load hosts from file"""
        if not isfile(self.hostfile):
            self.active_host = []
            self.available_hosts = []
        else:
            with open(self.hostfile, 'r') as f:
                hosts = json.load(f)
            self.active_host = hosts['active']
            self.available_hosts = hosts['available']

        if any(isinstance(i, list) for i in self.active_host):
            print("Error: more than one active host. Please check config file ~/.config/loon/host.json and modify or remove it if necessary.")

        # Python code to remove duplicate elements 
        def RemoveDups(duplicate): 
            final_list = [] 
            flag = False
            for num in duplicate: 
                if num not in final_list: 
                    final_list.append(num) 
                else: 
                    flag = True
            return final_list, flag
        
        self.available_hosts, flag = RemoveDups(self.available_hosts)
        
        if flag:
            # Save unique hosts immediately
            self.save_hosts()

        return

    def save_hosts(self):
        """Save hosts to file"""
        # if len(self.active_host)==0 or len(self.available_hosts)==0:
        #     raise ValueError("Cannot save to file due to null host.")
        hosts = {'active':self.active_host, 'available':self.available_hosts}
        if not isfile(self.hostfile):
            # Create parent dir if hostfile does not exist
            create_parentdir(self.hostfile)
        with open(self.hostfile, 'w') as f:
            json.dump(hosts, f)
        return

    def add(self, name, username, host, port=22):
        """Add a remote host"""
        info = [name, username, host, port]

        if info in self.available_hosts:
            print("=> Input host exists. Will not change.")
            return
        else:
            self.available_hosts.append(info)
            if len(self.active_host) == 0:
                self.active_host = info
            self.save_hosts()
            print("=> Added successfully!")
        return

    def host_check(self, name, username, host, port=22):
        host = []
        if name is not None:
            for h in self.available_hosts:
                if h[0] == name:
                    host = h.copy()
        else:
            info = [username, host, port]
            for h in self.available_hosts:
                if h[1:] == info:
                    host = h.copy()
        if len(host) == 0:
            print("=> Host does not exist, please check input with list command!")
            sys.exit(1)
        return host

    def delete(self, name, username, host, port=22):
        """Delete a remote host"""
        host2del = self.host_check(name, username, host, port)
        print("=> Removing host from available list...")
        self.available_hosts.remove(host2del)
        if host2del == self.active_host:
            print("=> Removing active host...")
            if len(self.available_hosts) > 0:
                self.active_host = self.available_hosts[0]
                print("=> Changing active host to %s" %self.active_host[0])
            else:
                self.active_host = []  # reset
                print("=> Reseting active host to []")
        self.save_hosts()
        return
    
    def switch(self, name, username, host, port=22):
        """Switch active host"""
        host2switch = self.host_check(name, username, host, port)
        self.active_host = host2switch
        self.save_hosts()
        print("=> Activated.")
        return

    def rename(self, old, new):
        """Rename host name"""
        host2rename = []        
        for index, h in enumerate(self.available_hosts):
            if h[0] == old:
                host2rename = h.copy()
                self.available_hosts[index][0] = new
        if len(host2rename) == 0:
            print("=> Host does not exist, please check input with list command!")
            sys.exit(1)
        if host2rename == self.active_host:
            self.active_host[0] = new
        self.save_hosts()
        return
        
        
    def list(self):
        """List all remote hosts"""

        title = ['Alias', 'Username', 'IP address', 'Port']
        content = self.available_hosts.copy()
        for host in content:
            if host == self.active_host:
                host[0] = '<'+host[0]+'>'
        pretty_table(title, content)
        print("<active host>")
        return
    
    def connect(self, privatekey_file="~/.ssh/id_rsa", passphrase='', open_channel=True):
        """Connect active host and open a session."""
        privatekey_file = os.path.expanduser(privatekey_file)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.active_host[2], self.active_host[3]))
        s = Session()
        s.handshake(sock)
        try:
            # Try using private key file first
            s.userauth_publickey_fromfile(self.active_host[1], privatekey_file, passphrase)
        except:
            # Use password to auth
            passwd = getpass('No private key found.\nEnter your password for %s: ' %self.active_host[1])
            s.userauth_password(self.active_host[1], passwd)
        self.session = s
        if open_channel:
            self.channel = self.session.open_session()
        return
    
    def cmd(self, commands, _logger=None, run_file=False, data_dir=None, remote_file=False, dir='/tmp', prog=None):
        """Run command(s) in active remote host using channel session
        Therefore, `open_channel` in `connect` method must be `True` before using it.

        Args:
            commands ([str]): commands/scripts run on active remote host
            run_file ([bool]): if `True`, run scripts instead of commands
            data_dir ([str]): a path representing data directory
            remote_file ([bool]): if `True`, collect input from remote host instead of local machine
            dir ([str]): Remote directory for storing local scripts
        """
        if not run_file:
            self.connect()
            self.channel.execute(commands)
        else:
            # Run scripts
            _logger.info(commands)
            scripts = commands
            # commands are scripts here
            if remote_file:
                # Run remote scripts
                # Support some wildcards
                # *,?,{}
                wildcards = r'\*|\?|\{\}'
                matches = [re.compile(wildcards).search(i) is not None for i in scripts]
                if any(matches):
                    commands_1 = list(map(lambda x: 'ls '+x, scripts))
                    commands_1 = ';'.join(commands_1)
                    self.connect()
                    self.channel.execute(commands_1)
                    scripts = self.get_result(print_info=False)[0].split('\n')
                    scripts.remove('')
                if prog is None:
                    commands_1 = list(map(lambda x: 'chmod u+x '+x, scripts))
                    commands_1 = ';'.join(commands_1)
                    commands_2 = ';'.join(scripts)
                    commands = commands_1 + ';' + commands_2
                else:
                    commands = list(map(lambda x: '{} '.format(prog)+x, scripts))
                    commands = ';'.join(commands)
                _logger.info(commands)
                self.connect()
                print("=> Getting results:")
                self.channel.execute(commands)
            else:
                # Run local scripts
                #
                # 1) upload
                self.upload(scripts, dir, _logger)
                if data_dir is not None:
                    self.upload(data_dir, dir, _logger)
                # 2) get all file names
                if len(scripts) == 1:
                    if isdir(scripts[0]): 
                        if list(scripts[0])[-1] == '/':
                            dir = os.path.join(dir, os.path.basename(os.path.dirname(scripts[0])))
                        else:
                            dir = os.path.join(dir, os.path.basename(scripts[0]))
                        scripts = glob.glob(scripts[0] + '/*')
                filelist = []
                for fp in scripts:
                    _logger.info("fp:%s"%fp)
                    fs = glob.glob(fp)
                    _logger.info("fs:%s"%fs)
                    for f in fs:
                        _logger.info("f:%s"%f)
                        if isdir(f):
                            print("Warning: directory %s is detected, note anything in it will be ignored to execute." %f)
                        elif isfile(f):
                            filelist.append(f)
                        else:
                            print('Error: file %s does not exist.'%f)
                            sys.exit(1)
                filelist = list(map(os.path.basename, filelist))
                _logger.info(filelist)
                # 3) run them one by one
                scripts = list(map(lambda x: '/'.join([dir, x]), filelist))
                if prog is None:
                    commands_1 = list(map(lambda x: 'chmod u+x '+x, scripts))
                    commands_1 = ';'.join(commands_1)
                    commands_2 = ';'.join(scripts)
                    commands = commands_1 + ';' + commands_2
                else:
                    commands = list(map(lambda x: '{} '.format(prog)+x, scripts))
                    commands = ';'.join(commands)
                _logger.info(commands)
                self.connect()
                print("=> Getting results:")
                self.channel.execute(commands)
                
        datalist = self.get_result()
        return datalist
    
    def get_result(self, print_info=True):
        """Get result from executed channel"""
        size, errinfo = self.channel.read_stderr()
        if size > 0:
            print('An error is raised by remote host, please read the info:\n')
            print(errinfo.decode('utf-8'), end="")
            sys.exit(1)
        else:
            # Get output
            datalist = []
            size, data = self.channel.read()
            # Here data is byte type
            while size > 0:
                data = data.decode('utf-8')
                if print_info:
                    print(data, end='')
                datalist.append(data)
                size, data = self.channel.read()
        
        # Return a list containing output from commands 
        return datalist

    def upload(self, source, destination, _logger):
        """Upload files to active remote host.

        Currently, it is dependent on scp command.

        Args:
            source [(list)]: list of files (directories) in local machine
            destination [(str)]: destination directory in remote host
        """
        username, host, port = self.active_host[1:]
        cmds = "scp -pr -P {port} {source} {username}@{host}:{destination}".format(port=port, source=' '.join(map(os.path.expanduser, source)), username=username, host=host, destination=destination)
        print("=> Starting upload...", end="\n\n")
        now = datetime.now()  
        _logger.info("Running " + cmds)
        run(cmds, shell=True)
        taken = datetime.now() - now
        print("\n=> Finished uploading in %ss" %taken.seconds)
        return
     
        
    def download(self, source, destination, _logger):
        """Download files to local machine from active remote host.
        
        Currently, it is dependent on scp command.

        Args:
            source [(list)]: list of files (directories) in remote host
            destination [(str)]: destination directory in local machine
        """
        username, host, port = self.active_host[1:]
        if not isdir(os.path.expanduser(destination)):
            os.makedirs(os.path.expanduser(destination))
        print("=> Starting downloading...", end="\n\n")
        now = datetime.now()  
        for i in source:
            cmds = "scp -pr -P {port} {username}@{host}:{source} {destination}".format(port=port, source=i, username=username, host=host, destination=os.path.expanduser(destination))
            _logger.info("==> Running " + cmds)
            run(cmds)
        taken = datetime.now() - now
        print("\n=> Finished downloading in %ss" %taken.seconds)
        return


class PBS:
    """
    Representation of PBS task
    """
    def __init__(self):
        self.tmp_header = os.path.join(data_dir, "PBS_HEADER.txt")
        self.tmp_cmds = os.path.join(data_dir, "PBS_CMDS.txt")
        return

    def gen_template(self, input, output):
        """Generate a PBS template"""
        if output is None:
            output = os.path.join(os.getcwd(), 'work.pbs')
        print("=> Generating %s" %output)
        if isfile(output):
            print("Warning: the output file exists, it will be overwritten.")
        if input is None:
            with io.open(output, 'w', encoding='utf-8', newline='\n') as f:
                with open(self.tmp_header, 'r') as header:
                    for i in header:
                        print(i, file=f, end="")
            with io.open(output, 'a', encoding='utf-8', newline='\n') as f:
                with open(self.tmp_cmds, 'r') as cmds:
                    for i in cmds:
                        print(i, file=f, end="")
        else:
            if not isfile(input):
                print("Error: cannot find the template file.")
                sys.exit(1)
            with io.open(output, 'w', encoding='utf-8', newline='\n') as f:
                with open(input, 'r') as inf:
                    for i in inf:
                        print(i, file=f, end="")
        print("=> Done.")
        return

    def gen_pbs(self):
        pass

    def sub(self, host, tasks, remote, dest, _logger):
        """Submit pbs tasks"""
        print('NOTE: loon does not check if file/directory exits.')
        print('PBS file must be LF mode (Unix), not CRLF mode (Windows)')
        print('====================================================')
        if dest is None:
            # Directly submit tasks
            for f in tasks:
                _logger.info('qsub ' + f)
                if remote:
                    host.cmd('qsub ' + f)
                else:
                    run('qsub ' + f)
        else:
            # Upload tasks and
            # then submit tasks
            filelist = []
            host.upload(tasks, dest, _logger)
            for f in tasks:
                if len(tasks) == 1 and isdir(f):
                    cmds = dest + '/' + f + '/*'
                    _logger.info('qsub ' + cmds)
                    host.cmd('qsub ' + cmds)
                    return
                else:
                    if isdir(f):
                        print("Warning: don't support directory in this situation, skipping %s"%f)
                    else:
                        filelist.append(dest + '/' + os.path.basename(f))
            cmds = ' '.join(filelist)
            _logger.info('qsub ' + cmds)
            host.cmd('qsub ' + cmds)
        return

    def check(self, host, job_id):
        """Check PBS task status"""
        if job_id is None:
            host.cmd('qstat')
        else:
            host.cmd('qstat ' + job_id)
        return

if __name__ == "__main__":
    print(this_dir)
    print(data_dir)
