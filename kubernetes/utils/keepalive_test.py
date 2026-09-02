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
import types
import unittest
from unittest import mock

import urllib3

from kubernetes.client import Configuration
from kubernetes.client.rest import RESTClientObject
from kubernetes.utils import keepalive
from kubernetes.utils.keepalive import tcp_keepalive_socket_options


def fake_socket_module(**names):
    """A stand-in for the socket module exposing only the given names."""

    defaults = {
        'SOL_SOCKET': socket.SOL_SOCKET,
        'SO_KEEPALIVE': socket.SO_KEEPALIVE,
        'IPPROTO_TCP': socket.IPPROTO_TCP,
    }
    defaults.update(names)
    return types.SimpleNamespace(**defaults)


class TestTcpKeepaliveSocketOptions(unittest.TestCase):

    def test_defaults_match_client_go(self):
        options = tcp_keepalive_socket_options()

        self.assertIn((socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1), options)
        self.assertIn(
            (socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 30), options)
        self.assertIn(
            (socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 15), options)
        self.assertIn((socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 9), options)

    def test_keeps_the_urllib3_defaults(self):
        options = tcp_keepalive_socket_options()

        defaults = urllib3.connection.HTTPConnection.default_socket_options
        for default in defaults:
            self.assertIn(default, options)

    def test_custom_timings(self):
        options = tcp_keepalive_socket_options(idle=5, interval=2, count=3)

        self.assertIn((socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 5), options)
        self.assertIn((socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 2), options)
        self.assertIn((socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 3), options)

    def test_timings_must_be_positive(self):
        for kwargs in ({'idle': 0}, {'interval': 0}, {'count': 0}):
            with self.assertRaises(ValueError):
                tcp_keepalive_socket_options(**kwargs)

    def test_options_are_setsockopt_triples(self):
        for option in tcp_keepalive_socket_options():
            self.assertEqual(3, len(option))
            for item in option:
                self.assertIsInstance(item, int)

    def test_options_apply_to_a_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            for level, name, value in tcp_keepalive_socket_options():
                sock.setsockopt(level, name, value)

            self.assertEqual(
                1, sock.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE))
            self.assertEqual(
                30, sock.getsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE))

    def test_falls_back_to_tcp_keepalive_on_macos(self):
        macos = fake_socket_module(
            TCP_KEEPALIVE=0x10,
            TCP_KEEPINTVL=socket.TCP_KEEPINTVL,
            TCP_KEEPCNT=socket.TCP_KEEPCNT,
        )
        with mock.patch.object(keepalive, 'socket', macos):
            options = tcp_keepalive_socket_options()

        self.assertIn((socket.IPPROTO_TCP, 0x10, 30), options)

    def test_skips_options_the_platform_lacks(self):
        with mock.patch.object(keepalive, 'socket', fake_socket_module()):
            options = tcp_keepalive_socket_options()

        self.assertIn((socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1), options)
        defaults = urllib3.connection.HTTPConnection.default_socket_options
        self.assertEqual(len(defaults) + 1, len(options))


class TestConfigurationKeepAlive(unittest.TestCase):

    def pool_socket_options(self, configuration):
        rest_client = RESTClientObject(configuration)
        return rest_client.pool_manager.connection_pool_kw.get(
            'socket_options')

    def test_off_by_default(self):
        configuration = Configuration()

        self.assertFalse(configuration.keep_alive)
        self.assertIsNone(self.pool_socket_options(configuration))

    def test_enabled(self):
        configuration = Configuration()
        configuration.keep_alive = True

        self.assertEqual(
            tcp_keepalive_socket_options(),
            self.pool_socket_options(configuration))

    def test_socket_options_win(self):
        configuration = Configuration()
        configuration.keep_alive = True
        configuration.socket_options = [
            (socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)]

        self.assertEqual(
            configuration.socket_options,
            self.pool_socket_options(configuration))


if __name__ == "__main__":
    unittest.main()
