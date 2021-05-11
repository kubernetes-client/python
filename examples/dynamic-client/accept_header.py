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

from kubernetes import config, dynamic
from kubernetes.client import api_client

def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the node api
    api = client.resources.get(api_version="v1", kind="Node")

    # Creating a custom header
    params = {'header_params': {'Accept': 'application/json;as=PartialObjectMetadataList;v=v1;g=meta.k8s.io'}}

    resp = api.get(**params)

    # Printing the kind and apiVersion after passing new header params.
    print("%s\t\t\t%s" %("VERSION", "KIND"))
    print("%s\t\t%s" %(resp.apiVersion, resp.kind))


if __name__ == "__main__":
    main()