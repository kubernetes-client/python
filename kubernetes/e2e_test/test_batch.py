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

import unittest
import uuid

from kubernetes.client import api_client
from kubernetes.client.apis import batch_v1_api
from kubernetes.client.configuration import configuration
from kubernetes.e2e_test import base


class TestClientBatch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.API_URL = 'http://127.0.0.1:8080/'
        cls.config = configuration

    @unittest.skipUnless(
        base.is_k8s_running(), "Kubernetes is not available")
    def test_job_apis(self):
        client = api_client.ApiClient(self.API_URL, config=self.config)
        api = batch_v1_api.BatchV1Api(client)

        name = 'test-job-' + str(uuid.uuid4())
        job_manifest = {
            'kind': 'Job',
            'spec': {
                'template':
                    {'spec':
                        {'containers': [
                            {'image': 'busybox',
                             'name': name,
                             'command': ["sh", "-c", "sleep 5"]
                             }],
                            'restartPolicy': 'Never'},
                        'metadata': {'name': name}}},
            'apiVersion': 'batch/v1',
            'metadata': {'name': name}}

        resp = api.create_namespaced_job(
            body=job_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)

        resp = api.read_namespaced_job(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)

        resp = api.delete_namespaced_job(
            name=name, body={}, namespace='default')


class TestClientBatchSSL(TestClientBatch):

    @classmethod
    def setUpClass(cls):
        cls.API_URL = 'https://127.0.0.1:8443/'
        cls.config = base.setSSLConfiguration()
