from __future__ import print_function
import time
import kube_resource
import json
from kube_resource.rest import ApiException
from pprint import pprint

with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as token_file:
    token=token_file.read()

kube_resource.configuration.api_key['Authorization'] = token
kube_resource.configuration.api_key_prefix['Authorization'] = 'Bearer'
kube_resource.configuration.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
api_instance = kube_resource.DefaultApi()

namespace = 'default'
resource = 'repos'
fqdn = 'git.k8s.com'

body = json.loads('{  "apiVersion": "git.k8s.com/v1",  "kind": "RePo",  "metadata": {    "name": "blog-repo"  },  "repo": "github.com/user/my-blog",  "oauth": 123456789,  "branch": "master",  "key": "user-git-deploy-secret",  "path": "/path/in/volume",  "image": "image to run job in",  "then": "hugo --destination=/home/user/hugosite/public",  "pvc": "persistent-volume-claim",  "username": "repo username",  "password": "repo password"}')

try: 
    # Create a Resource
    api_response = api_instance.apis_fqdn_v1_namespaces_namespace_resource_post(namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apis_fqdn_v1_namespaces_namespace_resource_post: %s\n" % e)