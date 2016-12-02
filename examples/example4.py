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

import os

from kubernetes import client, config
from kubernetes.client import configuration


def main():
    config_file = os.path.join(os.path.expanduser('~'), '.kube', 'config')
    contexts, active_context = config.list_kube_config_contexts(config_file)
    if not contexts:
        print("Cannot find any context in kube-config file.")
        return
    contexts = [context['name'] for context in contexts]
    active_context = active_context['name']
    for i, context in enumerate(contexts):
        format_str = "%d. %s"
        if context == active_context:
            format_str = "* " + format_str
        print(format_str % (i, context))
    context = input("Enter context number: ")
    context = int(context)
    if context not in range(len(contexts)):
        print(
            "Number out of range. Using default context %s." %
            active_context)
        context_name = active_context
    else:
        context_name = contexts[context]

    # Configs can be set in Configuration class directly or using helper
    # utility
    config.load_kube_config(config_file, context_name)

    print("Active host is %s" % configuration.host)

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for item in ret.items:
        print(
            "%s\t%s\t%s" %
            (item.status.pod_ip,
             item.metadata.namespace,
             item.metadata.name))


if __name__ == '__main__':
    main()
