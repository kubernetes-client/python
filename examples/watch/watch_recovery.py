# Copyright 2025 The Kubernetes Authors.
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
Uses watch to print a stream of Pod events from the default namespace.
The allow_watch_bookmarks flag is set to True, so the API server can send
BOOKMARK events.

If the connection to the API server is lost, the script will reconnect and 
resume watching from the most recently received resource version.

For more information, see:
- https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes
- https://kubernetes.io/docs/reference/using-api/api-concepts/#semantics-for-watch
"""

import urllib3

from kubernetes import config
from kubernetes.client import api_client
from kubernetes.client.exceptions import ApiException
from kubernetes.dynamic.client import DynamicClient

NAMESPACE = "default"


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    client = DynamicClient(api_client.ApiClient())
    api = client.resources.get(api_version="v1", kind="Pod")
    
    # Setting resource_version=None means the server will send synthetic
    # ADDED events for all resources that exist when the watch starts.
    resource_version = None
    while True:
        try:
            for event in api.watch(
                namespace=NAMESPACE,
                resource_version=resource_version,
                allow_watch_bookmarks=True,
            ):
                # Remember the last resourceVersion we saw, so we can resume
                # watching from there if the connection is lost.
                resource_version = event['object'].metadata.resourceVersion

                print("Event: %s %s %s" % (
                    resource_version,
                    event['type'],
                    event['object'].metadata.name,
                ))

        except ApiException as err:
            if err.status == 410:
                print("ERROR: The requested resource version is no longer available.")
                resource_version = None
            else:
                raise

        except urllib3.exceptions.ProtocolError:
            print("Lost connection to the k8s API server. Reconnecting...")


if __name__ == "__main__":
    main()
