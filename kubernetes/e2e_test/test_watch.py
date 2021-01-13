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

from kubernetes import watch
from kubernetes.client import api_client
from kubernetes.client.api import core_v1_api
from kubernetes.e2e_test import base


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


def config_map_with_value(name, value):
    return {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {
            "name": name,
            "labels": {"e2e-tests": "true"},
        },
        "data": {
            "key": value,
            "config": "dummy",
        }
    }


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    def test_watch_configmaps(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        # create a configmap
        name_a = 'configmap-a-' + short_uuid()
        configmap_a = config_map_with_value(name_a, "a")
        api.create_namespaced_config_map(
            body=configmap_a, namespace='default')

        # list all configmaps and extract the resource version
        resp = api.list_namespaced_config_map('default', label_selector="e2e-tests=true")
        rv = resp.metadata.resource_version

        # create another configmap
        name_b = 'configmap-b-' + short_uuid()
        configmap_b = config_map_with_value(name_b, "b")
        api.create_namespaced_config_map(
            body=configmap_b, namespace='default')

        # patch configmap b
        configmap_b['data']['config'] = "{}"
        api.patch_namespaced_config_map(
            name=name_b, namespace='default', body=configmap_b)

        # delete all configmaps
        api.delete_collection_namespaced_config_map(
            namespace='default', label_selector="e2e-tests=true")

        w = watch.Watch()
        # expect to observe all events happened after the initial LIST
        expect = ['ADDED', 'MODIFIED', 'DELETED', 'DELETED']
        i = 0
        # start watching with the resource version we got from the LIST
        for event in w.stream(api.list_namespaced_config_map,
                              namespace='default',
                              resource_version=rv,
                              timeout_seconds=5,
                              label_selector="e2e-tests=true"):
            self.assertEqual(event['type'], expect[i])
            # Kubernetes doesn't guarantee the order of the two objects
            # being deleted
            if i < 2:
                self.assertEqual(event['object'].metadata.name, name_b)
            i = i + 1

        self.assertEqual(i, 4)
