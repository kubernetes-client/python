# Copyright 2021 The Kubernetes Authors.
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

"""
This example demonstrates the following:
    - Creation of a custom resource definition (CRD) using dynamic-client
    - Creation of namespaced custom resources (CR) using the above CRD
    - List, patch (update), delete the custom resources
    - Delete the custom resource definition (CRD)
"""

from kubernetes import config, dynamic
from kubernetes import client as k8s_client
from kubernetes.dynamic.exceptions import ResourceNotFoundError
from kubernetes.client import api_client
import time

def list_ingressroute_for_all_namespaces(group, version, plural):
    custom_object_api = k8s_client.CustomObjectsApi()

    list_of_ingress_routes = custom_object_api.list_cluster_custom_object(
        group, version, plural
    )
    print(
        "%s\t\t\t%s\t\t\t%s\t\t%s\t\t\t\t%s"
        % ("NAME", "NAMESPACE", "FQDN", "TLS", "STRATEGY")
    )
    for item in list_of_ingress_routes["items"]:
        print(
            "%s\t%s\t\t%s\t%s\t%s"
            % (
                item["metadata"]["name"],
                item["metadata"]["namespace"],
                item["spec"]["virtualhost"]["fqdn"],
                item["spec"]["virtualhost"]["tls"],
                item["spec"]["strategy"]
            )
        )

def create_namespace(namespace_api, name):
    namespace_manifest = {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {"name": name, "resourceversion": "v1"},
    }
    namespace_api.create(body=namespace_manifest)


def delete_namespace(namespace_api, name):
    namespace_api.delete(name=name)

def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the custom resource definition (CRD) api
    crd_api = client.resources.get(
        api_version="apiextensions.k8s.io/v1", kind="CustomResourceDefinition"
    )

    namespace_api = client.resources.get(api_version="v1", kind="Namespace")

    # Creating a Namespaced CRD named "ingressroutes.apps.example.com"
    name = "ingressroutes.apps.example.com"

    crd_manifest = {
        "apiVersion": "apiextensions.k8s.io/v1",
        "kind": "CustomResourceDefinition",
        "metadata": {"name": name, "namespace": "default"},
        "spec": {
            "group": "apps.example.com",
            "versions": [
                {
                    "name": "v1",
                    "schema": {
                        "openAPIV3Schema": {
                            "properties": {
                                "spec": {
                                    "properties": {
                                        "strategy": {"type": "string"},
                                        "virtualhost": {
                                            "properties": {
                                                "fqdn": {"type": "string"},
                                                "tls": {
                                                    "properties": {
                                                        "secretName": {"type": "string"}
                                                    },
                                                    "type": "object",
                                                },
                                            },
                                            "type": "object",
                                        },
                                    },
                                    "type": "object",
                                }
                            },
                            "type": "object",
                        }
                    },
                    "served": True,
                    "storage": True,
                }
            ],
            "scope": "Namespaced",
            "names": {
                "plural": "ingressroutes",
                "listKind": "IngressRouteList",
                "singular": "ingressroute",
                "kind": "IngressRoute",
                "shortNames": ["ir"],
            },
        },
    }

    crd_creation_response = crd_api.create(crd_manifest)
    print(
        "\n[INFO] custom resource definition `ingressroutes.apps.example.com` created\n"
    )
    print("%s\t\t%s" % ("SCOPE", "NAME"))
    print(
        "%s\t%s\n"
        % (crd_creation_response.spec.scope, crd_creation_response.metadata.name)
    )

    # Fetching the "ingressroutes" CRD api

    try:
        ingressroute_api = client.resources.get(
            api_version="apps.example.com/v1", kind="IngressRoute"
        )
    except ResourceNotFoundError:
        # Need to wait a sec for the discovery layer to get updated
        time.sleep(2)

    ingressroute_api = client.resources.get(
        api_version="apps.example.com/v1", kind="IngressRoute"
    )

    # Creating a custom resource (CR) `ingress-route-*`, using the above CRD `ingressroutes.apps.example.com`

    namespace_first = "test-namespace-first"
    namespace_second = "test-namespace-second"

    create_namespace(namespace_api, namespace_first)
    create_namespace(namespace_api, namespace_second)

    ingressroute_manifest_first = {
        "apiVersion": "apps.example.com/v1",
        "kind": "IngressRoute",
        "metadata": {
            "name": "ingress-route-first",
            "namespace": namespace_first,
        },
        "spec": {
            "virtualhost": {
                "fqdn": "www.google.com",
                "tls": {"secretName": "google-tls"},
            },
            "strategy": "RoundRobin",
        },
    }

    ingressroute_manifest_second = {
        "apiVersion": "apps.example.com/v1",
        "kind": "IngressRoute",
        "metadata": {
            "name": "ingress-route-second",
            "namespace": namespace_second,
        },
        "spec": {
            "virtualhost": {
                "fqdn": "www.yahoo.com",
                "tls": {"secretName": "yahoo-tls"},
            },
            "strategy": "RoundRobin",
        },
    }

    ingressroute_api.create(body=ingressroute_manifest_first, namespace=namespace_first)
    ingressroute_api.create(body=ingressroute_manifest_second, namespace=namespace_second)
    print("\n[INFO] custom resources `ingress-route-*` created\n")

    # Listing the `ingress-route-*` custom resources

    list_ingressroute_for_all_namespaces(
        group="apps.example.com", version="v1", plural="ingressroutes"
    )

    # Patching the ingressroutes custom resources

    ingressroute_manifest_first["spec"]["strategy"] = "Random"
    ingressroute_manifest_second["spec"]["strategy"] = "WeightedLeastRequest"

    patch_ingressroute_first = ingressroute_api.patch(
        body=ingressroute_manifest_first, content_type="application/merge-patch+json"
    )
    patch_ingressroute_second = ingressroute_api.patch(
        body=ingressroute_manifest_second, content_type="application/merge-patch+json"
    )

    print(
        "\n[INFO] custom resources `ingress-route-*` patched to update the strategy\n"
    )
    list_ingressroute_for_all_namespaces(
        group="apps.example.com", version="v1", plural="ingressroutes"
    )

    # Deleting the ingressroutes custom resources

    delete_ingressroute_first = ingressroute_api.delete(
        name="ingress-route-first", namespace=namespace_first
    )
    delete_ingressroute_second = ingressroute_api.delete(
        name="ingress-route-second", namespace=namespace_second
    )

    print("\n[INFO] custom resources `ingress-route-*` deleted")

    # Deleting the namespaces

    delete_namespace(namespace_api, namespace_first)
    time.sleep(4)
    delete_namespace(namespace_api, namespace_second)
    time.sleep(4)

    print("\n[INFO] test namespaces deleted")

    # Deleting the ingressroutes.apps.example.com custom resource definition

    crd_api.delete(name=name)
    print(
        "\n[INFO] custom resource definition `ingressroutes.apps.example.com` deleted"
    )


if __name__ == "__main__":
    main()
