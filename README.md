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

From [PyPI](https://pypi.python.org/pypi/kubernetes/) directly:

```
pip install kubernetes
```

## Examples

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

(replace example1 with one of the filenames in the examples folder)

## Documentation

All APIs and Models' documentation can be found at the [Generated client's README file](kubernetes/README.md)

## Compatibility

`client-python` follows [semver](http://semver.org/), so until the major version of
client-python gets increased, your code will continue to work with explicitly
supported versions of Kubernetes clusters.

#### Compatibility matrix of supported client versions

- [client 9.y.z](https://pypi.org/project/kubernetes/9.0.1/): Kubernetes 1.12 or below (+-), Kubernetes 1.13 (✓), Kubernetes 1.14 or above (+-)
- [client 10.y.z](https://pypi.org/project/kubernetes/10.1.0/): Kubernetes 1.13 or below (+-), Kubernetes 1.14 (✓), Kubernetes 1.14 or above (+-)
- [client 11.y.z](https://pypi.org/project/kubernetes/11.0.0/): Kubernetes 1.14 or below (+-), Kubernetes 1.15 (✓), Kubernetes 1.16 or above (+-)
- [client 12.y.z](https://pypi.org/project/kubernetes/12.0.1/): Kubernetes 1.15 or below (+-), Kubernetes 1.16 (✓), Kubernetes 1.17 or above (+-)
- [client 17.y.z](https://pypi.org/project/kubernetes/17.17.0/): Kubernetes 1.16 or below (+-), Kubernetes 1.17 (✓), Kubernetes 1.18 or above (+-)
- [client 18.y.z](https://pypi.org/project/kubernetes/18.20.0/): Kubernetes 1.17 or below (+-), Kubernetes 1.18 (✓), Kubernetes 1.19 or above (+-)
- [client 19.y.z](https://pypi.org/project/kubernetes/19.15.0/): Kubernetes 1.18 or below (+-), Kubernetes 1.19 (✓), Kubernetes 1.20 or above (+-)
- [client 20.y.z](https://pypi.org/project/kubernetes/20.13.0/): Kubernetes 1.19 or below (+-), Kubernetes 1.20 (✓), Kubernetes 1.21 or above (+-)
- [client 21.y.z](https://pypi.org/project/kubernetes/21.7.0/): Kubernetes 1.20 or below (+-), Kubernetes 1.21 (✓), Kubernetes 1.22 or above (+-)
- [client 22.y.z](https://pypi.org/project/kubernetes/22.6.0/): Kubernetes 1.21 or below (+-), Kubernetes 1.22 (✓), Kubernetes 1.23 or above (+-)
- [client 23.y.z](https://pypi.org/project/kubernetes/23.6.0/): Kubernetes 1.22 or below (+-), Kubernetes 1.23 (✓), Kubernetes 1.24 or above (+-)
- [client 24.y.z](https://pypi.org/project/kubernetes/24.2.0/): Kubernetes 1.23 or below (+-), Kubernetes 1.24 (✓), Kubernetes 1.25 or above (+-)
- [client 25.y.z](https://pypi.org/project/kubernetes/25.3.0/): Kubernetes 1.24 or below (+-), Kubernetes 1.25 (✓), Kubernetes 1.26 or above (+-)
- [client 26.y.z](https://pypi.org/project/kubernetes/26.1.0/): Kubernetes 1.25 or below (+-), Kubernetes 1.26 (✓), Kubernetes 1.27 or above (+-)
- [client 27.y.z](https://pypi.org/project/kubernetes/27.2.0/): Kubernetes 1.26 or below (+-), Kubernetes 1.27 (✓), Kubernetes 1.28 or above (+-)
- [client 28.y.z](https://pypi.org/project/kubernetes/28.1.0/): Kubernetes 1.27 or below (+-), Kubernetes 1.28 (✓), Kubernetes 1.29 or above (+-)
- [client 29.y.z](https://pypi.org/project/kubernetes/29.0.0/): Kubernetes 1.28 or below (+-), Kubernetes 1.29 (✓), Kubernetes 1.30 or above (+-)

> See [here](#homogenizing-the-kubernetes-python-client-versions) for an explanation of why there is no v13-v16 release.

Key:

* `✓` Exactly the same features / API objects in both client-python and the Kubernetes
  version.
* `+` client-python has features or API objects that may not be present in the Kubernetes
 cluster, either due to that client-python has additional new API, or that the server has
 removed old API. However, everything they have in common (i.e., most APIs) will work.
 Please note that alpha APIs may vanish or change significantly in a single release.
* `-` The Kubernetes cluster has features the client-python library can't use, either due
 to the server has additional new API, or that client-python has removed old API. However,
 everything they share in common (i.e., most APIs) will work.

See the [CHANGELOG](./CHANGELOG.md) for a detailed description of changes
between client-python versions.

| Client version  | Canonical source for OpenAPI spec    | Maintenance status            |
|-----------------|--------------------------------------|-------------------------------|
| 5.0 Alpha/Beta  | Kubernetes main repo, 1.9 branch     | ✗                             |
| 5.0             | Kubernetes main repo, 1.9 branch     | ✗                             |
| 6.0 Alpha/Beta  | Kubernetes main repo, 1.10 branch    | ✗                             |
| 6.0             | Kubernetes main repo, 1.10 branch    | ✗                             |
| 7.0 Alpha/Beta  | Kubernetes main repo, 1.11 branch    | ✗                             |
| 7.0             | Kubernetes main repo, 1.11 branch    | ✗                             |
| 8.0 Alpha/Beta  | Kubernetes main repo, 1.12 branch    | ✗                             |
| 8.0             | Kubernetes main repo, 1.12 branch    | ✗                             |
| 9.0 Alpha/Beta  | Kubernetes main repo, 1.13 branch    | ✗                             |
| 9.0             | Kubernetes main repo, 1.13 branch    | ✗                             |
| 10.0 Alpha/Beta | Kubernetes main repo, 1.14 branch    | ✗                             |
| 10.0            | Kubernetes main repo, 1.14 branch    | ✗                             |
| 11.0 Alpha/Beta | Kubernetes main repo, 1.15 branch    | ✗                             |
| 11.0            | Kubernetes main repo, 1.15 branch    | ✗                             |
| 12.0 Alpha/Beta | Kubernetes main repo, 1.16 branch    | ✗                             |
| 12.0            | Kubernetes main repo, 1.16 branch    | ✗                             |
| 17.0 Alpha/Beta | Kubernetes main repo, 1.17 branch    | ✗                             |
| 17.0            | Kubernetes main repo, 1.17 branch    | ✗                             |
| 18.0 Alpha/Beta | Kubernetes main repo, 1.18 branch    | ✗                             |
| 18.0            | Kubernetes main repo, 1.18 branch    | ✗                             |
| 19.0 Alpha/Beta | Kubernetes main repo, 1.19 branch    | ✗                             |
| 19.0            | Kubernetes main repo, 1.19 branch    | ✗                             |
| 20.0 Alpha/Beta | Kubernetes main repo, 1.20 branch    | ✗                             |
| 20.0            | Kubernetes main repo, 1.20 branch    | ✗                             |
| 21.0 Alpha/Beta | Kubernetes main repo, 1.21 branch    | ✗                             |
| 21.0            | Kubernetes main repo, 1.21 branch    | ✗                             |
| 22.0 Alpha/Beta | Kubernetes main repo, 1.22 branch    | ✗                             |
| 22.0            | Kubernetes main repo, 1.22 branch    | ✗                             |
| 23.0 Alpha/Beta | Kubernetes main repo, 1.23 branch    | ✗                             |
| 23.0            | Kubernetes main repo, 1.23 branch    | ✗                             |
| 24.0 Alpha/Beta | Kubernetes main repo, 1.24 branch    | ✗                             |
| 24.0            | Kubernetes main repo, 1.24 branch    | ✗                             |
| 25.0 Alpha/Beta | Kubernetes main repo, 1.25 branch    | ✗                             |
| 25.0            | Kubernetes main repo, 1.25 branch    | ✗                             |
| 26.0 Alpha/Beta | Kubernetes main repo, 1.26 branch    | ✗                             |
| 26.0            | Kubernetes main repo, 1.26 branch    | ✗                             |
| 27.0 Alpha/Beta | Kubernetes main repo, 1.27 branch    | ✗                             |
| 27.0            | Kubernetes main repo, 1.27 branch    | ✓                             |
| 28.0 Alpha/Beta | Kubernetes main repo, 1.28 branch    | ✗                             |
| 28.0            | Kubernetes main repo, 1.28 branch    | ✓                             |
| 29.0 Alpha/Beta | Kubernetes main repo, 1.29 branch    | ✗                             |
| 29.0            | Kubernetes main repo, 1.29 branch    | ✓                             |

> See [here](#homogenizing-the-kubernetes-python-client-versions) for an explanation of why there is no v13-v16 release.

Key:

* `✓` Changes in main Kubernetes repo are manually ([should be automated](https://github.com/kubernetes-client/python/issues/177)) published to client-python when they are available.
* `✗` No longer maintained; please upgrade.

Kubernetes supports [three minor releases](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#supported-releases-and-component-skew) at a time. "Support" means we expect users to be running that version in production, though we may not port fixes back before the latest minor version. For example, when v1.3 comes out, v1.0 will no longer be supported. In consistent with Kubernetes support policy, we expect to support **three GA major releases** (corresponding to three Kubernetes minor releases) at a time.

Note: There would be no maintenance for alpha/beta releases except the latest one.

**Exception to the above support rule:** Since we are running behind on releases, we will support Alpha/Beta releases for a greater number of clients until we catch up with the upstream version.

## Homogenizing the Kubernetes Python Client versions

The client releases v12 and before following a versioning schema where the major version was 4 integer positions behind the Kubernetes minor on which the client is based on. For example, v12.0.0 is based on Kubernetes v1.16, v11.0.0 is based on Kubernetes v1.15 and so on.

This created a lot of confusion tracking two different version numbers for each client release. It was decided to homogenize the version scheme starting from the Kubernetes Python client based on Kubernetes v1.17. The versioning scheme of the client from this release would be vY.Z.P where Y and Z are the Kubernetes minor and patch release numbers from Kubernets v1.Y.Z and P is the client specific patch release numbers to accommodate changes and fixes done specifically to the client. For more details, refer [this issue](https://github.com/kubernetes-client/python/issues/1244).

## Community, Support, Discussion

If you have any problem on using the package or any suggestions, please start with reaching the [Kubernetes clients slack channel](https://kubernetes.slack.com/messages/C76GB48RK/), or filing an [issue](https://github.com/kubernetes-client/python/issues) to let us know. You can also reach the maintainers of this project at [SIG API Machinery](https://github.com/kubernetes/community/tree/master/sig-api-machinery), where this project falls under.

### Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

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
python -c "import ssl; print (ssl.OPENSSL_VERSION)"
```

You'll need a version with OpenSSL version 1.0.0 or later.

### Hostname doesn't match

If you get an `ssl.CertificateError` complaining about hostname match, your installed packages does not meet version [requirements](requirements.txt).
Specifically check `ipaddress` and `urllib3` package versions to make sure they met requirements in [requirements.txt](requirements.txt) file.

### Why Exec/Attach calls doesn't work

Starting from 4.0 release, we do not support directly calling exec or attach calls. you should use stream module to call them. so instead
of `resp = api.connect_get_namespaced_pod_exec(name, ...` you should call `resp = stream(api.connect_get_namespaced_pod_exec, name, ...`.

Using Stream will overwrite the requests protocol in _core_v1_api.CoreV1Api()_
This will cause a failure in  non-exec/attach calls. If you reuse your api client object, you will need to
recreate it between api calls that use _stream_ and other api calls.

See more at [exec example](examples/pod_exec.py).

**[⬆ back to top](#Installation)**
