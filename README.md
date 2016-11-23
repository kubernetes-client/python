# Kubernetes Python Client

[![Build Status](https://travis-ci.org/kubernetes-incubator/client-python.svg?branch=master)](https://travis-ci.org/kubernetes-incubator/client-python)

Python clients for talking to a [kubernetes](http://kubernetes.io/) cluster.

## Example

list all pods:

```python
import os

from kubernetes import client, util

# Configs can be set in Configuration class directly or using helper utility
util.load_kube_config(os.environ["HOME"] + '/.kube/config')

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
```

watch on namespace object:

```python
import os

from kubernetes import client, util

# Configs can be set in Configuration class directly or using helper utility
util.load_kube_config(os.environ["HOME"] + '/.kube/config')

v1 = client.CoreV1Api()
count = 10
watch = util.Watch()
for event in watch.stream(v1.list_namespace, _request_timeout=60):
    print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    count -= 1
    if not count:
        watch.stop()

print("Ended.")
```

More examples can be found in [examples](examples/) folder. To run examples, run this command:

```shell
python -m examples.example1
```

(replace example1 with the example base filename)


# Generated client README

All APIs and Models' documentation can be find at the [Generated client's README file](kubernetes/README.md)

