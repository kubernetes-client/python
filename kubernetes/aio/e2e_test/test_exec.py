# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import asyncio
import uuid
from unittest import IsolatedAsyncioTestCase

from aiohttp import WSMsgType

from kubernetes.aio import client
from kubernetes.aio.e2e_test import base
from kubernetes.aio.stream import WsApiClient
from kubernetes.aio.stream.ws_client import (
    CLOSE_CHANNEL, ERROR_CHANNEL, STDERR_CHANNEL, STDIN_CHANNEL,
    STDOUT_CHANNEL, V5_CHANNEL_PROTOCOL,
)


class TestExec(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_v5_exec(self):
        name = 'async-exec-' + uuid.uuid4().hex
        namespace = 'default'
        pod = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {'name': name},
            'spec': {
                'containers': [{
                    'name': 'busybox',
                    'image': 'busybox:1.36',
                    'command': ['/bin/sh', '-c', 'sleep 3600'],
                }],
            },
        }
        async with client.ApiClient(configuration=self.config) as api_client:
            core = client.CoreV1Api(api_client)
            await core.create_namespaced_pod(namespace, pod)
            try:
                async def wait_ready():
                    while True:
                        current = await core.read_namespaced_pod(name, namespace)
                        if current.status.phase in ('Failed', 'Succeeded'):
                            self.fail('Pod terminated before becoming ready: %s'
                                      % current.status)
                        if (current.status.container_statuses and
                                current.status.container_statuses[0].ready):
                            return
                        await asyncio.sleep(1)

                await asyncio.wait_for(wait_ready(), timeout=180)

                async with WsApiClient(configuration=self.config) as ws_client:
                    exec_api = client.CoreV1Api(ws_client)
                    result = await asyncio.wait_for(
                        exec_api.connect_get_namespaced_pod_exec(
                            name, namespace,
                            command=['/bin/sh', '-c',
                                     'printf stdout; printf stderr >&2'],
                            stderr=True, stdin=False, stdout=True, tty=False,
                        ),
                        timeout=30,
                    )
                    self.assertIn('stdout', result)
                    self.assertIn('stderr', result)

                    websocket = await exec_api.connect_get_namespaced_pod_exec_without_preload_content(
                        name, namespace,
                        command=['/bin/sh', '-c',
                                 'value=$(cat); printf "received:%s" "$value"; '
                                 'printf error-output >&2'],
                        stderr=True, stdin=True, stdout=True, tty=False,
                    )
                    async with websocket as ws:
                        self.assertEqual(V5_CHANNEL_PROTOCOL, ws.protocol)
                        await ws.send_bytes(bytes([STDIN_CHANNEL]) + b'hello')
                        await ws.send_bytes(bytes([CLOSE_CHANNEL, STDIN_CHANNEL]))

                        async def receive_output():
                            channels = {
                                STDOUT_CHANNEL: b'',
                                STDERR_CHANNEL: b'',
                                ERROR_CHANNEL: b'',
                            }
                            async for message in ws:
                                self.assertEqual(WSMsgType.BINARY, message.type)
                                channel, data = message.data[0], message.data[1:]
                                if channel in channels:
                                    channels[channel] += data
                            return channels

                        channels = await asyncio.wait_for(receive_output(), timeout=30)
                        self.assertEqual(b'received:hello', channels[STDOUT_CHANNEL])
                        self.assertEqual(b'error-output', channels[STDERR_CHANNEL])
                        self.assertEqual(
                            0, ws_client.parse_error_data(channels[ERROR_CHANNEL])
                        )
            finally:
                await core.delete_namespaced_pod(name, namespace)
