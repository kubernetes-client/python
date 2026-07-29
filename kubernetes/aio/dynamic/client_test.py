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

import asyncio
import unittest
import uuid

from kubernetes.aio.client import api_client
from kubernetes.aio.dynamic import DynamicClient
from kubernetes.aio.dynamic.exceptions import ResourceNotFoundError
from kubernetes.aio.dynamic.resource import ResourceField, ResourceInstance
from kubernetes.aio.e2e_test import base


def short_uuid():
    id_ = str(uuid.uuid4())
    return id_[-12:]


class TestDynamicClient(unittest.IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    async def test_cluster_custom_resources(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            with self.assertRaises(ResourceNotFoundError):
                await client.resources.get(api_version='apps.example.com/v1', kind='ClusterChangeMe')

            crd_api = await client.resources.get(
                api_version='apiextensions.k8s.io/v1',
                kind='CustomResourceDefinition')
            name = 'clusterchangemes.apps.example.com'
            crd_manifest = {
                "apiVersion": "apiextensions.k8s.io/v1",
                "kind": "CustomResourceDefinition",
                "metadata": {
                    "name": name,
                },
                "spec": {
                    "group": "apps.example.com",
                    "names": {
                        "kind": "ClusterChangeMe",
                        "listKind": "ClusterChangeMeList",
                        "plural": "clusterchangemes",
                        "singular": "clusterchangeme",
                    },
                    "scope": "Cluster",
                    "versions": [
                        {
                            "name": "v1",
                            "served": True,
                            "storage": True,
                            "schema": {
                                "openAPIV3Schema": {
                                    "type": "object",
                                    "properties": {
                                        "spec": {
                                            "type": "object",
                                            "properties": {"size": {"type": "integer"}},
                                        }
                                    },
                                }
                            },
                        }
                    ],
                },
            }

            resp = await crd_api.create(crd_manifest)
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            resp = await crd_api.get(
                name=name,
            )
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            try:
                await client.resources.get(api_version='apps.example.com/v1', kind='ClusterChangeMe')
            except ResourceNotFoundError:
                # Need to wait a sec for the discovery layer to get updated
                await asyncio.sleep(2)
            changeme_api = await client.resources.get(
                api_version='apps.example.com/v1', kind='ClusterChangeMe')
            resp = await changeme_api.get()
            self.assertEqual(resp.items, [])
            changeme_name = 'custom-resource' + short_uuid()
            changeme_manifest = {
                'apiVersion': 'apps.example.com/v1',
                'kind': 'ClusterChangeMe',
                'metadata': {
                    'name': changeme_name,
                },
                'spec': {}
            }

            resp = await changeme_api.create(body=changeme_manifest)
            self.assertEqual(resp.metadata.name, changeme_name)

            # watch with timeout
            count = 0
            async for _ in client.watch(changeme_api, timeout=3, namespace="default", name=changeme_name):
                count += 1
            self.assertTrue(count > 0, msg="no events received for watch")

            # without timeout, should be longer than the previous check
            async def _watch_no_timeout():
                async for _ in client.watch(changeme_api, namespace="default", name=changeme_name):
                    pass
            with self.assertRaises(asyncio.exceptions.TimeoutError):
                await asyncio.wait_for(_watch_no_timeout(), timeout=5)

            resp = await changeme_api.get(name=changeme_name)
            self.assertEqual(resp.metadata.name, changeme_name)

            changeme_manifest['spec']['size'] = 3
            resp = await changeme_api.patch(
                body=changeme_manifest,
                content_type='application/merge-patch+json'
            )
            self.assertEqual(resp.spec.size, 3)

            resp = await changeme_api.get(name=changeme_name)
            self.assertEqual(resp.spec.size, 3)

            resp = await changeme_api.get()
            self.assertEqual(len(resp.items), 1)

            await changeme_api.delete(name=changeme_name)

            resp = await changeme_api.get()
            self.assertEqual(len(resp.items), 0)

            await crd_api.delete(name=name)

            await asyncio.sleep(2)
            await client.resources.invalidate_cache()
            with self.assertRaises(ResourceNotFoundError):
                await client.resources.get(api_version='apps.example.com/v1', kind='ClusterChangeMe')

    async def test_namespaced_custom_resources(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            with self.assertRaises(ResourceNotFoundError):
                await client.resources.get(api_version='apps.example.com/v1', kind='ChangeMe')

            crd_api = await client.resources.get(
                api_version='apiextensions.k8s.io/v1',
                kind='CustomResourceDefinition')
            name = 'clusterchangemes.apps.example.com'
            crd_manifest = {
                "apiVersion": "apiextensions.k8s.io/v1",
                "kind": "CustomResourceDefinition",
                "metadata": {
                    "name": name,
                },
                "spec": {
                    "group": "apps.example.com",
                    "names": {
                        "kind": "ClusterChangeMe",
                        "listKind": "ClusterChangeMeList",
                        "plural": "clusterchangemes",
                        "singular": "clusterchangeme",
                    },
                    "scope": "Namespaced",
                    "versions": [
                        {
                            "name": "v1",
                            "served": True,
                            "storage": True,
                            "schema": {
                                "openAPIV3Schema": {
                                    "type": "object",
                                    "properties": {
                                        "spec": {
                                            "type": "object",
                                            "properties": {"size": {"type": "integer"}},
                                        }
                                    },
                                }
                            },
                        }
                    ],
                },
            }

            resp = await crd_api.create(crd_manifest)
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            resp = await crd_api.get(
                name=name,
            )
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            try:
                await client.resources.get(api_version='apps.example.com/v1', kind='ClusterChangeMe')
            except ResourceNotFoundError:
                # Need to wait a sec for the discovery layer to get updated
                await asyncio.sleep(2)
            changeme_api = await client.resources.get(
                api_version='apps.example.com/v1', kind='ClusterChangeMe')
            resp = await changeme_api.get()
            self.assertEqual(resp.items, [])
            changeme_name = 'custom-resource' + short_uuid()
            changeme_manifest = {
                'apiVersion': 'apps.example.com/v1',
                'kind': 'ClusterChangeMe',
                'metadata': {
                    'name': changeme_name,
                },
                'spec': {}
            }

            resp = await changeme_api.create(body=changeme_manifest, namespace='default')
            self.assertEqual(resp.metadata.name, changeme_name)

            resp = await changeme_api.get(name=changeme_name, namespace='default')
            self.assertEqual(resp.metadata.name, changeme_name)

            changeme_manifest['spec']['size'] = 3
            resp = await changeme_api.patch(
                body=changeme_manifest,
                namespace='default',
                content_type='application/merge-patch+json'
            )
            self.assertEqual(resp.spec.size, 3)

            resp = await changeme_api.get(name=changeme_name, namespace='default')
            self.assertEqual(resp.spec.size, 3)

            resp = await changeme_api.get(namespace='default')
            self.assertEqual(len(resp.items), 1)

            resp = await changeme_api.get()
            self.assertEqual(len(resp.items), 1)

            await changeme_api.delete(name=changeme_name, namespace='default')

            resp = await changeme_api.get(namespace='default')
            self.assertEqual(len(resp.items), 0)

            resp = await changeme_api.get()
            self.assertEqual(len(resp.items), 0)

            await crd_api.delete(name=name)

            await asyncio.sleep(2)
            await client.resources.invalidate_cache()
            with self.assertRaises(ResourceNotFoundError):
                await client.resources.get(api_version='apps.example.com/v1', kind='ChangeMe')

    async def test_service_apis(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            api = await client.resources.get(api_version='v1', kind='Service')

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

            resp = await api.create(
                body=service_manifest,
                namespace='default'
            )
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            resp = await api.get(
                name=name,
                namespace='default'
            )
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status)

            service_manifest['spec']['ports'] = [{'name': 'new',
                                                  'port': 8080,
                                                  'protocol': 'TCP',
                                                  'targetPort': 8080}]
            resp = await api.patch(
                body=service_manifest,
                name=name,
                namespace='default'
            )
            self.assertEqual(2, len(resp.spec.ports))
            self.assertTrue(resp.status)

            await api.delete(name=name, body={}, namespace='default')

    async def test_replication_controller_apis(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            api = await client.resources.get(
                api_version='v1', kind='ReplicationController')

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

            resp = await api.create(
                body=rc_manifest, namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertEqual(2, resp.spec.replicas)

            resp = await api.get(
                name=name, namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertEqual(2, resp.spec.replicas)

            await api.delete(
                name=name,
                namespace='default',
                propagation_policy='Background')

    async def test_configmap_apis(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            api = await client.resources.get(api_version='v1', kind='ConfigMap')

            name = 'test-configmap-' + short_uuid()
            test_configmap = {
                "kind": "ConfigMap",
                "apiVersion": "v1",
                "metadata": {
                    "name": name,
                    "labels": {
                        "e2e-test": "true",
                    },
                },
                "data": {
                    "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                    "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\n"
                }
            }

            resp = await api.create(
                body=test_configmap, namespace='default'
            )
            self.assertEqual(name, resp.metadata.name)

            resp = await api.get(
                name=name, namespace='default', label_selector="e2e-test=true")
            self.assertEqual(name, resp.metadata.name)

            count = 0
            async for _ in client.watch(api, timeout=3, namespace="default", name=name):
                count += 1
            self.assertTrue(count > 0, msg="no events received for watch")

            test_configmap['data']['config.json'] = "{}"
            await api.patch(name=name, namespace='default', body=test_configmap)

            await api.delete(name=name, body={}, namespace='default')

            resp = await api.get(
                namespace='default',
                pretty=True,
                label_selector="e2e-test=true")
            self.assertEqual([], resp.items)

    async def test_node_apis(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)

            api = await client.resources.get(api_version='v1', kind='Node')
            nodes = await api.get()
            for item in nodes.items:
                node = await api.get(name=item.metadata.name)
                self.assertTrue(len(dict(node.metadata.labels)) > 0)

    # test_node_apis_partial_object_metadata lists all nodes in the cluster,
    # but only retrieves object metadata
    async def test_node_apis_partial_object_metadata(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            api = await client.resources.get(api_version='v1', kind='Node')

            params = {
                'header_params': {
                    'Accept': 'application/json;as=PartialObjectMetadataList;v=v1;g=meta.k8s.io'}}
            resp = await api.get(**params)
            self.assertEqual('PartialObjectMetadataList', resp.kind)
            self.assertEqual('meta.k8s.io/v1', resp.apiVersion)

            params = {
                'header_params': {
                    'aCcePt': 'application/json;as=PartialObjectMetadataList;v=v1;g=meta.k8s.io'}}
            resp = await api.get(**params)
            self.assertEqual('PartialObjectMetadataList', resp.kind)
            self.assertEqual('meta.k8s.io/v1', resp.apiVersion)

    async def test_server_side_apply_api(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            api = await client.resources.get(api_version='v1', kind='Pod')

            name = 'pod-' + short_uuid()
            pod_manifest = {
                'apiVersion': 'apps/v1',
                'kind': 'Deployment',
                'metadata': {'labels': {'name': name},
                             'name': name},
                'spec': {'template': {'spec': {'containers': [{
                    'image': 'nginx',
                    'name': 'nginx',
                    'ports': [{'containerPort': 80,
                               'protocol': 'TCP'}]}]}}}}

            resp = await api.server_side_apply(
                namespace='default', body=pod_manifest,
                field_manager='kubernetes-unittests', dry_run="All")
        self.assertEqual('kubernetes-unittests', resp.metadata.managedFields[0].manager)


class TestDynamicClientSerialization(unittest.IsolatedAsyncioTestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()
        cls.pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {'name': 'foo-pod'},
            'spec': {'containers': [{'name': "main", 'image': "busybox"}]},
        }

    async def test_dict_type(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            self.assertEqual(client.serialize_body(self.pod_manifest), self.pod_manifest)

    async def test_resource_instance_type(self):
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            inst = ResourceInstance(client, self.pod_manifest)
            self.assertEqual(client.serialize_body(inst), self.pod_manifest)

    async def test_resource_field(self):
        """`ResourceField` is a special type which overwrites `__getattr__` method to return `None`
        when a non-existent attribute was accessed. which means it can pass any `hasattr(...)` tests.
        """
        params = {
            "foo": "bar",
            "self": True
        }
        res = ResourceField(params)
        self.assertEqual(res["foo"], params["foo"])
        self.assertEqual(res["self"], params["self"])

        # method will return original object when it doesn't know how to proceed
        async with api_client.ApiClient(configuration=self.config) as apic:
            client = await DynamicClient(apic)
            serialized = client.serialize_body(res)
        self.assertDictEqual(serialized, res.to_dict())
