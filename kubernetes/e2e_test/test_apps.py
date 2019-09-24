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
import yaml

from kubernetes.client import api_client
from kubernetes.client.apis import apps_v1_api
from kubernetes.client.models import v1_delete_options
from kubernetes.e2e_test import base


class TestClientApps(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    def test_create_deployment(self):
        client = api_client.ApiClient(configuration=self.config)
        api = apps_v1_api.AppsV1Api(client)
        name = 'nginx-deployment-' + str(uuid.uuid4())
        deployment = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: %s
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.15.4
        ports:
        - containerPort: 80
'''
        resp = api.create_namespaced_deployment(
            body=yaml.safe_load(deployment % name),
            namespace="default")
        resp = api.read_namespaced_deployment(name, 'default')
        self.assertIsNotNone(resp)

        options = v1_delete_options.V1DeleteOptions()
        resp = api.delete_namespaced_deployment(name, 'default', body=options)

    def test_create_daemonset(self):
        client = api_client.ApiClient(configuration=self.config)
        api = apps_v1_api.AppsV1Api(client)
        name = 'nginx-app-' + str(uuid.uuid4())
        daemonset = {
            'apiVersion': 'apps/v1',
            'kind': 'DaemonSet',
            'metadata': {
                'labels': {'app': 'nginx'},
                'name': '%s' % name,
            },
            'spec': {
                'selector': {
                    'matchLabels': {'app': 'nginx'},
                },
                'template': {
                    'metadata': {
                        'labels': {'app': 'nginx'},
                        'name': name},
                    'spec': {
                        'containers': [
                            {'name': 'nginx-app',
                             'image': 'nginx:1.15.4'},
                        ],
                    },
                },
                'updateStrategy': {
                    'type': 'RollingUpdate',
                },
            }
        }
        resp = api.create_namespaced_daemon_set('default', body=daemonset)
        resp = api.read_namespaced_daemon_set(name, 'default')
        self.assertIsNotNone(resp)

        options = v1_delete_options.V1DeleteOptions()
        resp = api.delete_namespaced_daemon_set(name, 'default', body=options)
