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
import unittest
import uuid

from kubernetes.client import api_client
from kubernetes.client.apis import core_v1_api
from kubernetes.e2e_test import base


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    def test_pod_apis(self):
        client = api_client.ApiClient(config=self.config)
        api = core_v1_api.CoreV1Api(client)

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

        resp = api.create_namespaced_pod(body=pod_manifest,
                                         namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)

        exec_command = ['/bin/sh',
                        '-c',
                        'for i in $(seq 1 3); do date; done']
        resp = api.connect_get_namespaced_pod_exec(name, 'default',
                                                   command=exec_command,
                                                   stderr=False, stdin=False,
                                                   stdout=True, tty=False)
        print('EXEC response : %s' % resp)
        self.assertEqual(3, len(resp.splitlines()))

        exec_command = 'uptime'
        resp = api.connect_post_namespaced_pod_exec(name, 'default',
                                                    command=exec_command,
                                                    stderr=False, stdin=False,
                                                    stdout=True, tty=False)
        print('EXEC response : %s' % resp)
        self.assertEqual(1, len(resp.splitlines()))

        resp = api.connect_post_namespaced_pod_exec(name, 'default',
                                                    command='/bin/sh',
                                                    stderr=True, stdin=True,
                                                    stdout=True, tty=False,
                                                    _preload_content=False)
        resp.write_stdin("echo test string 1\n")
        line = resp.readline_stdout(timeout=5)
        self.assertFalse(resp.peek_stderr())
        self.assertEqual("test string 1", line)
        resp.write_stdin("echo test string 2 >&2\n")
        line = resp.readline_stderr(timeout=5)
        self.assertFalse(resp.peek_stdout())
        self.assertEqual("test string 2", line)
        resp.write_stdin("exit\n")
        resp.update(timeout=5)
        self.assertFalse(resp.is_open())

        number_of_pods = len(api.list_pod_for_all_namespaces().items)
        self.assertTrue(number_of_pods > 0)

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_service_apis(self):
        client = api_client.ApiClient(config=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        service_manifest = {'apiVersion': 'v1',
                            'kind': 'Service',
                            'metadata': {'labels': {'name': name},
                                         'name': name,
                                         'resourceversion': 'v1'},
                            'spec': {'ports': [{'name': 'port',
                                                'port': 80,
                                                'protocol': 'TCP',
                                                'targetPort': 80}],
                                     'selector': {'name': name}}}

        resp = api.create_namespaced_service(body=service_manifest,
                                             namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = api.read_namespaced_service(name=name,
                                           namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        service_manifest['spec']['ports'] = [{'name': 'new',
                                              'port': 8080,
                                              'protocol': 'TCP',
                                              'targetPort': 8080}]
        resp = api.patch_namespaced_service(body=service_manifest,
                                            name=name,
                                            namespace='default')
        self.assertEqual(2, len(resp.spec.ports))
        self.assertTrue(resp.status)

        resp = api.delete_namespaced_service(name=name,
                                             namespace='default')

    def test_replication_controller_apis(self):
        client = api_client.ApiClient(config=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        rc_manifest = {
            'apiVersion': 'v1',
            'kind': 'ReplicationController',
            'metadata': {'labels': {'name': name},
                         'name': name},
            'spec': {'replicas': 2,
                     'selector': {'name': name},
                     'template': {'metadata': {
                         'labels': {'name': name}},
                         'spec': {'containers': [{
                             'image': 'nginx',
                             'name': 'nginx',
                             'ports': [{'containerPort': 80,
                                        'protocol': 'TCP'}]}]}}}}

        resp = api.create_namespaced_replication_controller(
            body=rc_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.read_namespaced_replication_controller(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.delete_namespaced_replication_controller(
            name=name, body={}, namespace='default')

    def test_configmap_apis(self):
        client = api_client.ApiClient(config=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'test-configmap-' + short_uuid()
        test_configmap = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": {
                "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n"
            }
        }

        resp = api.create_namespaced_config_map(
            body=test_configmap, namespace='default'
        )
        self.assertEqual(name, resp.metadata.name)

        resp = api.read_namespaced_config_map(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)

        test_configmap['data']['config.json'] = "{}"
        resp = api.patch_namespaced_config_map(
            name=name, namespace='default', body=test_configmap)

        resp = api.delete_namespaced_config_map(
            name=name, body={}, namespace='default')

        resp = api.list_namespaced_config_map('default', pretty=True)
        self.assertEqual([], resp.items)

    def test_node_apis(self):
        client = api_client.ApiClient(config=self.config)
        api = core_v1_api.CoreV1Api(client)

        for item in api.list_node().items:
            node = api.read_node(name=item.metadata.name)
            self.assertTrue(len(node.metadata.labels) > 0)
            self.assertTrue(isinstance(node.metadata.labels, dict))