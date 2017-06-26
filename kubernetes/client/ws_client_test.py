# Copyright 2017 The Kubernetes Authors.
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

import ssl
import unittest
import websocket

from .ws_client import get_websocket_url, websocket_call
from kubernetes.client import configuration
from unittest.mock import patch


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

    @patch.object(websocket._http, '_can_use_sni')
    @patch.object(websocket._http, '_open_socket')
    @patch.object(ssl.SSLContext, 'load_verify_locations')
    def test_use_of_correct_ca_cert(self, load_verify_locations, *ignored):
        # arrange
        expected = '/expected-ca.pem'
        configuration.ssl_ca_cert = expected
        load_verify_locations.side_effect = Exception("need not go further")

        # act
        with self.assertRaises(Exception):
            websocket_call(configuration, 'https://localhost',
                           {}, None, True, {})

        # assert
        actual = load_verify_locations.call_args[1]['cafile']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
