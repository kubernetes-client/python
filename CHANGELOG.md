# v10.0.0a1
**Bug Fix:**
- Make watch work with read_namespaced_pod_log [kubernetes-client/python-base#93](https://github.com/kubernetes-client/python-base/pull/93)
- Add Rbac support for creating from YAML [kubernetes-client/python#767](https://github.com/kubernetes-client/python/pull/767)

**New Feature:**
- Config loader supports loading from multiple kubeconfig files [kubernetes-client/python-base#94](https://github.com/kubernetes-client/python-base/pull/94)
- Add a script to fix setup on Windows [kubernetes-client/python#766](https://github.com/kubernetes-client/python/pull/766)
- Extend YAML load functionality to \*LIST and multi-resources [kubernetes-client/python#673](https://github.com/kubernetes-client/python/pull/673)

**API Change:**
- Remove the AdmissionregistrationV1alpha1 API group, containing only the InitializationConfiguration type [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)
- Promote Lease API to v1 [kubernetes/kubernetes#72239](https://github.com/kubernetes/kubernetes/pull/72239)
- The Ingress API is now available via `NetworkingV1beta1Api`. `ExtensionsV1beta1Api` Ingress objects are deprecated and will no longer be served in Kubernetes v1.18 [kubernetes/kubernetes#74057](https://github.com/kubernetes/kubernetes/pull/74057)
- Introduce RuntimeClass to NodeV1alpha1Api and NodeV1beta1Api [kubernetes/kubernetes#74433](https://github.com/kubernetes/kubernetes/pull/74433)
- Graduate PriorityClass API to GA SchedulingV1Api [kubernetes/kubernetes#73555](https://github.com/kubernetes/kubernetes/pull/73555)
- Introduce CSINodeInfo and CSIDriver to StorageV1beta1Api [kubernetes/kubernetes#74283](https://github.com/kubernetes/kubernetes/pull/74283)

# v9.0.0
**Bug Fix:**
- Add fieldSelector parameter to list/watch methods in custom objects spec [kubernetes-client/gen#106](https://github.com/kubernetes-client/gen/pull/106)

# v9.0.0b1
**Breaking Change:**
- Move dependancy adal under extra require [kubernetes-client/python-base#108](https://github.com/kubernetes-client/python-base/pull/108)

**Bug Fix:**
- Honor the specified resource version in stream request when watch restarts [kubernetes-client/python-base#109](https://github.com/kubernetes-client/python-base/pull/109)

**API Change:**
- Add timeoutSeconds parameter to CustomObjectsApi list/watch calls [kubernetes-client/gen#94](https://github.com/kubernetes-client/gen/pull/94)

**New Feature:**
- Avoid creating unused ThreadPools [kubernetes-client/gen#91](https://github.com/kubernetes-client/gen/pull/91)

# v9.0.0a1
**Bug Fix:**
- Refresh GCP auth tokens on API retrieval [kubernetes-client/python-base#92](https://github.com/kubernetes-client/python-base/pull/92)
- Fix kubeconfig loading failure when server uri contains trailing slash [kubernetes-client/python-base#45](https://github.com/kubernetes-client/python-base/pull/45)

**Security Fix:**
- Bump urllib3 version to pick up security fix for CVE-2018-20060 [kubernetes-client/python#707](https://github.com/kubernetes-client/python/pull/707)

**API Change:**
- Add dynamic audit configuration api: AuditregistrationV1alpha1Api [kubernetes/kubernetes#67547](https://github.com/kubernetes/kubernetes/pull/67547)
- CSIPersistentVolume feature, i.e. PersistentVolumes with CSIPersistentVolumeSource, is GA. CSIPersistentVolume feature gate is now deprecated and will be removed according to deprecation policy. [kubernetes/kubernetes#69929](https://github.com/kubernetes/kubernetes/pull/69929)
- Add support for CRD conversion webhook [kubernetes/kubernetes#67006](https://github.com/kubernetes/kubernetes/pull/67006)
- CRD supports multi-version Schema, Subresources and AdditionalPrintColumns (NOTE that CRDs created prior to 1.13 populated the top-level additionalPrinterColumns field by default. To apply an update that changes to per-version additionalPrinterColumns, the top-level additionalPrinterColumns field must be explicitly set to null). [kubernetes/kubernetes#70211](https://github.com/kubernetes/kubernetes/pull/70211)
- Add ability to control primary GID of containers through Pod Spec and PodSecurityPolicy [kubernetes/kubernetes#67802](https://github.com/kubernetes/kubernetes/pull/67802)
- Refactor GlusterFS PV spec. This patch introduces glusterfsPersistentVolumeSource addition to glusterfsVolumeSource. All fields remains same as glusterfsVolumeSource with an addition of a new field called `EndpointsNamespace` to define namespace of endpoint in the spec. [kubernetes/kubernetes#60195](https://github.com/kubernetes/kubernetes/pull/60195)
- Delete request's body parameter is optional [kubernetes/kubernetes#70032](https://github.com/kubernetes/kubernetes/pull/70032)
- Make service environment variables optional [kubernetes/kubernetes#68754](https://github.com/kubernetes/kubernetes/pull/68754)
- TokenReview now supports audience validation of tokens with audiences other than the kube-apiserver. [kubernetes/kubernetes#62692](https://github.com/kubernetes/kubernetes/pull/62692)

**Breaking Change:**
- Model v1beta1WebhookClientConfig is renamed to AdmissionregistrationV1beta1WebhookClientConfig, to avoid naming conflict with ApiextensionsV1beta1WebhookClientConfig introduced in: [kubernetes/kubernetes#67006](https://github.com/kubernetes/kubernetes/pull/67006)
- Delete request's body parameter is optional [kubernetes/kubernetes#70032](https://github.com/kubernetes/kubernetes/pull/70032)

# v8.0.1
**Bug Fix:**
- Refresh GCP auth tokens on API retrieval [kubernetes-client/python-base#92](https://github.com/kubernetes-client/python-base/pull/92)
- Fix kubeconfig loading failure when server uri contains trailing slash [kubernetes-client/python-base#45](https://github.com/kubernetes-client/python-base/pull/45)

**Security Fix:**
- Bump urllib3 version to pick up security fix for CVE-2018-20060 [kubernetes-client/python#707](https://github.com/kubernetes-client/python/pull/707)

# v7.0.1
**Security Fix:**
- Bump urllib3 version to pick up security fix for CVE-2018-20060 [kubernetes-client/python#707](https://github.com/kubernetes-client/python/pull/707)

# v6.1.0
- Python 3.7 support
- Update to Kubernetes 1.10.10 API

**Breaking Change:**
- **ACTION REQUIRED** Rename the currently being-used `async` parameter to `async_req` to support Python 3.7 because `async` is a reserved keyword in Python 3.7 [kubernetes-client/gen#67](https://github.com/kubernetes-client/gen/pull/67)
- **NOTE** Python 3.7 was released after v6.0.0 release. It's not necessary to upgrade your client to v6.1.0 if you do not use Python 3.7+.

**API change:**
- Add custom object status and scale api kubernetes-client/gen#72

# v8.0.0
**New Feature:**
- Add utility to create API resource from yaml file [kubernetes-client/python#655](https://github.com/kubernetes-client/python/pull/655)

# v8.0.0b1
**Bug Fix:**
- Update ExecProvider to use safe\_get() to tolerate kube-config file that sets
  `args: null` and `env: null` [kubernetes-client/python-base#91](https://github.com/kubernetes-client/python-base/pull/91)
- Properly deserialize API server's response when posting a deployment rollback [kubernetes/kubernetes#68909](https://github.com/kubernetes/kubernetes/pull/68909)

**API Change:**
- dry-run: CREATE/UPDATE/PATCH methods now support dryRun parameter [kubernetes/kubernetes#69359](https://github.com/kubernetes/kubernetes/pull/69359)

# v8.0.0a1
**New Feature:**
- Add exec-plugins support in kubeconfig [kubernetes-client/python-base#75](https://github.com/kubernetes-client/python-base/pull/75)

**Bug Fix:**
- Fix reading kubeconfig data with bytes in Python 3
  [kubernetes-client/python-base#86](https://github.com/kubernetes-client/python-base/pull/86)

**API Change:**
- Upon receiving a LIST request with expired continue token, the apiserver now returns a continue token together with the 410 "the from parameter is too old " error. If the client does not care about getting a list from a consistent snapshot, the client can use this token to continue listing from the next key, but the returned chunk will be from the latest snapshot [kubernetes/kubernetes#67284](https://github.com/kubernetes/kubernetes/pull/67284)
- Introduces autoscaling/v2beta2 and custom\_metrics/v1beta2, which implement metric selectors for Object and Pods metrics, as well as allowing AverageValue targets on Objects, similar to External metrics [kubernetes/kubernetes#64097](https://github.com/kubernetes/kubernetes/pull/64097)
- Create "coordination.k8s.io" api group with "Lease" api in it [kubernetes/kubernetes#64246](https://github.com/kubernetes/kubernetes/pull/64246)
- Added support to restore a volume from a volume snapshot data source: adds TypedLocalObjectReference in the core API and adds DataSource in PersistentVolumeClaimSpec [kubernetes/kubernetes#67087](https://github.com/kubernetes/kubernetes/pull/67087)
- ProcMount added to SecurityContext and AllowedProcMounts added to
  PodSecurityPolicy to allow paths in the container's /proc to not be masked [kubernetes/kubernetes#64283](https://github.com/kubernetes/kubernetes/pull/64283)
- Support both directory and block device for local volume plugin FileSystem
  VolumeMode [kubernetes/kubernetes#63011](https://github.com/kubernetes/kubernetes/pull/63011)
- SCTP is now supported as additional protocol (alpha) alongside TCP and UDP in
  Pod, Service, Endpoint, and NetworkPolicy [kubernetes/kubernetes#64973](https://github.com/kubernetes/kubernetes/pull/64973)
- RuntimeClass is a new API resource for defining different classes of runtimes
  that may be used to run containers in the cluster. Pods can select a
  RunitmeClass to use via the RuntimeClassName field. This feature is in alpha,
  and the RuntimeClass feature gate must be enabled in order to use it [kubernetes/kubernetes#67737](https://github.com/kubernetes/kubernetes/pull/67737)
- The PodShareProcessNamespace feature to configure PID namespace sharing within
  a pod has been promoted to beta [kubernetes/kubernetes#66507](https://github.com/kubernetes/kubernetes/pull/66507)
- To address the possibility dry-run requests overwhelming admission webhooks that rely on side effects and a reconciliation mechanism, a new field is being added to admissionregistration.k8s.io/v1beta1.ValidatingWebhookConfiguration and admissionregistration.k8s.io/v1beta1.MutatingWebhookConfiguration so that webhooks can explicitly register as having dry-run support. If a dry-run request is made on a resource that triggers a non dry-run supporting webhook, the request will be completely rejected, with "400: Bad Request". Additionally, a new field is being added to the admission.k8s.io/v1beta1.AdmissionReview API object, exposing to webhooks whether or not the request being reviewed is a dry-run [kubernetes/kubernetes#66936](https://github.com/kubernetes/kubernetes/pull/66936)
- Add custom object status and scale api [kubernetes-client/gen#72](https://github.com/kubernetes-client/gen/pull/72)
- dry-run: DELETE operations now support dryRun parameter [kubernetes/kubernetes#65105](https://github.com/kubernetes/kubernetes/pull/65105)
- Default extensions/v1beta1 Deployment's ProgressDeadlineSeconds to MaxInt32
  [kubernetes/kubernetes#66581](https://github.com/kubernetes/kubernetes/pull/66581)

# v7.0.0
**New Features:**
- Add support for refreshing Azure tokens [kubernetes-client/python-base#77](https://github.com/kubernetes-client/python-base/pull/77)

# v7.0.0b1
**New Features:**
- Add Azure support to authentication loading [kubernetes-client/python-base#74](https://github.com/kubernetes-client/python-base/pull/74)

# v7.0.0a1
**Breaking Change:**
- **ACTION REQUIRED** Rename the currently being-used `async` parameter to `async_req` to support Python 3.7 because it's a reserved keyword in Python 3.7 [kubernetes-client/gen#67](https://github.com/kubernetes-client/gen/pull/67)

**Bug Fix:**
- Watch now properly deserializes custom resource objects and updates resource version [kubernetes-client/python-base#64](https://github.com/kubernetes-client/python-base/pull/64)
- `idp-certificate-authority-data` in kubeconfig is now optional instead of required for OIDC token refresh [kubernetes-client/python-base#69](https://github.com/kubernetes-client/python-base/pull/69)

**API Change:**
- ApiextensionsV1beta1Api: Add PATCH and GET to custom_resource_definition_status [kubernetes/kubernetes#63619](https://github.com/kubernetes/kubernetes/pull/63619)
- ApiregistrationV1Api and ApiregistrationV1beta1Api: Add PATCH and GET to api_service_status [kubernetes/kubernetes#64063](https://github.com/kubernetes/kubernetes/pull/64063)
- CertificatesV1beta1Api: Add PATCH and GET to certificate_signing_request_status [kubernetes/kubernetes#64063](https://github.com/kubernetes/kubernetes/pull/64063)
- SchedulingV1beta1Api: Promote priority_class to beta [kubernetes/kubernetes#63100](https://github.com/kubernetes/kubernetes/pull/63100)
- PodSecurityPolicy now supports restricting hostPath volume mounts to be readOnly and under specific path prefixes [kubernetes/kubernetes#58647](https://github.com/kubernetes/kubernetes/pull/58647)
- The Sysctls experimental feature has been promoted to beta (enabled by default via the `Sysctls` feature flag). PodSecurityPolicy and Pod objects now have fields for specifying and controlling sysctls. Alpha sysctl annotations will be ignored by 1.11+ kubelets. All alpha sysctl annotations in existing deployments must be converted to API fields to be effective. [kubernetes/kubernetes#63717](https://github.com/kubernetes/kubernetes/pull/63717)
- Add CRD Versioning with NOP converter [kubernetes/kubernetes#63830](https://github.com/kubernetes/kubernetes/pull/63830)
- Volume topology aware dynamic provisioning [kubernetes/kubernetes#63233](https://github.com/kubernetes/kubernetes/pull/63233)
- Fixed incorrect OpenAPI schema for CustomResourceDefinition objects with a validation schema [kubernetes/kubernetes#65256](https://github.com/kubernetes/kubernetes/pull/65256)

# v6.0.0
- Config loader now supports OIDC auth [kubernetes-client/python-base#48](https://github.com/kubernetes-client/python-base/pull/48)
- Bug fix: fix expiry time checking in API token refresh [kubernetes-client/python-base#55](https://github.com/kubernetes-client/python-base/pull/55)

# v6.0.0b1
- Update to Kubernetes 1.10 cluster
- Config loader now raises exception on duplicated name in kubeconfig [kubernetes-client/python-base#47](https://github.com/kubernetes-client/python-base/pull/47)

**API change:**
- CustomObjectsApi: Add PATCH to CustomObjectsApi [kubernetes-client/gen#53](https://github.com/kubernetes-client/gen/pull/53)
- Promoting the apiregistration.k8s.io (aggregation) to GA (ApiregistrationV1Api) [kubernetes/kubernetes#58393](https://github.com/kubernetes/kubernetes/pull/58393)
- CoreV1Api: remove /proxy legacy API (deprecated since kubernetes v1.2). Use the /proxy subresources on objects that support HTTP proxying [kubernetes/kubernetes#59884](https://github.com/kubernetes/kubernetes/pull/59884)
- The `PodSecurityPolicy` API has been moved to the `policy/v1beta1` API group. The `PodSecurityPolicy` API in the `extensions/v1beta1` API group is deprecated and will be removed in a future release. Authorizations for using pod security policy resources should change to reference the `policy` API group after upgrading to 1.11 [kubernetes/kubernetes#54933](https://github.com/kubernetes/kubernetes/pull/54933)
- StorageV1beta1Api: Introduce new `VolumeAttachment` API Object [kubernetes/kubernetes#54463](https://github.com/kubernetes/kubernetes/pull/54463)
- V1FlexPersistentVolumeSource: PersistentVolume flexVolume sources can now reference secrets in a namespace other than the PersistentVolumeClaim's namespace [kubernetes/kubernetes#56460](https://github.com/kubernetes/kubernetes/pull/56460)
- ACTION REQUIRED: VolumeScheduling and LocalPersistentVolume features are beta and enabled by default.  The PersistentVolume NodeAffinity alpha annotation is deprecated and will be removed in a future release [kubernetes/kubernetes#59391](https://github.com/kubernetes/kubernetes/pull/59391)
- Allows HorizontalPodAutoscaler to use global metrics not associated with any Kubernetes object (for example metrics from a hoster service running outside of Kubernetes cluster) [kubernetes/kubernetes#60096](https://github.com/kubernetes/kubernetes/pull/60096)
- v1.Pod now has a field to configure whether a single process namespace should be shared between all containers in a pod. This feature is in alpha preview. [kubernetes/kubernetes#58716](https://github.com/kubernetes/kubernetes/pull/58716)
- delete_namespaced_service() now takes an required body (delete option) parameter. Refactor service storage to remove registry wrapper [kubernetes/kubernetes#59510](https://github.com/kubernetes/kubernetes/pull/59510)

**Documentation update:**
- Never let cluster-scoped resources skip webhooks [kubernetes/kubernetes#58185](https://github.com/kubernetes/kubernetes/pull/58185)
- Clarify that ListOptions.Timeout is not conditional on inactivity [kubernetes/kubernetes#58562](https://github.com/kubernetes/kubernetes/pull/58562)
- Indicate endpoint subsets are an optional field [kubernetes/kubernetes#59434](https://github.com/kubernetes/kubernetes/pull/59434)

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

