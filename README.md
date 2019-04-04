# Kubernetes Python Client

[![Build Status](https://travis-ci.org/kubernetes-client/python.svg?branch=master)](https://travis-ci.org/kubernetes-client/python)
[![PyPI version](https://badge.fury.io/py/kubernetes.svg)](https://badge.fury.io/py/kubernetes)
[![codecov](https://codecov.io/gh/kubernetes-client/python/branch/master/graph/badge.svg)](https://codecov.io/gh/kubernetes-client/python "Non-generated packages only")
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes.svg)](https://pypi.python.org/pypi/kubernetes)
[![Client Capabilities](https://img.shields.io/badge/Kubernetes%20client-Silver-blue.svg?style=flat&colorB=C0C0C0&colorA=306CE8)](http://bit.ly/kubernetes-client-capabilities-badge)
[![Client Support Level](https://img.shields.io/badge/kubernetes%20client-beta-green.svg?style=flat&colorA=306CE8)](http://bit.ly/kubernetes-client-support-badge)

Python client for the [kubernetes](http://kubernetes.io/) API.

## Installation

From source:

```
git clone --recursive https://github.com/kubernetes-client/python.git
cd python
python setup.py install
```

From [PyPi](https://pypi.python.org/pypi/kubernetes/) directly:

```
pip install kubernetes
```

## Example

list all pods:

```python
from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
```

watch on namespace object:

```python
from kubernetes import client, config, watch

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

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

## Compatibility

`client-python` follows [semver](http://semver.org/), so until the major version of
client-python gets increased, your code will continue to work with explicitly 
supported versions of Kubernetes clusters.

#### Compatibility matrix

|                    | Kubernetes 1.5 | Kubernetes 1.6 | Kubernetes 1.7 | Kubernetes 1.8 | Kubernetes 1.9 | Kubernetes 1.10 | Kubernetes 1.11 | Kubernetes 1.12 | Kubernetes 1.13 | Kubernetes 1.14 |
|--------------------|----------------|----------------|----------------|----------------|----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| client-python 1.0  | ✓              | -              | -              |-               |-               |-                |-                |-                |-                |-                |
| client-python 2.0  | +              | ✓              | -              |-               |-               |-                |-                |-                |-                |-                |
| client-python 3.0  | +              | +              | ✓              |-               |-               |-                |-                |-                |-                |-                |
| client-python 4.0  | +              | +              | +              |✓               |-               |-                |-                |-                |-                |-                |
| client-python 5.0  | +              | +              | +              |+               |✓               |-                |-                |-                |-                |-                |
| client-python 6.0  | +              | +              | +              |+               |+               |✓                |-                |-                |-                |-                |
| client-python 7.0  | +              | +              | +              |+               |+               |+                |✓                |-                |-                |-                |
| client-python 8.0  | +              | +              | +              |+               |+               |+                |+                |✓                |-                |-                |
| client-python 9.0  | +              | +              | +              |+               |+               |+                |+                |+                |✓                |-                |
| client-python 10.0 | +              | +              | +              |+               |+               |+                |+                |+                |+                |✓                |
| client-python HEAD | +              | +              | +              |+               |+               |+                |+                |+                |+                |✓                |

Key:

* `✓` Exactly the same features / API objects in both client-python and the Kubernetes
  version.
* `+` client-python has features or api objects that may not be present in the
  Kubernetes cluster, but everything they have in common will work.
* `-` The Kubernetes cluster has features the client-python library can't use
  (additional API objects, etc).

See the [CHANGELOG](./CHANGELOG.md) for a detailed description of changes
between client-python versions.

| Client version  | Canonical source for OpenAPI spec    | Maintenance status            |
|-----------------|--------------------------------------|-------------------------------|
| 1.0 Alpha/Beta  | Kubernetes main repo, 1.5 branch     | ✗                             |
| 1.0.x           | Kubernetes main repo, 1.5 branch     | ✗                             |
| 2.0 Alpha/Beta  | Kubernetes main repo, 1.6 branch     | ✗                             |
| 2.0.x           | Kubernetes main repo, 1.6 branch     | ✗                             |
| 3.0 Alpha/Beta  | Kubernetes main repo, 1.7 branch     | ✗                             |
| 3.0             | Kubernetes main repo, 1.7 branch     | ✗                             |
| 4.0 Alpha/Beta  | Kubernetes main repo, 1.8 branch     | ✗                             |
| 4.0             | Kubernetes main repo, 1.8 branch     | ✗                             |
| 5.0 Alpha/Beta  | Kubernetes main repo, 1.9 branch     | ✗                             |
| 5.0             | Kubernetes main repo, 1.9 branch     | ✗                             |
| 6.0 Alpha/Beta  | Kubernetes main repo, 1.10 branch    | ✗                             |
| 6.0             | Kubernetes main repo, 1.10 branch    | ✗                             |
| 7.0 Alpha/Beta  | Kubernetes main repo, 1.11 branch    | ✗                             |
| 7.0             | Kubernetes main repo, 1.11 branch    | ✓                             |
| 8.0 Alpha/Beta  | Kubernetes main repo, 1.12 branch    | ✗                             |
| 8.0             | Kubernetes main repo, 1.12 branch    | ✓                             |
| 9.0 Alpha/Beta  | Kubernetes main repo, 1.13 branch    | ✗                             |
| 9.0             | Kubernetes main repo, 1.13 branch    | ✓                             |
| 10.0 Alpha/Beta | Kubernetes main repo, 1.14 branch    | ✓                             |


Key:

* `✓` Changes in main Kubernetes repo are manually ([should be automated](https://github.com/kubernetes-client/python/issues/177)) published to client-python when they are available.
* `✗` No longer maintained; please upgrade.

Kubernetes supports [three minor releases](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#supported-releases-and-component-skew) at a time. "Support" means we expect users to be running that version in production, though we may not port fixes back before the latest minor version. For example, when v1.3 comes out, v1.0 will no longer be supported. In consistent with Kubernetes support policy, we expect to support **three GA major releases** (corresponding to three Kubernetes minor releases) at a time.

Note: There would be no maintenance for alpha/beta releases except the latest one.

## Community, Support, Discussion

If you have any problem on using the package or any suggestions, please start with reaching the [Kubernetes clients slack channel](https://kubernetes.slack.com/messages/C76GB48RK/), or filing an [issue](https://github.com/kubernetes-client/python/issues) to let us know. You can also reach the maintainers of this project at [SIG API Machinery](https://github.com/kubernetes/community/tree/master/sig-api-machinery).

### Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

## Kubernetes Incubator

This is a [Kubernetes Incubator project](https://github.com/kubernetes/community/blob/master/incubator.md). 

* [SIG: sig-api-machinery](https://github.com/kubernetes/community/tree/master/sig-api-machinery)


## Troubleshooting

### SSLError on macOS

If you get an SSLError, you likely need to update your version of python. The
version that ships with macOS may not be supported.

Install the latest version of python with [brew](https://brew.sh/):

```
brew install python
```

Once installed, you can query the version of OpenSSL like so:

```
python -c "import ssl; print ssl.OPENSSL_VERSION"
```

You'll need a version with OpenSSL version 1.0.0 or later.

### Hostname doesn't match

If you get an `ssl.CertificateError` complaining about hostname match, your installed packages does not meet version [requirements](requirements.txt). 
Specifically check `ipaddress` and `urllib3` package versions to make sure they met requirements in [requirements.txt](requirements.txt) file.

### Why Exec/Attach calls doesn't work
Starting from 4.0 release, we do not support directly calling exec or attach calls. you should use stream module to call them. so instead
of `resp = api.connect_get_namespaced_pod_exec(name, ...` you should call `resp = stream(api.connect_get_namespaced_pod_exec, name, ...`.
See more at [exec example](examples/exec.py).
