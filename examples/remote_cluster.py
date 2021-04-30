# Copyright 2018 The Kubernetes Authors.
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
This example demonstrates the communication between a remote cluster and a
server outside the cluster without kube client installed on it.
The communication is secured with the use of Bearer token.
"""

from kubernetes import client, config


def main():
    # Define the bearer token we are going to use to authenticate.
    # See here to create the token:
    # https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
    aToken = "<token>"

    # Create a configuration object
    aConfiguration = client.Configuration()

    # Specify the endpoint of your Kube cluster
    aConfiguration.host = "https://XXX.XXX.XXX.XXX:443"

    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    aConfiguration.verify_ssl = False
    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl=True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert="certificate"

    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    # Create a ApiClient with our config
    aApiClient = client.ApiClient(aConfiguration)

    # Do calls
    v1 = client.CoreV1Api(aApiClient)
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
