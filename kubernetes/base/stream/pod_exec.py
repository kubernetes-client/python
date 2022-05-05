# Copyright 2022 The Kubernetes Authors.
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

import functools
import io
import json
import selectors
import ssl
import threading
import time

import kubernetes.client.rest
import websocket
from . import ws_client

PIPE = -1
STDOUT = -2
DEVNULL = -3

STDIN_CHANNEL = chr(ws_client.STDIN_CHANNEL).encode()
STDOUT_CHANNEL = ws_client.STDOUT_CHANNEL
STDERR_CHANNEL = ws_client.STDERR_CHANNEL
ERROR_CHANNEL = ws_client.ERROR_CHANNEL
RESIZE_CHANNEL = chr(ws_client.RESIZE_CHANNEL).encode()
NOT_SET = object()


class Popen:
    """Execute a process in a pod container using a subprocess.Popen like
    interface. A mixture of connect_get_namespaced_pod_exec arguments and
    Popen arguments are implemented.

    :param func method: The kubernetes client method to call, typically connect_get_namespaced_pod_exec.    :param str name: The pod name to run in.
    :param str namespace: The namespace name the pod to run in.
    :param str[] command: The remote command to executem, not executed within a shell.
    :param str container: The container to execute the command in. Defaults to only container if there is only one container in the pod.
    :param bool|int stdin: Redirect the standard input stream of the pod for this call. True, False, PIPE, or DEVNULL, default False.
    :param bool|int stdout: Redirect the standard output stream of the pod for this call. True, False, PIPE, or DEVNULL, default False.
    :param bool|int stderr: Redirect the standard error stream of the pod for this call. True, False, PIPE, STDOUT, or DEVNULL, default False.
    :param bool tty: TTY if true indicates that a tty will be allocated for the exec call. Defaults to false.
    :param int bufsize: stream buffer size. -1 is system default, 0 is unbuffered, 1 in text mode is line buffered.
    :param str encoding: text encoding format if text mode.
    :param str errors: text encoding error strictness if text mode.
    :param bool text: Force enabling or disabling text mode. Default is tty value if encoding and errors are not set.
    :return: Popen instance
    """
    def __init__(self, method, name, namespace, *,
                 bufsize=-1, encoding=None, errors=None, text=None,
                 **kwargs):
        self.name = name
        self.namespace = namespace
        self.container = kwargs.get('container')
        self.command = kwargs.get('command')
        self.tty = kwargs.get('tty')
        self.result = None
        self.returncode = None
        self.encoding = encoding
        self.errors = errors
        self.stdin = None
        self.stdout = None
        self.stderr = None

        # Replicate much of subprocess.Popen.__init__'s logic here.
        if encoding is None and errors is None and text is None:
            self.text_mode = bool(self.tty)
        else:
            self.text_mode = bool(encoding or errors or text)
        if bufsize is None:
            bufsize = -1
        if not isinstance(bufsize, int):
            raise TypeError('bufsize must be an integer')
        if self.text_mode:
            if bufsize == 0:
                raise ValueError('bufsize of 0 not valid in text mode')
            if bufsize == 1:
                line_buffering = True
                bufsize = -1
            else:
                line_buffering = False
        if bufsize < 0:
            bufsize = io.DEFAULT_BUFFER_SIZE

        stdin = self._get_std_arg(kwargs, 'stdin', PIPE, DEVNULL)
        if stdin == PIPE:
            self.stdin = self._Input(self)
            if bufsize > 0:
                self.stdin = io.BufferedWriter(self.stdin, bufsize)
                if self.text_mode:
                    self.stdin = io.TextIOWrapper(self.stdin, encoding=encoding, errors=errors,
                                                  line_buffering=line_buffering, write_through=True)

        self._stdout_raw = None
        self._stderr_raw = None
        stdout = self._get_std_arg(kwargs, 'stdout', PIPE, DEVNULL)
        stderr = self._get_std_arg(kwargs, 'stderr', PIPE, STDOUT, DEVNULL)
        if stdout == PIPE:
            self._stdout_raw = self._Output(self)
            if bufsize == 0:
                self.stdout = self._stdout_raw
            else:
                self.stdout = io.BufferedReader(self._stdout_raw, bufsize)
                if self.text_mode:
                    self.stdout = io.TextIOWrapper(self.stdout, encoding=encoding, errors=errors)
            if stderr == STDOUT:
                self._stderr_raw = self._stdout_raw
        if stderr == PIPE:
            self._stderr_raw = self._Output(self)
            if bufsize == 0:
                self.stderr = self._stderr_raw
            else:
                self.stderr = io.BufferedReader(self._stderr_raw, bufsize)
                if self.text_mode:
                    self.stderr = io.TextIOWrapper(self.stderr, encoding=encoding, errors=errors)
        self._timeout = None
        self._recv_data_lock = threading.Lock()

        kwargs['_preload_content'] = False
        client = method.__self__.api_client
        client_request = client.request
        try:
            # Hijack the kubernetes client request method with our own _request method.
            client.request = functools.partial(self._request, client.configuration)
            method(name, namespace, **kwargs)
        finally:
            client.request = client_request

    def _get_std_arg(self, kwargs, name, *allowed):
        value = kwargs.get(name)
        if value in (None, False):
            return None
        if value is True:
            return PIPE
        if not isinstance(value, int):
            raise TypeError(name + ' must be boolean or integer')
        if value not in allowed:
            raise ValueError(name + ' invalid integer value')
        kwargs[name] = True
        return value

    def _request(self, configuration, _method, url, **kwargs):
        # This method gets called by the kubernetes client to do the http request.
        # Instead use the supplied url, query parameters, and headers to
        # establish a websocket connection.
        try:
            url = ws_client.get_websocket_url(url, kwargs.get('query_params'))
            self._websocket = ws_client.create_websocket(configuration, url, kwargs.get('headers'))
            self._is_ssl = isinstance(self._websocket.sock, ssl.SSLSocket)
            self._selector = selectors.DefaultSelector()
            self._selector.register(self._websocket, selectors.EVENT_READ)
        except (Exception, KeyboardInterrupt, SystemExit) as e:
            raise kubernetes.client.rest.ApiException(status=0, reason=str(e))

    @property
    def closed(self):
        return not self._websocket.sock or self._websocket.sock.fileno() == -1

    def close(self):
        self._selector.close()
        self._websocket.shutdown()

    @property
    def timeout(self):
        """Timeout from now of all subsequest reads of stdout and stderr.
        Returns 0 for non-blocking reads and returns None for blocking reads."""
        if self._timeout is None:
            return None
        now = time.time()
        if now > self._timeout:
            return 0
        return self._timeout - now

    @timeout.setter
    def timeout(self, timeout):
        if timeout is None:
            self._timeout = None
        else:
            if not isinstance(timeout, (int, float)):
                raise TypeError('timeout is not a number')
            self._timeout = time.time() + timeout

    def resize(self, width, height):
        """Inform the remote process the size of the TTY screen."""
        b = json.dumps({'Width':width,'Height':height}, separators=(',',':')).encode()
        self._websocket.send(RESIZE_CHANNEL + b, websocket.ABNF.OPCODE_BINARY)

    def communicate(self, input=None, timeout=NOT_SET):
        """Interact with process: Send data to stdin and close it.
        Read data from stdout and stderr, until end-of-file is
        reached.  Wait for process to terminate.

        The optional "input" argument should be data to be sent to the
        child process, or None, if no data should be sent to the child.
        communicate() returns a tuple (stdout, stderr).

        By default, all communication is in bytes, and therefore any
        "input" should be bytes, and the (stdout, stderr) will be bytes.
        If in text mode (indicated by self.text_mode), any "input" should
        be a string, and (stdout, stderr) will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode
        is triggered by setting any of tty, text, encoding, or errors.
        """
        if self.closed:
            raise ValueError('Cannot call communicate after websocket close')
        if timeout is not NOT_SET:
            self.timeout = timeout
        try:
            if self.stdin:
                if input:
                    self.stdin.write(input)
                self.stdin.close()
            if self.stdout:
                stdout = self.stdout.read()
                self.stdout.close()
            else:
                stdout = None
            if self.stderr:
                stderr = self.stderr.read()
                self.stderr.close()
            else:
                stderr = None
            self.wait()
            return stdout, stderr
        finally:
            self.close()

    def wait(self, timeout=NOT_SET):
        """Wait for child process to terminate; returns self.returncode."""
        if timeout is not NOT_SET:
            self.timeout = timeout
        try:
            if self.stdout:
                self.stdout.close()
            if self.stderr:
                self.stderr.close()
            while True:
                status = self._recv_data_frame()
                if not status:
                    if status is None:
                        raise TimeoutError()
                    return self.returncode
        finally:
            self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, value, traceback):
        self.close()

    class _Input(io.RawIOBase):
        def __init__(self, popen):
            super(Popen._Input, self).__init__()
            self._popen = popen

        def writable(self):
            return True

        def write(self, b):
            if self._popen.closed:
                return 0
            self._popen._websocket.send(STDIN_CHANNEL + b, websocket.ABNF.OPCODE_BINARY)
            return len(b)

        def close(self):
            super(Popen._Input, self).close()
            # This needs to close stdin on the remote process,
            # but the websocket protocol did not implement it.
            # See: https://github.com/kubernetes/kubernetes/issues/89899

    class _Output(io.RawIOBase):
        def __init__(self, popen):
            super(Popen._Output, self).__init__()
            self._popen = popen
            self._frames = []
            self._ix = 1

        def readable(self):
            return True

        def readinto(self, b):
            while not self._frames:
                status = self._popen._recv_data_frame()
                if not status:
                    if status is None:
                        raise TimeoutError()
                    return 0
            size = len(self._frames[0]) - self._ix
            if size <= len(b):
                b[:size] = self._frames[0][self._ix:]
                del self._frames[0]
                self._ix = 1
            else:
                size = len(b)
                b[:] = self._frames[0][self._ix:self._ix+size]
                self._ix += size
            return size

        def close(self):
            super(Popen._Output, self).close()
            self._frames = []
            self._ix = 1

    def _recv_data_frame(self):
        # Returns True if frame read, False if websocket is closed,
        # and None if timeed out with no frames read.
        if self.closed:
            return False
        timeout = self.timeout
        if not self._recv_data_lock.acquire(timeout != 0, timeout if timeout is not None and timeout > 0 else -1):
            return None
        try:
            if not self._is_ssl or not self._websocket.sock.pending():
                if not self._selector.select(timeout):
                    return None
            opcode, frame = self._websocket.recv_data_frame(True)
            if opcode == websocket.ABNF.OPCODE_BINARY:
                channel = frame.data[0]
                if channel == STDOUT_CHANNEL:
                    if self._stdout_raw and not self._stdout_raw.closed and len(frame.data) > 1:
                        self._stdout_raw._frames.append(frame.data)
                    return True
                if channel == STDERR_CHANNEL:
                    if self._stderr_raw and not self._stderr_raw.closed and len(frame.data) > 1:
                        self._stderr_raw._frames.append(frame.data)
                    return True
                if channel == ERROR_CHANNEL:
                    if frame.data[1] == ord('{') and frame.data[-1] == ord('}'):
                        self.result = json.loads(frame.data[1:])
                        if self.result['status'] == 'Success':
                            self.returncode = 0
                        elif self.result['reason'] == 'NonZeroExitCode':
                            for cause in self.result['details']['causes']:
                                if cause['reason'] == 'ExitCode':
                                    self.returncode = int(cause['message'])
                    else:
                        self.result = frame.data[1:].decode()
                    self.close()
                    return False
                self.close()
                raise websocket.WebSocketPayloadException('Unexpected websocket channel: ' + str(channel))
            if opcode in (websocket.ABNF.OPCODE_PING, websocket.ABNF.OPCODE_PONG):
                return True
            if opcode == websocket.ABNF.OPCODE_CLOSE:
                self.close()
                return False
            self.close()
            raise websocket.WebSocketProtocolException('Unexpected websocket opcode: ' + str(opcode))
        finally:
            self._recv_data_lock.release()
