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
    - Creation of cluster scoped custom resources (CR) using the above created CRD
    - List, patch (update), delete the custom resources
    - Delete the custom resource defintion (CRD)
"""

from kubernetes import config, dynamic
from kubernetes.dynamic.exceptions import ResourceNotFoundError
from kubernetes.client import api_client
import time


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the custom resource definition (CRD) api
    crd_api = client.resources.get(
        api_version="apiextensions.k8s.io/v1", kind="CustomResourceDefinition"
    )

    # Creating a Namespaced CRD named "ingressroutes.apps.example.com"
    name = "ingressroutes.apps.example.com"

    crd_manifest = {
        "apiVersion": "apiextensions.k8s.io/v1",
        "kind": "CustomResourceDefinition",
        "metadata": {
            "name": name,
        },
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
            "scope": "Cluster",
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
        "%s\t\t%s\n"
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

    ingressroute_manifest_first = {
        "apiVersion": "apps.example.com/v1",
        "kind": "IngressRoute",
        "metadata": {
            "name": "ingress-route-first",
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
        },
        "spec": {
            "virtualhost": {
                "fqdn": "www.yahoo.com",
                "tls": {"secretName": "yahoo-tls"},
            },
            "strategy": "RoundRobin",
        },
    }

    ingressroute_api.create(body=ingressroute_manifest_first)
    ingressroute_api.create(body=ingressroute_manifest_second)
    print("\n[INFO] custom resources `ingress-route-*` created\n")

    # Listing the `ingress-route-*` custom resources

    ingress_routes_list = ingressroute_api.get()
    print("%s\t\t\t%s\t\t%s\t\t\t\t%s" % ("NAME", "FQDN", "TLS", "STRATEGY"))
    for item in ingress_routes_list.items:
        print(
            "%s\t%s\t%s\t%s"
            % (
                item.metadata.name,
                item.spec.virtualhost.fqdn,
                item.spec.virtualhost.tls,
                item.spec.strategy,
            )
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
    patched_ingress_routes_list = ingressroute_api.get()
    print("%s\t\t\t%s\t\t%s\t\t\t\t%s" % ("NAME", "FQDN", "TLS", "STRATEGY"))
    for item in patched_ingress_routes_list.items:
        print(
            "%s\t%s\t%s\t%s"
            % (
                item.metadata.name,
                item.spec.virtualhost.fqdn,
                item.spec.virtualhost.tls,
                item.spec.strategy,
            )
        )

    # Deleting the ingressroutes custom resources

    delete_ingressroute_first = ingressroute_api.delete(name="ingress-route-first")
    delete_ingressroute_second = ingressroute_api.delete(name="ingress-route-second")

    print("\n[INFO] custom resources `ingress-route-*` deleted")

    # Deleting the ingressroutes.apps.example.com custom resource definition

    crd_api.delete(name=name)
    print(
        "\n[INFO] custom resource definition `ingressroutes.apps.example.com` deleted"
    )


if __name__ == "__main__":
    main()
