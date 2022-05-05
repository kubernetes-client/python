# Copyright 2019 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples of using kubernetes.stream.Popen, which exposes the pod exec call using a subprocess.Popen
like object, with support for both binary and text data.


kubernetes.stream.Popen Constructor

  method    - kubernetes api method, most likely connect_get_namespaced_pod_exec
  name      - name of the pod to exec in
  namespace - namespace of the pod to exec in
  command   - command line to exec
  container - container of the pod to exec in, only needed if more than one
  stdin     - stdin handling, True or PIPE creates self.stdin, DEVNULL enables but ignores
  stdout    - stdout handling, True or PIPE creates self.stdout, DEVNULL enables but ignores
  stderr    - stderr handling, True or PIPE creates self.stderr, STDOUT combines into stderr, DEVNULL enables but ignores
  tty       - True if a tty should be enabled
  bufsize   - stream buffer size, -1 is system default, 0 is unbuffered, 1 in text mode is line buffered
  encoding  - text encoding format
  errors    - text encoding error strictness
  text      - force enabling or disabling text mode, default is tty value if encoding and errors are not set

kubernetes.stream.Popen Fields

  name       - pod name
  namespace  - pod namespace
  container  - pod container
  command    - command run
  tty        - tty enabled
  encodning  - text mode encoding
  errors     - text mode errors strictness
  stdin      - if enabled, a writable io stream
  stdout     - if enabled, a readable io stream
  stderr     - if enabkedm a readable io stream
  returncode - exec process return code when complete
  result     - full result object returned by kubernetes
  closed     - flag if the connecition is closed
  timeout    - timeout setting

kubernetes.stream.Popen Methods

  communicate - same as subprocess.Popen.communicate
  wait        - same as subprocess.Popen.wait
  resize      - resize the tty width and height
  close       - close the kubernetes connection

"""

import os
import select
import sys
import termios
import time
import tty

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import Popen, STDOUT

##############################################################################
# 
##############################################################################

def exec_commands(api_instance):
    name = 'busybox-test'
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name,
                                                namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)

    if not resp:
        print("Pod %s does not exist. Creating it..." % name)
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'image': 'busybox',
                    'name': 'sleep',
                    "args": [
                        "/bin/sh",
                        "-c",
                        "while true;do date;sleep 5; done"
                    ]
                }]
            }
        }
        resp = api_instance.create_namespaced_pod(body=pod_manifest,
                                                  namespace='default')
        while True:
            resp = api_instance.read_namespaced_pod(name=name,
                                                    namespace='default')
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)
        print("Done.")

    ##################################################################
    # Calling exec and waiting for response
    command = ['/bin/sh', '-c', 'echo This message goes to stdout; echo This message goes to stderr >&2']
    popen = Popen(
        api_instance.connect_get_namespaced_pod_exec,
        name, 'default', command=command,
        stdin=False, stdout=True, stderr=True,
        tty=False, text=True,
    )
    stdout, stderr = popen.communicate()
    print("STDOUT: " + stdout, end='', flush=True)
    print("STDERR: " + stderr, end='', flush=True)

    ##################################################################
    # Calling a process interactively
    popen = Popen(
        api_instance.connect_get_namespaced_pod_exec,
        name, 'default', command=['/bin/sh'],
        stdin=True, stdout=True, stderr=True,
        tty=False, text=True, bufsize=1, # bufsize=1 will flush on newlines
    )
    commands = [
        "echo This message goes to stdout",
        "echo This message goes to stderr >&2",
    ]
    # Do non-blocking stdout and stderr reads.
    popen.timeout = 0
    while commands and not popen.closed:
        line = commands.pop(0)
        print("Running command... %s" % line, flush=True)
        popen.stdin.write(line + "\n")
        time.sleep(1)
        try:
            line = popen.stdout.readline()
            print("STDOUT: %s" % line, end='', flush=True)
        except TimeoutError:
            pass
        try:
            line = popen.stderr.readline()
            print("STERR: %s" % line, end='', flush=True)
        except TimeoutError:
            pass
    popen.stdin.write("date\n")
    popen.timeout = 3
    line = popen.stdout.readline()
    print("Server date command returns: %s" % line)
    popen.stdin.write("whoami\n")
    popen.timeout = 3
    line = popen.stdout.readline()
    print("Server user is: %s" % line)
    popen.close()

    ##################################################################
    # Full TTY integration running top, uses local posix apis and raw i/o.
    popen = Popen(
        api_instance.connect_get_namespaced_pod_exec,
        name, 'default', command=['top'],
        stdin=True, stdout=True, stderr=STDOUT, # Send all stderr to stdout
        tty=True, text=False, bufsize=0, # bufsize=0 will not buffer data
    )
    stdin = sys.stdin.fileno()
    tcattr = termios.tcgetattr(stdin)
    size = None
    stdout = sys.stdout.fileno()
    # Do non-blocking stdout reads
    popen.timeout = 0
    try:
        # Enable raw tty mode with no echoing or buffering
        tty.setraw(stdin)
        while True:
            resize = os.get_terminal_size()
            if not size or resize.columns != size.columns or resize.lines != size.lines:
                size = resize
                # Inform remote top of the size of the terminal.
                popen.resize(size.columns, size.lines)
            # Check if there is anything from our stdin
            r, _, _ = select.select([stdin], [], [], 0)
            if r:
                # Read from our stdin
                data = os.read(stdin, 1024)
                # Write it to remote top's stdin
                popen.stdin.write(data)
            try:
                # Try to read from top's stdout
                data = popen.stdout.read(1024)
                # If a zero length data, then stdout has been closed
                if not data:
                    break
                # Write remote top's stdout to our stdout
                os.write(stdout, data)
            except TimeoutError:
                # Nothing from stdout available at this time
                pass
    finally:
        # Restore the original tty attributes from raw mode
        termios.tcsetattr(stdin, termios.TCSANOW, tcattr)
    # stdout was closed, now wait for top to finish.
    popen.wait()


def main():
    config.load_kube_config()
    try:
        c = Configuration().get_default_copy()
    except AttributeError:
        c = Configuration()
        c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    exec_commands(core_v1)


if __name__ == '__main__':
    main()
