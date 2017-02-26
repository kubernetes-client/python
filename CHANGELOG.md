# v1.0.1
- Bugfix: blocking exec call should remove channel metadata #140

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

