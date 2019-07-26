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

    extension = client.ExtensionsV1beta1Api()

    body = client.ExtensionsV1beta1Ingress(
        api_version="v1beta1",
        kind="Ingress",
        metadata=client.V1ObjectMeta(
            name="ingress-example",
            annotations={"nginx.ingress.kubernetes.io/rewrite-target": "/"}),
        spec=client.ExtensionsV1beta1IngressSpec(
            rules=[client.ExtensionsV1beta1IngressRule(
                host="abc.xyz.com",
                http=client.ExtensionsV1beta1HTTPIngressRuleValue(
                    paths=list[client.ExtensionsV1beta1HTTPIngressPath(
                        path="/api",
                        backend=client.ExtensionsV1beta1IngressBackend(
                            service_name="ingress",
                            service_port=5000

                        )
                    )]
                )
            )
            ]
        )
    )

    extension.create_namespaced_ingress(
        namespace="kube-client",
        body=body
    )


if __name__ == "__main__":
    main()
