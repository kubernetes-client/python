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

import asyncio

from kubernetes.aio.client import api_client
from kubernetes.aio.client.configuration import Configuration
from kubernetes.aio.config import kube_config
from kubernetes.aio.dynamic import DynamicClient
from kubernetes.aio.dynamic.exceptions import ResourceNotFoundError


async def create_namespace(namespace_api, name):
    namespace_manifest = {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {"name": name, "resourceversion": "v1"},
    }
    await namespace_api.create(body=namespace_manifest)


async def delete_namespace(namespace_api, name):
    await namespace_api.delete(name=name)


async def main():
    # Creating a dynamic client
    config = Configuration()
    await kube_config.load_kube_config(client_configuration=config)
    async with api_client.ApiClient(configuration=config) as apic:
        client = await DynamicClient(apic)

        # fetching the custom resource definition (CRD) api
        crd_api = await client.resources.get(
            api_version="apiextensions.k8s.io/v1", kind="CustomResourceDefinition"
        )

        namespace_api = await client.resources.get(api_version="v1", kind="Namespace")

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
                                                            "secretName": {
                                                                "type": "string"
                                                            }
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

        crd_creation_response = await crd_api.create(crd_manifest)
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
            await client.resources.get(
                api_version="apps.example.com/v1", kind="IngressRoute"
            )
        except ResourceNotFoundError:
            # Need to wait a sec for the discovery layer to get updated
            await asyncio.sleep(2)

        ingressroute_api = await client.resources.get(
            api_version="apps.example.com/v1", kind="IngressRoute"
        )

        # Creating a custom resource (CR) `ingress-route-*`, using the above CRD `ingressroutes.apps.example.com`

        namespace_first = "test-namespace-first"
        namespace_second = "test-namespace-second"

        await create_namespace(namespace_api, namespace_first)
        await create_namespace(namespace_api, namespace_second)

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

        await ingressroute_api.create(
            body=ingressroute_manifest_first, namespace=namespace_first
        )
        await ingressroute_api.create(
            body=ingressroute_manifest_second, namespace=namespace_second
        )
        print("\n[INFO] custom resources `ingress-route-*` created\n")

        # Listing the `ingress-route-*` custom resources
        routes = await ingressroute_api.get()

        print(
            "%s\t\t\t%s\t\t\t%s\t\t%s\t\t\t\t%s"
            % ("NAME", "NAMESPACE", "FQDN", "TLS", "STRATEGY")
        )

        for item in routes["items"]:
            print(
                "%s\t%s\t\t%s\t%s\t%s"
                % (
                    item["metadata"]["name"],
                    item["metadata"]["namespace"],
                    item["spec"]["virtualhost"]["fqdn"],
                    item["spec"]["virtualhost"]["tls"],
                    item["spec"]["strategy"],
                )
            )

        # Patching the ingressroutes custom resources

        ingressroute_manifest_first["spec"]["strategy"] = "Random"
        ingressroute_manifest_second["spec"]["strategy"] = "WeightedLeastRequest"

        await ingressroute_api.patch(
            body=ingressroute_manifest_first,
            content_type="application/merge-patch+json",
        )
        await ingressroute_api.patch(
            body=ingressroute_manifest_second,
            content_type="application/merge-patch+json",
        )

        print(
            "\n[INFO] custom resources `ingress-route-*` patched to update the strategy\n"
        )

        routes = await ingressroute_api.get()

        print(
            "%s\t\t\t%s\t\t\t%s\t\t%s\t\t\t\t%s"
            % ("NAME", "NAMESPACE", "FQDN", "TLS", "STRATEGY")
        )

        for item in routes["items"]:
            print(
                "%s\t%s\t\t%s\t%s\t%s"
                % (
                    item["metadata"]["name"],
                    item["metadata"]["namespace"],
                    item["spec"]["virtualhost"]["fqdn"],
                    item["spec"]["virtualhost"]["tls"],
                    item["spec"]["strategy"],
                )
            )

        # Deleting the ingressroutes custom resources

        await ingressroute_api.delete(
            name="ingress-route-first", namespace=namespace_first
        )
        await ingressroute_api.delete(
            name="ingress-route-second", namespace=namespace_second
        )

        print("\n[INFO] custom resources `ingress-route-*` deleted")

        # Deleting the namespaces

        await delete_namespace(namespace_api, namespace_first)
        await asyncio.sleep(4)
        await delete_namespace(namespace_api, namespace_second)
        await asyncio.sleep(4)

        print("\n[INFO] test namespaces deleted")

        # Deleting the ingressroutes.apps.example.com custom resource definition

        await crd_api.delete(name=name)
        print(
            "\n[INFO] custom resource definition `ingressroutes.apps.example.com` deleted"
        )


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
