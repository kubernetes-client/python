# Copyright 2018 The Kubernetes Authors.
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

import unittest
from unittest.mock import MagicMock, patch

from . import ws_client as ws_client_module
from .ws_client import get_websocket_url, WSClient, V5_CHANNEL_PROTOCOL, V4_CHANNEL_PROTOCOL, CLOSE_CHANNEL, STDIN_CHANNEL
from .ws_client import websocket_proxycare
from kubernetes.client.configuration import Configuration
import os
import socket
import threading
import pytest
from kubernetes import stream, client, config
import websocket

try:
    import urllib3
    urllib3.disable_warnings()
except ImportError:
    pass
@pytest.fixture(autouse=True)
def dummy_kubeconfig(tmp_path, monkeypatch):
    # Creating a kubeconfig
    content = """
        apiVersion: v1
        kind: Config
        clusters:
        - name: default
          cluster:
            server: http://127.0.0.1:8888
        contexts:
        - name: default
          context:
            cluster: default
            user: default
        users:
        - name: default
          user: {}
        current-context: default
        """
    cfg_file = tmp_path / "kubeconfig"
    cfg_file.write_text(content)
    monkeypatch.setenv("KUBECONFIG", str(cfg_file))


def dictval(dict_obj, key, default=None):
		
    return dict_obj.get(key, default)

class DummyProxy(threading.Thread):
    """
    A minimal HTTP proxy that flags any CONNECT request and returns 200 OK.
    Listens on 127.0.0.1:8888 by default.
    """
    def __init__(self, host='127.0.0.1', port=8888):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.received_connect = False
        self._server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_sock.bind((self.host, 0))
        self._server_sock.listen(1)

    def run(self):
        conn, _ = self._server_sock.accept()
        try:
            data = conn.recv(1024).decode('utf-8', errors='ignore')
            if data.startswith('CONNECT '):
                self.received_connect = True
                conn.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")
        finally:
            conn.close()

class WSClientTest(unittest.TestCase):

    def test_websocket_client(self):
        for url, ws_url in [
                ('http://localhost/api', 'ws://localhost/api'),
                ('https://localhost/api', 'wss://localhost/api'),
                ('https://domain.com/api', 'wss://domain.com/api'),
                ('https://api.domain.com/api', 'wss://api.domain.com/api'),
                ('http://api.domain.com', 'ws://api.domain.com'),
                ('https://api.domain.com', 'wss://api.domain.com'),
                ('http://api.domain.com/', 'ws://api.domain.com/'),
                ('https://api.domain.com/', 'wss://api.domain.com/'),
                ]:
            self.assertEqual(get_websocket_url(url), ws_url)

    def test_websocket_proxycare(self):
        for proxy, idpass, no_proxy, expect_host, expect_port, expect_auth, expect_noproxy in [
                ( None,                             None,        None,                            None,                None, None, None ),
                ( 'http://proxy.example.com:8080/', None,        None,                            'proxy.example.com', 8080, None, None ),
                ( 'http://proxy.example.com:8080/', 'user:pass', None,                            'proxy.example.com', 8080, ('user','pass'), None),
                ( 'http://proxy.example.com:8080/', 'user:pass', '',                              'proxy.example.com', 8080, ('user','pass'), None),
                ( 'http://proxy.example.com:8080/', 'user:pass', '*',                             'proxy.example.com', 8080, ('user','pass'), ['*']),
                ( 'http://proxy.example.com:8080/', 'user:pass', '.example.com',                  'proxy.example.com', 8080, ('user','pass'), ['.example.com']),
                ( 'http://proxy.example.com:8080/', 'user:pass', 'localhost,.local,.example.com',  'proxy.example.com', 8080, ('user','pass'), ['localhost','.local','.example.com']),
                ]:
            #  input setup
            cfg = Configuration()
            if proxy:
                cfg.proxy = proxy
            if idpass:
                cfg.proxy_headers = urllib3.util.make_headers(proxy_basic_auth=idpass)
            if no_proxy is not None:
                cfg.no_proxy = no_proxy
						
						 
            connect_opts = websocket_proxycare({}, cfg, None, None)
            assert dictval(connect_opts, 'http_proxy_host') == expect_host
            assert dictval(connect_opts, 'http_proxy_port') == expect_port
            assert dictval(connect_opts, 'http_proxy_auth') == expect_auth
            assert dictval(connect_opts, 'http_no_proxy') == expect_noproxy


