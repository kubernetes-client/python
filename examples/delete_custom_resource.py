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

from __future__ import print_function

from pprint import pprint

from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load config from default location
config.load_kube_config()

# Create an instance of the API class
custom_api_instance = client.CustomObjectsApi()
api_instance = client.ExtensionsV1beta1Api()

name = "repo.git.k8s.com"
api_response = None
try:
    api_response = api_instance.read_third_party_resource(name)
except ApiException as e:
    if e.status != 404:
        print("Unknown error: %s" % e)
        exit(1)

if not api_response:
    print("'repo.git.k8s.com' Not found.\nPlease run the "
          "'create_custom_resource' example before running this example")
    exit(0)

body = client.V1DeleteOptions(propagation_policy="Foreground",
                              grace_period_seconds=5)

try:
    # Delete custom object
    print("\nDeleting custom object ...")
    api_response = custom_api_instance.delete_namespaced_custom_object(
        group="git.k8s.com", version="v1",
        namespace="default", plural="repos",
        name="blog-repo",
        body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling"
          " CustomObjectsApi->delete_namespaced_custom_object: %s\n" % e)

try:
    # Delete Third Party Resource
    print("\nDeleting Third Party Resource ...")
    api_response = api_instance.delete_third_party_resource(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling"
          " ExtensionsV1beta1Api->delete_third_party_resource: %s\n" % e)
