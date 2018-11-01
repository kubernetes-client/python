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

from kubernetes import utils, client
from kubernetes.e2e_test import base

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    def test_app_yaml(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/apps-deployment.yaml")
        self.assertEqual("apps/v1beta1", 
            k8s_api.get_api_resources().group_version)
        dep = k8s_api.read_namespaced_deployment(name="nginx-app",
            namespace="default")
        self.assertIsNotNone(dep)
        resp = k8s_api.delete_namespaced_deployment(
            name="nginx-app", namespace="default", 
            body={})
        
    def test_extension_yaml(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/extensions-deployment.yaml")
        self.assertEqual("extensions/v1beta1", 
            k8s_api.get_api_resources().group_version)
        dep = k8s_api.read_namespaced_deployment(name="nginx-deployment", 
            namespace="default")
        self.assertIsNotNone(dep)
        resp = k8s_api.delete_namespaced_deployment(
            name="nginx-deployment", namespace="default", 
            body={})
    
    def test_core_pod_yaml(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/core-pod.yaml")
        self.assertEqual("v1", 
            k8s_api.get_api_resources().group_version)
        pod = k8s_api.read_namespaced_pod(name="myapp-pod", 
            namespace="default")
        self.assertIsNotNone(pod)
        resp = k8s_api.delete_namespaced_pod(
            name="myapp-pod", namespace="default",
            body={})

    def test_core_service_yaml(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/core-service.yaml")
        self.assertEqual("v1", 
            k8s_api.get_api_resources().group_version)
        svc = k8s_api.read_namespaced_service(name="my-service",
            namespace="default")
        self.assertIsNotNone(svc)
        resp = k8s_api.delete_namespaced_service(
            name="my-service", namespace="default",
            body={})
        
    def test_core_namespace_yaml(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/core-namespace.yaml")
        self.assertEqual("v1", 
            k8s_api.get_api_resources().group_version)
        nmsp = k8s_api.read_namespace(name="development")
        self.assertIsNotNone(nmsp)
        resp = k8s_api.delete_namespace(name="development", body={})

    def test_deployment_in_namespace(self):
        k8s_client = client.ApiClient(configuration=self.config)
        core_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/core-namespace-dep.yaml")
        self.assertEqual("v1", 
            core_api.get_api_resources().group_version)
        nmsp = core_api.read_namespace(name="dep")
        self.assertIsNotNone(nmsp)
        dep_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/extensions-deployment-dep.yaml")
        dep = dep_api.read_namespaced_deployment(name="nginx-deployment", 
            namespace="dep")
        self.assertIsNotNone(dep)
        resp = dep_api.delete_namespaced_deployment(
            name="nginx-deployment", namespace="dep", 
            body={})
        resp = core_api.delete_namespace(name="dep", body={})
        
    def test_api_service(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        k8s_api = utils.create_from_yaml(k8s_client, 
            "kubernetes/e2e_test/test_yaml/api-service.yaml")
        self.assertEqual("apiregistration.k8s.io/v1beta1", 
            k8s_api.get_api_resources().group_version)
        svc = k8s_api.read_api_service(
            name="v1alpha1.wardle.k8s.io")
        self.assertIsNotNone(svc)
        resp = k8s_api.delete_api_service(
            name="v1alpha1.wardle.k8s.io", body={})