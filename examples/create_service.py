# Copyright 2016 The Kubernetes Authors.
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

from kubernetes import client, config


def main():
    # Fetching and loading Kubernetes Information
    config.load_kube_config()
    # For incluster details
    # config.incluster_kube_config()

    extension = client.CoreV1Api()

    body = client.V1Service(
            api_version="v1",
            kind="Service",
            metadata=client.V1ObjectMeta(
                name="service-example"
            ),
            spec=client.V1ServiceSpec(
                selector={"app": "myapp"},
                ports=[client.V1ServicePort(
                    port=80,
                    target_port=6785
                )]
            )
        )
    extension.create_namespaced_service(
        namespace="kube-client",
        body=body)


if __name__ == "__main__":
    main()
