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
from time import sleep

from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Load config from default location
config.load_kube_config()

# Create an instance of the API class
custom_api_instance = client.CustomObjectsApi()
extensions_api_instance = client.ExtensionsV1beta1Api()

tpr = client.V1beta1ThirdPartyResource()
tpr.api_version = "extensions/v1beta1"
tpr.kind = "ThirdPartyResource"
tpr.metadata = client.V1ObjectMeta(name="repo.git.k8s.com")
tpr.versions = [client.V1beta1APIVersion(name="v1")]

try:
    # Create Third Party Resource
    print("\nCreating Third Party Resource ...")
    api_response = extensions_api_instance.create_third_party_resource(tpr)
    pprint(api_response)
    sleep(10)
except ApiException as e:
    print("Exception when calling"
          " ExtensionsV1beta1Api->create_third_party_resource: %s\n" % e)

group = "git.k8s.com"
version = "v1"
namespace = "default"
plural = "repos"

body = {}
body['apiVersion'] = "git.k8s.com/v1"
body['kind'] = "Repo"
body['metadata'] = {}
body['metadata']['name'] = "blog-repo"
body['repo'] = "github.com/user/my-blog"
body['username'] = "username"
body['password'] = "password"
body['branch'] = "branch"

try:
    # Create custom object
    print("\nCreating custom object ...")
    api_response = custom_api_instance.create_namespaced_custom_object(
        group, version,
        namespace, plural,
        body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling"
          " CustomObjectsApi->create_namespaced_custom_object: %s\n" % e)
