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
from decimal import Decimal
from os import path

import yaml
import time

from kubernetes import client, utils
from kubernetes.client.rest import ApiException
from kubernetes.e2e_test import base
from kubernetes.utils import quantity


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()
        cls.path_prefix = "kubernetes/e2e_test/test_yaml/"
        cls.test_namespace = "e2e-test-utils"
        k8s_client = client.api_client.ApiClient(configuration=cls.config)
        core_v1 = client.CoreV1Api(api_client=k8s_client)
        body = client.V1Namespace(
            metadata=client.V1ObjectMeta(
                name=cls.test_namespace))

        # Delete the namespace if it already exists
        try:
            core_v1.delete_namespace(name=cls.test_namespace)
            time.sleep(10)  # Wait for the namespace to be deleted
        except ApiException as e:
            if e.status != 404:
                raise

        core_v1.create_namespace(body=body)

    @classmethod
    def tearDownClass(cls):
        k8s_client = client.api_client.ApiClient(configuration=cls.config)
        core_v1 = client.CoreV1Api(api_client=k8s_client)
        core_v1.delete_namespace(name=cls.test_namespace)

    # Tests for creating individual API objects

    def test_create_apps_deployment_from_yaml(self):
        """
        Should be able to create an apps/v1 deployment.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml")
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("nginx-app", dep.metadata.name)
        self.assertEqual(
            "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
        self.assertEqual(
            80, dep.spec.template.spec.containers[0].ports[0].container_port)
        self.assertEqual("nginx", dep.spec.template.spec.containers[0].name)
        self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
        self.assertEqual(3, dep.spec.replicas)

        while True:
            try:
                app_api.delete_namespaced_deployment(
                    name="nginx-app", namespace="default",
                    body={})
                break
            except ApiException:
                continue

    def test_create_apps_deployment_from_yaml_with_apply_is_idempotent(self):
        """
        Should be able to create an apps/v1 deployment.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        try:
            utils.process_from_yaml(
                k8s_client, self.path_prefix + "apps-deployment.yaml")
            app_api = client.AppsV1Api(k8s_client)
            dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                     namespace="default")
            self.assertIsNotNone(dep)
            self.assertEqual("nginx-app", dep.metadata.name)
            self.assertEqual(
                "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
            self.assertEqual(
                80, dep.spec.template.spec.containers[0].ports[0].container_port)
            self.assertEqual(
                "nginx", dep.spec.template.spec.containers[0].name)
            self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
            self.assertEqual(3, dep.spec.replicas)

            utils.process_from_yaml(
                k8s_client, self.path_prefix + "apps-deployment.yaml", apply=True)
            dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                     namespace="default")
            self.assertIsNotNone(dep)
            self.assertEqual("nginx-app", dep.metadata.name)
            self.assertEqual(
                "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
            self.assertEqual(
                80, dep.spec.template.spec.containers[0].ports[0].container_port)
            self.assertEqual(
                "nginx", dep.spec.template.spec.containers[0].name)
            self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
            self.assertEqual(3, dep.spec.replicas)
        except Exception as e:
            self.fail(e)
        finally:
            while True:
                try:
                    app_api.delete_namespaced_deployment(
                        name="nginx-app", namespace="default",
                        body={})
                    break
                except ApiException:
                    continue

    def test_create_apps_deployment_from_yaml_object(self):
        """
        Should be able to pass YAML objects directly to helper function.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        _path = self.path_prefix + "apps-deployment.yaml"
        with open(path.abspath(_path)) as f:
            yaml_objects = yaml.safe_load_all(f)
            utils.process_from_yaml(
                k8s_client,
                yaml_objects=yaml_objects,
            )
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("nginx-app", dep.metadata.name)
        self.assertEqual(
            "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
        self.assertEqual(
            80, dep.spec.template.spec.containers[0].ports[0].container_port)
        self.assertEqual("nginx", dep.spec.template.spec.containers[0].name)
        self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
        self.assertEqual(3, dep.spec.replicas)

        while True:
            try:
                app_api.delete_namespaced_deployment(
                    name="nginx-app", namespace="default",
                    body={})
                break
            except ApiException:
                continue

    def test_create_apps_deployment_from_yaml_obj(self):
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        with open(self.path_prefix + "apps-deployment.yaml") as f:
            yml_obj = yaml.safe_load(f)

        yml_obj["metadata"]["name"] = "nginx-app-3"

        utils.process_from_dict(k8s_client, yml_obj)

        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app-3",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("nginx-app-3", dep.metadata.name)
        self.assertEqual(
            "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
        self.assertEqual(
            80, dep.spec.template.spec.containers[0].ports[0].container_port)
        self.assertEqual("nginx", dep.spec.template.spec.containers[0].name)
        self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
        self.assertEqual(3, dep.spec.replicas)

        app_api.delete_namespaced_deployment(
            name="nginx-app-3", namespace="default",
            body={})

    def test_create_pod_from_yaml(self):
        """
        Should be able to create a pod.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-pod.yaml")
        core_api = client.CoreV1Api(k8s_client)
        pod = core_api.read_namespaced_pod(name="myapp-pod",
                                           namespace="default")
        self.assertIsNotNone(pod)
        self.assertEqual("myapp-pod", pod.metadata.name)
        self.assertEqual("busybox", pod.spec.containers[0].image)
        self.assertEqual("myapp-container", pod.spec.containers[0].name)

        core_api.delete_namespaced_pod(
            name="myapp-pod", namespace="default",
            body={})

    def test_create_service_from_yaml(self):
        """
        Should be able to create a service.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-service.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="my-service",
                                               namespace="default")
        self.assertIsNotNone(svc)
        self.assertEqual("my-service", svc.metadata.name)
        self.assertEqual("MyApp", svc.spec.selector["app"])

        core_api.delete_namespaced_service(
            name="my-service", namespace="default",
            body={})

    def test_create_namespace_from_yaml(self):
        """
        Should be able to create a namespace.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-namespace.yaml")
        core_api = client.CoreV1Api(k8s_client)
        nmsp = core_api.read_namespace(name="development")

        self.assertIsNotNone(nmsp)
        self.assertEqual("development", nmsp.metadata.name)

        core_api.delete_namespace(name="development", body={})

    def test_create_rbac_role_from_yaml(self):
        """
        Should be able to create a rbac role.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml")
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        self.assertEqual("pod-reader", rbac_role.metadata.name)
        self.assertEqual("pods", rbac_role.rules[0].resources[0])

        rbac_api.delete_namespaced_role(
            name="pod-reader", namespace="default", body={})

    def test_create_rbac_role_from_yaml_with_verbose_enabled(self):
        """
        Should be able to create a rbac role with verbose enabled.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml", verbose=True)
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        self.assertEqual("pod-reader", rbac_role.metadata.name)
        self.assertEqual("pods", rbac_role.rules[0].resources[0])

        rbac_api.delete_namespaced_role(
            name="pod-reader", namespace="default", body={})

    def test_create_deployment_non_default_namespace_from_yaml(self):
        """
        Should be able to create a namespace "dep",
        and then create a deployment in the just-created namespace.
        """
        k8s_client = client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "dep-namespace.yaml")
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "dep-deployment.yaml")
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)
        nmsp = core_api.read_namespace(name="dep")
        self.assertIsNotNone(nmsp)
        self.assertEqual("dep", nmsp.metadata.name)

        dep = ext_api.read_namespaced_deployment(name="nginx-deployment",
                                                 namespace="dep")
        self.assertIsNotNone(dep)
        ext_api.delete_namespaced_deployment(
            name="nginx-deployment", namespace="dep",
            body={})
        core_api.delete_namespace(name="dep", body={})

    def test_create_apiservice_from_yaml_with_conflict(self):
        """
        Should be able to create an API service.
        Should verify that creating the same API service should
        fail due to conflict.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "api-service.yaml")
        reg_api = client.ApiregistrationV1Api(k8s_client)
        svc = reg_api.read_api_service(
            name="v1alpha1.wardle.k8s.io")
        self.assertIsNotNone(svc)
        self.assertEqual("v1alpha1.wardle.k8s.io", svc.metadata.name)
        self.assertEqual("wardle.k8s.io", svc.spec.group)
        self.assertEqual("v1alpha1", svc.spec.version)

        with self.assertRaises(utils.FailToProcessError) as cm:
            utils.process_from_yaml(
                k8s_client, "kubernetes/e2e_test/test_yaml/api-service.yaml")
        exp_error = ('Error from server (Conflict): '
                     '{"kind":"Status","apiVersion":"v1","metadata":{},'
                     '"status":"Failure",'
                     '"message":"apiservices.apiregistration.k8s.io '
                     '\\"v1alpha1.wardle.k8s.io\\" already exists",'
                     '"reason":"AlreadyExists",'
                     '"details":{"name":"v1alpha1.wardle.k8s.io",'
                     '"group":"apiregistration.k8s.io","kind":"apiservices"},'
                     '"code":409}\n'
                     )
        self.assertEqual(exp_error, str(cm.exception))
        reg_api.delete_api_service(
            name="v1alpha1.wardle.k8s.io", body={})

    # Tests for creating API objects from lists

    def test_create_general_list_from_yaml(self):
        """
        Should be able to create a service and a deployment
        from a kind: List yaml file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="list-service-test",
                                               namespace="default")
        self.assertIsNotNone(svc)
        self.assertEqual("list-service-test", svc.metadata.name)
        self.assertEqual("list-deployment-test", svc.spec.selector["app"])

        dep = ext_api.read_namespaced_deployment(name="list-deployment-test",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("list-deployment-test", dep.metadata.name)
        self.assertEqual(
            "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
        self.assertEqual(1, dep.spec.replicas)

        core_api.delete_namespaced_service(name="list-service-test",
                                           namespace="default", body={})
        ext_api.delete_namespaced_deployment(name="list-deployment-test",
                                             namespace="default", body={})

    def test_create_namespace_list_from_yaml(self):
        """
        Should be able to create two namespaces
        from a kind: NamespaceList yaml file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "namespace-list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        nmsp_1 = core_api.read_namespace(name="mock-1")
        self.assertIsNotNone(nmsp_1)
        self.assertEqual("mock-1", nmsp_1.metadata.name)
        self.assertEqual("mock-1", nmsp_1.metadata.labels["name"])

        nmsp_2 = core_api.read_namespace(name="mock-2")
        self.assertIsNotNone(nmsp_2)
        self.assertEqual("mock-2", nmsp_2.metadata.name)
        self.assertEqual("mock-2", nmsp_2.metadata.labels["name"])

        core_api.delete_namespace(name="mock-1", body={})
        core_api.delete_namespace(name="mock-2", body={})

    def test_create_implicit_service_list_from_yaml_with_conflict(self):
        """
        Should be able to create two services from a kind: ServiceList
        json file that implicitly indicates the kind of individual objects
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        with self.assertRaises(utils.FailToProcessError):
            utils.process_from_yaml(
                k8s_client, self.path_prefix + "implicit-svclist.json")
        core_api = client.CoreV1Api(k8s_client)
        svc_3 = core_api.read_namespaced_service(name="mock-3",
                                                 namespace="default")
        self.assertIsNotNone(svc_3)
        self.assertEqual("mock-3", svc_3.metadata.name)
        self.assertEqual("mock-3", svc_3.metadata.labels["app"])

        svc_4 = core_api.read_namespaced_service(name="mock-4",
                                                 namespace="default")
        self.assertIsNotNone(svc_4)
        self.assertEqual("mock-4", svc_4.metadata.name)
        self.assertEqual("mock-4", svc_4.metadata.labels["app"])

        core_api.delete_namespaced_service(name="mock-3",
                                           namespace="default", body={})
        core_api.delete_namespaced_service(name="mock-4",
                                           namespace="default", body={})

    # Tests for creating multi-resource from directory

    def test_create_multi_resource_from_directory(self):
        """
        Should be able to create a service and a replication controller
        from a directory
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_directory(
            k8s_client, self.path_prefix + "multi-resource/")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock",
                                               namespace="default")
        self.assertIsNotNone(svc)
        self.assertEqual("mock", svc.metadata.name)
        self.assertEqual("mock", svc.metadata.labels["app"])
        self.assertEqual("mock", svc.spec.selector["app"])

        ctr = core_api.read_namespaced_replication_controller(
            name="mock", namespace="default")
        self.assertIsNotNone(ctr)
        self.assertEqual("mock", ctr.metadata.name)
        self.assertEqual("mock", ctr.spec.template.metadata.labels["app"])
        self.assertEqual("mock", ctr.spec.selector["app"])
        self.assertEqual(1, ctr.spec.replicas)
        self.assertEqual("k8s.gcr.io/pause:2.0",
                         ctr.spec.template.spec.containers[0].image)
        self.assertEqual("mock-container",
                         ctr.spec.template.spec.containers[0].name)

        core_api.delete_namespaced_replication_controller(
            name="mock", namespace="default", propagation_policy="Background")
        core_api.delete_namespaced_service(name="mock",
                                           namespace="default", body={})

    # Tests for multi-resource yaml objects

    def test_create_from_multi_resource_yaml(self):
        """
        Should be able to create a service and a replication controller
        from a multi-resource yaml file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock",
                                               namespace="default")
        self.assertIsNotNone(svc)
        self.assertEqual("mock", svc.metadata.name)
        self.assertEqual("mock", svc.metadata.labels["app"])
        self.assertEqual("mock", svc.spec.selector["app"])

        ctr = core_api.read_namespaced_replication_controller(
            name="mock", namespace="default")
        self.assertIsNotNone(ctr)
        self.assertEqual("mock", ctr.metadata.name)
        self.assertEqual("mock", ctr.spec.template.metadata.labels["app"])
        self.assertEqual("mock", ctr.spec.selector["app"])
        self.assertEqual(1, ctr.spec.replicas)
        self.assertEqual("k8s.gcr.io/pause:2.0",
                         ctr.spec.template.spec.containers[0].image)
        self.assertEqual("mock-container",
                         ctr.spec.template.spec.containers[0].name)

        core_api.delete_namespaced_replication_controller(
            name="mock", namespace="default", propagation_policy="Background")
        core_api.delete_namespaced_service(name="mock",
                                           namespace="default", body={})

    def test_create_from_list_in_multi_resource_yaml(self):
        """
        Should be able to create the items in the PodList and a deployment
        specified in the multi-resource file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource-with-list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        app_api = client.AppsV1Api(k8s_client)
        pod_0 = core_api.read_namespaced_pod(
            name="mock-pod-0", namespace="default")
        self.assertIsNotNone(pod_0)
        self.assertEqual("mock-pod-0", pod_0.metadata.name)
        self.assertEqual("mock-pod-0", pod_0.metadata.labels["app"])
        self.assertEqual("mock-pod-0", pod_0.spec.containers[0].name)
        self.assertEqual("busybox", pod_0.spec.containers[0].image)

        pod_1 = core_api.read_namespaced_pod(
            name="mock-pod-1", namespace="default")
        self.assertIsNotNone(pod_1)
        self.assertEqual("mock-pod-1", pod_1.metadata.name)
        self.assertEqual("mock-pod-1", pod_1.metadata.labels["app"])
        self.assertEqual("mock-pod-1", pod_1.spec.containers[0].name)
        self.assertEqual("busybox", pod_1.spec.containers[0].image)

        dep = app_api.read_namespaced_deployment(
            name="mock", namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("mock", dep.metadata.name)
        self.assertEqual("mock", dep.spec.template.metadata.labels["app"])
        self.assertEqual(3, dep.spec.replicas)

        core_api.delete_namespaced_pod(
            name="mock-pod-0", namespace="default", body={})
        core_api.delete_namespaced_pod(
            name="mock-pod-1", namespace="default", body={})
        app_api.delete_namespaced_deployment(
            name="mock", namespace="default", body={})

    def test_create_from_multi_resource_yaml_with_conflict(self):
        """
        Should be able to create a service from the first yaml file.
        Should fail to create the same service from the second yaml file
        and create a replication controller.
        Should raise an exception for failure to create the same service twice.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "yaml-conflict-first.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock-2",
                                               namespace="default")
        self.assertIsNotNone(svc)
        self.assertEqual("mock-2", svc.metadata.name)
        self.assertEqual("mock-2", svc.metadata.labels["app"])
        self.assertEqual("mock-2", svc.spec.selector["app"])
        self.assertEqual(99, svc.spec.ports[0].port)

        with self.assertRaises(utils.FailToProcessError) as cm:
            utils.process_from_yaml(
                k8s_client, self.path_prefix + "yaml-conflict-multi.yaml")
        exp_error = ('Error from server (Conflict): {"kind":"Status",'
                     '"apiVersion":"v1","metadata":{},"status":"Failure",'
                     '"message":"services \\"mock-2\\" already exists",'
                     '"reason":"AlreadyExists","details":{"name":"mock-2",'
                     '"kind":"services"},"code":409}\n'
                     )
        self.assertEqual(exp_error, str(cm.exception))
        ctr = core_api.read_namespaced_replication_controller(
            name="mock-2", namespace="default")
        self.assertIsNotNone(ctr)
        core_api.delete_namespaced_replication_controller(
            name="mock-2", namespace="default", propagation_policy="Background")
        core_api.delete_namespaced_service(name="mock-2",
                                           namespace="default", body={})

    def test_create_from_multi_resource_yaml_with_multi_conflicts(self):
        """
        Should create an apps/v1 deployment
        and fail to create the same deployment twice.
        Should raise an exception that contains two error messages.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        with self.assertRaises(utils.FailToProcessError) as cm:
            utils.process_from_yaml(
                k8s_client, self.path_prefix + "triple-nginx.yaml")
        exp_error = ('Error from server (Conflict): {"kind":"Status",'
                     '"apiVersion":"v1","metadata":{},"status":"Failure",'
                     '"message":"deployments.apps \\"triple-nginx\\" '
                     'already exists","reason":"AlreadyExists",'
                     '"details":{"name":"triple-nginx","group":"apps",'
                     '"kind":"deployments"},"code":409}\n'
                     )
        exp_error += exp_error
        self.assertEqual(exp_error, str(cm.exception))
        ext_api = client.AppsV1Api(k8s_client)
        dep = ext_api.read_namespaced_deployment(name="triple-nginx",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        ext_api.delete_namespaced_deployment(
            name="triple-nginx", namespace="default",
            body={})

    def test_create_namespaced_apps_deployment_from_yaml(self):
        """
        Should be able to create an apps/v1beta1 deployment
                in a test namespace.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml",
            namespace=self.test_namespace)
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                 namespace=self.test_namespace)
        self.assertIsNotNone(dep)
        app_api.delete_namespaced_deployment(
            name="nginx-app", namespace=self.test_namespace,
            body={})

    def test_create_from_list_in_multi_resource_yaml_namespaced(self):
        """
        Should be able to create the items in the PodList and a deployment
        specified in the multi-resource file in a test namespace
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource-with-list.yaml",
            namespace=self.test_namespace)
        core_api = client.CoreV1Api(k8s_client)
        app_api = client.AppsV1Api(k8s_client)
        pod_0 = core_api.read_namespaced_pod(
            name="mock-pod-0", namespace=self.test_namespace)
        self.assertIsNotNone(pod_0)
        pod_1 = core_api.read_namespaced_pod(
            name="mock-pod-1", namespace=self.test_namespace)
        self.assertIsNotNone(pod_1)
        dep = app_api.read_namespaced_deployment(
            name="mock", namespace=self.test_namespace)
        self.assertIsNotNone(dep)
        core_api.delete_namespaced_pod(
            name="mock-pod-0", namespace=self.test_namespace, body={})
        core_api.delete_namespaced_pod(
            name="mock-pod-1", namespace=self.test_namespace, body={})
        app_api.delete_namespaced_deployment(
            name="mock", namespace=self.test_namespace, body={})

    def test_delete_namespace_from_yaml(self):
        """
        Should be able to delete a namespace
        Create namespace from file first and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-namespace.yaml")
        core_api = client.CoreV1Api(k8s_client)
        nmsp = core_api.read_namespace(name="development")
        self.assertIsNotNone(nmsp)
        """
        Delete namespace from yaml
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-namespace.yaml", action="delete")
        time.sleep(10)
        namespace_status = False
        try:
            nmsp = core_api.read_namespace(name="development")
            namespace_status = True
        except Exception as e:
            self.assertFalse(namespace_status)
        self.assertFalse(namespace_status)

    def test_delete_apps_deployment_from_yaml(self):
        """
        Should delete a deployment
        First create deployment from file and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml")
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        """
        Deployment should be created
        Now delete deployment using delete_from_yaml method
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml", action="delete")
        deployment_status = False
        time.sleep(10)
        try:
            response = app_api.read_namespaced_deployment(
                name="nginx-app", namespace="default")
            deployment_status = True
        except Exception as e:
            self.assertFalse(deployment_status)

        self.assertFalse(deployment_status)

    def test_delete_service_from_yaml(self):
        """
        Should be able to delete a service
        Create service from yaml first and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-service.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="my-service",
                                               namespace="default")
        self.assertIsNotNone(svc)
        """
        Delete service from yaml
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-service.yaml", action="delete")
        service_status = False
        time.sleep(10)
        try:
            response = core_api.read_namespaced_service(
                name="my-service", namespace="default")
            service_status = True
        except Exception as e:
            self.assertFalse(service_status)
        self.assertFalse(service_status)

    def test_delete_pod_from_yaml(self):
        """
        Should be able to delete pod
        Create pod from file first and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-pod.yaml")
        core_api = client.CoreV1Api(k8s_client)
        pod = core_api.read_namespaced_pod(name="myapp-pod",
                                           namespace="default")
        self.assertIsNotNone(pod)
        """
        Delete pod using delete_from_yaml
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "core-pod.yaml", action="delete")
        time.sleep(10)
        pod_status = False
        try:
            response = core_api.read_namespaced_pod(name="myapp-pod",
                                                    namespace="default")
            pod_status = True
        except Exception as e:
            self.assertFalse(pod_status)
        self.assertFalse(pod_status)

    def test_delete_rbac_role_from_yaml(self):
        """
        Should be able to delete rbac role
        Create rbac role from file first and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml")
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        """
        Delete rbac role from yaml
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml", action="delete")
        rbac_role_status = False
        time.sleep(10)
        try:
            response = rbac_api.read_namespaced_role(
                name="pod-reader", namespace="default")
            rbac_role_status = True
        except Exception as e:
            self.assertFalse(rbac_role_status)
        self.assertFalse(rbac_role_status)

    def test_delete_rbac_role_from_yaml_with_verbose_enabled(self):
        """
        Should delete a rbac role with verbose enabled
        Create rbac role with verbose enabled and ensure it is created
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml", verbose=True)
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        """
        Delete the rbac role from yaml
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml", verbose=True, action="delete")

        rbac_role_status = False
        time.sleep(10)
        try:
            response = rbac_api.read_namespaced_role(
                name="pod-reader", namespace="default")
            rbac_role_status = True
        except Exception as e:
            self.assertFalse(rbac_role_status)
        self.assertFalse(rbac_role_status)

    # Deletion Tests for multi resource objects in yaml files

    def test_delete_from_multi_resource_yaml(self):
        """
        Should be able to delete service and replication controller
        from the multi resource yaml files
        Create the resources first and ensure they exist
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock",
                                               namespace="default")
        self.assertIsNotNone(svc)
        ctr = core_api.read_namespaced_replication_controller(
            name="mock", namespace="default")
        self.assertIsNotNone(ctr)
        """
        Delete service and replication controller using yaml file
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource.yaml", action="delete")
        svc_status = False
        replication_status = False
        time.sleep(10)
        try:
            resp_svc = core_api.read_namespaced_service(name="mock",
                                                        namespace="default")
            svc_status = True
            resp_repl = core_api.read_namespaced_replication_controller(
                name="mock", namespace="default")
            repl_status = True
        except Exception as e:
            self.assertFalse(svc_status)
            self.assertFalse(replication_status)
        self.assertFalse(svc_status)
        self.assertFalse(replication_status)

    def test_delete_from_list_in_multi_resource_yaml(self):
        """
        Should delete the items in PodList and the deployment in the yaml file
        Create the items first and ensure they exist
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource-with-list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        app_api = client.AppsV1Api(k8s_client)
        pod_0 = core_api.read_namespaced_pod(
            name="mock-pod-0", namespace="default")
        self.assertIsNotNone(pod_0)
        pod_1 = core_api.read_namespaced_pod(
            name="mock-pod-1", namespace="default")
        self.assertIsNotNone(pod_1)
        dep = app_api.read_namespaced_deployment(
            name="mock", namespace="default")
        self.assertIsNotNone(dep)
        """
        Delete the PodList and Deployment using the yaml file
        """
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "multi-resource-with-list.yaml", action="delete")
        time.sleep(10)
        pod0_status = False
        pod1_status = False
        deploy_status = False
        try:
            core_api.read_namespaced_pod(
                name="mock-pod-0", namespace="default")
            core_api.read_namespaced_pod(
                name="mock-pod-1", namespace="default")
            app_api.read_namespaced_deployment(
                name="mock", namespace="default")
            pod0_status = True
            pod1_status = True
            deploy_status = True
        except Exception as e:
            self.assertFalse(pod0_status)
            self.assertFalse(pod1_status)
            self.assertFalse(deploy_status)
        self.assertFalse(pod0_status)
        self.assertFalse(pod1_status)
        self.assertFalse(deploy_status)

    def test_delete_apps_deployment_from_yaml_with_apply(self):
        """
        Should be able to create and delete an apps/v1 deployment using apply.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        # Create the deployment
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml", apply=True)
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                    namespace="default")
        self.assertIsNotNone(dep)
        self.assertEqual("nginx-app", dep.metadata.name)
        self.assertEqual(
            "nginx:1.15.4", dep.spec.template.spec.containers[0].image)
        self.assertEqual(
            80, dep.spec.template.spec.containers[0].ports[0].container_port)
        self.assertEqual(
            "nginx", dep.spec.template.spec.containers[0].name)
        self.assertEqual("nginx", dep.spec.template.metadata.labels["app"])
        self.assertEqual(3, dep.spec.replicas)

        # Delete the deployment using apply
        utils.process_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml", apply=True, action="delete")
        time.sleep(10)  # Wait for the deletion to propagate

        # Verify the deployment is deleted
        with self.assertRaises(ApiException) as cm:
            app_api.read_namespaced_deployment(name="nginx-app",
                                                namespace="default")
        self.assertEqual(cm.exception.status, 404)


class TestUtilsUnitTests(unittest.TestCase):

    def test_parse_quantity(self):
        # == trivial returns ==
        self.assertEqual(quantity.parse_quantity(Decimal(1)), Decimal(1))
        self.assertEqual(quantity.parse_quantity(float(1)), Decimal(1))
        self.assertEqual(quantity.parse_quantity(1), Decimal(1))

        # == exceptions ==
        self.assertRaises(
            ValueError, lambda: quantity.parse_quantity("1000kb")
        )
        self.assertRaises(
            ValueError, lambda: quantity.parse_quantity("1000ki")
        )
        self.assertRaises(
            ValueError, lambda: quantity.parse_quantity("1000foo"))
        self.assertRaises(ValueError, lambda: quantity.parse_quantity("foo"))

        # == no suffix ==
        self.assertEqual(quantity.parse_quantity("1000"), Decimal(1000))

        # == base 1024 ==
        self.assertEqual(quantity.parse_quantity("1Ki"), Decimal(1024))
        self.assertEqual(quantity.parse_quantity("1Mi"), Decimal(1024**2))
        self.assertEqual(quantity.parse_quantity("1Gi"), Decimal(1024**3))
        self.assertEqual(quantity.parse_quantity("1Ti"), Decimal(1024**4))
        self.assertEqual(quantity.parse_quantity("1Pi"), Decimal(1024**5))
        self.assertEqual(quantity.parse_quantity("1Ei"), Decimal(1024**6))
        self.assertEqual(quantity.parse_quantity("1024Ki"), Decimal(1024**2))
        self.assertEqual(quantity.parse_quantity("0.5Ki"), Decimal(512))

        # == base 1000 ==
        self.assertAlmostEqual(quantity.parse_quantity(
            "1n"), Decimal(0.000_000_001))
        self.assertAlmostEqual(
            quantity.parse_quantity("1u"), Decimal(0.000_001))
        self.assertAlmostEqual(quantity.parse_quantity("1m"), Decimal(0.001))
        self.assertEqual(quantity.parse_quantity("1k"), Decimal(1_000))
        self.assertEqual(quantity.parse_quantity("1M"), Decimal(1_000_000))
        self.assertEqual(quantity.parse_quantity("1G"), Decimal(1_000_000_000))
        self.assertEqual(quantity.parse_quantity(
            "1T"), Decimal(1_000_000_000_000))
        self.assertEqual(quantity.parse_quantity(
            "1P"), Decimal(1_000_000_000_000_000))
        self.assertEqual(
            quantity.parse_quantity("1E"), Decimal(1_000_000_000_000_000_000))
        self.assertEqual(quantity.parse_quantity("1000k"), Decimal(1_000_000))
        self.assertEqual(quantity.parse_quantity("500k"), Decimal(500_000))

    def test_format_quantity(self):
        """Unit test for quantity.format_quantity. Testing the different SI suffixes and
        function should return the expected string"""

        # == unknown suffixes ==
        self.assertRaises(
            ValueError, lambda: quantity.format_quantity(Decimal(1_000), "kb")
        )
        self.assertRaises(
            ValueError, lambda: quantity.format_quantity(Decimal(1_000), "ki")
        )
        self.assertRaises(
            ValueError, lambda: quantity.format_quantity(Decimal(1_000), "foo")
        )

        # == no suffix ==
        self.assertEqual(quantity.format_quantity(Decimal(1_000), ""), "1000")
        self.assertEqual(quantity.format_quantity(
            Decimal(1_000), None), "1000")

        # == base 1024 ==
        self.assertEqual(quantity.format_quantity(Decimal(1024), "Ki"), "1Ki")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**2), "Mi"), "1Mi")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**3), "Gi"), "1Gi")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**4), "Ti"), "1Ti")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**5), "Pi"), "1Pi")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**6), "Ei"), "1Ei")
        self.assertEqual(quantity.format_quantity(
            Decimal(1024**2), "Ki"), "1024Ki")
        self.assertEqual(quantity.format_quantity(
            Decimal((1024**3) / 2), "Gi"), "0.5Gi")
        # Decimal((1024**3)/3) are 0.3333333333333333148296162562Gi; expecting to
        # be quantized to 0.3Gi
        self.assertEqual(
            quantity.format_quantity(
                Decimal(
                    (1024**3) / 3),
                "Gi",
                quantize=Decimal(.5)),
            "0.3Gi")

        # == base 1000 ==
        self.assertEqual(quantity.format_quantity(
            Decimal(0.000_000_001), "n"), "1n")
        self.assertEqual(quantity.format_quantity(
            Decimal(0.000_001), "u"), "1u")
        self.assertEqual(quantity.format_quantity(Decimal(0.001), "m"), "1m")
        self.assertEqual(quantity.format_quantity(Decimal(1_000), "k"), "1k")
        self.assertEqual(quantity.format_quantity(
            Decimal(1_000_000), "M"), "1M")
        self.assertEqual(quantity.format_quantity(
            Decimal(1_000_000_000), "G"), "1G")
        self.assertEqual(
            quantity.format_quantity(Decimal(1_000_000_000_000), "T"), "1T"
        )
        self.assertEqual(
            quantity.format_quantity(Decimal(1_000_000_000_000_000), "P"), "1P"
        )
        self.assertEqual(
            quantity.format_quantity(
                Decimal(1_000_000_000_000_000_000), "E"), "1E"
        )
        self.assertEqual(quantity.format_quantity(
            Decimal(1_000_000), "k"), "1000k")
        # Decimal(1_000_000/3) are 333.3333333333333139307796955k; expecting to
        # be quantized to 333k
        self.assertEqual(
            quantity.format_quantity(
                Decimal(1_000_000 / 3), "k", quantize=Decimal(1000)
            ),
            "333k",
        )
