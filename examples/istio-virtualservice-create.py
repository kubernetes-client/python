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
    print("Creating virtualservice:")
    https = []
    matchs = []
    matchs.append(client.IstioNetworkingV1alpha3HTTPMatchRequest(uri={"exact": "/productpage"}))
    port = client.IstioNetworkingV1alpha3PortSelector(number=9080)
    dest = client.IstioNetworkingV1alpha3Destination(host="productpage", port=port, subset="v1")
    routes = []
    routes.append(client.IstioNetworkingV1alpha3HTTPRouteDestination(destination=dest))
    https.append(client.IstioNetworkingV1alpha3HTTPRoute(match=matchs, route=routes))
    spec = client.IstioNetworkingV1alpha3VirtualServiceSpec(gateways=["bookinfo-gateway"], hosts=["*"], http=https)
    virtual_service = client.IstioNetworkingV1alpha3VirtualService(api_version="networking.istio.io/v1alpha3",
                                                                   kind="VirtualService",
                                                                   spec=spec,
                                                                   metadata=client.V1ObjectMeta(name="bookinfo"))
    ret = v1.create_namespaced_virtual_service(body=virtual_service, namespace="default")
    print("result:%s" % ret)


if __name__ == '__main__':
    main()
