# v3.0.0b1
- Add proper GCP config loader and refresher kubernetes-client/python-base#22
- Add ws_streaming_protocol and use v4 by default kubernetes-client/python-base#20
- Respect the KUBECONFIG environment variable if set kubernetes-client/python-base#19
- Allow setting maxsize for PoolManager kubernetes-client/python-base#18
- Restricting the websocket-client to <=0.40 #299

# v3.0.0a1
- Update client to kubernetes 1.7 
- Support ThirdPartyResources (TPR) and CustomResourceDefinitions (CRD). Note that TPR is deprecated in kubernetes #251 #201
- Better dependency management #136
- Add support for python3.6 #244

# v1.0.2
- Bugfix: support RFC6902 'json-patch' operations #187

# v2.0.0
- No changes. The same as `v2.0.0b1`.

# v2.0.0b2
- Bugfix: support RFC6902 'json-patch' operations #187

# v1.0.1
- Bugfix: urllib3 1.21 fails tests, Excluding version 1.21 from dependencies #197

# v2.0.0b1
- Add support for attach API calls #180
- Bugfix: token file should not be decoded #182
- Inline primitive models (e.g. v1.Time and resource.Quantity) #179
- Bugfix: urllib3 1.21 fails tests, Excluding version 1.21 from dependencies #197

# v2.0.0a1
- Update to kubernetes 1.6 spec #169

# v1.0.0
- Bugfix: blocking exec call should remove channel metadata #140
- Add close method to websocket api of interactive exec #145

# v1.0.0b3
- Bugfix: Missing websocket-client dependency #131

# v1.0.0b2
- Support exec calls in both interactive and non-interactive mode #58

# v1.0.0b1

- Support insecure-skip-tls-verify config flag #99
- Added example for using yaml files as models #63
- Added end to end tests #41, #94
- Bugfix: Fix ValueError in list_namespaced_config_map #104
- Bugfix: Export missing models #101
- Bugfix: Patch operations #93

# v1.0.0a5

- Bugfix: Missing fields in some models #85, kubernetes/kubernetes#39465

# v1.0.0a4

- Bugfix: Fixed broken config loader #77

# v1.0.0a3

- Add context switch to kube config loader #46 
- Add default kube config location #64
- Add suport for accessing multiple clusters #7
- Bugfix: Python client does not resolve relative paths in kubeconfig #68
- Bugfix: `read_namespaced_pod_log` get None response #57
- Improved test coverage #54
- Improved client generator #49

# v1.0.0-alpha2

- auto-generated client from K8s OpenAPI spec
- kube-config support
- in-cluster config support: Run scripts inside kubernetes cluster
- watch support

# v1.0.0-alpha1
Skipped because of a failed initial release.

