# Copyright 2026 The Kubernetes Authors.
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

import socket
from typing import List, Tuple

import urllib3


# client-go dials the API server with a 30 second keepalive:
# https://github.com/kubernetes/client-go/blob/master/transport/cache.go
# Go folds that single duration into the idle time and leaves the probe
# interval and count at its own defaults, 15 seconds and 9 probes:
# https://github.com/golang/go/blob/master/src/net/tcpsock.go
# https://github.com/golang/go/blob/master/src/net/dial.go
DEFAULT_IDLE = 30
DEFAULT_INTERVAL = 15
DEFAULT_COUNT = 9

SocketOptions = List[Tuple[int, int, int]]


def tcp_keepalive_socket_options(
    idle: int = DEFAULT_IDLE,
    interval: int = DEFAULT_INTERVAL,
    count: int = DEFAULT_COUNT,
) -> SocketOptions:
    """Build urllib3 socket options that enable TCP keepalive.

    The defaults match what client-go asks the kernel for, so an idle
    watch is probed after ``idle`` seconds and dropped after ``count``
    unanswered probes ``interval`` seconds apart.

    The returned list starts from ``urllib3``'s own default socket
    options, which disable Nagle's algorithm. urllib3 replaces its
    defaults with whatever list it is given rather than merging, so
    building on them keeps that behaviour.

    Options the platform does not define are left out: macOS spells the
    idle time ``TCP_KEEPALIVE``, and Windows only grew the idle and
    interval options in Windows 10 1709.
    """

    for name, value in (('idle', idle), ('interval', interval),
                        ('count', count)):
        if value < 1:
            raise ValueError('%s must be at least 1' % name)

    options = list(urllib3.connection.HTTPConnection.default_socket_options)
    options.append((socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1))

    if hasattr(socket, 'TCP_KEEPIDLE'):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, idle))
    elif hasattr(socket, 'TCP_KEEPALIVE'):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPALIVE, idle))

    if hasattr(socket, 'TCP_KEEPINTVL'):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval))

    if hasattr(socket, 'TCP_KEEPCNT'):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPCNT, count))

    return options
