# -*- coding: utf-8 -*-

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

import time
import uuid
from unittest import IsolatedAsyncioTestCase

from kubernetes.aio.client import api_client
from kubernetes.aio.dynamic import DynamicClient
from kubernetes.aio.e2e_test import base

# from kubernetes.aio.stream import WsApiClient


def short_uuid():
    id_ = str(uuid.uuid4())
    return id_[-12:]


class TestDynamicClient(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_pod_apis(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            pod_resource = await client.resources.get(kind='Pod', api_version='v1')

            name = 'busybox-test-' + short_uuid()
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

            resp = await client.create(pod_resource, body=pod_manifest, namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)

            while True:
                resp = await client.get(pod_resource, name=name, namespace='default')
                self.assertEqual(name, resp.metadata.name)
                self.assertTrue(resp.status.phase)
                if resp.status.phase != 'Pending':
                    break
                time.sleep(1)

            resp = await client.get(pod_resource)
            number_of_pods = len(resp.items)
            self.assertTrue(number_of_pods > 0)

            await client.delete(pod_resource, name=name, body={}, namespace='default')
