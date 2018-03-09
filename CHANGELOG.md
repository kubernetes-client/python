# v6.0.0b1
- Update to Kubernetes 1.10 cluster
- New API: add PATCH to CustomObjectsApi [kubernetes-client/gen#53](https://github.com/kubernetes-client/gen/pull/53)
- Documentation update: never let cluster-scoped resources skip webhooks [kubernetes/kubernetes#58185](https://github.com/kubernetes/kubernetes/pull/58185)

# v5.0.0
- No changes. The same as `v5.0.0b1`.

# v5.0.0b1
- Update to Kubernetes 1.9 cluster
- Label selector for pods is now required and must match the pod template's labels for v1beta2 StatefulSetSpec, ReplicaSetSpec, DaemonSetSpec and DeploymentSpec kubernetes/kubernetes#55357
- The dynamic admission webhook is split into two kinds, mutating and validating. The kinds have changed completely and old code must be ported to admissionregistration.k8s.io/v1beta1 - MutatingWebhookConfiguration and ValidatingWebhookConfiguration kubernetes/kubernetes#55282
- DaemonSet, Deployment, ReplicaSet, and StatefulSet have been promoted to GA and are available in the apps/v1 group version kubernetes/kubernetes#53679
- Introduce new storage.k8s.io/v1alpha1 VolumeAttachment object kubernetes/kubernetes#54463
- Introduce core/v1 RBDPersistentVolumeSource kubernetes/kubernetes#54302
- StatefulSet status now has support for conditions kubernetes/kubernetes#55268
- DaemonSet status now has support for conditions kubernetes/kubernetes#55272

# v4.0.0
- api change V1PersistentVolumeSpec to V1ScaleIOPersistentVolumeSource #397.

# v4.0.0b1
- Make sure PyPI source distribution is complete with all files from the root directory

# v4.0.0a1
- Update to Kubernetes 1.8 cluster
- IntOrString is now object thus it can be int or string. #18 #359
- Adding stream package to support calls like exec. The old way of calling them is deprecated. See [Troubleshooting](README.md#why-execattach-calls-doesnt-work)).
- config.http_proxy_url is deprecated. use configuration.proxy instead.
- Configuration is not a singleton object anymore. Please use Configuraion.set_default to change default configuration.
- Configuration class does not support `ws_streaming_protocol` anymore. In ApiClient.set_default_header set `sec-websocket-protocol` to the preferred websocket protocol.

# v3.0.0
- Fix Operation names for subresources kubernetes/kubernetes#49357

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

