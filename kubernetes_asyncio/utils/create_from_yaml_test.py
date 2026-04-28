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

from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from kubernetes_asyncio.utils import create_from_dict, create_from_yaml


class CreateFromYamlTest(IsolatedAsyncioTestCase):

    async def test_create_from_yaml(self):
        api_client = AsyncMock()
        api_client.call_api = AsyncMock()
        api_client.call_api.return_value = 'mock-value'

        created = await create_from_yaml(api_client, 'kubernetes_asyncio/utils/nginx-deployment.yaml')

        # simple check for api call
        self.assertEqual(api_client.call_api.call_args[0][0],
                         '/apis/apps/v1/namespaces/{namespace}/deployments')

        # returned values
        self.assertEqual(created, [['mock-value']])

    async def test_create_from_dict(self):
        api_client = AsyncMock()
        api_client.call_api = AsyncMock()
        api_client.call_api.return_value = 'mock-value'

        created = await create_from_dict(api_client, {
            'apiVersion': 'apps/v1',
            'kind': 'Deployment',
            'metadata': {
                'name': 'nginx-deployment'},
            'spec': {
                'replicas': 3,
            }
        })

        # simple check for api call
        self.assertEqual(api_client.call_api.call_args[0][0],
                         '/apis/apps/v1/namespaces/{namespace}/deployments')

        # returned values
        self.assertEqual(created, ['mock-value'])
