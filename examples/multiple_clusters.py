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
# install pick using "pip install pick". It is not included
# as a dependency because it only used in examples
from pick import pick


def main():

    contexts, active_context = config.list_kube_config_contexts()
    if not contexts:
        print("Cannot find any context in kube-config file.")
        return
    contexts = [context['name'] for context in contexts]
    active_index = contexts.index(active_context['name'])
    cluster1, first_index = pick(contexts, title="Pick the first context",
                                 default_index=active_index)
    cluster2, _ = pick(contexts, title="Pick the second context",
                       default_index=first_index)

    client1 = client.CoreV1Api(
        api_client=config.new_client_from_config(context=cluster1))
    client2 = client.CoreV1Api(
        api_client=config.new_client_from_config(context=cluster2))

    print("\nList of pods on %s:" % cluster1)
    for i in client1.list_pod_for_all_namespaces().items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    print("\n\nList of pods on %s:" % cluster2)
    for i in client2.list_pod_for_all_namespaces().items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
