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
from unittest.mock import AsyncMock, Mock

from kubernetes.aio.client import ApiClient
from kubernetes.aio.utils import create_from_dict, create_from_yaml


class CreateFromYamlTest(IsolatedAsyncioTestCase):

    async def test_create_from_yaml(self):
        api_client = ApiClient()
        api_client.call_api = AsyncMock()
        api_client.call_api.return_value.read = AsyncMock()
        api_client.response_deserialize = Mock()
        api_client.response_deserialize.return_value.data = 'mock-value'

        created = await create_from_yaml(api_client, 'kubernetes/aio/utils/nginx-deployment.yaml')

        # simple check for api call
        self.assertEqual(api_client.call_api.await_args.args[0], 'POST')
        self.assertTrue(api_client.call_api.await_args.args[1].endswith(
            '/apis/apps/v1/namespaces/default/deployments'))

        # returned values
        self.assertEqual(created, [['mock-value']])

    async def test_create_from_dict(self):
        api_client = ApiClient()
        api_client.call_api = AsyncMock()
        api_client.call_api.return_value.read = AsyncMock()
        api_client.response_deserialize = Mock()
        api_client.response_deserialize.return_value.data = 'mock-value'

        created = await create_from_dict(api_client, {
            'apiVersion': 'apps/v1',
            'kind': 'Deployment',
            'metadata': {
                'name': 'nginx-deployment'},
            'spec': {
                'replicas': 3,
                'selector': {'matchLabels': {'app': 'nginx'}},
                'template': {
                    'metadata': {'labels': {'app': 'nginx'}},
                    'spec': {
                        'containers': [{
                            'name': 'nginx',
                            'image': 'nginx:1.7.9',
                        }],
                    },
                },
            }
        })

        # simple check for api call
        self.assertEqual(api_client.call_api.await_args.args[0], 'POST')
        self.assertTrue(api_client.call_api.await_args.args[1].endswith(
            '/apis/apps/v1/namespaces/default/deployments'))

        # returned values
        self.assertEqual(created, ['mock-value'])
