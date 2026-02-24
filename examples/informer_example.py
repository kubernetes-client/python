# Copyright 2024 The Kubernetes Authors.
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

"""Example: use SharedInformer to watch pods in the default namespace.

The informer runs a background daemon thread that keeps a local cache
synchronised with the Kubernetes API server.  The main thread is free to
query the cache at any time without worrying about connectivity or retries.
"""

import time

import kubernetes
from kubernetes import config
from kubernetes.client import CoreV1Api
from kubernetes.informer import ADDED, DELETED, MODIFIED, SharedInformer


def on_pod_added(pod):
    name = pod.metadata.name if hasattr(pod, "metadata") else pod["metadata"]["name"]
    print("[ADDED]   ", name)


def on_pod_modified(pod):
    name = pod.metadata.name if hasattr(pod, "metadata") else pod["metadata"]["name"]
    print("[MODIFIED]", name)


def on_pod_deleted(pod):
    name = pod.metadata.name if hasattr(pod, "metadata") else pod["metadata"]["name"]
    print("[DELETED] ", name)


def main():
    config.load_kube_config()

    v1 = CoreV1Api()
    informer = SharedInformer(
        list_func=v1.list_namespaced_pod,
        namespace="default",
        resync_period=60,
    )

    informer.add_event_handler(ADDED, on_pod_added)
    informer.add_event_handler(MODIFIED, on_pod_modified)
    informer.add_event_handler(DELETED, on_pod_deleted)

    informer.start()
    print('Informer started. Watching pods in "default" namespace ...')

    try:
        while True:
            cached = informer.cache.list()
            print("Cached pods: {}".format(len(cached)))
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        informer.stop()
        print("Informer stopped.")


if __name__ == "__main__":
    main()
