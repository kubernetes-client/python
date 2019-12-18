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

import yaml
from kubernetes import utils, client
from kubernetes.client.rest import ApiException
from kubernetes.e2e_test import base


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()
        cls.path_prefix = "kubernetes/e2e_test/test_yaml/"
        cls.test_namespace = "e2e-test-utils"
        k8s_client = client.api_client.ApiClient(configuration=cls.config)
        core_v1 = client.CoreV1Api(api_client=k8s_client)
        body = client.V1Namespace(metadata=client.V1ObjectMeta(name=cls.test_namespace))
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
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "apps-deployment.yaml")
        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app",
                                                 namespace="default")
        self.assertIsNotNone(dep)
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

        utils.create_from_dict(k8s_client, yml_obj)

        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app-3",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        app_api.delete_namespaced_deployment(
            name="nginx-app-3", namespace="default",
            body={})

    def test_create_pod_from_yaml(self):
        """
        Should be able to create a pod.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "core-pod.yaml")
        core_api = client.CoreV1Api(k8s_client)
        pod = core_api.read_namespaced_pod(name="myapp-pod",
                                           namespace="default")
        self.assertIsNotNone(pod)
        core_api.delete_namespaced_pod(
            name="myapp-pod", namespace="default",
            body={})

    def test_create_service_from_yaml(self):
        """
        Should be able to create a service.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "core-service.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="my-service",
                                               namespace="default")
        self.assertIsNotNone(svc)
        core_api.delete_namespaced_service(
            name="my-service", namespace="default",
            body={})

    def test_create_namespace_from_yaml(self):
        """
        Should be able to create a namespace.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "core-namespace.yaml")
        core_api = client.CoreV1Api(k8s_client)
        nmsp = core_api.read_namespace(name="development")
        self.assertIsNotNone(nmsp)
        core_api.delete_namespace(name="development", body={})

    def test_create_rbac_role_from_yaml(self):
        """
        Should be able to create an rbac role.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml")
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        rbac_api.delete_namespaced_role(
            name="pod-reader", namespace="default", body={})

    def test_create_rbac_role_from_yaml_with_verbose_enabled(self):
        """
        Should be able to create an rbac role with verbose enabled.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "rbac-role.yaml", verbose=True)
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader", namespace="default")
        self.assertIsNotNone(rbac_role)
        rbac_api.delete_namespaced_role(
            name="pod-reader", namespace="default", body={})

    def test_create_deployment_non_default_namespace_from_yaml(self):
        """
        Should be able to create a namespace "dep",
        and then create a deployment in the just-created namespace.
        """
        k8s_client = client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "dep-namespace.yaml")
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "dep-deployment.yaml")
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)
        nmsp = core_api.read_namespace(name="dep")
        self.assertIsNotNone(nmsp)
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
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "api-service.yaml")
        reg_api = client.ApiregistrationV1beta1Api(k8s_client)
        svc = reg_api.read_api_service(
            name="v1alpha1.wardle.k8s.io")
        self.assertIsNotNone(svc)
        with self.assertRaises(utils.FailToCreateError) as cm:
            utils.create_from_yaml(
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
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="list-service-test",
                                               namespace="default")
        self.assertIsNotNone(svc)
        dep = ext_api.read_namespaced_deployment(name="list-deployment-test",
                                                 namespace="default")
        self.assertIsNotNone(dep)
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
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "namespace-list.yaml")
        core_api = client.CoreV1Api(k8s_client)
        nmsp_1 = core_api.read_namespace(name="mock-1")
        self.assertIsNotNone(nmsp_1)
        nmsp_2 = core_api.read_namespace(name="mock-2")
        self.assertIsNotNone(nmsp_2)
        core_api.delete_namespace(name="mock-1", body={})
        core_api.delete_namespace(name="mock-2", body={})

    def test_create_implicit_service_list_from_yaml_with_conflict(self):
        """
        Should be able to create two services from a kind: ServiceList
        json file that implicitly indicates the kind of individual objects
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        with self.assertRaises(utils.FailToCreateError):
            utils.create_from_yaml(
                k8s_client, self.path_prefix + "implicit-svclist.json")
        core_api = client.CoreV1Api(k8s_client)
        svc_3 = core_api.read_namespaced_service(name="mock-3",
                                                 namespace="default")
        self.assertIsNotNone(svc_3)
        svc_4 = core_api.read_namespaced_service(name="mock-4",
                                                 namespace="default")
        self.assertIsNotNone(svc_4)
        core_api.delete_namespaced_service(name="mock-3",
                                           namespace="default", body={})
        core_api.delete_namespaced_service(name="mock-4",
                                           namespace="default", body={})

    # Tests for multi-resource yaml objects

    def test_create_from_multi_resource_yaml(self):
        """
        Should be able to create a service and a replication controller
        from a multi-resource yaml file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "multi-resource.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock",
                                               namespace="default")
        self.assertIsNotNone(svc)
        ctr = core_api.read_namespaced_replication_controller(
            name="mock", namespace="default")
        self.assertIsNotNone(ctr)
        core_api.delete_namespaced_replication_controller(
            name="mock", namespace="default", body={})
        core_api.delete_namespaced_service(name="mock",
                                           namespace="default", body={})

    def test_create_from_list_in_multi_resource_yaml(self):
        """
        Should be able to create the items in the PodList and a deployment
        specified in the multi-resource file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        utils.create_from_yaml(
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
        utils.create_from_yaml(
            k8s_client, self.path_prefix + "yaml-conflict-first.yaml")
        core_api = client.CoreV1Api(k8s_client)
        svc = core_api.read_namespaced_service(name="mock-2",
                                               namespace="default")
        self.assertIsNotNone(svc)
        with self.assertRaises(utils.FailToCreateError) as cm:
            utils.create_from_yaml(
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
            name="mock-2", namespace="default", body={})
        core_api.delete_namespaced_service(name="mock-2",
                                           namespace="default", body={})

    def test_create_from_multi_resource_yaml_with_multi_conflicts(self):
        """
        Should create an apps/v1 deployment
        and fail to create the same deployment twice.
        Should raise an exception that contains two error messages.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        with self.assertRaises(utils.FailToCreateError) as cm:
            utils.create_from_yaml(
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
        utils.create_from_yaml(
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
        utils.create_from_yaml(
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

    def test_create_apps_deployment_from_dict(self):
        """
        Should be able to create a deployment.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        deployment_dict = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": "nginx-app-4",
                "labels": {"app": "nginx"}
            },
            "spec": {
                "replicas": 3,
                "selector": {"matchLabels": {"app": "nginx"}},
                "template": {
                    "metadata": {"labels": {"app": "nginx"}},
                    "spec": {
                        "containers": [
                            {
                                "name": "nginx",
                                "image": "nginx:1.15.4",
                                "ports": [{"containerPort": 80}]
                            }
                        ]
                    }
                }
            }
        }
        utils.create_from_dict(k8s_client, deployment_dict)

        app_api = client.AppsV1Api(k8s_client)
        dep = app_api.read_namespaced_deployment(name="nginx-app-4",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        app_api.delete_namespaced_deployment(
            name="nginx-app-4", namespace="default",
            body={})

    def test_create_pod_from_dict(self):
        """
        Should be able to create a pod.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        pod_dict = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "name": "nginx-app-pod",
                "labels": {"app": "nginx"}
            },
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:1.15.4",
                        "ports": [{"containerPort": 80}]
                    }
                ]
            }
        }
        utils.create_from_dict(k8s_client, pod_dict)

        pod = core_api.read_namespaced_pod(name="nginx-app-pod",
                                           namespace="default")
        self.assertIsNotNone(pod)
        core_api.delete_namespaced_pod(
            name="nginx-app-pod", namespace="default",
            body={})

    def test_create_service_from_dict(self):
        """
        Should be able to create a service.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        service_dict = {
            "kind": "Service",
            "apiVersion": "v1",
            "metadata": {
                "name": "test-service"
            },
            "spec": {
                "selector": {
                    "app": "TestApp"
                },
                "ports": [
                    {
                        "protocol": "TCP",
                        "port": 80,
                        "targetPort": 9376
                    }
                ]
            }
        }
        utils.create_from_dict(k8s_client, service_dict)
        svc = core_api.read_namespaced_service(name="test-service",
                                               namespace="default")
        self.assertIsNotNone(svc)
        core_api.delete_namespaced_service(
            name="test-service", namespace="default",
            body={})

    def test_create_namespace_from_dict(self):
        """
        Should be able to create a namespace.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        namespace_dict = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "namespace-development",
                "labels": {"name": "namespace-development"}
            }
        }
        utils.create_from_dict(k8s_client, namespace_dict)
        nmsp = core_api.read_namespace(name="namespace-development")
        self.assertIsNotNone(nmsp)
        core_api.delete_namespace(name="namespace-development", body={})

    def test_create_rbac_role_from_dict(self):
        """
        Should be able to create an rbac role.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role_dict = {
            "apiVersion": "rbac.authorization.k8s.io/v1",
            "kind": "Role",
            "metadata": {
                "name": "pod-reader-1",
            },
            "rules": [
                {
                    "apiGroups": [""],
                    "resources": ["pods"],
                    "verbs": ["get", "watch", "list"],
                }
            ]
        }
        utils.create_from_dict(k8s_client, rbac_role_dict)

        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader-1", namespace="default")
        self.assertIsNotNone(rbac_role)
        rbac_api.delete_namespaced_role(
            name="pod-reader-1", namespace="default", body={})

    def test_create_rbac_role_from_dict_with_verbose_enabled(self):
        """
        Should be able to create an rbac role with verbose enabled.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        rbac_api = client.RbacAuthorizationV1Api(k8s_client)
        rbac_role_dict = {
            "apiVersion": "rbac.authorization.k8s.io/v1",
            "kind": "Role",
            "metadata": {
                "name": "pod-reader-2",
            },
            "rules": [
                {
                    "apiGroups": [""],
                    "resources": ["pods"],
                    "verbs": ["get", "watch", "list"],
                }
            ]
        }
        utils.create_from_dict(k8s_client, rbac_role_dict, verbose=True)
        rbac_role = rbac_api.read_namespaced_role(
            name="pod-reader-2", namespace="default")
        self.assertIsNotNone(rbac_role)
        rbac_api.delete_namespaced_role(
            name="pod-reader-2", namespace="default", body={})

    def test_create_deployment_non_default_namespace_from_dict(self):
        """
        Should be able to create a namespace "dep",
        and then create a deployment in the just-created namespace.
        """
        k8s_client = client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)
        namespace_dict = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "dep-nmsp",
                "labels": {"name": "dep-nmsp"}
            }
        }
        utils.create_from_dict(k8s_client, namespace_dict)
        nmsp = core_api.read_namespace(name="dep-nmsp")

        self.assertIsNotNone(nmsp)

        deployment_dict = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": "nginx-app-5",
                "labels": {"app": "nginx"}
            },
            "spec": {
                "replicas": 3,
                "selector": {"matchLabels": {"app": "nginx"}},
                "template": {
                    "metadata": {"labels": {"app": "nginx"}},
                    "spec": {
                        "containers": [
                            {
                                "name": "nginx",
                                "image": "nginx:1.15.4",
                                "ports": [{"containerPort": 80}]
                            }
                        ]
                    }
                }
            }
        }
        utils.create_from_dict(k8s_client, deployment_dict,
                               namespace="dep-nmsp")

        dep = ext_api.read_namespaced_deployment(name="nginx-app-5",
                                                 namespace="dep-nmsp")
        self.assertIsNotNone(dep)

        ext_api.delete_namespaced_deployment(
            name="nginx-app-5", namespace="dep-nmsp",
            body={})
        core_api.delete_namespace(name="dep-nmsp", body={})

    def test_create_apiservice_from_dict_with_conflict(self):
        """
        Should be able to create an API service.
        Should verify that creating the same API service should
        fail due to conflict.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        reg_api = client.ApiregistrationV1beta1Api(k8s_client)
        apiservice_dict = {
            "apiVersion": "apiregistration.k8s.io/v1beta1",
            "kind": "APIService",
            "metadata": {
                "name": "v1alpha1.test.k8s.io",
            },
            "spec": {
                "insecureSkipTLSVerify": True,
                "group": "test.k8s.io",
                "groupPriorityMinimum": 1000,
                "versionPriority": 15,
                "service": {
                    "name": "api",
                    "namespace": "test",
                },
                "version": "v1alpha1"
            }
        }
        utils.create_from_dict(k8s_client, apiservice_dict)
        svc = reg_api.read_api_service(
            name="v1alpha1.test.k8s.io")
        self.assertIsNotNone(svc)
        with self.assertRaises(utils.FailToCreateError) as cm:
            utils.create_from_dict(k8s_client, apiservice_dict)
        exp_error = ('Error from server (Conflict): '
                     '{"kind":"Status","apiVersion":"v1","metadata":{},'
                     '"status":"Failure",'
                     '"message":"apiservices.apiregistration.k8s.io '
                     '\\"v1alpha1.test.k8s.io\\" already exists",'
                     '"reason":"AlreadyExists",'
                     '"details":{"name":"v1alpha1.test.k8s.io",'
                     '"group":"apiregistration.k8s.io","kind":"apiservices"},'
                     '"code":409}\n'
                     )
        self.assertEqual(exp_error, str(cm.exception))
        reg_api.delete_api_service(
            name="v1alpha1.test.k8s.io", body={})

    # Tests for creating API objects from lists

    def test_create_general_list_from_dict(self):
        """
        Should be able to create a service and a deployment
        from a kind: List dict file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        ext_api = client.AppsV1Api(k8s_client)

        service_dict = {
            "kind": "Service",
            "apiVersion": "v1",
            "metadata": {
                "name": "list-service-test-2"
            },
            "spec": {
                "selector": {
                    "app": "TestApp"
                },
                "ports": [
                    {
                        "protocol": "TCP",
                        "port": 80,
                        "targetPort": 9376
                    }
                ]
            }
        }

        deploy_dict = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": "list-deployment-test-2",
                "labels": {"app": "nginx"}
            },
            "spec": {
                "replicas": 1,
                "selector": {"matchLabels": {"app": "nginx"}},
                "template": {
                    "metadata": {"labels": {"app": "nginx"}},
                    "spec": {
                        "containers": [
                            {
                                "name": "nginx",
                                "image": "nginx:1.15.4",
                                "ports": [{"containerPort": 80}]
                            }
                        ]
                    }
                }
            }
        }
        list_dict = {
            "apiVersion": "v1",
            "kind": "List",
            "items": [
                service_dict,
                deploy_dict,
            ]
        }
        utils.create_from_dict(k8s_client, list_dict)

        svc = core_api.read_namespaced_service(name="list-service-test-2",
                                               namespace="default")
        self.assertIsNotNone(svc)
        dep = ext_api.read_namespaced_deployment(name="list-deployment-test-2",
                                                 namespace="default")
        self.assertIsNotNone(dep)
        core_api.delete_namespaced_service(name="list-service-test-2",
                                           namespace="default", body={})
        ext_api.delete_namespaced_deployment(name="list-deployment-test-2",
                                             namespace="default", body={})

    def test_create_namespace_list_from_dict(self):
        """
        Should be able to create two namespaces
        from a kind: NamespaceList dict file
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)

        nmsp_dict_1 = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "nmsp-1",
                "labels": {"name": "nmsp-1"}
            }
        }
        nmsp_dict_2 = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "nmsp-2",
                "labels": {"name": "nmsp-2"}
            }
        }
        nmsp_list_dict = {
            "apiVersion": "v1",
            "kind": "NamespaceList",
            "items": [
                nmsp_dict_1,
                nmsp_dict_2,
            ]
        }

        utils.create_from_dict(k8s_client, nmsp_list_dict)
        nmsp_1 = core_api.read_namespace(name="nmsp-1")
        self.assertIsNotNone(nmsp_1)
        nmsp_2 = core_api.read_namespace(name="nmsp-2")
        self.assertIsNotNone(nmsp_2)
        core_api.delete_namespace(name="nmsp-1", body={})
        core_api.delete_namespace(name="nmsp-2", body={})

    def test_create_namespace_list_from_dict_with_conflict(self):
        """
        Should be able to create single namespace
        Should verify that creating the same namespace should
        fail due to conflict.
        """
        k8s_client = client.api_client.ApiClient(configuration=self.config)
        core_api = client.CoreV1Api(k8s_client)
        nmsp_dict = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": "nmsp-3",
                "labels": {"name": "nmsp-3"}
            }
        }
        nmsp_list_dict = {
            "apiVersion": "v1",
            "kind": "NamespaceList",
            "items": [
                nmsp_dict,
                nmsp_dict,
            ]
        }
        with self.assertRaises(utils.FailToCreateError) as cm:
            utils.create_from_dict(k8s_client, nmsp_list_dict)
        exp_error = ('Error from server (Conflict): '
                     '{"kind":"Status","apiVersion":"v1","metadata":{},'
                     '"status":"Failure",'
                     '"message":"namespaces '
                     '\\"nmsp-3\\" already exists",'
                     '"reason":"AlreadyExists",'
                     '"details":{"name":"nmsp-3",'
                     '"kind":"namespaces"},'
                     '"code":409}\n'
                     )
        self.assertEqual(exp_error, str(cm.exception))
        nmsp = core_api.read_namespace(name="nmsp-3")
        self.assertIsNotNone(nmsp)
        core_api.delete_namespace(name="nmsp-3", body={})
