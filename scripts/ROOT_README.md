# Kubernetes Python Client

Python clients for talking to a [kubernetes](http://kubernetes.io/) cluster.

## Example

```python
from __future__ import absolute_import

import k8sclient
import os

v1=k8sclient.CoreV1Api()
print "Listing pods with their IPs:"
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
  print "%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name)
```

# Generated client README

for generated client documentation, refer to [generated README](GEN_README.md).

