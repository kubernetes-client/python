# Kubernetes Python Client

[![Build Status](https://travis-ci.org/kubernetes-incubator/client-python.svg?branch=master)](https://travis-ci.org/kubernetes-incubator/client-python)
[![PyPI version](https://badge.fury.io/py/kubernetes.svg)](https://badge.fury.io/py/kubernetes)

Python client for the [kubernetes](http://kubernetes.io/) API.

## Installation

From source:

```
git clone https://github.com/kubernetes-incubator/client-python.git
cd client-python
python setup.py install
```

From [PyPi](https://pypi.python.org/pypi/kubernetes/) directly:

```
pip install kubernetes
```

## Example

list all pods:

```python
import os

from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(os.path.join(os.path.expanduser('~'), '.kube', 'config'))

v1=client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
```

watch on namespace object:

```python
import os

from kubernetes import client, config, watch

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(os.path.join(os.path.expanduser('~'), '.kube', 'config'))

v1 = client.CoreV1Api()
count = 10
w = watch.Watch()
for event in w.stream(v1.list_namespace, _request_timeout=60):
    print("Event: %s %s" % (event['type'], event['object'].metadata.name))
    count -= 1
    if not count:
        w.stop()

print("Ended.")
```

More examples can be found in [examples](examples/) folder. To run examples, run this command:

```shell
python -m examples.example1
```

(replace example1 with the example base filename)


## Documentation

All APIs and Models' documentation can be found at the [Generated client's README file](kubernetes/README.md)

## Community, Support, Discussion

You can reach the maintainers of this project at:

* [Slack](http://slack.kubernetes.io): #sig-api-machinery
* Mailing List: [https://groups.google.com/forum/#!forum/kubernetes-sig-api-machinery](https://groups.google.com/forum/#!forum/kubernetes-sig-api-machinery)

If you have a problem with the package or suggestions. Please file an [issue](https://github.com/kubernetes-incubator/client-python/issues).

### Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

## Kubernetes Incubator

This is a [Kubernetes Incubator project](https://github.com/kubernetes/community/blob/master/incubator.md). 

* SIG: sig-api-machinery
