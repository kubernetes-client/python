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
This example demonstrates how to pass the custom header in the cluster.

"""

import asyncio

from kubernetes.aio.client import api_client
from kubernetes.aio.client.configuration import Configuration
from kubernetes.aio.config import kube_config
from kubernetes.aio.dynamic import DynamicClient


async def main():
    # Creating a dynamic client
    config = Configuration()
    await kube_config.load_kube_config(client_configuration=config)
    async with api_client.ApiClient(configuration=config) as apic:
        async with DynamicClient(apic) as client:
            # fetching the node api
            api = await client.resources.get(api_version="v1", kind="Node")

            # Creating a custom header
            params = {
                "header_params": {
                    "Accept": "application/json;as=PartialObjectMetadataList;v=v1;g=meta.k8s.io"
                }
            }

            resp = await api.get(**params)

    # Printing the kind and apiVersion after passing new header params.
    print("VERSION\t\t\t\tKIND")
    print(f"{resp.apiVersion}\t\t{resp.kind}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    loop.close()
