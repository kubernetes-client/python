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

import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlparse

from kubernetes import client

from . import ws_client
from .stream import _websocket_request


class StreamTest(unittest.TestCase):
    def test_generated_portforward_preserves_multiple_ports(self):
        api = client.CoreV1Api(client.ApiClient(client.Configuration(
            host='https://example.com',
            proxy='',
            no_proxy='',
        )))

        with (
            patch.object(ws_client, 'create_websocket') as create_websocket,
            patch.object(ws_client, 'PortForward') as port_forward,
        ):
            result = _websocket_request(
                ws_client.portforward_call,
                {'_preload_content': False},
                api.connect_get_namespaced_pod_portforward,
                'pod',
                'default',
                ports='80,443',
            )

        self.assertIs(port_forward.return_value, result)
        port_forward.assert_called_once_with(
            create_websocket.return_value,
            [80, 443],
        )
        websocket_url = create_websocket.call_args.args[1]
        self.assertEqual('wss', urlparse(websocket_url).scheme)
        self.assertEqual(
            ['80,443'], parse_qs(urlparse(websocket_url).query)['ports'])

    def test_generated_api_request_uses_websocket_transport(self):
        request = {}

        def websocket_call(configuration, method, url, **kwargs):
            request.update(method=method, url=url, kwargs=kwargs)
            return ws_client.WSResponse(data='output', status=200)

        api = client.CoreV1Api()
        output = _websocket_request(
            websocket_call,
            None,
            api.connect_get_namespaced_pod_exec,
            'pod',
            'default',
            command=['echo', 'hello'],
        )

        self.assertEqual('output', output)
        self.assertEqual('GET', request['method'])
        self.assertIn(
            '/api/v1/namespaces/default/pods/pod/exec?',
            request['url'],
        )
        self.assertIn('command=echo&command=hello', request['url'])


if __name__ == '__main__':
    unittest.main()
