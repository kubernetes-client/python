## Creating a Third Party Resource

```
from __future__ import print_function

from pprint import pprint

import kubernetes
from kubernetes import config
from kubernetes.rest import ApiException

config.load_kube_config()
api_instance = kubernetes.ThirdPartyResources()

namespace = 'default'
resource = 'repos'
fqdn = 'git.k8s.com'

body = {}
body['apiVersion'] = "git.k8s.com/v1"
body['kind'] = "RePo"
body['metadata'] = {}
body['metadata']['name'] = "blog-repo"
body['repo'] = "github.com/user/my-blog"
body['username'] = "username"
body['password'] = "password"
body['branch'] = "branch"



try: 
    # Create a Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_post(
        namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_post: %s\n" % 
        e)
```