class WSClientProtocolTest(unittest.TestCase):
    """Tests for WSClient V5 protocol handling"""

    def setUp(self):
        # Mock configuration to avoid real connections in WSClient.__init__
        self.config_mock = MagicMock()
        self.config_mock.assert_hostname = False
        self.config_mock.api_key = {}
        self.config_mock.proxy = None
        self.config_mock.ssl_ca_cert = None
        self.config_mock.cert_file = None
        self.config_mock.key_file = None
        self.config_mock.verify_ssl = True

    def test_create_websocket_header(self):
        """Verify sec-websocket-protocol header requests v5 first"""
        # Patch WebSocket class in the module
        with patch.object(ws_client_module, 'WebSocket', autospec=True) as mock_ws_cls:
            mock_ws = mock_ws_cls.return_value

            WSClient(self.config_mock, "ws://test", headers=None, capture_all=True)

            mock_ws.connect.assert_called_once()
            call_args = mock_ws.connect.call_args
            # connect(url, **options)
            # check kwargs for 'header'
            kwargs = call_args[1]
            self.assertIn('header', kwargs)
            expected_header = f"sec-websocket-protocol: {V5_CHANNEL_PROTOCOL},{V4_CHANNEL_PROTOCOL}"
            self.assertIn(expected_header, kwargs['header'])

    def test_close_channel_v5(self):
        """Verify close_channel sends correct frame when v5 is negotiated"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create:
            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True)
            client.close_channel(0)

            mock_ws.send.assert_called_with(bytes([CLOSE_CHANNEL, STDIN_CHANNEL]), opcode=websocket.ABNF.OPCODE_BINARY)

    def test_close_channel_v4(self):
        """Verify close_channel does nothing when v4 is negotiated"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create:
            mock_ws = MagicMock()
            mock_ws.subprotocol = V4_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True)
            client.close_channel(0)

            mock_ws.send.assert_not_called()

    def test_update_receives_close_v5(self):
        """Verify update processes close signal when v5 is negotiated"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create, \
            patch('select.select') as mock_select:

            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_ws.sock.fileno.return_value = 10

            # Setup frame with close signal for channel 0
            frame = MagicMock()
            frame.data = bytes([CLOSE_CHANNEL, STDIN_CHANNEL])
            mock_ws.recv_data_frame.return_value = (websocket.ABNF.OPCODE_BINARY, frame)

            mock_create.return_value = mock_ws
            # Make select return ready
            mock_select.return_value = ([mock_ws.sock], [], [])

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True)
            client.update(timeout=0)

            self.assertIn(0, client._closed_channels)

    def test_update_ignores_close_signal_v4(self):
        """Verify update treats 0xFF as regular data (or ignores signal interpretation) when v4"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create, \
            patch('select.select') as mock_select:

            mock_ws = MagicMock()
            mock_ws.subprotocol = V4_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_ws.sock.fileno.return_value = 10

            # Setup frame that looks like close signal but should be treated as data
            frame = MagicMock()
            frame.data = bytes([CLOSE_CHANNEL, STDIN_CHANNEL])
            mock_ws.recv_data_frame.return_value = (websocket.ABNF.OPCODE_BINARY, frame)

            mock_create.return_value = mock_ws
            mock_select.return_value = ([mock_ws.sock], [], [])

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True, binary=True) # binary=True to avoid decode errors
            client.update(timeout=0)

            # Should NOT be in closed channels
            self.assertNotIn(0, client._closed_channels)
            # Should be in data channels (channel 255 with data \x00)
            # Code: channel = data[0] (255), data = data[1:] (\x00)
            # if channel (255) not in _channels...
            self.assertIn(255, client._channels)
            self.assertEqual(client._channels[255], b'\x00')

    def test_readline_channel_closed_with_leftover_data(self):
        """Verify readline_channel flushes remaining buffer when channel is closed"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create:
            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True, binary=False)

            # Simulate some data in the channel buffer, and then close it
            client._channels[1] = "hello"
            client._closed_channels.add(1)

            # First call to readline should flush "hello" even though there is no newline
            line1 = client.readline_channel(1)
            self.assertEqual(line1, "hello")

            # Subsequent call should return empty string
            line2 = client.readline_channel(1)
            self.assertEqual(line2, "")

    def test_readline_channel_closed_with_leftover_data_binary(self):
        """Verify readline_channel flushes remaining buffer when channel is closed in binary mode"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create:
            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True, binary=True)

            # Simulate some bytes in the channel buffer, and then close it
            client._channels[1] = b"hello-binary"
            client._closed_channels.add(1)

            # First call to readline should flush leftover bytes
            line1 = client.readline_channel(1)
            self.assertEqual(line1, b"hello-binary")

            # Subsequent call should return empty bytes
            line2 = client.readline_channel(1)
            self.assertEqual(line2, b"")

    def test_read_channel_closed_with_leftover_data(self):
        """Verify read_channel drains leftover data and then short-circuits on closed channel"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create:
            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_ws.sock.fileno.return_value = 10
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True, binary=False)

            # Simulate leftover data and closed channel
            client._channels[1] = "hello"
            client._closed_channels.add(1)

            # First call should drain data
            data1 = client.read_channel(1)
            self.assertEqual(data1, "hello")

            # Subsequent call should short-circuit and return empty string
            # Patch `update` to assert it is NOT called (short-circuit)
            with patch.object(client, 'update') as mock_update:
                data2 = client.read_channel(1)
                self.assertEqual(data2, "")
                mock_update.assert_not_called()

    def test_peek_channel_closed_with_leftover_data(self):
        """Verify peek_channel allows peeking leftover data and then short-circuits after draining"""
        with patch.object(ws_client_module, 'create_websocket') as mock_create, \
             patch('select.poll') as mock_poll:
            mock_poll.return_value.poll.return_value = []
            mock_ws = MagicMock()
            mock_ws.subprotocol = V5_CHANNEL_PROTOCOL
            mock_ws.connected = True
            mock_ws.sock.fileno.return_value = 10
            mock_create.return_value = mock_ws

            client = WSClient(self.config_mock, "ws://test", headers=None, capture_all=True, binary=False)

            # Simulate leftover data and closed channel
            client._channels[1] = "hello"
            client._closed_channels.add(1)

            # First peek should return data without draining
            data1 = client.peek_channel(1)
            self.assertEqual(data1, "hello")

            # Second peek should still return data
            data2 = client.peek_channel(1)
            self.assertEqual(data2, "hello")

            # Drain it
            client.read_channel(1)

            # Now peek should short-circuit and return empty string
            # Patch `update` to assert it is NOT called (short-circuit)
            with patch.object(client, 'update') as mock_update:
                data3 = client.peek_channel(1)
                self.assertEqual(data3, "")
                mock_update.assert_not_called()



@pytest.fixture(scope="module")
def dummy_proxy():
    #Dummy Proxy
    proxy = DummyProxy(port=8888)
    proxy.start()
    yield proxy

@pytest.fixture(autouse=True)
def clear_proxy_env(monkeypatch):
    for var in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy"):
        monkeypatch.delenv(var, raising=False)

def apply_proxy_to_conf():
    #apply HTTPS_PROXY env var and set it as global.   
    cfg = client.Configuration.get_default_copy()
    cfg.proxy = os.getenv("HTTPS_PROXY")
    cfg.no_proxy = os.getenv("NO_PROXY", "")
    client.Configuration.set_default(cfg)

def test_rest_call_ignores_env(dummy_proxy, monkeypatch):
    # HTTPS_PROXY to dummy proxy
    monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:8888")
    # Avoid real HTTP request
    monkeypatch.setattr(client.CoreV1Api, "list_namespace", lambda self, *_args, **_kwargs: None)
    # Load config using kubeconfig
    config.load_kube_config(config_file=os.environ["KUBECONFIG"])
    apply_proxy_to_conf()
    # HTTPS_PROXY to dummy proxy
    monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:8888")
    config.load_kube_config(config_file=os.environ["KUBECONFIG"])
    apply_proxy_to_conf()
    v1 = client.CoreV1Api()
    v1.list_namespace(_preload_content=False)
    assert not dummy_proxy.received_connect, "REST path should ignore HTTPS_PROXY"

def test_websocket_call_honors_env(dummy_proxy, monkeypatch):
    # set HTTPS_PROXY again
    monkeypatch.setenv("HTTPS_PROXY", "http://127.0.0.1:8888")
    # Load kubeconfig
    config.load_kube_config(config_file=os.environ["KUBECONFIG"])
    apply_proxy_to_conf()
    opts = websocket_proxycare({}, client.Configuration.get_default_copy(), None, None)
    assert opts.get('http_proxy_host') == '127.0.0.1'
    assert opts.get('http_proxy_port') == 8888
    # Optionally verify no_proxy parsing
    assert opts.get('http_no_proxy') is None

if __name__ == '__main__':
    unittest.main()
