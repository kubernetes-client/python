# This example used code(the `Interceptor` related part) from
# http://sqizit.bartletts.id.au/2011/02/14/pseudo-terminals-in-python/
# which is licensed under the MIT license:
# Copyright (c) 2011 Joshua D. Bartlett
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import errno
import fcntl
import json
import os
import pty
import select
import signal
import struct
import sys
import termios
import time
import tty

import six

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.apis import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream

# The following escape codes are xterm codes.
# See http://rtfm.etla.org/xterm/ctlseq.html for more.
START_ALTERNATE_MODE = set('\x1b[?{0}h'.format(i) for i in
                           ('1049', '47', '1047'))
END_ALTERNATE_MODE = set('\x1b[?{0}l'.format(i) for i in
                         ('1049', '47', '1047'))
ALTERNATE_MODE_FLAGS = tuple(START_ALTERNATE_MODE) + tuple(END_ALTERNATE_MODE)


def findlast(s, substrs):
    """
    Finds whichever of the given substrings occurs last in the given string
           and returns that substring, or returns None if no such strings
           occur.
    """
    i = -1
    result = None
    for substr in substrs:
        pos = s.rfind(substr)
        if pos > i:
            i = pos
            result = substr
    return result


class Interceptor(object):
    """
    This class does the actual work of the pseudo terminal. The spawn()
           function is the main entrypoint.
    """

    def __init__(self, k8s_stream=None):
        self.k8s_stream = k8s_stream
        self.master_fd = None

    def spawn(self, argv=None):
        """
        Create a spawned process.
        Based on the code for pty.spawn().
        """
        if not argv:
            argv = [os.environ['SHELL']]

        pid, master_fd = pty.fork()
        self.master_fd = master_fd
        if pid == pty.CHILD:
            os.execlp(argv[0], *argv)

        old_handler = signal.signal(signal.SIGWINCH, self._signal_winch)
        try:
            mode = tty.tcgetattr(pty.STDIN_FILENO)
            tty.setraw(pty.STDIN_FILENO)
            restore = 1
        except tty.error:    # This is the same as termios.error
            restore = 0
        self._init_fd()
        try:
            self._copy()
        except (IOError, OSError):
            if restore:
                tty.tcsetattr(pty.STDIN_FILENO, tty.TCSAFLUSH, mode)

        self.k8s_stream.close()
        self.k8s_stream = None
        if self.master_fd:
            os.close(self.master_fd)
            self.master_fd = None
        signal.signal(signal.SIGWINCH, old_handler)

    def _init_fd(self):
        """
        Called once when the pty is first set up.
        """
        self._set_pty_size()

    def _signal_winch(self, signum, frame):
        """
        Signal handler for SIGWINCH - window size has changed.
        """
        self._set_pty_size()

    def _set_pty_size(self):
        """
        Sets the window size of the child pty based on the window size of
               our own controlling terminal.
        """
        packed = fcntl.ioctl(pty.STDOUT_FILENO,
                             termios.TIOCGWINSZ,
                             struct.pack('HHHH', 0, 0, 0, 0))
        rows, cols, h_pixels, v_pixels = struct.unpack('HHHH', packed)
        self.k8s_stream.write_channel(4,
                                      json.dumps({"Height": rows,
                                                  "Width": cols}))

    def _copy(self):
        """
        Main select loop. Passes all data to self.master_read() or
               self.stdin_read().
        """
        assert self.k8s_stream is not None
        k8s_stream = self.k8s_stream
        while True:
            try:
                rfds, wfds, xfds = select.select([pty.STDIN_FILENO,
                                                  k8s_stream.sock.sock],
                                                 [], [])
            except select.error as e:
                no = e.errno if six.PY3 else e[0]
                if no == errno.EINTR:
                    continue

            if pty.STDIN_FILENO in rfds:
                data = os.read(pty.STDIN_FILENO, 1024)
                self.stdin_read(data)
            if k8s_stream.sock.sock in rfds:
                # read from k8s_stream
                if k8s_stream.peek_stdout():
                    self.master_read(k8s_stream.read_stdout())
                # error occurs
                if k8s_stream.peek_channel(3):
                    break

    def write_stdout(self, data):
        """
        Writes to stdout as if the child process had written the data.
        """
        os.write(pty.STDOUT_FILENO, data)

    def write_master(self, data):
        """
        Writes to the child process from its controlling terminal.
        """
        assert self.k8s_stream is not None
        self.k8s_stream.write_stdin(data)

    def master_read(self, data):
        """
        Called when there is data to be sent from the child process back to
               the user.
        """
        flag = findlast(data, ALTERNATE_MODE_FLAGS)
        if flag is not None:
            if flag in START_ALTERNATE_MODE:
                # This code is executed when the child process switches the
                #       terminal into alternate mode. The line below
                #       assumes that the user has opened vim, and writes a
                #       message.
                self.write_master('IEntering special mode.\x1b')
            elif flag in END_ALTERNATE_MODE:
                # This code is executed when the child process switches the
                #       terminal back out of alternate mode. The line below
                #       assumes that the user has returned to the command
                #       prompt.
                self.write_master('echo "Leaving special mode."\r')
        self.write_stdout(data)

    def stdin_read(self, data):
        """
        Called when there is data to be sent from the user/controlling
               terminal down to the child process.
        """
        self.write_master(data)


config.load_kube_config()
c = Configuration()
c.assert_hostname = False
Configuration.set_default(c)
api = core_v1_api.CoreV1Api()
name = 'busybox-test'

resp = None
try:
    resp = api.read_namespaced_pod(name=name,
                                   namespace='default')
except ApiException as e:
    if e.status != 404:
        print("Unknown error: %s" % e)
        exit(1)

if not resp:
    print("Pod %s does not exits. Creating it..." % name)
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
    resp = api.create_namespaced_pod(body=pod_manifest,
                                     namespace='default')
    while True:
        resp = api.read_namespaced_pod(name=name,
                                       namespace='default')
        if resp.status.phase != 'Pending':
            break
        time.sleep(1)
    print("Done.")


# Calling exec interactively with tty enabled.
exec_command = ['/bin/sh']
resp = stream(api.connect_post_namespaced_pod_exec, name, 'default',
              command=exec_command,
              stderr=True, stdin=True,
              stdout=True, tty=True,
              _preload_content=False)

i = Interceptor(k8s_stream=resp)
i.write_stdout('Now in pty mode.\r\n')
i.spawn(sys.argv[1:])
i.write_stdout('\r\nThe pty mode is over.\r\n')
