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

import uuid
from unittest import IsolatedAsyncioTestCase

from kubernetes_asyncio.client import api_client
from kubernetes_asyncio.client.api import core_v1_api
from kubernetes_asyncio.e2e_test import base


class TestApplyPatch(IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_apply_patch(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = "cm-test" + str(uuid.uuid4())
        manifest = dict(
            apiVersion="v1",
            kind="ConfigMap",
            metadata=dict(
                namespace="default",
                name=name,
            ),
            data={"hello": "world!"},
        )

        resp = await api.patch_namespaced_config_map(
            _content_type="application/apply-patch+yaml",
            field_manager="test",
            body=manifest,
            name=name,
            namespace="default",
        )
        self.assertEqual(name, resp.metadata.name)

        cm = await api.read_namespaced_config_map(name=name, namespace="default")
        self.assertEqual(name, cm.metadata.name)

        # strategic merge patch for object
        cm.data["new"] = "value"
        resp = await api.patch_namespaced_config_map(
            field_manager="test",
            body=cm,
            name=name,
            namespace="default",
        )
        self.assertEqual(resp.data, {'hello': 'world!', 'new': 'value'})

        resp = await api.delete_namespaced_config_map(
            name=name, body={}, namespace="default"
        )
