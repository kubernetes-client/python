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
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    v1 = client.IstioV1alpha3Api()
    print("Patch virtual service:")
    source = v1.read_namespaced_virtual_service(name="bookinfo", namespace="default")
    source.spec.http[0].match.append(client.IstioNetworkingV1alpha3HTTPMatchRequest(uri={"prefix": "/productpage"}))
    i = v1.patch_namespaced_virtual_service(name="bookinfo", namespace="default", body=source)
    print("%s\t%s\t%s\t%s\t%s" %
          (i.metadata.namespace, i.metadata.name, i.spec.gateways, i.spec.hosts, i.spec.http))


if __name__ == '__main__':
    main()
