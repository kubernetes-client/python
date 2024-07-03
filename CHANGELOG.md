# v30.1.0

Kubernetes API Version: v1.30.1


# v30.1.0b1

Kubernetes API Version: v1.30.1


# v30.1.0a1

Kubernetes API Version: v1.30.1

### API Change
- Fixes a 1.30.0 regression in openapi descriptions of imagePullSecrets and hostAliases fields to mark the fields used as keys in those lists as either defaulted or required. ([kubernetes/kubernetes#124553](https://github.com/kubernetes/kubernetes/pull/124553), [@pmalek](https://github.com/pmalek)) [SIG API Machinery]
- Fixes a 1.30.0 regression in openapi descriptions of imagePullSecrets and hostAliases fields to mark the fields used as keys in those lists as either defaulted or required. ([kubernetes/kubernetes#124694](https://github.com/kubernetes/kubernetes/pull/124694), [@pmalek](https://github.com/pmalek)) [SIG API Machinery]
- Added (alpha) support for the `managedBy` field on Jobs. Jobs with a custom value of this field - any value other than `kubernetes.io/job-controller` - were skipped by the job controller, and their reconciliation was delegated to an external controller, indicated by the value of the field. Jobs that didn't have this field at all, or where the field value was the reserved string `kubernetes.io/job-controller`, were reconciled by the built-in job controller.
   ([kubernetes/kubernetes#123273](https://github.com/kubernetes/kubernetes/pull/123273), [@mimowo](https://github.com/mimowo))
- Added alpha-level support for the SuccessPolicy in Jobs.
   ([kubernetes/kubernetes#123412](https://github.com/kubernetes/kubernetes/pull/123412), [@tenzen-y](https://github.com/tenzen-y))
- Added the `CEL` library for IP Addresses and CIDRs. This was made available for use starting from version `1.31`.
   ([kubernetes/kubernetes#121912](https://github.com/kubernetes/kubernetes/pull/121912), [@JoelSpeed](https://github.com/JoelSpeed))
- Allowed container runtimes to fix an image garbage collection bug by adding an `image_id` field to the CRI Container message.
   ([kubernetes/kubernetes#123508](https://github.com/kubernetes/kubernetes/pull/123508), [@saschagrunert](https://github.com/saschagrunert))
- Dynamic Resource Allocation: DRA drivers can now use "structured parameters" to let the scheduler handle claim allocation.
   ([kubernetes/kubernetes#123516](https://github.com/kubernetes/kubernetes/pull/123516), [@pohly](https://github.com/pohly))
- Fixed accidental enablement of the new alpha `optionalOldSelf` API field in `CustomResourceDefinition` validation rules, which should only have been allowed to be set when the `CRDValidationRatcheting` feature gate is enabled.
   ([kubernetes/kubernetes#122329](https://github.com/kubernetes/kubernetes/pull/122329), [@jpbetz](https://github.com/jpbetz))
- Implemented the `prescore` extension point for the `volumeBinding` plugin. It now returns skip if it doesn't do anything in Score.
   ([kubernetes/kubernetes#115768](https://github.com/kubernetes/kubernetes/pull/115768), [@AxeZhan](https://github.com/AxeZhan))
- Kubelet would fail if NodeSwap was used with LimitedSwap and cgroupv1 node.
   ([kubernetes/kubernetes#123738](https://github.com/kubernetes/kubernetes/pull/123738), [@kannon92](https://github.com/kannon92))
- Promoted `AdmissionWebhookMatchConditions` to GA. The feature is now stable, and the feature gate is now locked to default.
   ([kubernetes/kubernetes#123560](https://github.com/kubernetes/kubernetes/pull/123560), [@ivelichkovich](https://github.com/ivelichkovich))
- Structured Authentication Configuration now supports `DiscoveryURL`. If specified, `discoveryURL` overrides the URL used to fetch discovery information. This is for scenarios where the well-known and jwks endpoints are hosted at a different location than the issuer (such as locally in the cluster).
   ([kubernetes/kubernetes#123527](https://github.com/kubernetes/kubernetes/pull/123527), [@aramase](https://github.com/aramase))
- The `StorageVersionMigration` API, previously available as a Custom Resource Definition (CRD), is now a built-in API in Kubernetes.
   ([kubernetes/kubernetes#123344](https://github.com/kubernetes/kubernetes/pull/123344), [@nilekhc](https://github.com/nilekhc))
- When configuring a JWT authenticator:
  
  If `username.expression` used 'claims.email', then 'claims.email_verified' must have been used in `username.expression` or `extra[*].valueExpression` or `claimValidationRules[*].expression`. An example claim validation rule expression that matches the validation automatically applied when `username.claim` is set to 'email' is 'claims.?email_verified.orValue(true)'.
   ([kubernetes/kubernetes#123737](https://github.com/kubernetes/kubernetes/pull/123737), [@enj](https://github.com/enj))
- `readOnly` volumes now support recursive read-only mounts for kernel versions >= 5.12."
   ([kubernetes/kubernetes#123180](https://github.com/kubernetes/kubernetes/pull/123180), [@AkihiroSuda](https://github.com/AkihiroSuda))
- cri-api: Implemented KEP-3857: Recursive Read-only (RRO) mounts.
   ([kubernetes/kubernetes#123272](https://github.com/kubernetes/kubernetes/pull/123272), [@AkihiroSuda](https://github.com/AkihiroSuda))
- kube-apiserver: the AuthenticationConfiguration type accepted in `--authentication-config` files has been promoted to `apiserver.config.k8s.io/v1beta1`.
   ([kubernetes/kubernetes#123696](https://github.com/kubernetes/kubernetes/pull/123696), [@aramase](https://github.com/aramase))
- kubelet allowed specifying a custom root directory for pod logs (instead of the default /var/log/pods) using the `podLogsDir` key in kubelet configuration.
   ([kubernetes/kubernetes#112957](https://github.com/kubernetes/kubernetes/pull/112957), [@mxpv](https://github.com/mxpv))
- resource.k8s.io/ResourceClaim (alpha API): The strategic merge patch strategy for the `status.reservedFor` array was changed so that a strategic-merge-patch can now add individual entries. This change may break clients using strategic merge patch to update status, which rely on the previous behavior (replacing the entire array).
   ([kubernetes/kubernetes#122276](https://github.com/kubernetes/kubernetes/pull/122276), [@pohly](https://github.com/pohly))
- Added a CBOR implementation of `runtime.Serializer`. Until CBOR graduates to Alpha, API servers will refuse to start if configured with CBOR support. ([kubernetes/kubernetes#122881](https://github.com/kubernetes/kubernetes/pull/122881), [@benluddy](https://github.com/benluddy))
- Added a alpha feature, behind the `RelaxedEnvironmentVariableValidation` feature gate.
  When that gate is enabled, Kubernetes allows almost all printable ASCII characters to be used in the names
  of environment variables for containers in Pods. ([kubernetes/kubernetes#123385](https://github.com/kubernetes/kubernetes/pull/123385), [@HirazawaUi](https://github.com/HirazawaUi))
- Added a new (alpha) field, `trafficDistribution`, to the Service `spec` to express preferences for traffic distribution to endpoints. Enabled through the `ServiceTrafficDistribution` feature gate. ([kubernetes/kubernetes#123487](https://github.com/kubernetes/kubernetes/pull/123487), [@gauravkghildiyal](https://github.com/gauravkghildiyal))
- Added audienceMatchPolicy field to AuthenticationConfiguration and support for configuring multiple audiences.
  The "audienceMatchPolicy" can be empty (or unset) when a single audience is specified in the "audiences" field.
  The "audienceMatchPolicy" must be set to "MatchAny" when multiple audiences are specified in the "audiences" field. ([kubernetes/kubernetes#123165](https://github.com/kubernetes/kubernetes/pull/123165), [@aramase](https://github.com/aramase))
- Added consistent vanity import to files and provided tooling for verifying and updating them. ([kubernetes/kubernetes#120642](https://github.com/kubernetes/kubernetes/pull/120642), [@jcchavezs](https://github.com/jcchavezs))
- Added the `disable-force-detach` CLI option for `kube-controller-manager`. By default, it's set to `false`. When enabled, it prevents force detaching volumes based on maximum unmount time and node status. If activated, the non-graceful node shutdown feature must be used to recover from node failure. Additionally, if a pod needs to be forcibly terminated at the risk of corruption, the appropriate VolumeAttachment object must be deleted. ([kubernetes/kubernetes#120344](https://github.com/kubernetes/kubernetes/pull/120344), [@rohitssingh](https://github.com/rohitssingh))
- Added to `MutableFeatureGate` the ability to override the default setting of feature gates, to allow default-enabling a feature on a component-by-component basis instead of for all affected components simultaneously. ([kubernetes/kubernetes#122647](https://github.com/kubernetes/kubernetes/pull/122647), [@benluddy](https://github.com/benluddy))
- Aggregated discovery supports both `v2beta1` and v2 types and feature is promoted to GA. ([kubernetes/kubernetes#122882](https://github.com/kubernetes/kubernetes/pull/122882), [@Jefftree](https://github.com/Jefftree))
- Alpha support for field selectors on custom resources has been added. With the `CustomResourceFieldSelectors` feature gate enabled, the CustomResourceDefinition API now allows specifying `selectableFields`. Listing a field there enables filtering custom resources for that CustomResourceDefinition in list or watch requests. ([kubernetes/kubernetes#122717](https://github.com/kubernetes/kubernetes/pull/122717), [@jpbetz](https://github.com/jpbetz))
- AppArmor profiles can now be configured through fields on the `PodSecurityContext` and container `SecurityContext`. The beta AppArmor annotations are deprecated, and AppArmor status is no longer included in the node ready condition. ([kubernetes/kubernetes#123435](https://github.com/kubernetes/kubernetes/pull/123435), [@tallclair](https://github.com/tallclair))
- Contextual logging is now in beta and enabled by default. Check out the [KEP](https://github.com/kubernetes/enhancements/issues/3077) and [official documentation](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#contextual-logging) for more details. ([kubernetes/kubernetes#122589](https://github.com/kubernetes/kubernetes/pull/122589), [@pohly](https://github.com/pohly))
- Enabled concurrent log rotation in kubelet. You can now configure the maximum number of concurrent rotations with the `containerLogMaxWorkers` setting, and adjust the monitoring interval with `containerLogMonitorInterval`. ([kubernetes/kubernetes#114301](https://github.com/kubernetes/kubernetes/pull/114301), [@harshanarayana](https://github.com/harshanarayana))
- Graduated pod scheduling gates to general availability.
  The `PodSchedulingReadiness` feature gate no longer has any effect, and the
  `.spec.schedulingGates` field is always available within the Pod and PodTemplate APIs. ([kubernetes/kubernetes#123575](https://github.com/kubernetes/kubernetes/pull/123575), [@Huang-Wei](https://github.com/Huang-Wei))
- Graduated support for `minDomains` in pod topology spread constraints, to general availability.
  The `MinDomainsInPodTopologySpread` feature gate no longer has any effect, and the field is
  always available within the Pod and PodTemplate APIs. ([kubernetes/kubernetes#123481](https://github.com/kubernetes/kubernetes/pull/123481), [@sanposhiho](https://github.com/sanposhiho))
- In kubelet configuration, the `.memorySwap.swapBehavior` field now accepts a new value `NoSwap`, which becomes the default if unspecified. The previously accepted `UnlimitedSwap` value has been dropped.
   ([kubernetes/kubernetes#122745](https://github.com/kubernetes/kubernetes/pull/122745), [@kannon92](https://github.com/kannon92))
- Kube-apiserver: the AuthorizationConfiguration type accepted in `--authorization-config` files has been promoted to `apiserver.config.k8s.io/v1beta1`. ([kubernetes/kubernetes#123640](https://github.com/kubernetes/kubernetes/pull/123640), [@liggitt](https://github.com/liggitt))
- OIDC authentication will now fail if the username asserted based on a CEL expression config is the empty string.  Previously the request would be authenticated with the username set to the empty string. ([kubernetes/kubernetes#123568](https://github.com/kubernetes/kubernetes/pull/123568), [@enj](https://github.com/enj))
- Removed note that `hostAliases` are not supported on hostNetwork Pods from the PodSpec API. The feature has been supported since v1.8. ([kubernetes/kubernetes#122422](https://github.com/kubernetes/kubernetes/pull/122422), [@neolit123](https://github.com/neolit123))
- Structured Authentication Configuration now supports configuring multiple JWT authenticators. The maximum allowed JWT authenticators in the authentication configuration is 64. ([kubernetes/kubernetes#123431](https://github.com/kubernetes/kubernetes/pull/123431), [@aramase](https://github.com/aramase))
- Text logging in Kubernetes components now uses [textlogger](https://pkg.go.dev/k8s.io/klog/v2@v2.120.0/textlogger). The same split streams of info and error log entries with buffering of info entries is now also supported for text output (off by default, alpha feature). Previously, this was only supported for JSON. Performance is better also without split streams. ([kubernetes/kubernetes#114672](https://github.com/kubernetes/kubernetes/pull/114672), [@pohly](https://github.com/pohly))
- The API server now detects and fails on startup if there are conflicting issuers between JWT authenticators and service account configurations. Previously, such configurations would run but could be inconsistently effective depending on the credential. ([kubernetes/kubernetes#123561](https://github.com/kubernetes/kubernetes/pull/123561), [@enj](https://github.com/enj))
- The JWT authenticator configuration set via the `--authentication-config` flag is now dynamically reloaded as the file changes on disk. ([kubernetes/kubernetes#123525](https://github.com/kubernetes/kubernetes/pull/123525), [@enj](https://github.com/enj))
- The `StructuredAuthenticationConfiguration` feature is now beta and enabled. ([kubernetes/kubernetes#123719](https://github.com/kubernetes/kubernetes/pull/123719), [@enj](https://github.com/enj))
- The `kube_codegen` tool now ignores the vendor folder during code generation.
   ([kubernetes/kubernetes#122729](https://github.com/kubernetes/kubernetes/pull/122729), [@jparrill](https://github.com/jparrill))
- The kubernetes repo now uses Go workspaces.  This should not impact end users at all, but does have impact for developers of downstream projects.  Switching to workspaces caused some breaking changes in the flags to the various k8s.io/code-generator tools.  Downstream consumers should look at staging/src/k8s.io/code-generator/kube_codegen.sh to see the changes. ([kubernetes/kubernetes#123529](https://github.com/kubernetes/kubernetes/pull/123529), [@thockin](https://github.com/thockin))
- Updated an audit annotation key used by the `…/serviceaccounts/<name>/token` resource handler.
  The annotation used to persist the issued credential identifier is now `authentication.kubernetes.io/issued-credential-id`. ([kubernetes/kubernetes#123098](https://github.com/kubernetes/kubernetes/pull/123098), [@munnerz](https://github.com/munnerz)) [SIG Auth]
- Users are now allowed to mutate `FSGroupPolicy` and `PodInfoOnMount` in `CSIDriver.Spec`. ([kubernetes/kubernetes#116209](https://github.com/kubernetes/kubernetes/pull/116209), [@haoruan](https://github.com/haoruan))
- ValidatingAdmissionPolicy was promoted to GA and will be `enabled` by default. ([kubernetes/kubernetes#123405](https://github.com/kubernetes/kubernetes/pull/123405), [@cici37](https://github.com/cici37))
- When scheduling a mix of pods using `ResourceClaims` and others that don't, scheduling a pod with `ResourceClaims` has a lower impact on scheduling latency. ([kubernetes/kubernetes#121876](https://github.com/kubernetes/kubernetes/pull/121876), [@pohly](https://github.com/pohly))
- When working with client-go events, it's now recommended to use `NewEventBroadcasterAdapterWithContext` instead of `NewEventBroadcasterAdapter` if contextual logging support is needed. ([kubernetes/kubernetes#122142](https://github.com/kubernetes/kubernetes/pull/122142), [@pohly](https://github.com/pohly))
- A new (alpha) field, `trafficDistribution`, has been added to the Service `spec`.
  This field provides a way to express preferences for how traffic is distributed to the endpoints for a Service.
  It can be enabled through the `ServiceTrafficDistribution` feature gate. ([kubernetes/kubernetes#123487](https://github.com/kubernetes/kubernetes/pull/123487), [@gauravkghildiyal](https://github.com/gauravkghildiyal)) [SIG API Machinery, Apps and Network]
- Add alpha-level support for the SuccessPolicy in Jobs ([kubernetes/kubernetes#123412](https://github.com/kubernetes/kubernetes/pull/123412), [@tenzen-y](https://github.com/tenzen-y)) [SIG API Machinery, Apps and Testing]
- Added (alpha) support for the managedBy field on Jobs. Jobs with a custom value of this field - any
  value other than `kubernetes.io/job-controller` - are skipped by the job controller, and their
  reconciliation is delegated to an external controller, indicated by the value of the field. Jobs that
  don't have this field at all, or where the field value is the reserved string `kubernetes.io/job-controller`,
  are reconciled by the built-in job controller. ([kubernetes/kubernetes#123273](https://github.com/kubernetes/kubernetes/pull/123273), [@mimowo](https://github.com/mimowo)) [SIG API Machinery, Apps and Testing]
- Added a alpha feature, behind the `RelaxedEnvironmentVariableValidation` feature gate.
  When that gate is enabled, Kubernetes allows almost all printable ASCII characters to be used in the names
  of environment variables for containers in Pods. ([kubernetes/kubernetes#123385](https://github.com/kubernetes/kubernetes/pull/123385), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Apps, Node and Testing]
- Added alpha support for field selectors on custom resources.
  Provided that the `CustomResourceFieldSelectors` feature gate is enabled, the CustomResourceDefinition
  API now lets you specify `selectableFields`. Listing a field there allows filtering custom resources for that
  CustomResourceDefinition in **list** or **watch** requests. ([kubernetes/kubernetes#122717](https://github.com/kubernetes/kubernetes/pull/122717), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Added support for configuring multiple JWT authenticators in Structured Authentication Configuration. The maximum allowed JWT authenticators in the authentication configuration is 64. ([kubernetes/kubernetes#123431](https://github.com/kubernetes/kubernetes/pull/123431), [@aramase](https://github.com/aramase)) [SIG Auth and Testing]
- Aggregated discovery supports both v2beta1 and v2 types and feature is promoted to GA ([kubernetes/kubernetes#122882](https://github.com/kubernetes/kubernetes/pull/122882), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery and Testing]
- Allowing container runtimes to fix an image garbage collection bug by adding an `image_id` field to the CRI Container message. ([kubernetes/kubernetes#123508](https://github.com/kubernetes/kubernetes/pull/123508), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- AppArmor profiles can now be configured through fields on the PodSecurityContext and container SecurityContext.
  - The beta AppArmor annotations are deprecated.
  - AppArmor status is no longer included in the node ready condition ([kubernetes/kubernetes#123435](https://github.com/kubernetes/kubernetes/pull/123435), [@tallclair](https://github.com/tallclair)) [SIG API Machinery, Apps, Auth, Node and Testing]
- Conflicting issuers between JWT authenticators and service account config are now detected and fail on API server startup.  Previously such a config would run but would be inconsistently effective depending on the credential. ([kubernetes/kubernetes#123561](https://github.com/kubernetes/kubernetes/pull/123561), [@enj](https://github.com/enj)) [SIG API Machinery and Auth]
- Dynamic Resource Allocation: DRA drivers may now use "structured parameters" to let the scheduler handle claim allocation. ([kubernetes/kubernetes#123516](https://github.com/kubernetes/kubernetes/pull/123516), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Cluster Lifecycle, Instrumentation, Node, Release, Scheduling, Storage and Testing]
- Graduated pod scheduling gates to general availability.
  The `PodSchedulingReadiness` feature gate no longer has any effect, and the
  `.spec.schedulingGates` field is always available within the Pod and PodTemplate APIs. ([kubernetes/kubernetes#123575](https://github.com/kubernetes/kubernetes/pull/123575), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Graduated support for `minDomains` in pod topology spread constraints, to general availability.
  The `MinDomainsInPodTopologySpread` feature gate no longer has any effect, and the field is
  always available within the Pod and PodTemplate APIs. ([kubernetes/kubernetes#123481](https://github.com/kubernetes/kubernetes/pull/123481), [@sanposhiho](https://github.com/sanposhiho)) [SIG API Machinery, Apps, Scheduling and Testing]
- JWT authenticator config set via the --authentication-config flag is now dynamically reloaded as the file changes on disk. ([kubernetes/kubernetes#123525](https://github.com/kubernetes/kubernetes/pull/123525), [@enj](https://github.com/enj)) [SIG API Machinery, Auth and Testing]
- Kube-apiserver: the AuthenticationConfiguration type accepted in `--authentication-config` files has been promoted to `apiserver.config.k8s.io/v1beta1`. ([kubernetes/kubernetes#123696](https://github.com/kubernetes/kubernetes/pull/123696), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Kube-apiserver: the AuthorizationConfiguration type accepted in `--authorization-config` files has been promoted to `apiserver.config.k8s.io/v1beta1`. ([kubernetes/kubernetes#123640](https://github.com/kubernetes/kubernetes/pull/123640), [@liggitt](https://github.com/liggitt)) [SIG Auth and Testing]
- Kubelet should fail if NodeSwap is used with LimitedSwap and cgroupv1 node. ([kubernetes/kubernetes#123738](https://github.com/kubernetes/kubernetes/pull/123738), [@kannon92](https://github.com/kannon92)) [SIG API Machinery, Node and Testing]
- Kubelet: a custom root directory for pod logs (instead of default /var/log/pods) can be specified using the `podLogsDir`
  key in kubelet configuration. ([kubernetes/kubernetes#112957](https://github.com/kubernetes/kubernetes/pull/112957), [@mxpv](https://github.com/mxpv)) [SIG API Machinery, Node, Scalability and Testing]
- Kubelet: the `.memorySwap.swapBehavior` field in kubelet configuration accepts a new value `NoSwap` and makes this the default if unspecified; the previously accepted `UnlimitedSwap` value has been dropped. ([kubernetes/kubernetes#122745](https://github.com/kubernetes/kubernetes/pull/122745), [@kannon92](https://github.com/kannon92)) [SIG API Machinery, Node and Testing]
- OIDC authentication will now fail if the username asserted based on a CEL expression config is the empty string.  Previously the request would be authenticated with the username set to the empty string. ([kubernetes/kubernetes#123568](https://github.com/kubernetes/kubernetes/pull/123568), [@enj](https://github.com/enj)) [SIG API Machinery, Auth and Testing]
- PodSpec API: remove note that hostAliases are not supported on hostNetwork Pods. The feature has been supported since v1.8. ([kubernetes/kubernetes#122422](https://github.com/kubernetes/kubernetes/pull/122422), [@neolit123](https://github.com/neolit123)) [SIG API Machinery and Apps]
- Promote AdmissionWebhookMatchConditions to GA. The feature is now stable and the feature gate is now locked to default. ([kubernetes/kubernetes#123560](https://github.com/kubernetes/kubernetes/pull/123560), [@ivelichkovich](https://github.com/ivelichkovich)) [SIG API Machinery and Testing]
- Structured Authentication Configuration now supports `DiscoveryURL`. 
  discoveryURL if specified, overrides the URL used to fetch discovery information. 
  This is for scenarios where the well-known and jwks endpoints are hosted at a different
  location than the issuer (such as locally in the cluster). ([kubernetes/kubernetes#123527](https://github.com/kubernetes/kubernetes/pull/123527), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Support Recursive Read-only (RRO) mounts  (KEP-3857) ([kubernetes/kubernetes#123180](https://github.com/kubernetes/kubernetes/pull/123180), [@AkihiroSuda](https://github.com/AkihiroSuda)) [SIG API Machinery, Apps, Node and Testing]
- The StructuredAuthenticationConfiguration feature is now beta and enabled by default. ([kubernetes/kubernetes#123719](https://github.com/kubernetes/kubernetes/pull/123719), [@enj](https://github.com/enj)) [SIG API Machinery and Auth]
- The `StorageVersionMigration` API, which was previously available as a Custom Resource Definition (CRD), is now a built-in API in Kubernetes. ([kubernetes/kubernetes#123344](https://github.com/kubernetes/kubernetes/pull/123344), [@nilekhc](https://github.com/nilekhc)) [SIG API Machinery, Apps, Auth, CLI and Testing]
- The kubernetes repo now uses Go workspaces.  This should not impact end users at all, but does have impact for developers of downstream projects.  Switching to workspaces caused some breaking changes in the flags to the various k8s.io/code-generator tools.  Downstream consumers should look at staging/src/k8s.io/code-generator/kube_codegen.sh to see the changes. ([kubernetes/kubernetes#123529](https://github.com/kubernetes/kubernetes/pull/123529), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Storage and Testing]
- ValidatingAdmissionPolicy is promoted to GA and will be enabled by default. ([kubernetes/kubernetes#123405](https://github.com/kubernetes/kubernetes/pull/123405), [@cici37](https://github.com/cici37)) [SIG API Machinery, Apps, Auth and Testing]
- When configuring a JWT authenticator:
  
  If username.expression uses 'claims.email', then 'claims.email_verified' must be used in
  username.expression or extra[*].valueExpression or claimValidationRules[*].expression.
  An example claim validation rule expression that matches the validation automatically
  applied when username.claim is set to 'email' is 'claims.?email_verified.orValue(true)'. ([kubernetes/kubernetes#123737](https://github.com/kubernetes/kubernetes/pull/123737), [@enj](https://github.com/enj)) [SIG API Machinery and Auth]
- Added a CBOR implementation of `runtime.Serializer`. Until CBOR graduates to Alpha, API servers will refuse to start if configured with CBOR support. ([kubernetes/kubernetes#122881](https://github.com/kubernetes/kubernetes/pull/122881), [@benluddy](https://github.com/benluddy)) [SIG API Machinery]
- Added audienceMatchPolicy field to AuthenticationConfiguration and support for configuring multiple audiences.
  
  - The "audienceMatchPolicy" can be empty (or unset) when a single audience is specified in the "audiences" field.
  - The "audienceMatchPolicy" must be set to "MatchAny" when multiple audiences are specified in the "audiences" field. ([kubernetes/kubernetes#123165](https://github.com/kubernetes/kubernetes/pull/123165), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Contextual logging is now beta and enabled by default. ([kubernetes/kubernetes#122589](https://github.com/kubernetes/kubernetes/pull/122589), [@pohly](https://github.com/pohly)) [SIG Instrumentation]
- Cri-api: KEP-3857: Recursive Read-only (RRO) mounts ([kubernetes/kubernetes#123272](https://github.com/kubernetes/kubernetes/pull/123272), [@AkihiroSuda](https://github.com/AkihiroSuda)) [SIG Node]
- Enabled a mechanism for concurrent log rotatation via `kubelet` using a configuration entity of `containerLogMaxWorkers` which controls the maximum number of concurrent rotation that can be performed and an interval configuration of `containerLogMonitorInterval` that can aid is configuring the monitoring duration to best suite your cluster's log generation standards. ([kubernetes/kubernetes#114301](https://github.com/kubernetes/kubernetes/pull/114301), [@harshanarayana](https://github.com/harshanarayana)) [SIG API Machinery, Node and Testing]
- Text logging in Kubernetes components now uses [textlogger](https://pkg.go.dev/k8s.io/klog/v2@v2.120.0/textlogger). The same split streams of info and error log entries with buffering of info entries is now also supported for text output (off by default, alpha feature). Previously, this was only supported for JSON. Performance is better also without split streams. ([kubernetes/kubernetes#114672](https://github.com/kubernetes/kubernetes/pull/114672), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Storage and Testing]
- This change adds the following CLI option for `kube-controller-manager`:
  - `disable-force-detach` (defaults to `false`): Prevent force detaching volumes based on maximum unmount time and node status. If enabled, the non-graceful node shutdown feature must be used to recover from node failure (see https://kubernetes.io/blog/2023/08/16/kubernetes-1-28-non-graceful-node-shutdown-ga/). If enabled and a pod must be forcibly terminated at the risk of corruption, then the appropriate VolumeAttachment object (see here: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/) must be deleted. ([kubernetes/kubernetes#120344](https://github.com/kubernetes/kubernetes/pull/120344), [@rohitssingh](https://github.com/rohitssingh)) [SIG API Machinery, Apps, Storage and Testing]
- Updated an audit annotation key used by the `…/serviceaccounts/<name>/token` resource handler.
  The annotation used to persist the issued credential identifier is now `authentication.kubernetes.io/issued-credential-id`. ([kubernetes/kubernetes#123098](https://github.com/kubernetes/kubernetes/pull/123098), [@munnerz](https://github.com/munnerz)) [SIG Auth]
- Add CEL library for IP Addresses and CIDRs. This will not be available for use until 1.31. ([kubernetes/kubernetes#121912](https://github.com/kubernetes/kubernetes/pull/121912), [@JoelSpeed](https://github.com/JoelSpeed)) [SIG API Machinery]
- Added to MutableFeatureGate the ability to override the default setting of feature gates, to allow default-enabling a feature on a component-by-component basis instead of for all affected components simultaneously. ([kubernetes/kubernetes#122647](https://github.com/kubernetes/kubernetes/pull/122647), [@benluddy](https://github.com/benluddy)) [SIG API Machinery and Cluster Lifecycle]
- Adds a rule on the kube_codegen tool to ignore vendor folder during the code generation. ([kubernetes/kubernetes#122729](https://github.com/kubernetes/kubernetes/pull/122729), [@jparrill](https://github.com/jparrill)) [SIG API Machinery and Cluster Lifecycle]
- Allow users to mutate FSGroupPolicy and PodInfoOnMount in CSIDriver.Spec ([kubernetes/kubernetes#116209](https://github.com/kubernetes/kubernetes/pull/116209), [@haoruan](https://github.com/haoruan)) [SIG API Machinery, Storage and Testing]
- Client-go events: `NewEventBroadcasterAdapterWithContext` should be used instead of `NewEventBroadcasterAdapter` if the goal is to support contextual logging. ([kubernetes/kubernetes#122142](https://github.com/kubernetes/kubernetes/pull/122142), [@pohly](https://github.com/pohly)) [SIG API Machinery, Instrumentation and Scheduling]
- Fixes accidental enablement of the new alpha `optionalOldSelf` API field in CustomResourceDefinition validation rules, which should only be allowed to be set when the CRDValidationRatcheting feature gate is enabled. ([kubernetes/kubernetes#122329](https://github.com/kubernetes/kubernetes/pull/122329), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Implement  `prescore` extension point for `volumeBinding` plugin. Return skip if it doesn't do anything in Score. ([kubernetes/kubernetes#115768](https://github.com/kubernetes/kubernetes/pull/115768), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling, Storage and Testing]
- Resource.k8s.io/ResourceClaim (alpha API): the strategic merge patch strategy for the `status.reservedFor` array was changed such that a strategic-merge-patch can add individual entries. This breaks clients using strategic merge patch to update status which rely on the previous behavior (replacing the entire array). ([kubernetes/kubernetes#122276](https://github.com/kubernetes/kubernetes/pull/122276), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- When scheduling a mixture of pods using ResourceClaims and others which don't, scheduling a pod with ResourceClaims impacts scheduling latency less. ([kubernetes/kubernetes#121876](https://github.com/kubernetes/kubernetes/pull/121876), [@pohly](https://github.com/pohly)) [SIG API Machinery, Node, Scheduling and Testing]


# v29.0.0

Kubernetes API Version: v1.29.0

### Bug or Regression
- Fix UTF-8 failures in Watch (#2100, @davidopic)
- Fix upper version boundary of urllib3, since other dependencies don't support urllib3 in version 2 (#2105, @jsaalfeld)

# v29.0.0b1

Kubernetes API Version: v1.29.0

### Bug or Regression
- Fix UTF-8 failures in Watch (#2100, @davidopic)
- Fix upper version boundary of urllib3, since other dependencies don't support urllib3 in version 2 (#2105, @jsaalfeld)

# v29.0.0a1

Kubernetes API Version: v1.29.0

### API Change
- '`kube-apiserver`: adds `--authentication-config` flag for reading `AuthenticationConfiguration`
  files. `--authentication-config` flag is mutually exclusive with the existing `--oidc-*`
  flags.' ([kubernetes/kubernetes#119142](https://github.com/kubernetes/kubernetes/pull/119142), [@aramase](https://github.com/aramase))
- '`kube-scheduler` component config (`KubeSchedulerConfiguration`) `kubescheduler.config.k8s.io/v1beta3`
  is removed in `v1.29`. Migrated `kube-scheduler` configuration files to `kubescheduler.config.k8s.io/v1`.' ([kubernetes/kubernetes#119994](https://github.com/kubernetes/kubernetes/pull/119994), [@SataQiu](https://github.com/SataQiu))
- A new sleep action for the `PreStop` lifecycle hook was added, allowing containers to pause for a specified duration before termination. ([kubernetes/kubernetes#119026](https://github.com/kubernetes/kubernetes/pull/119026), [@AxeZhan](https://github.com/AxeZhan))
- Added CEL expressions to `v1alpha1 AuthenticationConfiguration`. ([kubernetes/kubernetes#121078](https://github.com/kubernetes/kubernetes/pull/121078), [@aramase](https://github.com/aramase))
- Added Windows support for InPlace Pod Vertical Scaling feature. ([kubernetes/kubernetes#112599](https://github.com/kubernetes/kubernetes/pull/112599), [@fabi200123](https://github.com/fabi200123)) [SIG Autoscaling, Node, Scalability, Scheduling and Windows]
- Added `ImageMaximumGCAge` field to Kubelet configuration, which allows a user to set the maximum age an image is unused before it's garbage collected. ([kubernetes/kubernetes#121275](https://github.com/kubernetes/kubernetes/pull/121275), [@haircommander](https://github.com/haircommander))
- Added `UserNamespacesPodSecurityStandards` feature gate to enable user namespace support for Pod Security Standards.
  Enabling this feature will modify all Pod Security Standard rules to allow setting: `spec[.*].securityContext.[runAsNonRoot,runAsUser]`.
  This feature gate should only be enabled if all nodes in the cluster support the user namespace feature and have it enabled.
  The feature gate will not graduate or be enabled by default in future Kubernetes releases. ([kubernetes/kubernetes#118760](https://github.com/kubernetes/kubernetes/pull/118760), [@saschagrunert](https://github.com/saschagrunert)) [SIG API Machinery, Auth, Node and Release]
- Added `optionalOldSelf` to `x-kubernetes-validations` to support ratcheting CRD schema constraints. ([kubernetes/kubernetes#121034](https://github.com/kubernetes/kubernetes/pull/121034), [@alexzielenski](https://github.com/alexzielenski))
- Added a new `ServiceCIDR` type that allows to dynamically configure the cluster range used to allocate `Service ClusterIPs` addresses. ([kubernetes/kubernetes#116516](https://github.com/kubernetes/kubernetes/pull/116516), [@aojea](https://github.com/aojea))
- Added a new `ipMode` field to the `.status` of Services where `type` is set to `LoadBalancer`.
  The new field is behind the `LoadBalancerIPMode` feature gate. ([kubernetes/kubernetes#119937](https://github.com/kubernetes/kubernetes/pull/119937), [@RyanAoh](https://github.com/RyanAoh)) [SIG API Machinery, Apps, Cloud Provider, Network and Testing]
- Added options for configuring `nf_conntrack_udp_timeout`, and `nf_conntrack_udp_timeout_stream` variables of netfilter conntrack subsystem. ([kubernetes/kubernetes#120808](https://github.com/kubernetes/kubernetes/pull/120808), [@aroradaman](https://github.com/aroradaman))
- Added support for CEL expressions to `v1alpha1 AuthorizationConfiguration` webhook `matchConditions`. ([kubernetes/kubernetes#121223](https://github.com/kubernetes/kubernetes/pull/121223), [@ritazh](https://github.com/ritazh))
- Added support for projecting `certificates.k8s.io/v1alpha1` ClusterTrustBundle objects into pods. ([kubernetes/kubernetes#113374](https://github.com/kubernetes/kubernetes/pull/113374), [@ahmedtd](https://github.com/ahmedtd))
- Added the `DisableNodeKubeProxyVersion` feature gate. If `DisableNodeKubeProxyVersion` is enabled, the `kubeProxyVersion` field is not set. ([kubernetes/kubernetes#120954](https://github.com/kubernetes/kubernetes/pull/120954), [@HirazawaUi](https://github.com/HirazawaUi))
- Fixed a bug where CEL expressions in CRD validation rules would incorrectly compute a high estimated cost for functions that return strings, lists or maps.
  The incorrect cost was evident when the result of a function was used in subsequent operations. ([kubernetes/kubernetes#119800](https://github.com/kubernetes/kubernetes/pull/119800), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth and Cloud Provider]
- Fixed the API comments for the Job `Ready` field in status. ([kubernetes/kubernetes#121765](https://github.com/kubernetes/kubernetes/pull/121765), [@mimowo](https://github.com/mimowo))
- Fixed the API comments for the `FailIndex` Job pod failure policy action. ([kubernetes/kubernetes#121764](https://github.com/kubernetes/kubernetes/pull/121764), [@mimowo](https://github.com/mimowo))
- Go API: the `ResourceRequirements` struct was replaced with `VolumeResourceRequirements` for use with volumes. ([kubernetes/kubernetes#118653](https://github.com/kubernetes/kubernetes/pull/118653), [@pohly](https://github.com/pohly))
- Graduated `Job BackoffLimitPerIndex` feature to `beta`. ([kubernetes/kubernetes#121356](https://github.com/kubernetes/kubernetes/pull/121356), [@mimowo](https://github.com/mimowo))
- Marked the `onPodConditions` field as optional in `Job`'s pod failure policy. ([kubernetes/kubernetes#120204](https://github.com/kubernetes/kubernetes/pull/120204), [@mimowo](https://github.com/mimowo))
- Promoted `PodReadyToStartContainers` condition to `beta`. ([kubernetes/kubernetes#119659](https://github.com/kubernetes/kubernetes/pull/119659), [@kannon92](https://github.com/kannon92))
- The `flowcontrol.apiserver.k8s.io/v1beta3` `FlowSchema` and `PriorityLevelConfiguration` APIs has been promoted to `flowcontrol.apiserver.k8s.io/v1`, with the following changes:
  - `PriorityLevelConfiguration`: the `.spec.limited.nominalConcurrencyShares` field defaults to `30` only if the field is omitted (v1beta3 also defaulted an explicit `0` value to `30`). Specifying an explicit `0` value is not allowed in the `v1` version in v1.29 to ensure compatibility with `v1.28` API servers. In `v1.30`, explicit `0` values will be allowed in this field in the `v1` API.
  The `flowcontrol.apiserver.k8s.io/v1beta3` APIs are deprecated and will no longer be served in v1.32. All existing objects are available via the `v1` APIs. Transition clients and manifests to use the `v1` APIs before upgrading to `v1.32`. ([kubernetes/kubernetes#121089](https://github.com/kubernetes/kubernetes/pull/121089), [@tkashem](https://github.com/tkashem))
- The `kube-proxy` command-line documentation was updated to clarify that
  `--bind-address` does not actually have anything to do with binding to an
  address, and you probably don't actually want to be using it. ([kubernetes/kubernetes#120274](https://github.com/kubernetes/kubernetes/pull/120274), [@danwinship](https://github.com/danwinship))
- The `kube-scheduler` `selectorSpread` plugin has been removed, please use the `podTopologySpread` plugin instead. ([kubernetes/kubernetes#117720](https://github.com/kubernetes/kubernetes/pull/117720), [@kerthcet](https://github.com/kerthcet))
- The `matchLabelKeys/mismatchLabelKeys` feature is introduced to the hard/soft `PodAffinity/PodAntiAffinity`. ([kubernetes/kubernetes#116065](https://github.com/kubernetes/kubernetes/pull/116065), [@sanposhiho](https://github.com/sanposhiho))
- When updating a CRD, per-expression cost limit check are now skipped for `x-kubernetes-validations` rules of versions that are not mutated. ([kubernetes/kubernetes#121460](https://github.com/kubernetes/kubernetes/pull/121460), [@jiahuif](https://github.com/jiahuif))
- `CSINodeExpandSecret` feature has been promoted to `GA` in this release and is enabled
  by default. The CSI drivers can make use of the `secretRef` values passed in `NodeExpansion`
  request optionally sent by the CSI Client from this release onwards. ([kubernetes/kubernetes#121303](https://github.com/kubernetes/kubernetes/pull/121303), [@humblec](https://github.com/humblec))
- `NodeStageVolume` calls will now be retried if the CSI node driver is not running. ([kubernetes/kubernetes#120330](https://github.com/kubernetes/kubernetes/pull/120330), [@rohitssingh](https://github.com/rohitssingh))
- `PersistentVolumeLastPhaseTransitionTime` is now beta and enabled by default. ([kubernetes/kubernetes#120627](https://github.com/kubernetes/kubernetes/pull/120627), [@RomanBednar](https://github.com/RomanBednar))
- `ValidatingAdmissionPolicy` type checking now supports CRDs and API extensions types. ([kubernetes/kubernetes#119109](https://github.com/kubernetes/kubernetes/pull/119109), [@jiahuif](https://github.com/jiahuif))
- `kube-apiserver`: added `--authorization-config` flag for reading a configuration file containing an `apiserver.config.k8s.io/v1alpha1 AuthorizationConfiguration` object. The `--authorization-config` flag is mutually exclusive with `--authorization-modes` and `--authorization-webhook-*` flags. The `alpha` `StructuredAuthorizationConfiguration` feature flag must be enabled for `--authorization-config` to be specified. ([kubernetes/kubernetes#120154](https://github.com/kubernetes/kubernetes/pull/120154), [@palnabarun](https://github.com/palnabarun))
- `kube-proxy` now has a new nftables-based mode, available by running
  
      `kube-proxy --feature-gates NFTablesProxyMode=true --proxy-mode nftables`
  
  This is currently an alpha-level feature and while it probably will not
  eat your data, it may nibble at it a bit. (It passes e2e testing but has
  not yet seen real-world use.)
  
  At this point it should be functionally mostly identical to the iptables
  mode, except that it does not (and will not) support Service NodePorts on
  127.0.0.1. (Also note that there are currently no command-line arguments
  for the nftables-specific config; you will need to use a config file if
  you want to set the equivalent of any of the `--iptables-xxx` options.)
  
  As this code is still very new, it has not been heavily optimized yet;
  while it is expected to _eventually_ have better performance than the
  iptables backend, very little performance testing has been done so far. ([kubernetes/kubernetes#121046](https://github.com/kubernetes/kubernetes/pull/121046), [@danwinship](https://github.com/danwinship))
- `kube-proxy`: Added an option/flag for configuring the `nf_conntrack_tcp_be_liberal` sysctl (in the kernel's netfilter conntrack subsystem).  When enabled, `kube-proxy` will not install the `DROP` rule for invalid conntrack states, which currently breaks users of asymmetric routing. ([kubernetes/kubernetes#120354](https://github.com/kubernetes/kubernetes/pull/120354), [@aroradaman](https://github.com/aroradaman))
- Added support for projecting certificates.k8s.io/v1alpha1 ClusterTrustBundle objects into pods. ([kubernetes/kubernetes#113374](https://github.com/kubernetes/kubernetes/pull/113374), [@ahmedtd](https://github.com/ahmedtd)) [SIG API Machinery, Apps, Auth, Node, Storage and Testing]
- Adds `optionalOldSelf` to `x-kubernetes-validations` to support ratcheting CRD schema constraints ([kubernetes/kubernetes#121034](https://github.com/kubernetes/kubernetes/pull/121034), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery]
- Fix API comment for the Job Ready field in status ([kubernetes/kubernetes#121765](https://github.com/kubernetes/kubernetes/pull/121765), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]
- Fix API comments for the FailIndex Job pod failure policy action. ([kubernetes/kubernetes#121764](https://github.com/kubernetes/kubernetes/pull/121764), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]
- A new sleep action for the PreStop lifecycle hook is added, allowing containers to pause for a specified duration before termination. ([kubernetes/kubernetes#119026](https://github.com/kubernetes/kubernetes/pull/119026), [@AxeZhan](https://github.com/AxeZhan)) [SIG API Machinery, Apps, Node and Testing]
- Add ImageMaximumGCAge field to Kubelet configuration, which allows a user to set the maximum age an image is unused before it's garbage collected. ([kubernetes/kubernetes#121275](https://github.com/kubernetes/kubernetes/pull/121275), [@haircommander](https://github.com/haircommander)) [SIG API Machinery and Node]
- Add a new ServiceCIDR type that allows to dynamically configure the cluster range used to allocate Service ClusterIPs addresses ([kubernetes/kubernetes#116516](https://github.com/kubernetes/kubernetes/pull/116516), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Auth, CLI, Network and Testing]
- Add the DisableNodeKubeProxyVersion feature gate. If DisableNodeKubeProxyVersion is enabled, the kubeProxyVersion field is not set. ([kubernetes/kubernetes#120954](https://github.com/kubernetes/kubernetes/pull/120954), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG API Machinery, Apps and Node]
- Added Windows support for InPlace Pod Vertical Scaling feature. ([kubernetes/kubernetes#112599](https://github.com/kubernetes/kubernetes/pull/112599), [@fabi200123](https://github.com/fabi200123)) [SIG Autoscaling, Node, Scalability, Scheduling and Windows]
- Added `UserNamespacesPodSecurityStandards` feature gate to enable user namespace support for Pod Security Standards.
  Enabling this feature will modify all Pod Security Standard rules to allow setting: `spec[.*].securityContext.[runAsNonRoot,runAsUser]`.
  This feature gate should only be enabled if all nodes in the cluster support the user namespace feature and have it enabled.
  The feature gate will not graduate or be enabled by default in future Kubernetes releases. ([kubernetes/kubernetes#118760](https://github.com/kubernetes/kubernetes/pull/118760), [@saschagrunert](https://github.com/saschagrunert)) [SIG API Machinery, Auth, Node and Release]
- Added options for configuring nf_conntrack_udp_timeout, and nf_conntrack_udp_timeout_stream variables of netfilter conntrack subsystem. ([kubernetes/kubernetes#120808](https://github.com/kubernetes/kubernetes/pull/120808), [@aroradaman](https://github.com/aroradaman)) [SIG API Machinery and Network]
- Adds CEL expressions to v1alpha1 AuthenticationConfiguration. ([kubernetes/kubernetes#121078](https://github.com/kubernetes/kubernetes/pull/121078), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Adds support for CEL expressions to v1alpha1 AuthorizationConfiguration webhook matchConditions. ([kubernetes/kubernetes#121223](https://github.com/kubernetes/kubernetes/pull/121223), [@ritazh](https://github.com/ritazh)) [SIG API Machinery and Auth]
- CSINodeExpandSecret feature has been promoted to GA in this release and enabled by default. The CSI drivers can make use of the `secretRef` values passed in NodeExpansion request optionally sent by the CSI Client from this release onwards. ([kubernetes/kubernetes#121303](https://github.com/kubernetes/kubernetes/pull/121303), [@humblec](https://github.com/humblec)) [SIG API Machinery, Apps and Storage]
- Graduate Job BackoffLimitPerIndex feature to Beta ([kubernetes/kubernetes#121356](https://github.com/kubernetes/kubernetes/pull/121356), [@mimowo](https://github.com/mimowo)) [SIG Apps]
- Kube-apiserver: adds --authorization-config flag for reading a configuration file containing an apiserver.config.k8s.io/v1alpha1 AuthorizationConfiguration object. --authorization-config flag is mutually exclusive with --authorization-modes and --authorization-webhook-* flags. The alpha StructuredAuthorizationConfiguration feature flag must be enabled for --authorization-config to be specified. ([kubernetes/kubernetes#120154](https://github.com/kubernetes/kubernetes/pull/120154), [@palnabarun](https://github.com/palnabarun)) [SIG API Machinery, Auth and Testing]
- Kube-proxy now has a new nftables-based mode, available by running
  
      kube-proxy --feature-gates NFTablesProxyMode=true --proxy-mode nftables
  
  This is currently an alpha-level feature and while it probably will not
  eat your data, it may nibble at it a bit. (It passes e2e testing but has
  not yet seen real-world use.)
  
  At this point it should be functionally mostly identical to the iptables
  mode, except that it does not (and will not) support Service NodePorts on
  127.0.0.1. (Also note that there are currently no command-line arguments
  for the nftables-specific config; you will need to use a config file if
  you want to set the equivalent of any of the `--iptables-xxx` options.)
  
  As this code is still very new, it has not been heavily optimized yet;
  while it is expected to _eventually_ have better performance than the
  iptables backend, very little performance testing has been done so far. ([kubernetes/kubernetes#121046](https://github.com/kubernetes/kubernetes/pull/121046), [@danwinship](https://github.com/danwinship)) [SIG API Machinery and Network]
- Kube-proxy: Added an option/flag for configuring the `nf_conntrack_tcp_be_liberal` sysctl (in the kernel's netfilter conntrack subsystem).  When enabled, kube-proxy will not install the DROP rule for invalid conntrack states, which currently breaks users of asymmetric routing. ([kubernetes/kubernetes#120354](https://github.com/kubernetes/kubernetes/pull/120354), [@aroradaman](https://github.com/aroradaman)) [SIG API Machinery and Network]
- PersistentVolumeLastPhaseTransitionTime is now beta, enabled by default. ([kubernetes/kubernetes#120627](https://github.com/kubernetes/kubernetes/pull/120627), [@RomanBednar](https://github.com/RomanBednar)) [SIG Storage]
- Promote PodReadyToStartContainers condition to beta. ([kubernetes/kubernetes#119659](https://github.com/kubernetes/kubernetes/pull/119659), [@kannon92](https://github.com/kannon92)) [SIG Node and Testing]
- The flowcontrol.apiserver.k8s.io/v1beta3 FlowSchema and PriorityLevelConfiguration APIs has been promoted to flowcontrol.apiserver.k8s.io/v1, with the following changes:
  - PriorityLevelConfiguration: the `.spec.limited.nominalConcurrencyShares` field defaults to `30` only if the field is omitted (v1beta3 also defaulted an explicit `0` value to `30`). Specifying an explicit `0` value is not allowed in the `v1` version in v1.29 to ensure compatibility with 1.28 API servers. In v1.30, explicit `0` values will be allowed in this field in the `v1` API.
  The flowcontrol.apiserver.k8s.io/v1beta3 APIs are deprecated and will no longer be served in v1.32. All existing objects are available via the `v1` APIs. Transition clients and manifests to use the `v1` APIs before upgrading to v1.32. ([kubernetes/kubernetes#121089](https://github.com/kubernetes/kubernetes/pull/121089), [@tkashem](https://github.com/tkashem)) [SIG API Machinery and Testing]
- The kube-proxy command-line documentation was updated to clarify that
  `--bind-address` does not actually have anything to do with binding to an
  address, and you probably don't actually want to be using it. ([kubernetes/kubernetes#120274](https://github.com/kubernetes/kubernetes/pull/120274), [@danwinship](https://github.com/danwinship)) [SIG Network]
- The matchLabelKeys/mismatchLabelKeys feature is introduced to the hard/soft PodAffinity/PodAntiAffinity. ([kubernetes/kubernetes#116065](https://github.com/kubernetes/kubernetes/pull/116065), [@sanposhiho](https://github.com/sanposhiho)) [SIG API Machinery, Apps, Cloud Provider, Scheduling and Testing]
- ValidatingAdmissionPolicy Type Checking now supports CRDs and API extensions types. ([kubernetes/kubernetes#119109](https://github.com/kubernetes/kubernetes/pull/119109), [@jiahuif](https://github.com/jiahuif)) [SIG API Machinery, Apps, Auth and Testing]
- When updating a CRD, per-expression cost limit check is skipped for x-kubernetes-validations rules of versions that are not mutated. ([kubernetes/kubernetes#121460](https://github.com/kubernetes/kubernetes/pull/121460), [@jiahuif](https://github.com/jiahuif)) [SIG API Machinery]
- Added a new `ipMode` field to the `.status` of Services where `type` is set to `LoadBalancer`.
  The new field is behind the `LoadBalancerIPMode` feature gate. ([kubernetes/kubernetes#119937](https://github.com/kubernetes/kubernetes/pull/119937), [@RyanAoh](https://github.com/RyanAoh)) [SIG API Machinery, Apps, Cloud Provider, Network and Testing]
- Fixed a bug where CEL expressions in CRD validation rules would incorrectly compute a high estimated cost for functions that return strings, lists or maps.
  The incorrect cost was evident when the result of a function was used in subsequent operations. ([kubernetes/kubernetes#119800](https://github.com/kubernetes/kubernetes/pull/119800), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth and Cloud Provider]
- Go API: the ResourceRequirements struct needs to be replaced with VolumeResourceRequirements for use with volumes. ([kubernetes/kubernetes#118653](https://github.com/kubernetes/kubernetes/pull/118653), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Node, Scheduling, Storage and Testing]
- Kube-apiserver: adds --authentication-config flag for reading AuthenticationConfiguration files. --authentication-config flag is mutually exclusive with the existing --oidc-* flags. ([kubernetes/kubernetes#119142](https://github.com/kubernetes/kubernetes/pull/119142), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Kube-scheduler component config (KubeSchedulerConfiguration) kubescheduler.config.k8s.io/v1beta3 is removed in v1.29. Migrate kube-scheduler configuration files to kubescheduler.config.k8s.io/v1. ([kubernetes/kubernetes#119994](https://github.com/kubernetes/kubernetes/pull/119994), [@SataQiu](https://github.com/SataQiu)) [SIG Scheduling and Testing]
- Mark the onPodConditions field as optional in Job's pod failure policy. ([kubernetes/kubernetes#120204](https://github.com/kubernetes/kubernetes/pull/120204), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]
- Retry NodeStageVolume calls if CSI node driver is not running ([kubernetes/kubernetes#120330](https://github.com/kubernetes/kubernetes/pull/120330), [@rohitssingh](https://github.com/rohitssingh)) [SIG Apps, Storage and Testing]
- The kube-scheduler `selectorSpread` plugin has been removed, please use the `podTopologySpread` plugin instead. ([kubernetes/kubernetes#117720](https://github.com/kubernetes/kubernetes/pull/117720), [@kerthcet](https://github.com/kerthcet)) [SIG Scheduling]


# v28.1.0

Kubernetes API Version: v1.28.2

### API Change
- Fixed a bug where CEL expressions in CRD validation rules would incorrectly compute a high estimated cost for functions that return strings, lists or maps.
  The incorrect cost was evident when the result of a function was used in subsequent operations. ([kubernetes/kubernetes#119807](https://github.com/kubernetes/kubernetes/pull/119807), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth and Cloud Provider]
- Mark Job onPodConditions as optional in pod failure policy ([kubernetes/kubernetes#120208](https://github.com/kubernetes/kubernetes/pull/120208), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]


# v28.1.0b1

Kubernetes API Version: v1.28.1


# v28.1.0a1

Kubernetes API Version: v1.28.1

### API Change
- A CDIDevice field is included in the Device Plugin's `ContainerAllocateResponse`. This field maps to the CDIDevice field in the CRI protocol. ([kubernetes/kubernetes#118254](https://github.com/kubernetes/kubernetes/pull/118254), [@elezar](https://github.com/elezar)) [SIG Node and Testing]
- ACTION_REQUIRED
  When an Indexed Job has a number of completions higher than 10^5 and parallelism higher than 10^4, and a big number of Indexes fail, Kubernetes might not be able to track the termination of the Job. Kubernetes now emits a warning, at Job creation, when the Job manifest exceeds both of these limits. ([kubernetes/kubernetes#118420](https://github.com/kubernetes/kubernetes/pull/118420), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps]
- Added `ServedVersions` field to `StorageVersion` API. ([kubernetes/kubernetes#118386](https://github.com/kubernetes/kubernetes/pull/118386), [@Richabanker](https://github.com/Richabanker))
- Added `IP mode` field to loadbalancer status ingress. ([kubernetes/kubernetes#118895](https://github.com/kubernetes/kubernetes/pull/118895), [@RyanAoh](https://github.com/RyanAoh))
- Added `podReplacementPolicy` and terminating field to job api. ([kubernetes/kubernetes#119301](https://github.com/kubernetes/kubernetes/pull/119301), [@kannon92](https://github.com/kannon92))
- Added a new `namespaceParamRef` field to `admissionregistration.k8s.io/v1alpha1.ValidatingAdmissionPolicy`. ([kubernetes/kubernetes#119215](https://github.com/kubernetes/kubernetes/pull/119215), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery and Testing]
- Added a warning that TLS 1.3 ciphers are not configurable. ([kubernetes/kubernetes#115399](https://github.com/kubernetes/kubernetes/pull/115399), [@3u13r](https://github.com/3u13r)) [SIG API Machinery and Node]
- Added error handling for seccomp localhost configurations that do not properly set a `localhostProfile`. ([kubernetes/kubernetes#117020](https://github.com/kubernetes/kubernetes/pull/117020), [@cji](https://github.com/cji))
- Added fields `reason` and `fieldPath` into CRD validation rules to allow users to specify reason and field path when validation failed. ([kubernetes/kubernetes#118041](https://github.com/kubernetes/kubernetes/pull/118041), [@cici37](https://github.com/cici37)) [SIG API Machinery]
- Added namespace access support to the CEL expressions of ValidatingAdmissionPolicy via a `namespaceObject`
  variable with expressions. ([kubernetes/kubernetes#118267](https://github.com/kubernetes/kubernetes/pull/118267), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]
- Added new `CRDValidationRatcheting` alpha feature. During a PATCH or UPDATE Validation Ratcheting discards errors thrown by unchanged portions of the resource from most OpenAPI schema validations. ([kubernetes/kubernetes#118990](https://github.com/kubernetes/kubernetes/pull/118990), [@alexzielenski](https://github.com/alexzielenski))
- Added new annotation `batch.kubernetes.io/cronjob-scheduled-timestamp` to Job objects scheduled from CronJobs. ([kubernetes/kubernetes#118137](https://github.com/kubernetes/kubernetes/pull/118137), [@helayoty](https://github.com/helayoty))
- Added new config option `delayCacheUntilActive` to `KubeSchedulerConfiguration` that can provide a tradeoff between memory efficiency and scheduling speed when their leadership is updated in `kube-scheduler` ([kubernetes/kubernetes#115754](https://github.com/kubernetes/kubernetes/pull/115754), [@linxiulei](https://github.com/linxiulei)) [SIG API Machinery and Scheduling]
- Changed how KMS v2 encryption at rest can generate data encryption keys.
  When you enable the `KMSv2KDF` feature gate (off by default), KMS v2 uses a key derivation function to generate single use data encryption keys from a secret seed combined with some random data. This eliminates the need for a counter based nonce while avoiding nonce collision concerns associated with AES-GCM's 12 byte nonce. ([kubernetes/kubernetes#118828](https://github.com/kubernetes/kubernetes/pull/118828), [@enj](https://github.com/enj))
- Exposed `rest.DefaultServerUrlFor` function. ([kubernetes/kubernetes#118055](https://github.com/kubernetes/kubernetes/pull/118055), [@timofurrer](https://github.com/timofurrer))
- Extended the Job API for alpha version of `BackoffLimitPerIndex`. ([kubernetes/kubernetes#119294](https://github.com/kubernetes/kubernetes/pull/119294), [@mimowo](https://github.com/mimowo))
- Graduated `AdmissionWebhookMatchCondition` feature to beta. ([kubernetes/kubernetes#119380](https://github.com/kubernetes/kubernetes/pull/119380), [@a-hilaly](https://github.com/a-hilaly))
- If using cgroups v2, then the cgroup aware OOM killer will be enabled for container cgroups via  `memory.oom.group` .  This causes processes within the cgroup to be treated as a unit and killed simultaneously in the event of an OOM kill on any process in the cgroup. ([kubernetes/kubernetes#117793](https://github.com/kubernetes/kubernetes/pull/117793), [@tzneal](https://github.com/tzneal)) [SIG Apps, Node and Testing]
- In the API Priority and Fairness feature, priority levels that are exempt from limitation can now be given a nominal and a lendable concurrency and their dispatching borrows from the concurrency limits of the other priority levels.  For details see https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/1040-priority-and-fairness#dispatching . ([kubernetes/kubernetes#118782](https://github.com/kubernetes/kubernetes/pull/118782), [@MikeSpreitzer](https://github.com/MikeSpreitzer)) [SIG API Machinery]
- Indexed Job pods now have the pod completion index set as a pod label. ([kubernetes/kubernetes#118883](https://github.com/kubernetes/kubernetes/pull/118883), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG Apps]
- Kube-proxy: added `--logging-format` flag to support structured logging. ([kubernetes/kubernetes#117800](https://github.com/kubernetes/kubernetes/pull/117800), [@cyclinder](https://github.com/cyclinder))
- NodeVolumeLimits implement the `PreFilter` extension point for skipping the Filter phase if the Pod doesn't use volumes with limits. ([kubernetes/kubernetes#115398](https://github.com/kubernetes/kubernetes/pull/115398), [@tangwz](https://github.com/tangwz)) [SIG Scheduling]
- PersistentVolumes have a new `LastPhaseTransitionTime` field which holds a timestamp of when the volume last transitioned its phase. ([kubernetes/kubernetes#116469](https://github.com/kubernetes/kubernetes/pull/116469), [@RomanBednar](https://github.com/RomanBednar))
- Pods which set `hostNetwork: true` and declare ports, get the `hostPort` field set automatically. Previously this would happen in the PodTemplate of a Deployment, DaemonSet or other workload API.  Now `hostPort` will only be set when an actual Pod is being created.  If this presents a problem, setting the feature gate "DefaultHostNetworkHostPortsInPodTemplates" to true will revert this behavior.  Please file a kubernetes bug if you need to do this. ([kubernetes/kubernetes#117696](https://github.com/kubernetes/kubernetes/pull/117696), [@thockin](https://github.com/thockin)) [SIG Apps]
- Promoted API groups `ValidatingAdmissionPolicy` and `ValidatingAdmissionPolicyBinding` to `v1beta1`. ([kubernetes/kubernetes#118644](https://github.com/kubernetes/kubernetes/pull/118644), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery, Apps and Testing]
- Promoted the feature gate `ValidtaingAdmissionPolicy` to beta, and it is turned off by default. ([kubernetes/kubernetes#119409](https://github.com/kubernetes/kubernetes/pull/119409), [@alexzielenski](https://github.com/alexzielenski))
- Registered_metric_total, disabled_metric_total, hidden_metric_total & kubernetes_feature_enabled are promoted to `BETA` stability. ([kubernetes/kubernetes#119264](https://github.com/kubernetes/kubernetes/pull/119264), [@logicalhan](https://github.com/logicalhan)) [SIG API Machinery, Architecture, Cluster Lifecycle and Instrumentation]
- Removed `resizeStatus` enum from `pvc.Status` and replaced with `AllocatedResourceStatus`. ([kubernetes/kubernetes#116335](https://github.com/kubernetes/kubernetes/pull/116335), [@gnufied](https://github.com/gnufied)) [SIG API Machinery, Apps, Auth, Node, Storage and Testing]
- Removed `WindowsHostProcessContainers` feature-gate. ([kubernetes/kubernetes#117570](https://github.com/kubernetes/kubernetes/pull/117570), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Auth, Node and Windows]
- Revised the comment about the feature-gate level for `PodFailurePolicy` from alpha to beta. ([kubernetes/kubernetes#117802](https://github.com/kubernetes/kubernetes/pull/117802), [@kerthcet](https://github.com/kerthcet)) [SIG API Machinery and Apps]
- StatefulSet pods now have the pod index set as a pod label `statefulset.kubernetes.io/pod-index`. ([kubernetes/kubernetes#119232](https://github.com/kubernetes/kubernetes/pull/119232), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG Apps]
- Support for proxying a request to a peer kube-apiserver if the local apiserver is not able to serve it due to version skew or in the case the requested api is disabled on the local apiserver ([kubernetes/kubernetes#117740](https://github.com/kubernetes/kubernetes/pull/117740), [@Richabanker](https://github.com/Richabanker)) [SIG API Machinery, Apps, Auth, Cloud Provider, Network, Node and Testing]
- Supported `BackoffLimitPerIndex` in Jobs. ([kubernetes/kubernetes#118009](https://github.com/kubernetes/kubernetes/pull/118009), [@mimowo](https://github.com/mimowo))
- The `IPTablesOwnershipCleanup` feature (KEP-3178) is now GA; kubelet no longer
  creates the `KUBE-MARK-DROP` chain (which has been unused for several releases)
  or the `KUBE-MARK-MASQ` chain (which is now only created by kube-proxy). ([kubernetes/kubernetes#119374](https://github.com/kubernetes/kubernetes/pull/119374), [@danwinship](https://github.com/danwinship))
- The `SelfSubjectReview` API is promoted to `authentication.k8s.io/v1` and the `kubectl auth whoami` command is GA. ([kubernetes/kubernetes#117713](https://github.com/kubernetes/kubernetes/pull/117713), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Architecture, Auth, CLI and Testing]
- The names of ResourceClaims generated from ResourceClaimTemplate are now generated. The base name is still `<pod>-<claim name>`, but a random suffix will avoid name collisions. ([kubernetes/kubernetes#117351](https://github.com/kubernetes/kubernetes/pull/117351), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Node, Scheduling and Testing]
- The new feature gate "SidecarContainers" is now available. This feature introduces sidecar containers, a new type of init container that starts before other containers but remains running for the full duration of the pod's lifecycle and will not block pod termination. ([kubernetes/kubernetes#116429](https://github.com/kubernetes/kubernetes/pull/116429), [@gjkim42](https://github.com/gjkim42)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Updated the comment about the feature-gate level for `PodFailurePolicy` from alpha to beta ([kubernetes/kubernetes#118278](https://github.com/kubernetes/kubernetes/pull/118278), [@mimowo](https://github.com/mimowo))
- `client-go`: Improved memory use of reflector caches when watching large numbers
  of objects which do not change frequently. ([kubernetes/kubernetes#113362](https://github.com/kubernetes/kubernetes/pull/113362), [@sxllwx](https://github.com/sxllwx))
- `component-base/logs` is now stricter about not applying configurations multiple
  times and will return an error when that is attempted. Can be overridden by binaries
  which need to do that. ([kubernetes/kubernetes#117108](https://github.com/kubernetes/kubernetes/pull/117108), [@pohly](https://github.com/pohly))
- `kube-controller-manager`: The `LegacyServiceAccountTokenCleanUp` feature gate
  is now available as alpha (off by default). When enabled, the `legacy-service-account-token-cleaner`
  controller loop removes service account token secrets that have not been used
  in the time specified by `--legacy-service-account-token-clean-up-period` (defaulting
  to one year), **and are** referenced from the `.secrets` list of a ServiceAccount
  object, **and are not** referenced from pods. ([kubernetes/kubernetes#115554](https://github.com/kubernetes/kubernetes/pull/115554), [@yt2985](https://github.com/yt2985))
- `kube-scheduler` component config (KubeSchedulerConfiguration) `kubescheduler.config.k8s.io/v1beta2`
  is removed in `v1.28`. Migrate `kube-scheduler` configuration files to `kubescheduler.config.k8s.io/v1`. ([kubernetes/kubernetes#117649](https://github.com/kubernetes/kubernetes/pull/117649), [@SataQiu](https://github.com/SataQiu))
- Aggregated discovery now returns `responseKind: {}` for resources which are missing group/version/kind information, to ensure compatibility with v0.26.0-v0.26.3 clients. ([kubernetes/kubernetes#119835](https://github.com/kubernetes/kubernetes/pull/119835), [@liggitt](https://github.com/liggitt)) [SIG API Machinery and Testing]
- Fix CustomResourceDefinition status.storedVersions validation error messages. ([kubernetes/kubernetes#119653](https://github.com/kubernetes/kubernetes/pull/119653), [@sttts](https://github.com/sttts)) [SIG API Machinery]
- Kube-proxy in Kubernetes >= 1.28 up until v1.28.0-beta.0 ignored the `-v` command line flag when combined with `--config`. ([kubernetes/kubernetes#119867](https://github.com/kubernetes/kubernetes/pull/119867), [@pohly](https://github.com/pohly)) [SIG Network]
- PersistentVolumes have a new LastPhaseTransitionTime field which holds a timestamp of when the volume last transitioned its phase. ([kubernetes/kubernetes#116469](https://github.com/kubernetes/kubernetes/pull/116469), [@RomanBednar](https://github.com/RomanBednar)) [SIG API Machinery, Apps, Auth, Node, Release, Storage and Testing]
- Promoted API groups `ValidatingAdmissionPolicy` and `ValidatingAdmissionPolicyBinding` to `v1beta1`. ([kubernetes/kubernetes#118644](https://github.com/kubernetes/kubernetes/pull/118644), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery, Apps and Testing]
- Promoted the feature gate `ValidtaingAdmissionPolicy` to beta and it is turned off by default. ([kubernetes/kubernetes#119409](https://github.com/kubernetes/kubernetes/pull/119409), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery, Apps, Auth, Instrumentation, Node, Release, Storage and Testing]
- Changed how KMS v2 encryption at rest can generate data encryption keys. When you enable the `KMSv2KDF` feature gate (off by default), KMS v2 uses a key derivation function to generate single use data encryption keys from a secret seed combined with some random data.  This eliminates the need for a counter based nonce while avoiding nonce collision concerns associated with AES-GCM's 12 byte nonce. ([kubernetes/kubernetes#118828](https://github.com/kubernetes/kubernetes/pull/118828), [@enj](https://github.com/enj)) [SIG API Machinery, Auth and Testing]
- A CDIDevice field is includes in the Device Plugin's `ContainerAllocateResponse`. This field maps to the CDIDevice field in the CRI protocol. ([kubernetes/kubernetes#118254](https://github.com/kubernetes/kubernetes/pull/118254), [@elezar](https://github.com/elezar)) [SIG Node and Testing]
- Add new annotation `batch.kubernetes.io/cronjob-scheduled-timestamp` to Job objects scheduled from CronJobs. ([kubernetes/kubernetes#118137](https://github.com/kubernetes/kubernetes/pull/118137), [@helayoty](https://github.com/helayoty)) [SIG Apps]
- Add podReplacementPolicy and terminating field to job api ([kubernetes/kubernetes#119301](https://github.com/kubernetes/kubernetes/pull/119301), [@kannon92](https://github.com/kannon92)) [SIG API Machinery and Apps]
- Added fields `reason` and `fieldPath` into CRD validation rules to allow users to specify reason and field path when validation failed. ([kubernetes/kubernetes#118041](https://github.com/kubernetes/kubernetes/pull/118041), [@cici37](https://github.com/cici37)) [SIG API Machinery]
- Added namespace access support to the CEL expressions of ValidatingAdmissionPolicy via a `namespaceObject`
  variable with expressions. ([kubernetes/kubernetes#118267](https://github.com/kubernetes/kubernetes/pull/118267), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]
- Adds new CRDValidationRatcheting alpha feature. During a PATCH or UPDATE Validation Ratcheting discards errors thrown by unchanged portions of the resource from most OpenAPI schema validations. ([kubernetes/kubernetes#118990](https://github.com/kubernetes/kubernetes/pull/118990), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node and Storage]
- Adds new namespaceParamRef to admissionregistration.k8s.io/v1alpha1.ValidatingAdmissionPolicy ([kubernetes/kubernetes#119215](https://github.com/kubernetes/kubernetes/pull/119215), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery and Testing]
- Extend the Job API for alpha version of BackoffLimitPerIndex ([kubernetes/kubernetes#119294](https://github.com/kubernetes/kubernetes/pull/119294), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]
- Graduate `AdmissionWebhookMatchCondition` feature to beta ([kubernetes/kubernetes#119380](https://github.com/kubernetes/kubernetes/pull/119380), [@a-hilaly](https://github.com/a-hilaly)) [SIG API Machinery]
- In the API Priority and Fairness feature, priority levels that are exempt from limitation can now be given a nominal and a lendable concurrency and their dispatching borrows from the concurrency limits of the other priority levels.  For details see https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/1040-priority-and-fairness#dispatching . ([kubernetes/kubernetes#118782](https://github.com/kubernetes/kubernetes/pull/118782), [@MikeSpreitzer](https://github.com/MikeSpreitzer)) [SIG API Machinery]
- Indexed Job pods now have the pod completion index set as a pod label. ([kubernetes/kubernetes#118883](https://github.com/kubernetes/kubernetes/pull/118883), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG Apps]
- Kube-proxy: add '--logging-format' flag to support structured logging ([kubernetes/kubernetes#117800](https://github.com/kubernetes/kubernetes/pull/117800), [@cyclinder](https://github.com/cyclinder)) [SIG API Machinery, Architecture, Instrumentation and Network]
- Registered_metric_total, disabled_metric_total, hidden_metric_total & kubernetes_feature_enabled are promoted to `BETA` stability. ([kubernetes/kubernetes#119264](https://github.com/kubernetes/kubernetes/pull/119264), [@logicalhan](https://github.com/logicalhan)) [SIG API Machinery, Architecture, Cluster Lifecycle and Instrumentation]
- Removed `resizeStatus` enum from `pvc.Status` and replaced with `AllocatedResourceStatus` ([kubernetes/kubernetes#116335](https://github.com/kubernetes/kubernetes/pull/116335), [@gnufied](https://github.com/gnufied)) [SIG API Machinery, Apps, Auth, Node, Storage and Testing]
- StatefulSet pods now have the pod index set as a pod label `statefulset.kubernetes.io/pod-index`. ([kubernetes/kubernetes#119232](https://github.com/kubernetes/kubernetes/pull/119232), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG Apps]
- Support BackoffLimitPerIndex in Jobs ([kubernetes/kubernetes#118009](https://github.com/kubernetes/kubernetes/pull/118009), [@mimowo](https://github.com/mimowo)) [SIG API Machinery, Apps and Testing]
- Support for proxying a request to a peer kube-apiserver if the local apiserver is not able to serve it due to version skew or in the case the requested api is disabled on the local apiserver ([kubernetes/kubernetes#117740](https://github.com/kubernetes/kubernetes/pull/117740), [@Richabanker](https://github.com/Richabanker)) [SIG API Machinery, Apps, Auth, Cloud Provider, Network, Node and Testing]
- The IPTablesOwnershipCleanup feature (KEP-3178) is now GA; kubelet no longer
  creates the KUBE-MARK-DROP chain (which has been unused for several releases)
  or the KUBE-MARK-MASQ chain (which is now only created by kube-proxy). ([kubernetes/kubernetes#119374](https://github.com/kubernetes/kubernetes/pull/119374), [@danwinship](https://github.com/danwinship)) [SIG API Machinery, Network and Node]
- The names of ResourceClaims generated from ResourceClaimTemplate are now generated. The base name is still `<pod>-<claim name>`, but a random suffix will avoid name collisions. ([kubernetes/kubernetes#117351](https://github.com/kubernetes/kubernetes/pull/117351), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Node, Scheduling and Testing]
- The new feature gate "SidecarContainers" is now available. This feature introduces sidecar containers, a new type of init container that starts before other containers but remains running for the full duration of the pod's lifecycle and will not block pod termination. ([kubernetes/kubernetes#116429](https://github.com/kubernetes/kubernetes/pull/116429), [@gjkim42](https://github.com/gjkim42)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Add ServedVersions field to StorageVersion API ([kubernetes/kubernetes#118386](https://github.com/kubernetes/kubernetes/pull/118386), [@Richabanker](https://github.com/Richabanker)) [SIG API Machinery and Testing]
- Component-base/logs is now more strict about not applying configurations multiple times and will return an error when that is attempted. Can be overridden by binaries which need to do that. ([kubernetes/kubernetes#117108](https://github.com/kubernetes/kubernetes/pull/117108), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Cloud Provider, Instrumentation, Scheduling and Testing]
- ACTION_REQUIRED
  When an Indexed Job has a number of completions higher than 10^5 and parallelism higher than 10^4, and a big number of Indexes fail, Kubernetes might not be able to track the termination of the Job. Kubernetes now emits a warning, at Job creation, when the Job manifest exceeds both of these limits. ([kubernetes/kubernetes#118420](https://github.com/kubernetes/kubernetes/pull/118420), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps]
- Expose rest.DefaultServerUrlFor function ([kubernetes/kubernetes#118055](https://github.com/kubernetes/kubernetes/pull/118055), [@timofurrer](https://github.com/timofurrer)) [SIG API Machinery]
- If using cgroups v2, then the cgroup aware OOM killer will be enabled for container cgroups via  `memory.oom.group` .  This causes processes within the cgroup to be treated as a unit and killed simultaneously in the event of an OOM kill on any process in the cgroup. ([kubernetes/kubernetes#117793](https://github.com/kubernetes/kubernetes/pull/117793), [@tzneal](https://github.com/tzneal)) [SIG Apps, Node and Testing]
- Update the comment about the feature-gate level for PodFailurePolicy from alpha to beta ([kubernetes/kubernetes#118278](https://github.com/kubernetes/kubernetes/pull/118278), [@mimowo](https://github.com/mimowo)) [SIG Apps]
- Added a warning that TLS 1.3 ciphers are not configurable. ([kubernetes/kubernetes#115399](https://github.com/kubernetes/kubernetes/pull/115399), [@3u13r](https://github.com/3u13r)) [SIG API Machinery and Node]
- Added error handling for seccomp localhost configurations that do not properly set a localhostProfile ([kubernetes/kubernetes#117020](https://github.com/kubernetes/kubernetes/pull/117020), [@cji](https://github.com/cji)) [SIG API Machinery and Node]
- Added new config option `delayCacheUntilActive` to `KubeSchedulerConfiguration` that can provide a tradeoff between memory efficiency and scheduling speed when their leadership is updated in `kube-scheduler` ([kubernetes/kubernetes#115754](https://github.com/kubernetes/kubernetes/pull/115754), [@linxiulei](https://github.com/linxiulei)) [SIG API Machinery and Scheduling]
- Client-go: Improved memory use of reflector caches when watching large numbers of objects which do not change frequently ([kubernetes/kubernetes#113362](https://github.com/kubernetes/kubernetes/pull/113362), [@sxllwx](https://github.com/sxllwx)) [SIG API Machinery]
- Kube-controller-manager: The `LegacyServiceAccountTokenCleanUp` feature gate is now available as alpha (off by default). When enabled, the `legacy-service-account-token-cleaner` controller loop removes service account token secrets that have not been used in the time specified by `--legacy-service-account-token-clean-up-period` (defaulting to one year), **and are** referenced from the `.secrets` list of a ServiceAccount object, **and are not** referenced from pods. ([kubernetes/kubernetes#115554](https://github.com/kubernetes/kubernetes/pull/115554), [@yt2985](https://github.com/yt2985)) [SIG API Machinery, Apps, Auth, Release and Testing]
- Kube-scheduler component config (KubeSchedulerConfiguration) kubescheduler.config.k8s.io/v1beta2 is removed in v1.28. Migrate kube-scheduler configuration files to kubescheduler.config.k8s.io/v1. ([kubernetes/kubernetes#117649](https://github.com/kubernetes/kubernetes/pull/117649), [@SataQiu](https://github.com/SataQiu)) [SIG API Machinery, Scheduling and Testing]
- NodeVolumeLimits implement the PreFilter extension point for skipping the Filter phase if the Pod doesn't use volumes with limits. ([kubernetes/kubernetes#115398](https://github.com/kubernetes/kubernetes/pull/115398), [@tangwz](https://github.com/tangwz)) [SIG Scheduling]
- Pods which set `hostNetwork: true` and declare ports get the `hostPort` field set automatically.  Previously this would happen in the PodTemplate of a Deployment, DaemonSet or other workload API.  Now `hostPort` will only be set when an actual Pod is being created.  If this presents a problem, setting the feature gate "DefaultHostNetworkHostPortsInPodTemplates" to true will revert this behavior.  Please file a kubernetes bug if you need to do this. ([kubernetes/kubernetes#117696](https://github.com/kubernetes/kubernetes/pull/117696), [@thockin](https://github.com/thockin)) [SIG Apps]
- Removing WindowsHostProcessContainers feature-gate ([kubernetes/kubernetes#117570](https://github.com/kubernetes/kubernetes/pull/117570), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Auth, Node and Windows]
- Revised the comment about the feature-gate level for PodFailurePolicy from alpha to beta ([kubernetes/kubernetes#117802](https://github.com/kubernetes/kubernetes/pull/117802), [@kerthcet](https://github.com/kerthcet)) [SIG API Machinery and Apps]
- The `SelfSubjectReview` API is promoted to `authentication.k8s.io/v1` and the `kubectl auth whoami` command is GA. ([kubernetes/kubernetes#117713](https://github.com/kubernetes/kubernetes/pull/117713), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Architecture, Auth, CLI and Testing]

# v27.2.0

Kubernetes API Version: v1.27.3

### Documentation
- Fix request_timeout example and doc. Arg name should be _request_timeout. Single value type should be int or long. (#2071, @hemslo)

# v27.2.0b1

Kubernetes API Version: v1.27.2

# v27.2.0a1

Kubernetes API Version: v1.27.2

### API Change
- Added error handling for seccomp localhost configurations that do not properly set a localhostProfile ([kubernetes/kubernetes#117020](https://github.com/kubernetes/kubernetes/pull/117020), [@cji](https://github.com/cji)) [SIG API Machinery and Node]
- Fixed an issue where kubelet does not set case-insensitive headers for http probes. (#117182, @dddddai) ([kubernetes/kubernetes#117324](https://github.com/kubernetes/kubernetes/pull/117324), [@dddddai](https://github.com/dddddai)) [SIG API Machinery, Apps and Node]
- Revised the comment about the feature-gate level for PodFailurePolicy from alpha to beta ([kubernetes/kubernetes#117815](https://github.com/kubernetes/kubernetes/pull/117815), [@kerthcet](https://github.com/kerthcet)) [SIG Apps]
- A fix in the `resource.k8s.io/v1alpha1/ResourceClaim` API avoids harmless (?) ".status.reservedFor: element 0: associative list without keys has an element that's a map type" errors in the apiserver. Validation now rejects the incorrect reuse of the same UID in different entries. ([kubernetes/kubernetes#115354](https://github.com/kubernetes/kubernetes/pull/115354), [@pohly](https://github.com/pohly))
- A terminating pod on a node that is not caused by preemption no longer prevents `kube-scheduler` from preempting pods on that node
  - Rename `PreemptionByKubeScheduler` to `PreemptionByScheduler` ([kubernetes/kubernetes#114623](https://github.com/kubernetes/kubernetes/pull/114623), [@Huang-Wei](https://github.com/Huang-Wei))
- API: resource.k8s.io/v1alpha1.PodScheduling was renamed to resource.k8s.io/v1alpha2.PodSchedulingContext. ([kubernetes/kubernetes#116556](https://github.com/kubernetes/kubernetes/pull/116556), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Scheduling and Testing]
- Added CEL runtime cost calculation into ValidatingAdmissionPolicy, matching the evaluation cost
  restrictions that already apply to CustomResourceDefinition.
  If rule evaluation uses more compute than the limit, the API server aborts the evaluation and the
  admission check that was being performed is aborted; the `failurePolicy` for the ValidatingAdmissionPolicy
  determines the outcome. ([kubernetes/kubernetes#115747](https://github.com/kubernetes/kubernetes/pull/115747), [@cici37](https://github.com/cici37))
- Added `auditAnnotations` to `ValidatingAdmissionPolicy`, enabling CEL to be used to add audit annotations to request audit events.
  Added `validationActions` to `ValidatingAdmissionPolicyBinding`, enabling validation failures to be handled by any combination of the warn, audit and deny enforcement actions. ([kubernetes/kubernetes#115973](https://github.com/kubernetes/kubernetes/pull/115973), [@jpbetz](https://github.com/jpbetz))
- Added `messageExpression` field to `ValidationRule`. ([kubernetes/kubernetes#115969](https://github.com/kubernetes/kubernetes/pull/115969), [@DangerOnTheRanger](https://github.com/DangerOnTheRanger))
- Added `messageExpression` to `ValidatingAdmissionPolicy`, to set custom failure message via CEL expression. ([kubernetes/kubernetes#116397](https://github.com/kubernetes/kubernetes/pull/116397), [@jiahuif](https://github.com/jiahuif)) [SIG API Machinery]
- Added a new IPAddress object kind
  - Added a new ClusterIP allocator. The new allocator removes previous Service CIDR block size limitations for IPv4, and limits IPv6 size to a /64 ([kubernetes/kubernetes#115075](https://github.com/kubernetes/kubernetes/pull/115075), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Auth, CLI, Cluster Lifecycle, Network and Testing]
- Added a new alpha API: ClusterTrustBundle (`certificates.k8s.io/v1alpha1`).
  A ClusterTrustBundle may be used to distribute [X.509](https://www.itu.int/rec/T-REC-X.509) trust anchors to workloads within the cluster. ([kubernetes/kubernetes#113218](https://github.com/kubernetes/kubernetes/pull/113218), [@ahmedtd](https://github.com/ahmedtd)) [SIG API Machinery, Auth and Testing]
- Added authorization check support to the CEL expressions of ValidatingAdmissionPolicy via a `authorizer`
  variable with expressions. The new variable provides a builder that allows expressions such `authorizer.group('').resource('pods').check('create').allowed()`. ([kubernetes/kubernetes#116054](https://github.com/kubernetes/kubernetes/pull/116054), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Testing]
- Added matchConditions field to ValidatingAdmissionPolicy and enabled support for CEL based custom match criteria. ([kubernetes/kubernetes#116350](https://github.com/kubernetes/kubernetes/pull/116350), [@maxsmythe](https://github.com/maxsmythe))
- Added new option to the `InterPodAffinity` scheduler plugin to ignore existing
  pods` preferred inter-pod affinities if the incoming pod has no preferred inter-pod
  affinities. This option can be used as an optimization for higher scheduling throughput
  (at the cost of an occasional pod being scheduled non-optimally/violating existing
  pods preferred inter-pod affinities). To enable this scheduler option, set the
  `InterPodAffinity` scheduler plugin arg `ignorePreferredTermsOfExistingPods: true` ([kubernetes/kubernetes#114393](https://github.com/kubernetes/kubernetes/pull/114393), [@danielvegamyhre](https://github.com/danielvegamyhre))
- Added the `MatchConditions` field to `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` for the v1beta and v1 apis. 
  
  The `AdmissionWebhookMatchConditions` featuregate is now in Alpha ([kubernetes/kubernetes#116261](https://github.com/kubernetes/kubernetes/pull/116261), [@ivelichkovich](https://github.com/ivelichkovich)) [SIG API Machinery and Testing]
- Added validation to ensure that if `service.kubernetes.io/topology-aware-hints` and `service.kubernetes.io/topology-mode` annotations are both set, they are set to the same value.Also Added deprecation warning if `service.kubernetes.io/topology-aware-hints` annotation is used. ([kubernetes/kubernetes#116612](https://github.com/kubernetes/kubernetes/pull/116612), [@robscott](https://github.com/robscott))
- Added warnings about workload resources (Pods, ReplicaSets, Deployments, Jobs, CronJobs, or ReplicationControllers) whose names are not valid DNS labels. ([kubernetes/kubernetes#114412](https://github.com/kubernetes/kubernetes/pull/114412), [@thockin](https://github.com/thockin))
- Adds feature gate `NodeLogQuery` which provides cluster administrators with a streaming view of logs using kubectl without them having to implement a client side reader or logging into the node. ([kubernetes/kubernetes#96120](https://github.com/kubernetes/kubernetes/pull/96120), [@LorbusChris](https://github.com/LorbusChris))
- Api: validation of a `PodSpec` now rejects invalid `ResourceClaim` and `ResourceClaimTemplate` names. For a pod, the name generated for the `ResourceClaim` when using a template also must be valid. ([kubernetes/kubernetes#116576](https://github.com/kubernetes/kubernetes/pull/116576), [@pohly](https://github.com/pohly))
- Bump default API QPS limits for Kubelet. ([kubernetes/kubernetes#116121](https://github.com/kubernetes/kubernetes/pull/116121), [@wojtek-t](https://github.com/wojtek-t))
- Enabled the `StatefulSetStartOrdinal` feature gate in beta ([kubernetes/kubernetes#115260](https://github.com/kubernetes/kubernetes/pull/115260), [@pwschuurman](https://github.com/pwschuurman))
- Enabled usage of `kube-proxy`, `kube-scheduler` and `kubelet` HTTP APIs for changing the logging
   verbosity at runtime for JSON output. ([kubernetes/kubernetes#114609](https://github.com/kubernetes/kubernetes/pull/114609), [@pohly](https://github.com/pohly))
- Encryption of API Server at rest configuration now allows the use of wildcards in the list of resources.  For example, *.* can be used to encrypt all resources, including all current and future custom resources. ([kubernetes/kubernetes#115149](https://github.com/kubernetes/kubernetes/pull/115149), [@nilekhc](https://github.com/nilekhc))
- Extended the kubelet's PodResources API to include resources allocated in `ResourceClaims` via `DynamicResourceAllocation`. Additionally, added a new `Get()` method to query a specific pod for its resources. ([kubernetes/kubernetes#115847](https://github.com/kubernetes/kubernetes/pull/115847), [@moshe010](https://github.com/moshe010)) [SIG Node]
- Forbid to set matchLabelKeys when labelSelector is not set in topologySpreadConstraints ([kubernetes/kubernetes#116535](https://github.com/kubernetes/kubernetes/pull/116535), [@denkensk](https://github.com/denkensk))
- GCE does not support LoadBalancer Services with ports with different protocols (TCP and UDP) ([kubernetes/kubernetes#115966](https://github.com/kubernetes/kubernetes/pull/115966), [@aojea](https://github.com/aojea)) [SIG Apps and Cloud Provider]
- GRPC probes are now a GA feature. `GRPCContainerProbe` feature gate was locked to default value and will be removed in v1.29. If you were setting this feature gate explicitly, please remove it now. ([kubernetes/kubernetes#116233](https://github.com/kubernetes/kubernetes/pull/116233), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev))
- Graduated `Kubelet Topology Manager` to GA. ([kubernetes/kubernetes#116093](https://github.com/kubernetes/kubernetes/pull/116093), [@swatisehgal](https://github.com/swatisehgal))
- Graduated `KubeletTracing` to beta, which means that the feature gate is now enabled by default. ([kubernetes/kubernetes#115750](https://github.com/kubernetes/kubernetes/pull/115750), [@saschagrunert](https://github.com/saschagrunert))
- Graduated seccomp profile defaulting to GA.
  
  Set the kubelet `--seccomp-default` flag or `seccompDefault` kubelet configuration field to `true` to make pods on that node default to using the `RuntimeDefault` seccomp profile.
  
  Enabling seccomp for your workload can have a negative performance impact depending on the kernel and container runtime version in use.
  
  Guidance for identifying and mitigating those issues is outlined in the Kubernetes [seccomp tutorial](https://k8s.io/docs/tutorials/security/seccomp). ([kubernetes/kubernetes#115719](https://github.com/kubernetes/kubernetes/pull/115719), [@saschagrunert](https://github.com/saschagrunert)) [SIG API Machinery, Node, Storage and Testing]
- Graduated the container resource metrics feature on `HPA` to beta. ([kubernetes/kubernetes#116046](https://github.com/kubernetes/kubernetes/pull/116046), [@sanposhiho](https://github.com/sanposhiho))
- Implemented API streaming for the `watch-cache`
  
  When `sendInitialEvents` `ListOption` is set together with `watch=true`, it begins the watch stream with synthetic init events followed by a synthetic "Bookmark" after which the server continues streaming events. ([kubernetes/kubernetes#110960](https://github.com/kubernetes/kubernetes/pull/110960), [@p0lyn0mial](https://github.com/p0lyn0mial))
- Introduced API for streaming.
  
  Added `SendInitialEvents` field to the `ListOptions`. When the new option is set together with `watch=true`, it begins the watch stream with synthetic init events followed by a synthetic "Bookmark" after which the server continues streaming events. ([kubernetes/kubernetes#115402](https://github.com/kubernetes/kubernetes/pull/115402), [@p0lyn0mial](https://github.com/p0lyn0mial))
- Introduced a breaking change to the `resource.k8s.io` API in its `AllocationResult` struct. This change allows a kubelet plugin for the `DynamicResourceAllocation` feature to service allocations from multiple resource driver controllers. ([kubernetes/kubernetes#116332](https://github.com/kubernetes/kubernetes/pull/116332), [@klueska](https://github.com/klueska))
- Introduces new alpha functionality to the reflector, allowing user to enable API streaming.
  
  To activate this feature, users can set the `ENABLE_CLIENT_GO_WATCH_LIST_ALPHA` environmental variable.
  It is important to note that the server must support streaming for this feature to function properly.
  If streaming is not supported by the server, the reflector will revert to the previous method
  of obtaining data through LIST/WATCH semantics. ([kubernetes/kubernetes#110772](https://github.com/kubernetes/kubernetes/pull/110772), [@p0lyn0mial](https://github.com/p0lyn0mial)) [SIG API Machinery]
- K8s.io/client-go/tools/record.EventBroadcaster: after Shutdown() is called, the broadcaster now gives up immediately after a failure to write an event to a sink. Previously it tried multiple times for 12 seconds in a goroutine. ([kubernetes/kubernetes#115514](https://github.com/kubernetes/kubernetes/pull/115514), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- K8s.io/component-base/logs: usage of the pflag values in a normal Go flag set led to panics when printing the help message ([kubernetes/kubernetes#114680](https://github.com/kubernetes/kubernetes/pull/114680), [@pohly](https://github.com/pohly)) [SIG Instrumentation]
- Kubeadm: explicitly set `priority` for static pods with `priorityClassName: system-node-critical` ([kubernetes/kubernetes#114338](https://github.com/kubernetes/kubernetes/pull/114338), [@champtar](https://github.com/champtar)) [SIG Cluster Lifecycle]
- Kubelet: a "maxParallelImagePulls" field can now be specified in the kubelet configuration file to control how many image pulls the kubelet can perform in parallel. ([kubernetes/kubernetes#115220](https://github.com/kubernetes/kubernetes/pull/115220), [@ruiwen-zhao](https://github.com/ruiwen-zhao)) [SIG API Machinery, Node and Scalability]
- Kubelet: changed `MemoryThrottlingFactor` default value to `0.9` and formulas to calculate `memory.high` ([kubernetes/kubernetes#115371](https://github.com/kubernetes/kubernetes/pull/115371), [@pacoxu](https://github.com/pacoxu))
- Kubernetes components that perform leader election now only support using `Leases` for this. ([kubernetes/kubernetes#114055](https://github.com/kubernetes/kubernetes/pull/114055), [@aimuz](https://github.com/aimuz))
- Migrated the `DaemonSet` controller (within `kube-controller-manager`) to use [contextual logging](https://k8s.io/docs/concepts/cluster-administration/system-logs/#contextual-logging) ([kubernetes/kubernetes#113622](https://github.com/kubernetes/kubernetes/pull/113622), [@249043822](https://github.com/249043822))
- New `service.kubernetes.io/topology-mode` annotation has been introduced as a replacement for the `service.kubernetes.io/topology-aware-hints` annotation.
  - `service.kubernetes.io/topology-aware-hints` annotation has been deprecated.
  - kube-proxy now accepts any value that is not "disabled" for these annotations, enabling custom implementation-specific and/or future built-in heuristics to be used. ([kubernetes/kubernetes#116522](https://github.com/kubernetes/kubernetes/pull/116522), [@robscott](https://github.com/robscott)) [SIG Apps, Network and Testing]
- Pods owned by a Job now uses the labels `batch.kubernetes.io/job-name` and `batch.kubernetes.io/controller-uid`.
  The legacy labels `job-name` and `controller-uid` are still added for compatibility. ([kubernetes/kubernetes#114930](https://github.com/kubernetes/kubernetes/pull/114930), [@kannon92](https://github.com/kannon92))
- Promoted `CronJobTimeZone` feature to GA ([kubernetes/kubernetes#115904](https://github.com/kubernetes/kubernetes/pull/115904), [@soltysh](https://github.com/soltysh))
- Promoted `SelfSubjectReview` to Beta ([kubernetes/kubernetes#116274](https://github.com/kubernetes/kubernetes/pull/116274), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Auth, CLI and Testing]
- Relaxed API validation to allow pod node selector to be mutable for gated pods (additions only, no deletions or mutations). ([kubernetes/kubernetes#116161](https://github.com/kubernetes/kubernetes/pull/116161), [@danielvegamyhre](https://github.com/danielvegamyhre))
- Remove `kubernetes.io/grpc` standard appProtocol ([kubernetes/kubernetes#116866](https://github.com/kubernetes/kubernetes/pull/116866), [@LiorLieberman](https://github.com/LiorLieberman)) [SIG API Machinery and Apps]
- Remove deprecated `--enable-taint-manager` and `--pod-eviction-timeout` CLI ([kubernetes/kubernetes#115840](https://github.com/kubernetes/kubernetes/pull/115840), [@atosatto](https://github.com/atosatto))
- Removed support for the `v1alpha1` kubeletplugin API of `DynamicResourceManagement`. All plugins must be updated to `v1alpha2` in order to function properly. ([kubernetes/kubernetes#116558](https://github.com/kubernetes/kubernetes/pull/116558), [@klueska](https://github.com/klueska))
- The API server now re-uses data encryption keys while the kms v2 plugin key ID is stable.  Data encryption keys are still randomly generated on server start but an atomic counter is used to prevent nonce collisions. ([kubernetes/kubernetes#116155](https://github.com/kubernetes/kubernetes/pull/116155), [@enj](https://github.com/enj))
- The PodDisruptionBudget `spec.unhealthyPodEvictionPolicy` field has graduated to beta and is enabled by default. On servers with the feature enabled, this field may be set to `AlwaysAllow` to always allow unhealthy pods covered by the PodDisruptionBudget to be evicted. ([kubernetes/kubernetes#115363](https://github.com/kubernetes/kubernetes/pull/115363), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps, Auth and Node]
- The `DownwardAPIHugePages` kubelet feature graduated to stable / GA. ([kubernetes/kubernetes#115721](https://github.com/kubernetes/kubernetes/pull/115721), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps and Node]
- The following feature gates for volume expansion GA features have now been removed and must no longer be referenced in `--feature-gates` flags: `ExpandCSIVolumes`, `ExpandInUsePersistentVolumes`, `ExpandPersistentVolumes` ([kubernetes/kubernetes#113942](https://github.com/kubernetes/kubernetes/pull/113942), [@mengjiao-liu](https://github.com/mengjiao-liu))
- The list-type of the alpha `resourceClaims` field introduced to `Pods` in `1.26.0` was modified from `set` to `map`, resolving an incompatibility with use of this schema in `CustomResourceDefinitions` and with server-side apply. ([kubernetes/kubernetes#114585](https://github.com/kubernetes/kubernetes/pull/114585), [@JoelSpeed](https://github.com/JoelSpeed))
- Updated API reference for Requests, specifying they must not exceed limits ([kubernetes/kubernetes#115434](https://github.com/kubernetes/kubernetes/pull/115434), [@ehashman](https://github.com/ehashman))
- Updated `KMSv2` to beta ([kubernetes/kubernetes#115123](https://github.com/kubernetes/kubernetes/pull/115123), [@aramase](https://github.com/aramase))
- Updated: Redefine AppProtocol field description and add new standard values ([kubernetes/kubernetes#115433](https://github.com/kubernetes/kubernetes/pull/115433), [@LiorLieberman](https://github.com/LiorLieberman)) [SIG API Machinery, Apps and Network]
- `/metrics/slis` is now available for control plane components allowing you to scrape health check metrics. ([kubernetes/kubernetes#114997](https://github.com/kubernetes/kubernetes/pull/114997), [@Richabanker](https://github.com/Richabanker))
- `APIServerTracing` feature gate is now enabled by default. Tracing in the API
  Server is still disabled by default, and requires a config file to enable. ([kubernetes/kubernetes#116144](https://github.com/kubernetes/kubernetes/pull/116144), [@dashpole](https://github.com/dashpole))
- `NodeResourceFit` and `NodeResourcesBalancedAllocation` implement the `PreScore`
  extension point for a more performant calculation. ([kubernetes/kubernetes#115655](https://github.com/kubernetes/kubernetes/pull/115655), [@tangwz](https://github.com/tangwz))
- `PodSchedulingReadiness` is graduated to beta. ([kubernetes/kubernetes#115815](https://github.com/kubernetes/kubernetes/pull/115815), [@Huang-Wei](https://github.com/Huang-Wei))
- `PodSpec.Container.Resources` became mutable for CPU and memory resource types.
  - `PodSpec.Container.ResizePolicy` (new object) gives users control over how their containers are resized.
  - `PodStatus.Resize` status describes the state of a requested Pod resize.
  - `PodStatus.ResourcesAllocated` describes node resources allocated to Pod.
  - `PodStatus.Resources` describes node resources applied to running containers by CRI.
  - `UpdateContainerResources` CRI API now supports both Linux and Windows. ([kubernetes/kubernetes#102884](https://github.com/kubernetes/kubernetes/pull/102884), [@vinaykul](https://github.com/vinaykul))
- `SELinuxMountReadWriteOncePod` graduated to Beta. ([kubernetes/kubernetes#116425](https://github.com/kubernetes/kubernetes/pull/116425), [@jsafrane](https://github.com/jsafrane))
- `StatefulSetAutoDeletePVC` feature gate promoted to beta. ([kubernetes/kubernetes#116501](https://github.com/kubernetes/kubernetes/pull/116501), [@mattcary](https://github.com/mattcary))
- `StatefulSet` names must be DNS labels, rather than subdomains. Any `StatefulSet`
  which took advantage of subdomain validation (by having dots in the name) can't
  possibly have worked, because we eventually set `pod.spec.hostname` from the `StatefulSetName`,
  and that is validated as a DNS label. ([kubernetes/kubernetes#114172](https://github.com/kubernetes/kubernetes/pull/114172), [@thockin](https://github.com/thockin))
- `ValidatingAdmissionPolicy` now provides a status field that contains results of type checking the validation expression.
  The type checking is fully informational, and the behavior of the policy is unchanged. ([kubernetes/kubernetes#115668](https://github.com/kubernetes/kubernetes/pull/115668), [@jiahuif](https://github.com/jiahuif))
- `cacheSize` field in `EncryptionConfiguration` is not supported for KMSv2 provider ([kubernetes/kubernetes#113121](https://github.com/kubernetes/kubernetes/pull/113121), [@aramase](https://github.com/aramase))
- `k8s.io/component-base/logs` now also supports adding command line flags to a `flag.FlagSet`. ([kubernetes/kubernetes#114731](https://github.com/kubernetes/kubernetes/pull/114731), [@pohly](https://github.com/pohly))
- `kubelet`: migrated `--container-runtime-endpoint` and `--image-service-endpoint`
  to kubelet config ([kubernetes/kubernetes#112136](https://github.com/kubernetes/kubernetes/pull/112136), [@pacoxu](https://github.com/pacoxu))
- `resource.k8s.io/v1alpha1` was replaced with `resource.k8s.io/v1alpha2`. Before
  upgrading a cluster, all objects in resource.k8s.io/v1alpha1 (ResourceClaim, ResourceClaimTemplate,
  ResourceClass, PodScheduling) must be deleted. The changes are internal, so
  YAML files which create pods and resource claims don't need changes except for
  the newer `apiVersion`. ([kubernetes/kubernetes#116299](https://github.com/kubernetes/kubernetes/pull/116299), [@pohly](https://github.com/pohly))
- `volumes`: `resource.claims` is now cleared for PVC specs during create or update of a pod spec with inline PVC template or of a PVC because it has no effect. ([kubernetes/kubernetes#115928](https://github.com/kubernetes/kubernetes/pull/115928), [@pohly](https://github.com/pohly))
- Added a new alpha API: ClusterTrustBundle (`certificates.k8s.io/v1alpha1`).
  A ClusterTrustBundle may be used to distribute [X.509](https://www.itu.int/rec/T-REC-X.509) trust anchors to workloads within the cluster. ([kubernetes/kubernetes#113218](https://github.com/kubernetes/kubernetes/pull/113218), [@ahmedtd](https://github.com/ahmedtd)) [SIG API Machinery, Auth and Testing]
- Remove `kubernetes.io/grpc` standard appProtocol ([kubernetes/kubernetes#116866](https://github.com/kubernetes/kubernetes/pull/116866), [@LiorLieberman](https://github.com/LiorLieberman)) [SIG API Machinery and Apps]
- API: resource.k8s.io/v1alpha1.PodScheduling was renamed to resource.k8s.io/v1alpha2.PodSchedulingContext. ([kubernetes/kubernetes#116556](https://github.com/kubernetes/kubernetes/pull/116556), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Scheduling and Testing]
- APIServerTracing feature gate is now enabled by default. Tracing in the API Server is still disabled by default, and requires a config file to enable. ([kubernetes/kubernetes#116144](https://github.com/kubernetes/kubernetes/pull/116144), [@dashpole](https://github.com/dashpole)) [SIG API Machinery and Testing]
- Added CEL runtime cost calculation into ValidatingAdmissionPolicy, matching the evaluation cost
  restrictions that already apply to CustomResourceDefinition.
  If rule evaluation uses more compute than the limit, the API server aborts the evaluation and the
  admission check that was being performed is aborted; the `failurePolicy` for the ValidatingAdmissionPolicy
  determines the outcome. ([kubernetes/kubernetes#115747](https://github.com/kubernetes/kubernetes/pull/115747), [@cici37](https://github.com/cici37)) [SIG API Machinery]
- Added `messageExpression` to `ValidatingAdmissionPolicy`, to set custom failure message via CEL expression. ([kubernetes/kubernetes#116397](https://github.com/kubernetes/kubernetes/pull/116397), [@jiahuif](https://github.com/jiahuif)) [SIG API Machinery]
- Added a new IPAddress object kind
  - Added a new ClusterIP allocator. The new allocator removes previous Service CIDR block size limitations for IPv4, and limits IPv6 size to a /64 ([kubernetes/kubernetes#115075](https://github.com/kubernetes/kubernetes/pull/115075), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Auth, CLI, Cluster Lifecycle, Network and Testing]
- Added a new alpha API: ClusterTrustBundle (`certificates.k8s.io/v1alpha1`).
  A ClusterTrustBundle may be used to distribute [X.509](https://www.itu.int/rec/T-REC-X.509) trust anchors to workloads within the cluster. ([kubernetes/kubernetes#113218](https://github.com/kubernetes/kubernetes/pull/113218), [@ahmedtd](https://github.com/ahmedtd)) [SIG API Machinery, Auth and Testing]
- Added authorization check support to the CEL expressions of ValidatingAdmissionPolicy via a `authorizer`
  variable with expressions. The new variable provides a builder that allows expressions such `authorizer.group('').resource('pods').check('create').allowed()`. ([kubernetes/kubernetes#116054](https://github.com/kubernetes/kubernetes/pull/116054), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Testing]
- Added matchConditions field to ValidatingAdmissionPolicy, enabled support for CEL based custom match criteria. ([kubernetes/kubernetes#116350](https://github.com/kubernetes/kubernetes/pull/116350), [@maxsmythe](https://github.com/maxsmythe)) [SIG API Machinery and Testing]
- Added messageExpression field to ValidationRule. (#115969, @DangerOnTheRanger) ([kubernetes/kubernetes#115969](https://github.com/kubernetes/kubernetes/pull/115969), [@DangerOnTheRanger](https://github.com/DangerOnTheRanger)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Instrumentation, Node and Testing]
- Added the `MatchConditions` field to `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` for the v1beta and v1 apis. 
  
  The `AdmissionWebhookMatchConditions` featuregate is now in Alpha ([kubernetes/kubernetes#116261](https://github.com/kubernetes/kubernetes/pull/116261), [@ivelichkovich](https://github.com/ivelichkovich)) [SIG API Machinery and Testing]
- Added validation to ensure that if `service.kubernetes.io/topology-aware-hints` and `service.kubernetes.io/topology-mode` annotations are both set, they are set to the same value.
  - Added deprecation warning if `service.kubernetes.io/topology-aware-hints` annotation is used. ([kubernetes/kubernetes#116612](https://github.com/kubernetes/kubernetes/pull/116612), [@robscott](https://github.com/robscott)) [SIG Apps, Network and Testing]
- Adds auditAnnotations to ValidatingAdmissionPolicy, enabling CEL to be used to add audit annotations to request audit events.
  Adds validationActions to ValidatingAdmissionPolicyBinding, enabling validation failures to be handled by any combination of the warn, audit and deny enforcement actions. ([kubernetes/kubernetes#115973](https://github.com/kubernetes/kubernetes/pull/115973), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Testing]
- Adds feature gate `NodeLogQuery` which provides cluster administrators with a streaming view of logs using kubectl without them having to implement a client side reader or logging into the node. ([kubernetes/kubernetes#96120](https://github.com/kubernetes/kubernetes/pull/96120), [@LorbusChris](https://github.com/LorbusChris)) [SIG API Machinery, Apps, CLI, Node, Testing and Windows]
- Api: validation of a PodSpec now rejects invalid ResourceClaim and ResourceClaimTemplate names. For a pod, the name generated for the ResourceClaim when using a template also must be valid. ([kubernetes/kubernetes#116576](https://github.com/kubernetes/kubernetes/pull/116576), [@pohly](https://github.com/pohly)) [SIG Apps]
- Bump default API QPS limits for Kubelet. ([kubernetes/kubernetes#116121](https://github.com/kubernetes/kubernetes/pull/116121), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Node]
- Enable the "StatefulSetStartOrdinal" feature gate in beta ([kubernetes/kubernetes#115260](https://github.com/kubernetes/kubernetes/pull/115260), [@pwschuurman](https://github.com/pwschuurman)) [SIG API Machinery and Apps]
- Extended the kubelet's PodResources API to include resources allocated in `ResourceClaims` via `DynamicResourceAllocation`. Additionally, added a new `Get()` method to query a specific pod for its resources. ([kubernetes/kubernetes#115847](https://github.com/kubernetes/kubernetes/pull/115847), [@moshe010](https://github.com/moshe010)) [SIG Node]
- Forbid to set matchLabelKeys when labelSelector isn’t set in topologySpreadConstraints ([kubernetes/kubernetes#116535](https://github.com/kubernetes/kubernetes/pull/116535), [@denkensk](https://github.com/denkensk)) [SIG API Machinery, Apps and Scheduling]
- GCE does not support LoadBalancer Services with ports with different protocols (TCP and UDP) ([kubernetes/kubernetes#115966](https://github.com/kubernetes/kubernetes/pull/115966), [@aojea](https://github.com/aojea)) [SIG Apps and Cloud Provider]
- GRPC probes are now a GA feature. GRPCContainerProbe feature gate was locked to default value and will be removed in v1.29. If you were setting this feature gate explicitly, please remove it now. ([kubernetes/kubernetes#116233](https://github.com/kubernetes/kubernetes/pull/116233), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG API Machinery, Apps and Node]
- Graduate Kubelet Topology Manager to GA. ([kubernetes/kubernetes#116093](https://github.com/kubernetes/kubernetes/pull/116093), [@swatisehgal](https://github.com/swatisehgal)) [SIG API Machinery, Node and Testing]
- Graduate `KubeletTracing` to beta, which means that the feature gate is now enabled by default. ([kubernetes/kubernetes#115750](https://github.com/kubernetes/kubernetes/pull/115750), [@saschagrunert](https://github.com/saschagrunert)) [SIG Instrumentation and Node]
- Graduate the container resource metrics feature on HPA to beta. ([kubernetes/kubernetes#116046](https://github.com/kubernetes/kubernetes/pull/116046), [@sanposhiho](https://github.com/sanposhiho)) [SIG Autoscaling]
- Introduced a breaking change to the `resource.k8s.io` API in its `AllocationResult` struct. This change allows a kubelet plugin for the `DynamicResourceAllocation` feature to service allocations from multiple resource driver controllers. ([kubernetes/kubernetes#116332](https://github.com/kubernetes/kubernetes/pull/116332), [@klueska](https://github.com/klueska)) [SIG API Machinery, Apps, CLI, Node, Scheduling and Testing]
- Introduces new alpha functionality to the reflector, allowing user to enable API streaming.
  
  To activate this feature, users can set the `ENABLE_CLIENT_GO_WATCH_LIST_ALPHA` environmental variable.
  It is important to note that the server must support streaming for this feature to function properly.
  If streaming is not supported by the server, the reflector will revert to the previous method
  of obtaining data through LIST/WATCH semantics. ([kubernetes/kubernetes#110772](https://github.com/kubernetes/kubernetes/pull/110772), [@p0lyn0mial](https://github.com/p0lyn0mial)) [SIG API Machinery]
- Kubelet: change MemoryThrottlingFactor default value to 0.9 and formulas to calculate memory.high ([kubernetes/kubernetes#115371](https://github.com/kubernetes/kubernetes/pull/115371), [@pacoxu](https://github.com/pacoxu)) [SIG API Machinery, Apps and Node]
- Migrated the DaemonSet controller (within `kube-controller-manager) to use [contextual logging](https://k8s.io/docs/concepts/cluster-administration/system-logs/#contextual-logging) ([kubernetes/kubernetes#113622](https://github.com/kubernetes/kubernetes/pull/113622), [@249043822](https://github.com/249043822)) [SIG API Machinery, Apps, Instrumentation and Testing]
- New `service.kubernetes.io/topology-mode` annotation has been introduced as a replacement for the `service.kubernetes.io/topology-aware-hints` annotation.
  - `service.kubernetes.io/topology-aware-hints` annotation has been deprecated.
  - kube-proxy now accepts any value that is not "disabled" for these annotations, enabling custom implementation-specific and/or future built-in heuristics to be used. ([kubernetes/kubernetes#116522](https://github.com/kubernetes/kubernetes/pull/116522), [@robscott](https://github.com/robscott)) [SIG Apps, Network and Testing]
- NodeResourceFit and NodeResourcesBalancedAllocation implement the PreScore extension point for a more performant calculation. ([kubernetes/kubernetes#115655](https://github.com/kubernetes/kubernetes/pull/115655), [@tangwz](https://github.com/tangwz)) [SIG Scheduling]
- Pods owned by a Job will now use the labels `batch.kubernetes.io/job-name` and `batch.kubernetes.io/controller-uid`.
  The legacy labels `job-name` and `controller-uid` are still added for compatibility. ([kubernetes/kubernetes#114930](https://github.com/kubernetes/kubernetes/pull/114930), [@kannon92](https://github.com/kannon92)) [SIG Apps]
- Promote CronJobTimeZone feature to GA ([kubernetes/kubernetes#115904](https://github.com/kubernetes/kubernetes/pull/115904), [@soltysh](https://github.com/soltysh)) [SIG API Machinery and Apps]
- Promoted `SelfSubjectReview` to Beta ([kubernetes/kubernetes#116274](https://github.com/kubernetes/kubernetes/pull/116274), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Auth, CLI and Testing]
- Relax API validation to allow pod node selector to be mutable for gated pods (additions only, no deletions or mutations). ([kubernetes/kubernetes#116161](https://github.com/kubernetes/kubernetes/pull/116161), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG Apps, Scheduling and Testing]
- Remove deprecated `--enable-taint-manager` and `--pod-eviction-timeout` CLI flags ([kubernetes/kubernetes#115840](https://github.com/kubernetes/kubernetes/pull/115840), [@atosatto](https://github.com/atosatto)) [SIG API Machinery, Apps, Node and Testing]
- Resource.k8s.io/v1alpha1 was replaced with resource.k8s.io/v1alpha2. Before upgrading a cluster, all objects in resource.k8s.io/v1alpha1 (ResourceClaim, ResourceClaimTemplate, ResourceClass, PodScheduling) must be deleted. The changes will be internal, so YAML files which create pods and resource claims don't need changes except for the newer `apiVersion`. ([kubernetes/kubernetes#116299](https://github.com/kubernetes/kubernetes/pull/116299), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, CLI, Node, Scheduling and Testing]
- SELinuxMountReadWriteOncePod graduated to Beta. ([kubernetes/kubernetes#116425](https://github.com/kubernetes/kubernetes/pull/116425), [@jsafrane](https://github.com/jsafrane)) [SIG Storage and Testing]
- StatefulSetAutoDeletePVC feature gate promoted to beta. ([kubernetes/kubernetes#116501](https://github.com/kubernetes/kubernetes/pull/116501), [@mattcary](https://github.com/mattcary)) [SIG Apps, Auth and Testing]
- The API server now re-uses data encryption keys while the kms v2 plugin's key ID is stable.  Data encryption keys are still randomly generated on server start but an atomic counter is used to prevent nonce collisions. ([kubernetes/kubernetes#116155](https://github.com/kubernetes/kubernetes/pull/116155), [@enj](https://github.com/enj)) [SIG API Machinery, Auth and Testing]
- The API server's encryption at rest configuration now allows the use of wildcards in the list of resources.  For example, '*.*' can be used to encrypt all resources, including all current and future custom resources. ([kubernetes/kubernetes#115149](https://github.com/kubernetes/kubernetes/pull/115149), [@nilekhc](https://github.com/nilekhc)) [SIG API Machinery, Auth and Testing]
- Update KMSv2 to beta ([kubernetes/kubernetes#115123](https://github.com/kubernetes/kubernetes/pull/115123), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- Updated: Redefine AppProtocol field description and add new standard values ([kubernetes/kubernetes#115433](https://github.com/kubernetes/kubernetes/pull/115433), [@LiorLieberman](https://github.com/LiorLieberman)) [SIG API Machinery, Apps and Network]
- ValidatingAdmissionPolicy now provides a status field that contains results of type checking the validation expression.
  The type checking is fully informational, and the behavior of the policy is unchanged. ([kubernetes/kubernetes#115668](https://github.com/kubernetes/kubernetes/pull/115668), [@jiahuif](https://github.com/jiahuif)) [SIG API Machinery, Auth, Cloud Provider and Testing]
- We have removed support for the v1alpha1 kubeletplugin API of DynamicResourceManagement. All plugins must update to v1alpha2 in order to function properly going forward. ([kubernetes/kubernetes#116558](https://github.com/kubernetes/kubernetes/pull/116558), [@klueska](https://github.com/klueska)) [SIG API Machinery, Apps, CLI, Node, Scheduling and Testing]
- Graduated seccomp profile defaulting to GA.
  
  Set the kubelet `--seccomp-default` flag or `seccompDefault` kubelet configuration field to `true` to make pods on that node default to using the `RuntimeDefault` seccomp profile.
  
  Enabling seccomp for your workload can have a negative performance impact depending on the kernel and container runtime version in use.
  
  Guidance for identifying and mitigating those issues is outlined in the Kubernetes [seccomp tutorial](https://k8s.io/docs/tutorials/security/seccomp). ([kubernetes/kubernetes#115719](https://github.com/kubernetes/kubernetes/pull/115719), [@saschagrunert](https://github.com/saschagrunert)) [SIG API Machinery, Node, Storage and Testing]
- Implements API for streaming for the watch-cache
  
  When sendInitialEvents ListOption is set together with watch=true, it begins the watch stream with synthetic init events followed by a synthetic "Bookmark" after which the server continues streaming events. ([kubernetes/kubernetes#110960](https://github.com/kubernetes/kubernetes/pull/110960), [@p0lyn0mial](https://github.com/p0lyn0mial)) [SIG API Machinery]
- Introduce API for streaming.
  
  Add SendInitialEvents field to the ListOptions. When the new option is set together with watch=true, it begins the watch stream with synthetic init events followed by a synthetic "Bookmark" after which the server continues streaming events. ([kubernetes/kubernetes#115402](https://github.com/kubernetes/kubernetes/pull/115402), [@p0lyn0mial](https://github.com/p0lyn0mial)) [SIG API Machinery]
- Kubelet: a "maxParallelImagePulls" field can now be specified in the kubelet configuration file to control how many image pulls the kubelet can perform in parallel. ([kubernetes/kubernetes#115220](https://github.com/kubernetes/kubernetes/pull/115220), [@ruiwen-zhao](https://github.com/ruiwen-zhao)) [SIG API Machinery, Node and Scalability]
- PodSchedulingReadiness is graduated to beta. ([kubernetes/kubernetes#115815](https://github.com/kubernetes/kubernetes/pull/115815), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG API Machinery, Apps, Scheduling and Testing]
- In-place resize feature for Kubernetes Pods
  - Changed the Pod API so that the `resources` defined for containers are mutable for `cpu` and `memory` resource types.
  - Added `resizePolicy` for containers in a pod to allow users control over how their containers are resized.
  - Added `allocatedResources` field to container status in pod status that describes the node resources allocated to a pod.
  - Added `resources` field to container status that reports actual resources applied to running containers.
  - Added `resize` field to pod status that describes the state of a requested pod resize.
  For details, see KEPs below. ([kubernetes/kubernetes#102884](https://github.com/kubernetes/kubernetes/pull/102884), [@vinaykul](https://github.com/vinaykul)) [SIG API Machinery, Apps, Instrumentation, Node, Scheduling and Testing]
- The PodDisruptionBudget `spec.unhealthyPodEvictionPolicy` field has graduated to beta and is enabled by default. On servers with the feature enabled, this field may be set to `AlwaysAllow` to always allow unhealthy pods covered by the PodDisruptionBudget to be evicted. ([kubernetes/kubernetes#115363](https://github.com/kubernetes/kubernetes/pull/115363), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps, Auth and Node]
- The `DownwardAPIHugePages` kubelet feature graduated to stable / GA. ([kubernetes/kubernetes#115721](https://github.com/kubernetes/kubernetes/pull/115721), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps and Node]
- Volumes: `resource.claims` gets cleared for PVC specs during create or update of a pod spec with inline PVC template or of a PVC because it has no effect. ([kubernetes/kubernetes#115928](https://github.com/kubernetes/kubernetes/pull/115928), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps and Storage]
- A fix in the resource.k8s.io/v1alpha1/ResourceClaim API avoids harmless (?) ".status.reservedFor: element 0: associative list without keys has an element that's a map type" errors in the apiserver. Validation now rejects the incorrect reuse of the same UID in different entries. ([kubernetes/kubernetes#115354](https://github.com/kubernetes/kubernetes/pull/115354), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- CacheSize field in EncryptionConfiguration is not supported for KMSv2 provider ([kubernetes/kubernetes#113121](https://github.com/kubernetes/kubernetes/pull/113121), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth and Testing]
- K8s.io/client-go/tools/record.EventBroadcaster: after Shutdown() is called, the broadcaster now gives up immediately after a failure to write an event to a sink. Previously it tried multiple times for 12 seconds in a goroutine. ([kubernetes/kubernetes#115514](https://github.com/kubernetes/kubernetes/pull/115514), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- K8s.io/component-base/logs now also supports adding command line flags to a flag.FlagSet. ([kubernetes/kubernetes#114731](https://github.com/kubernetes/kubernetes/pull/114731), [@pohly](https://github.com/pohly)) [SIG Architecture]
- Update API reference for Requests, specifying they must not exceed limits ([kubernetes/kubernetes#115434](https://github.com/kubernetes/kubernetes/pull/115434), [@ehashman](https://github.com/ehashman)) [SIG Architecture, Docs and Node]
- `/metrics/slis` is made available for control plane components allowing you to scrape health check metrics. ([kubernetes/kubernetes#114997](https://github.com/kubernetes/kubernetes/pull/114997), [@Richabanker](https://github.com/Richabanker)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scheduling, Storage and Testing]
- A terminating pod on a node that is not caused by preemption won't prevent kube-scheduler from preempting pods on that node
  - Rename 'PreemptionByKubeScheduler' to 'PreemptionByScheduler' ([kubernetes/kubernetes#114623](https://github.com/kubernetes/kubernetes/pull/114623), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- Added new option to the InterPodAffinity scheduler plugin to ignore existing pods` preferred inter-pod affinities if the incoming pod has no preferred inter-pod affinities. This option can be used as an optimization for higher scheduling throughput (at the cost of an occasional pod being scheduled non-optimally/violating existing pods' preferred inter-pod affinities). To enable this scheduler option, set the InterPodAffinity scheduler plugin arg "ignorePreferredTermsOfExistingPods: true". ([kubernetes/kubernetes#114393](https://github.com/kubernetes/kubernetes/pull/114393), [@danielvegamyhre](https://github.com/danielvegamyhre)) [SIG API Machinery and Scheduling]
- Added warnings about workload resources (Pods, ReplicaSets, Deployments, Jobs, CronJobs, or ReplicationControllers) whose names are not valid DNS labels. ([kubernetes/kubernetes#114412](https://github.com/kubernetes/kubernetes/pull/114412), [@thockin](https://github.com/thockin)) [SIG API Machinery and Apps]
- K8s.io/component-base/logs: usage of the pflag values in a normal Go flag set led to panics when printing the help message ([kubernetes/kubernetes#114680](https://github.com/kubernetes/kubernetes/pull/114680), [@pohly](https://github.com/pohly)) [SIG Instrumentation]
- Kube-proxy, kube-scheduler and kubelet have HTTP APIs for changing the logging verbosity at runtime. This now also works for JSON output. ([kubernetes/kubernetes#114609](https://github.com/kubernetes/kubernetes/pull/114609), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Cloud Provider, Instrumentation and Testing]
- Kubeadm: explicitly set `priority` for static pods with `priorityClassName: system-node-critical` ([kubernetes/kubernetes#114338](https://github.com/kubernetes/kubernetes/pull/114338), [@champtar](https://github.com/champtar)) [SIG Cluster Lifecycle]
- Kubelet: migrate "--container-runtime-endpoint" and "--image-service-endpoint" to kubelet config ([kubernetes/kubernetes#112136](https://github.com/kubernetes/kubernetes/pull/112136), [@pacoxu](https://github.com/pacoxu)) [SIG API Machinery, Node and Scalability]
- Kubernetes components that perform leader election now only support using Leases for this. ([kubernetes/kubernetes#114055](https://github.com/kubernetes/kubernetes/pull/114055), [@aimuz](https://github.com/aimuz)) [SIG API Machinery, Cloud Provider and Scheduling]
- StatefulSet names must be DNS labels, rather than subdomains.  Any StatefulSet which took advantage of subdomain validation (by having dots in the name) can't possibly have worked, because we eventually set `pod.spec.hostname` from the StatefulSetName, and that is validated as a DNS label. ([kubernetes/kubernetes#114172](https://github.com/kubernetes/kubernetes/pull/114172), [@thockin](https://github.com/thockin)) [SIG Apps]
- The following feature gates for volume expansion GA features have been removed and must no longer be referenced in `--feature-gates` flags: ExpandCSIVolumes, ExpandInUsePersistentVolumes, ExpandPersistentVolumes ([kubernetes/kubernetes#113942](https://github.com/kubernetes/kubernetes/pull/113942), [@mengjiao-liu](https://github.com/mengjiao-liu)) [SIG API Machinery, Apps and Testing]
- The list-type of the alpha resourceClaims field introduced to Pods in 1.26.0 was modified from "set" to "map", resolving an incompatibility with use of this schema in CustomResourceDefinitions and with server-side apply. ([kubernetes/kubernetes#114585](https://github.com/kubernetes/kubernetes/pull/114585), [@JoelSpeed](https://github.com/JoelSpeed)) [SIG API Machinery]


# v26.1.0

Kubernetes API Version: v1.26.1

### Bug or Regression
- The timeout unit of the WSClient update method is now always seconds for both poll and select functions. (#1976, @t-yrka)

### Feature
- Adds support for loading CA certificates from a file using the `idp-certificate-authority` key for the oidc plugin. (#1916, @vgupta3)

# v26.1.0b1

Kubernetes API Version: v1.26.1

### Bug or Regression
- The timeout unit of the WSClient update method is now always seconds for both poll and select functions. (#1976, @t-yrka)

### Feature
- Adds support for loading CA certificates from a file using the `idp-certificate-authority` key for the oidc plugin. (#1916, @vgupta3)

# v26.1.0a1

Kubernetes API Version: v1.26.1

### API Change
- The list-type of the alpha resourceClaims field introduced to Pods in 1.26.0 was modified from "set" to "map", resolving an incompatibility with use of this schema in CustomResourceDefinitions and with server-side apply. ([kubernetes/kubernetes#114617](https://github.com/kubernetes/kubernetes/pull/114617), [@JoelSpeed](https://github.com/JoelSpeed)) [SIG API Machinery]
- 'A new `preEnqueue` extension point was added to scheduler's component config
  `v1beta2/v1beta3/v1`.'
   ([kubernetes/kubernetes#113275](https://github.com/kubernetes/kubernetes/pull/113275), [@Huang-Wei](https://github.com/Huang-Wei))
- 'Added a `ResourceClaim` API (in the `resource.k8s.io/v1alpha1` API group and
  behind the `DynamicResourceAllocation` feature gate).
  The new API is now more flexible than the existing Device Plugins feature of Kubernetes because it
  allows Pods to request (claim) special kinds of resources, which can be available at node level, cluster
  level, or following any other model you implement.' ([kubernetes/kubernetes#111023](https://github.com/kubernetes/kubernetes/pull/111023), [@pohly](https://github.com/pohly))
- 'Container `preStop` and `postStart` lifecycle handlers using `httpGet` now
  honor the specified `scheme` and `headers` fields. This enables setting custom
  headers and changing the scheme to `HTTPS`, consistent with container
  startup/readiness/liveness probe capabilities. Lifecycle handlers configured
  with `scheme: HTTPS` that encounter errors indicating the endpoint is actually
  using HTTP fall back to making the request over HTTP for compatibility with
  previous releases. When this happens, a `LifecycleHTTPFallback` event is recorded
  in the namespace of the pod and a `kubelet_lifecycle_handler_http_fallbacks_total`
  metric in the kubelet is incremented. Cluster administrators can opt out of the
  expanded lifecycle handler capabilities by setting
  `--feature-gates=ConsistentHTTPGetHandlers=false` in `kubelet`.'
   ([kubernetes/kubernetes#86139](https://github.com/kubernetes/kubernetes/pull/86139), [@jasimmons](https://github.com/jasimmons))
- 'Graduated `JobTrackingWithFinalizers` to stable.
  Jobs created before the feature was enabled are still tracked without finalizers.
  Jobs tracked with finalizers have the annotation batch.kubernetes.io/job-tracking.
  If the annotation is present and the user attempts to remove it, the control plane adds it back.
  The annotation `batch.kubernetes.io/job-tracking` is now deprecated.
  The control plane will ignore it and stop adding it for new Jobs in v1.27.' ([kubernetes/kubernetes#113510](https://github.com/kubernetes/kubernetes/pull/113510), [@alculquicondor](https://github.com/alculquicondor))
- 'Kubelet added the following Pod failure conditions:
  - `DisruptionTarget` (graceful node shutdown, node pressure eviction)' ([kubernetes/kubernetes#112360](https://github.com/kubernetes/kubernetes/pull/112360), [@mimowo](https://github.com/mimowo))
- 'Priority and Fairness has introduced a new feature called _borrowing_ that allows an API priority level
  to borrow a number of seats from other priority level(s). As a cluster operator, you can enable borrowing
  for a certain priority level configuration object via the two newly introduced fields `lendablePercent`, and
  `borrowingLimitPercent` located under the `.spec.limited` field of the designated priority level.
  This change added the following metrics:
    - `apiserver_flowcontrol_nominal_limit_seats`: Nominal number of execution seats configured for each priority level
    - `apiserver_flowcontrol_lower_limit_seats`: Configured lower bound on number of execution seats available to each priority level
    - `apiserver_flowcontrol_upper_limit_seats`: Configured upper bound on number of execution seats available to each priority level
    - `apiserver_flowcontrol_demand_seats`: Observations, at the end of every nanosecond, of (the number of seats each priority level could use) / (nominal number of seats for that level)
    - `apiserver_flowcontrol_demand_seats_high_watermark`: High watermark, over last adjustment period, of demand_seats
    - `apiserver_flowcontrol_demand_seats_average`: Time-weighted average, over last adjustment period, of demand_seats
    - `apiserver_flowcontrol_demand_seats_stdev`: Time-weighted standard deviation, over last adjustment period, of demand_seats
    - `apiserver_flowcontrol_demand_seats_smoothed`: Smoothed seat demands
    - `apiserver_flowcontrol_target_seats`: Seat allocation targets
    - `apiserver_flowcontrol_seat_fair_frac`: Fair fraction of server's concurrency to allocate to each priority level that can use it
    - `apiserver_flowcontrol_current_limit_seats`: current derived number of execution seats available to each priority level
  The possibility of borrowing means that the old metric `apiserver_flowcontrol_request_concurrency_limit` can no longer mean both the configured concurrency limit and the enforced concurrency limit. Henceforth it means the configured concurrency limit.' ([kubernetes/kubernetes#113485](https://github.com/kubernetes/kubernetes/pull/113485), [@MikeSpreitzer](https://github.com/MikeSpreitzer))
- '`NodeInclusionPolicy` in `podTopologySpread` plugin is now enabled by default.'
   ([kubernetes/kubernetes#113500](https://github.com/kubernetes/kubernetes/pull/113500), [@kerthcet](https://github.com/kerthcet))
- '`PodDisruptionBudget` now adds an alpha `spec.unhealthyPodEvictionPolicy` field.
  When the `PDBUnhealthyPodEvictionPolicy` feature-gate is enabled in `kube-apiserver`,
  setting this field to `"AlwaysAllow"` allows pods to be evicted if they do not
  have a ready condition, regardless of whether the PodDisruptionBudget is currently
  healthy.'
   ([kubernetes/kubernetes#113375](https://github.com/kubernetes/kubernetes/pull/113375), [@atiratree](https://github.com/atiratree))
- '`metav1.LabelSelectors` specified in API objects are now validated to ensure
  they do not contain invalid label values that will error at time of use. Existing
  invalid objects can be updated, but new objects are required to contain valid
  label selectors.'
   ([kubernetes/kubernetes#113699](https://github.com/kubernetes/kubernetes/pull/113699), [@liggitt](https://github.com/liggitt))
- Add `percentageOfNodesToScore` as a scheduler profile level parameter to API version `v1`. When a profile `percentageOfNodesToScore` is set, it will override global `percentageOfNodesToScore`. ([kubernetes/kubernetes#112521](https://github.com/kubernetes/kubernetes/pull/112521), [@yuanchen8911](https://github.com/yuanchen8911))
- Add auth API to get self subject attributes (new selfsubjectreviews API is added). 
  The corresponding command for kubctl is provided - `kubectl auth whoami`. ([kubernetes/kubernetes#111333](https://github.com/kubernetes/kubernetes/pull/111333), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Auth, CLI and Testing]
- Added `kubernetes_feature_enabled` metric series to track whether each active feature gate is enabled. ([kubernetes/kubernetes#112690](https://github.com/kubernetes/kubernetes/pull/112690), [@logicalhan](https://github.com/logicalhan))
- Added a `--topology-manager-policy-options` flag to the kubelet to support fine tuning the topology manager policies. The first policy option, `prefer-closest-numa-nodes`, allows these policies to favor sets of NUMA nodes with shorter distance between nodes when making admission decisions. ([kubernetes/kubernetes#112914](https://github.com/kubernetes/kubernetes/pull/112914), [@PiotrProkop](https://github.com/PiotrProkop))
- Added a feature that allows a `StatefulSet` to start numbering replicas from an arbitrary non-negative ordinal, using the `.spec.ordinals.start` field. ([kubernetes/kubernetes#112744](https://github.com/kubernetes/kubernetes/pull/112744), [@pwschuurman](https://github.com/pwschuurman))
- Added a kube-proxy flag (`--iptables-localhost-nodeports`, default true) to allow disabling NodePort services on loopback addresses. Note: this only applies to iptables mode and ipv4. ([kubernetes/kubernetes#108250](https://github.com/kubernetes/kubernetes/pull/108250), [@cyclinder](https://github.com/cyclinder))
- Added a new namespace alpha field to `DataSourceRef` field in `PersistentVolumeClaim` API. ([kubernetes/kubernetes#113186](https://github.com/kubernetes/kubernetes/pull/113186), [@ttakahashi21](https://github.com/ttakahashi21))
- Aggregated discovery will be alpha and can be toggled with the `AggregatedDiscoveryEndpoint` feature flag. ([kubernetes/kubernetes#113171](https://github.com/kubernetes/kubernetes/pull/113171), [@Jefftree](https://github.com/Jefftree))
- Clarified the CFS quota as 100ms in the code comments and set the minimum `cpuCFSQuotaPeriod` to 1ms to match Linux kernel expectations. ([kubernetes/kubernetes#112123](https://github.com/kubernetes/kubernetes/pull/112123), [@paskal](https://github.com/paskal))
- Component-base: make the validation logic about LeaderElectionConfiguration consistent between component-base and client-go ([kubernetes/kubernetes#111758](https://github.com/kubernetes/kubernetes/pull/111758), [@SataQiu](https://github.com/SataQiu)) [SIG API Machinery and Scheduling]
- Deprecated the `apiserver_request_slo_duration_seconds` metric for v1.27 in favor of `apiserver_request_sli_duration_seconds` for naming consistency purposes with other SLI-specific metrics and to avoid any confusion between SLOs and SLIs. ([kubernetes/kubernetes#112679](https://github.com/kubernetes/kubernetes/pull/112679), [@dgrisonnet](https://github.com/dgrisonnet))
- Enable the "Retriable and non-retriable pod failures for jobs" feature into beta. ([kubernetes/kubernetes#113360](https://github.com/kubernetes/kubernetes/pull/113360), [@mimowo](https://github.com/mimowo))
- Enabled `kube-controller-manager` to support '--concurrent-horizontal-pod-autoscaler-syncs' flag to set the number of horizontal pod autoscaler controller workers. ([kubernetes/kubernetes#108501](https://github.com/kubernetes/kubernetes/pull/108501), [@zroubalik](https://github.com/zroubalik))
- Fixed spurious `field is immutable` errors validating updates to Event API objects via the `events.k8s.io/v1` API. ([kubernetes/kubernetes#112183](https://github.com/kubernetes/kubernetes/pull/112183), [@liggitt](https://github.com/liggitt))
- Graduated `ServiceInternalTrafficPolicy` feature to GA. ([kubernetes/kubernetes#113496](https://github.com/kubernetes/kubernetes/pull/113496), [@avoltz](https://github.com/avoltz))
- In 'kube-proxy`: The "userspace" proxy mode (deprecated for over a year) is no
  longer supported on either Linux or Windows. Users should use "iptables" or "ipvs"
  on Linux, or "kernelspace" on Windows.
   ([kubernetes/kubernetes#112133](https://github.com/kubernetes/kubernetes/pull/112133), [@knabben](https://github.com/knabben))
- Introduce `v1beta3` for Priority and Fairness with the following changes to the API spec:
  - rename 'assuredConcurrencyShares' (located under `spec.limited') to 'nominalConcurrencyShares'.
  - apply strategic merge patch annotations to 'Conditions' of flowschemas and `prioritylevelconfigurations`. ([kubernetes/kubernetes#112306](https://github.com/kubernetes/kubernetes/pull/112306), [@tkashem](https://github.com/tkashem))
- Introduced `v1alpha1` API for validating admission policies, enabling extensible admission control via CEL expressions (KEP  3488: CEL for Admission Control). To use, enable the `ValidatingAdmissionPolicy` feature gate and the `admissionregistration.k8s.io/v1alpha1` API via `--runtime-config`. ([kubernetes/kubernetes#113314](https://github.com/kubernetes/kubernetes/pull/113314), [@cici37](https://github.com/cici37))
- KMS: added validation for duplicate kms config name when auto reload is enabled. If you enabled automatic reload of encryption configuration with API server flag `--encryption-provider-config-automatic-reload`, ensure all the KMS provider names (v1 and v2) in the encryption configuration are unique. ([kubernetes/kubernetes#113697](https://github.com/kubernetes/kubernetes/pull/113697), [@aramase](https://github.com/aramase))
- Kubelet external Credential Provider feature is moved to GA. Credential Provider Plugin and Credential Provider Config APIs updated from `v1beta1` to `v1` with no API changes. ([kubernetes/kubernetes#111616](https://github.com/kubernetes/kubernetes/pull/111616), [@ndixita](https://github.com/ndixita))
- Legacy klog flags are no longer available. Only `-v` and `-vmodule` are still supported. ([kubernetes/kubernetes#112120](https://github.com/kubernetes/kubernetes/pull/112120), [@pohly](https://github.com/pohly)) [SIG Architecture, CLI, Instrumentation, Node and Testing]
- Moved `MixedProtocolLBService` from beta to GA. ([kubernetes/kubernetes#112895](https://github.com/kubernetes/kubernetes/pull/112895), [@janosi](https://github.com/janosi))
- New Pod API field `.spec.schedulingGates` is introduced to enable users to control when to mark a Pod as scheduling ready. ([kubernetes/kubernetes#113274](https://github.com/kubernetes/kubernetes/pull/113274), [@Huang-Wei](https://github.com/Huang-Wei))
- Protobuf serialization of metav1.MicroTime timestamps (used in `Lease` and `Event` API objects) has been corrected to truncate to microsecond precision, to match the documented behavior and JSON/YAML serialization. Any existing persisted data is truncated to microsecond when read from etcd. ([kubernetes/kubernetes#111936](https://github.com/kubernetes/kubernetes/pull/111936), [@haoruan](https://github.com/haoruan))
- Removed feature gates `ServiceLoadBalancerClass` and `ServiceLBNodePortControl`. These feature gates were enabled (and locked) since `v1.24`. ([kubernetes/kubernetes#112577](https://github.com/kubernetes/kubernetes/pull/112577), [@andrewsykim](https://github.com/andrewsykim))
- Reverted regression that prevented `client-go` latency metrics to be reported with a template URL to avoid label cardinality. ([kubernetes/kubernetes#111752](https://github.com/kubernetes/kubernetes/pull/111752), [@aanm](https://github.com/aanm))
- The `EndpointSliceTerminatingCondition` feature gate was graduated to GA. The gate is now locked and will be removed in v1.28. ([kubernetes/kubernetes#113351](https://github.com/kubernetes/kubernetes/pull/113351), [@andrewsykim](https://github.com/andrewsykim))
- `DynamicKubeletConfig` feature gate has been removed from the API server.
  Dynamic kubelet reconfiguration now can't be used even when older nodes are still
  attempting to rely on it. This is aligned with the Kubernetes version skew policy.
   ([kubernetes/kubernetes#112643](https://github.com/kubernetes/kubernetes/pull/112643), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev))
- `kubectl wait` command with `jsonpath` flag will wait for target path until timeout.
   ([kubernetes/kubernetes#109525](https://github.com/kubernetes/kubernetes/pull/109525), [@jonyhy96](https://github.com/jonyhy96))
- Add a `ResourceClaim` API (in the resource.k8s.io/v1alpha1 API group and
  behind the `DynamicResourceAllocation` feature gate).
  The new API is more flexible than the existing Device Plugins feature of Kubernetes because it
  allows Pods to request (claim) special kinds of resources, which can be available at node level, cluster
  level, or following any other model you implement. ([kubernetes/kubernetes#111023](https://github.com/kubernetes/kubernetes/pull/111023), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Release, Scheduling, Storage and Testing]
- PodDisruptionBudget adds an alpha `spec.unhealthyPodEvictionPolicy` field. When the `PDBUnhealthyPodEvictionPolicy` feature-gate is enabled in `kube-apiserver`, setting this field to `"AlwaysAllow"` allows pods to be evicted if they do not have a ready condition, regardless of whether the PodDisruptionBudget is currently healthy. ([kubernetes/kubernetes#113375](https://github.com/kubernetes/kubernetes/pull/113375), [@atiratree](https://github.com/atiratree)) [SIG API Machinery, Apps, Auth and Testing]
- A new `preEnqueue` extension point is added to scheduler's component config v1beta2/v1beta3/v1. ([kubernetes/kubernetes#113275](https://github.com/kubernetes/kubernetes/pull/113275), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG API Machinery, Apps, Instrumentation, Scheduling and Testing]
- Add a new namespace alpha field to dataSourceRef field in PersistentVolumeClaim API. ([kubernetes/kubernetes#113186](https://github.com/kubernetes/kubernetes/pull/113186), [@ttakahashi21](https://github.com/ttakahashi21)) [SIG API Machinery, Apps, Storage and Testing]
- Add a kube-proxy flag (--iptables-localhost-nodeports, default true) to allow disabling NodePort services on loopback addresses. Note: this only applies to iptables mode and ipv4. ([kubernetes/kubernetes#108250](https://github.com/kubernetes/kubernetes/pull/108250), [@cyclinder](https://github.com/cyclinder)) [SIG API Machinery, Cloud Provider, Network, Node, Scalability, Storage and Testing]
- Added a --topology-manager-policy-options flag to the kubelet to support fine tuning the topology manager policies. The first policy option, `prefer-closest-numa-nodes`, allows these policies to favor sets of NUMA nodes with shorter distance between nodes when making admission decisions. ([kubernetes/kubernetes#112914](https://github.com/kubernetes/kubernetes/pull/112914), [@PiotrProkop](https://github.com/PiotrProkop)) [SIG API Machinery and Node]
- Added a feature that allows a StatefulSet to start numbering replicas from an arbitrary non-negative ordinal, using the `.spec.ordinals.start` field. ([kubernetes/kubernetes#112744](https://github.com/kubernetes/kubernetes/pull/112744), [@pwschuurman](https://github.com/pwschuurman)) [SIG API Machinery and Apps]
- Deprecate the apiserver_request_slo_duration_seconds metric for v1.27 in favor of apiserver_request_sli_duration_seconds for naming consistency purposes with other SLI-specific metrics and to avoid any confusion between SLOs and SLIs. ([kubernetes/kubernetes#112679](https://github.com/kubernetes/kubernetes/pull/112679), [@dgrisonnet](https://github.com/dgrisonnet)) [SIG API Machinery and Instrumentation]
- Enable the "Retriable and non-retriable pod failures for jobs" feature into beta ([kubernetes/kubernetes#113360](https://github.com/kubernetes/kubernetes/pull/113360), [@mimowo](https://github.com/mimowo)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Graduate JobTrackingWithFinalizers to stable.
  Jobs created before the feature was enabled are still tracked without finalizers.
  Users can choose to migrate jobs to tracking with finalizers by adding the annotation batch.kubernetes.io/job-tracking.
  If the annotation was already present and the user attempts to remove it, the control plane adds the annotation back. ([kubernetes/kubernetes#113510](https://github.com/kubernetes/kubernetes/pull/113510), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps and Testing]
- Graduate ServiceInternalTrafficPolicy feature to GA ([kubernetes/kubernetes#113496](https://github.com/kubernetes/kubernetes/pull/113496), [@avoltz](https://github.com/avoltz)) [SIG Apps and Network]
- If you enabled automatic reload of encryption configuration with API server flag --encryption-provider-config-automatic-reload, ensure all the KMS provider names (v1 and v2) in the encryption configuration are unique. ([kubernetes/kubernetes#113697](https://github.com/kubernetes/kubernetes/pull/113697), [@aramase](https://github.com/aramase)) [SIG API Machinery and Auth]
- Introduce v1alpha1 API for validating admission policies, enabling extensible admission control via CEL expressions (KEP  3488: CEL for Admission Control). To use, enable the `ValidatingAdmissionPolicy` feature gate and the `admissionregistration.k8s.io/v1alpha1` API via `--runtime-config`. ([kubernetes/kubernetes#113314](https://github.com/kubernetes/kubernetes/pull/113314), [@cici37](https://github.com/cici37)) [SIG API Machinery, Auth, Cloud Provider and Testing]
- Kubelet adds the following pod failure conditions:
  - DisruptionTarget (graceful node shutdown, node pressure eviction) ([kubernetes/kubernetes#112360](https://github.com/kubernetes/kubernetes/pull/112360), [@mimowo](https://github.com/mimowo)) [SIG Apps, Node and Testing]
- Metav1.LabelSelectors specified in API objects are now validated to ensure they do not contain invalid label values that will error at time of use. Existing invalid objects can be updated, but new objects are required to contain valid label selectors. ([kubernetes/kubernetes#113699](https://github.com/kubernetes/kubernetes/pull/113699), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Auth, Network and Storage]
- Moving MixedProtocolLBService from beta to GA ([kubernetes/kubernetes#112895](https://github.com/kubernetes/kubernetes/pull/112895), [@janosi](https://github.com/janosi)) [SIG Apps, Network and Testing]
- New Pod API field `.spec.schedulingGates` is introduced to enable users to control when to mark a Pod as scheduling ready. ([kubernetes/kubernetes#113274](https://github.com/kubernetes/kubernetes/pull/113274), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Apps, Scheduling and Testing]
- NodeInclusionPolicy in podTopologySpread plugin is enabled by default. ([kubernetes/kubernetes#113500](https://github.com/kubernetes/kubernetes/pull/113500), [@kerthcet](https://github.com/kerthcet)) [SIG API Machinery, Apps, Scheduling and Testing]
- Priority and Fairness has introduced a new feature called _borrowing_ that allows an API priority level
  to borrow a number of seats from other priority level(s). As a cluster operator, you can enable borrowing
  for a certain priority level configuration object via the two newly introduced fields `lendablePercent`, and
  `borrowingLimitPercent` located under the `.spec.limited` field of the designated priority level.
  This PR adds the following metrics.
  - `apiserver_flowcontrol_nominal_limit_seats`: Nominal number of execution seats configured for each priority level
  - `apiserver_flowcontrol_lower_limit_seats`: Configured lower bound on number of execution seats available to each priority level
  - `apiserver_flowcontrol_upper_limit_seats`: Configured upper bound on number of execution seats available to each priority level
  - `apiserver_flowcontrol_demand_seats`: Observations, at the end of every nanosecond, of (the number of seats each priority level could use) / (nominal number of seats for that level)
  - `apiserver_flowcontrol_demand_seats_high_watermark`: High watermark, over last adjustment period, of demand_seats
  - `apiserver_flowcontrol_demand_seats_average`: Time-weighted average, over last adjustment period, of demand_seats
  - `apiserver_flowcontrol_demand_seats_stdev`: Time-weighted standard deviation, over last adjustment period, of demand_seats
  - `apiserver_flowcontrol_demand_seats_smoothed`: Smoothed seat demands
  - `apiserver_flowcontrol_target_seats`: Seat allocation targets
  - `apiserver_flowcontrol_seat_fair_frac`: Fair fraction of server's concurrency to allocate to each priority level that can use it
  - `apiserver_flowcontrol_current_limit_seats`: current derived number of execution seats available to each priority level
  
  The possibility of borrowing means that the old metric apiserver_flowcontrol_request_concurrency_limit can no longer mean both the configured concurrency limit and the enforced concurrency limit.  Henceforth it means the configured concurrency limit. ([kubernetes/kubernetes#113485](https://github.com/kubernetes/kubernetes/pull/113485), [@MikeSpreitzer](https://github.com/MikeSpreitzer)) [SIG API Machinery and Testing]
- The EndpointSliceTerminatingCondition feature gate has graduated to GA. The gate is now locked and will be removed in v1.28. ([kubernetes/kubernetes#113351](https://github.com/kubernetes/kubernetes/pull/113351), [@andrewsykim](https://github.com/andrewsykim)) [SIG API Machinery, Apps, Network and Testing]
- Yes, aggregated discovery will be alpha and can be toggled with the AggregatedDiscoveryEndpoint feature flag ([kubernetes/kubernetes#113171](https://github.com/kubernetes/kubernetes/pull/113171), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Network, Node, Release, Scalability, Scheduling, Storage and Testing]
- **Additional documentation e.g., KEPs (Kubernetes Enhancement Proposals), usage docs, etc.**:
  
  <!--
  This section can be blank if this pull request does not require a release note.
  
  When adding links which point to resources within git repositories, like
  KEPs or supporting documentation, please reference a specific commit and avoid
  linking directly to the master branch. This ensures that links reference a
  specific point in time, rather than a document that may change over time.
  
  See here for guidance on getting permanent links to files: https://help.github.com/en/articles/getting-permanent-links-to-files
  
  Please use the following format for linking documentation:
  - [KEP]: <link>
  - [Usage]: <link>
  - [Other doc]: <link>
  --> ([kubernetes/kubernetes#86139](https://github.com/kubernetes/kubernetes/pull/86139), [@jasimmons](https://github.com/jasimmons)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Contributor Experience, Instrumentation, Network, Node, Release, Scheduling, Storage and Testing]
- Add percentageOfNodesToScore as a scheduler profile level parameter to API version v1. If a profile percentageOfNodesToScore is set, it will override global percentageOfNodesToScore. ([kubernetes/kubernetes#112521](https://github.com/kubernetes/kubernetes/pull/112521), [@yuanchen8911](https://github.com/yuanchen8911)) [SIG API Machinery, Scheduling and Testing]
- Kube-controller-manager supports '--concurrent-horizontal-pod-autoscaler-syncs' flag to set the number of horizontal pod autoscaler controller workers. ([kubernetes/kubernetes#108501](https://github.com/kubernetes/kubernetes/pull/108501), [@zroubalik](https://github.com/zroubalik)) [SIG API Machinery, Apps and Autoscaling]
- Kube-proxy: The "userspace" proxy mode (deprecated for over a year) is no longer supported on either Linux or Windows.  Users should use "iptables" or "ipvs" on Linux, or "kernelspace" on Windows. ([kubernetes/kubernetes#112133](https://github.com/kubernetes/kubernetes/pull/112133), [@knabben](https://github.com/knabben)) [SIG API Machinery, Network, Scalability, Testing and Windows]
- Kubectl wait command with jsonpath flag will wait for target path appear until timeout. ([kubernetes/kubernetes#109525](https://github.com/kubernetes/kubernetes/pull/109525), [@jonyhy96](https://github.com/jonyhy96)) [SIG CLI and Testing]
- Kubelet external Credential Provider feature is moved to GA. Credential Provider Plugin and Credential Provider Config APIs updated from v1beta1 to v1 with no API changes. ([kubernetes/kubernetes#111616](https://github.com/kubernetes/kubernetes/pull/111616), [@ndixita](https://github.com/ndixita)) [SIG API Machinery, Node, Scheduling and Testing]
- The `DynamicKubeletConfig` feature gate has been removed from the API server. Dynamic kubelet reconfiguration now cannot be used even when older nodes are still attempting to rely on it. This is aligned with the Kubernetes version skew policy. ([kubernetes/kubernetes#112643](https://github.com/kubernetes/kubernetes/pull/112643), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG API Machinery, Apps, Auth, Node and Testing]
- Add `kubernetes_feature_enabled` metric series to track whether each active feature gate is enabled. ([kubernetes/kubernetes#112690](https://github.com/kubernetes/kubernetes/pull/112690), [@logicalhan](https://github.com/logicalhan)) [SIG API Machinery, Architecture, Cluster Lifecycle, Instrumentation, Network, Node and Scheduling]
- Introduce v1beta3 for Priority and Fairness with the following changes to the API spec:
  - rename 'assuredConcurrencyShares' (located under spec.limited') to 'nominalConcurrencyShares'
  - apply strategic merge patch annotations to 'Conditions' of flowschemas and prioritylevelconfigurations ([kubernetes/kubernetes#112306](https://github.com/kubernetes/kubernetes/pull/112306), [@tkashem](https://github.com/tkashem)) [SIG API Machinery and Testing]
- Legacy klog flags are no longer available. Only `-v` and `-vmodule` are still supported. ([kubernetes/kubernetes#112120](https://github.com/kubernetes/kubernetes/pull/112120), [@pohly](https://github.com/pohly)) [SIG Architecture, CLI, Instrumentation, Node and Testing]
- The feature gates ServiceLoadBalancerClass and ServiceLBNodePortControl have been removed. These feature gates were enabled (and locked) since v1.24. ([kubernetes/kubernetes#112577](https://github.com/kubernetes/kubernetes/pull/112577), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- Add auth API to get self subject attributes (new selfsubjectreviews API is added). 
  The corresponding command for kubctl is provided - `kubectl auth whoami`. ([kubernetes/kubernetes#111333](https://github.com/kubernetes/kubernetes/pull/111333), [@nabokihms](https://github.com/nabokihms)) [SIG API Machinery, Auth, CLI and Testing]
- Clarified the CFS quota as 100ms in the code comments and set the minimum cpuCFSQuotaPeriod to 1ms to match Linux kernel expectations. ([kubernetes/kubernetes#112123](https://github.com/kubernetes/kubernetes/pull/112123), [@paskal](https://github.com/paskal)) [SIG API Machinery and Node]
- Component-base: make the validation logic about LeaderElectionConfiguration consistent between component-base and client-go ([kubernetes/kubernetes#111758](https://github.com/kubernetes/kubernetes/pull/111758), [@SataQiu](https://github.com/SataQiu)) [SIG API Machinery and Scheduling]
- Fixes spurious `field is immutable` errors validating updates to Event API objects via the `events.k8s.io/v1` API ([kubernetes/kubernetes#112183](https://github.com/kubernetes/kubernetes/pull/112183), [@liggitt](https://github.com/liggitt)) [SIG Apps]
- Protobuf serialization of metav1.MicroTime timestamps (used in `Lease` and `Event` API objects) has been corrected to truncate to microsecond precision, to match the documented behavior and JSON/YAML serialization. Any existing persisted data is truncated to microsecond when read from etcd. ([kubernetes/kubernetes#111936](https://github.com/kubernetes/kubernetes/pull/111936), [@haoruan](https://github.com/haoruan)) [SIG API Machinery]
- Revert regression that prevented client-go latency metrics to be reported with a template URL to avoid label cardinality. ([kubernetes/kubernetes#111752](https://github.com/kubernetes/kubernetes/pull/111752), [@aanm](https://github.com/aanm)) [SIG API Machinery]
- [kubelet] Change default `cpuCFSQuotaPeriod` value with enabled `cpuCFSQuotaPeriod` flag from 100ms to 100µs to match the Linux CFS and k8s defaults. `cpuCFSQuotaPeriod` of 100ms now requires `customCPUCFSQuotaPeriod` flag to be set to work. ([kubernetes/kubernetes#111520](https://github.com/kubernetes/kubernetes/pull/111520), [@paskal](https://github.com/paskal)) [SIG API Machinery and Node]


# v25.3.0

Kubernetes API Version: v1.25.3

### Feature
- Adds support for loading CA certificates from a file using the `idp-certificate-authority` key for the oidc plugin. (#1916, @vgupta3)

# v25.3.0b1

Kubernetes API Version: v1.25.3

### Feature
- Adds support for loading CA certificates from a file using the `idp-certificate-authority` key for the oidc plugin. (#1916, @vgupta3)

# v25.2.0b1

Kubernetes API Version: v1.25.3

### Feature
- Adds support for loading CA certificates from a file using the `idp-certificate-authority` key for the oidc plugin. (#1916, @vgupta3)

# v25.2.0a1

Kubernetes API Version: v1.25.2

### API Change
- Revert regression that prevented client-go latency metrics to be reported with a template URL to avoid label cardinality. ([kubernetes/kubernetes#112055](https://github.com/kubernetes/kubernetes/pull/112055), [@aanm](https://github.com/aanm)) [SIG API Machinery]
- Add `NodeInclusionPolicy` to `TopologySpreadConstraints` in PodSpec. ([kubernetes/kubernetes#108492](https://github.com/kubernetes/kubernetes/pull/108492), [@kerthcet](https://github.com/kerthcet))
- Added KMS v2alpha1 support. ([kubernetes/kubernetes#111126](https://github.com/kubernetes/kubernetes/pull/111126), [@aramase](https://github.com/aramase))
- Added a deprecated warning for node beta label usage in PV/SC/RC and CSI Storage Capacity. ([kubernetes/kubernetes#108554](https://github.com/kubernetes/kubernetes/pull/108554), [@pacoxu](https://github.com/pacoxu))
- Added a new feature gate `CheckpointRestore` to enable support to checkpoint containers. If enabled it is possible to checkpoint a container using the newly kubelet API (/checkpoint/{podNamespace}/{podName}/{containerName}). ([kubernetes/kubernetes#104907](https://github.com/kubernetes/kubernetes/pull/104907), [@adrianreber](https://github.com/adrianreber)) [SIG Node and Testing]
- Added alpha support for user namespaces in pods phase 1 (KEP 127, feature gate: UserNamespacesStatelessPodsSupport) ([kubernetes/kubernetes#111090](https://github.com/kubernetes/kubernetes/pull/111090), [@rata](https://github.com/rata))
- As of v1.25, the PodSecurity `restricted` level no longer requires pods that set .spec.os.name="windows" to also set Linux-specific securityContext fields. If a 1.25+ cluster has unsupported [out-of-skew](https://kubernetes.io/releases/version-skew-policy/#kubelet) nodes prior to v1.23 and wants to ensure namespaces enforcing the `restricted` policy continue to require Linux-specific securityContext fields on all pods, ensure a version of the `restricted` prior to v1.25 is selected by labeling the namespace (for example, `pod-security.kubernetes.io/enforce-version: v1.24`) ([kubernetes/kubernetes#105919](https://github.com/kubernetes/kubernetes/pull/105919), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Changed ownership semantics of PersistentVolume's spec.claimRef from `atomic` to `granular`. ([kubernetes/kubernetes#110495](https://github.com/kubernetes/kubernetes/pull/110495), [@alexzielenski](https://github.com/alexzielenski))
- Extended ContainerStatus CRI API to allow runtime response with container resource requests and limits that are in effect.
  - UpdateContainerResources CRI API now supports both Linux and Windows. ([kubernetes/kubernetes#111645](https://github.com/kubernetes/kubernetes/pull/111645), [@vinaykul](https://github.com/vinaykul))
- For v1.25, Kubernetes will be using Golang 1.19, In this PR the version is updated to 1.19rc2 as GA is not yet available. ([kubernetes/kubernetes#111254](https://github.com/kubernetes/kubernetes/pull/111254), [@dims](https://github.com/dims))
- Introduced NodeIPAM support for multiple ClusterCIDRs ([kubernetes/kubernetes#2593](https://github.com/kubernetes/enhancements/issues/2593)) as an alpha feature.
  Set feature gate `MultiCIDRRangeAllocator=true`, determines whether the `MultiCIDRRangeAllocator` controller can be used, while the kube-controller-manager flag below will pick the active controller.
  Enabled the `MultiCIDRRangeAllocator` by setting `--cidr-allocator-type=MultiCIDRRangeAllocator` flag in kube-controller-manager. ([kubernetes/kubernetes#109090](https://github.com/kubernetes/kubernetes/pull/109090), [@sarveshr7](https://github.com/sarveshr7))
- Introduced PodHasNetwork condition for pods. ([kubernetes/kubernetes#111358](https://github.com/kubernetes/kubernetes/pull/111358), [@ddebroy](https://github.com/ddebroy))
- Introduced support for handling pod failures with respect to the configured pod failure policy rules. ([kubernetes/kubernetes#111113](https://github.com/kubernetes/kubernetes/pull/111113), [@mimowo](https://github.com/mimowo))
- Introduction of the `DisruptionTarget` pod condition type. Its `reason` field indicates the reason for pod termination:
  - PreemptionByKubeScheduler (Pod preempted by kube-scheduler)
  - DeletionByTaintManager (Pod deleted by taint manager due to NoExecute taint)
  - EvictionByEvictionAPI (Pod evicted by Eviction API)
  - DeletionByPodGC (an orphaned Pod deleted by PodGC) ([kubernetes/kubernetes#110959](https://github.com/kubernetes/kubernetes/pull/110959), [@mimowo](https://github.com/mimowo))
- Kube-Scheduler ComponentConfig is graduated to GA, `kubescheduler.config.k8s.io/v1` is available now.
  Plugin `SelectorSpread` is removed in v1. ([kubernetes/kubernetes#110534](https://github.com/kubernetes/kubernetes/pull/110534), [@kerthcet](https://github.com/kerthcet))
- Local Storage Capacity Isolation feature is GA in 1.25 release. For systems (rootless) that cannot check root file system, please use kubelet config --local-storage-capacity-isolation=false to disable this feature. Once disabled, pod cannot set local ephemeral storage request/limit, and emptyDir sizeLimit niether. ([kubernetes/kubernetes#111513](https://github.com/kubernetes/kubernetes/pull/111513), [@jingxu97](https://github.com/jingxu97))
- Make PodSpec.Ports' description clearer on how this information is only informational and how it can be incorrect. ([kubernetes/kubernetes#110564](https://github.com/kubernetes/kubernetes/pull/110564), [@j4m3s-s](https://github.com/j4m3s-s)) [SIG API Machinery, Network and Node]
- On compatible systems, a mounter's Unmount implementation is changed to not return an error when the specified target can be detected as not a mount point. On Linux, the behavior of detecting a mount point depends on `umount` command is validated when the mounter is created. Additionally, mount point checks will be skipped in CleanupMountPoint/CleanupMountWithForce if the mounter's Unmount having the changed behavior of not returning error when target is not a mount point. ([kubernetes/kubernetes#109676](https://github.com/kubernetes/kubernetes/pull/109676), [@cartermckinnon](https://github.com/cartermckinnon)) [SIG Storage]
- PersistentVolumeClaim objects are no longer left with storage class set to `nil` forever, but will be updated retroactively once any StorageClass is set or created as default. ([kubernetes/kubernetes#111467](https://github.com/kubernetes/kubernetes/pull/111467), [@RomanBednar](https://github.com/RomanBednar))
- Promote StatefulSet minReadySeconds to GA. This means `--feature-gates=StatefulSetMinReadySeconds=true` are not needed on kube-apiserver and kube-controller-manager binaries and they'll be removed soon following policy at https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation ([kubernetes/kubernetes#110896](https://github.com/kubernetes/kubernetes/pull/110896), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Testing]
- Promoted CronJob's TimeZone support to beta. ([kubernetes/kubernetes#111435](https://github.com/kubernetes/kubernetes/pull/111435), [@soltysh](https://github.com/soltysh))
- Promoted DaemonSet MaxSurge to GA. This means `--feature-gates=DaemonSetUpdateSurge=true` are not needed on kube-apiserver and kube-controller-manager binaries and they'll be removed soon following policy at https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation . ([kubernetes/kubernetes#111194](https://github.com/kubernetes/kubernetes/pull/111194), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Scheduler: included supported ScoringStrategyType list in error message for NodeResourcesFit plugin ([kubernetes/kubernetes#111206](https://github.com/kubernetes/kubernetes/pull/111206), [@SataQiu](https://github.com/SataQiu))
- The Go API for logging configuration in `k8s.io/component-base` was moved to `k8s.io/component-base/logs/api/v1`. The configuration file format and command line flags are the same as before. ([kubernetes/kubernetes#105797](https://github.com/kubernetes/kubernetes/pull/105797), [@pohly](https://github.com/pohly))
- The Pod `spec.podOS` field is promoted to GA. The `IdentifyPodOS` feature gate unconditionally enabled, and will no longer be accepted as a `--feature-gates` parameter in 1.27. ([kubernetes/kubernetes#111229](https://github.com/kubernetes/kubernetes/pull/111229), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- The PodTopologySpread is respected after rolling upgrades. ([kubernetes/kubernetes#111441](https://github.com/kubernetes/kubernetes/pull/111441), [@denkensk](https://github.com/denkensk))
- The `CSIInlineVolume` feature has moved from beta to GA. ([kubernetes/kubernetes#111258](https://github.com/kubernetes/kubernetes/pull/111258), [@dobsonj](https://github.com/dobsonj))
- The `PodSecurity` admission plugin has graduated to GA and is enabled by default. The admission configuration version has been promoted to `pod-security.admission.config.k8s.io/v1`. ([kubernetes/kubernetes#110459](https://github.com/kubernetes/kubernetes/pull/110459), [@wangyysde](https://github.com/wangyysde))
- The `endPort` field in Network Policy is now promoted to GA
  Network Policy providers that support `endPort` field now can use it to specify a range of ports to apply a Network Policy.
  Previously, each Network Policy could only target a single port.
  Please be aware that `endPort` field MUST BE SUPPORTED by the Network Policy provider. In case your provider does not support `endPort` and this field is specified in a Network Policy, the Network Policy will be created covering only the port field (single port). ([kubernetes/kubernetes#110868](https://github.com/kubernetes/kubernetes/pull/110868), [@rikatz](https://github.com/rikatz))
- The `metadata.clusterName` field is completely removed. This should not have any user-visible impact. ([kubernetes/kubernetes#109602](https://github.com/kubernetes/kubernetes/pull/109602), [@lavalamp](https://github.com/lavalamp))
- The `minDomains` field in Pod Topology Spread is graduated to beta ([kubernetes/kubernetes#110388](https://github.com/kubernetes/kubernetes/pull/110388), [@sanposhiho](https://github.com/sanposhiho)) [SIG API Machinery and Apps]
- The command line flag `enable-taint-manager` for kube-controller-manager is deprecated and will be removed in 1.26. The feature that it supports, taint based eviction, is enabled by default and will continue to be implicitly enabled when the flag is removed. ([kubernetes/kubernetes#111411](https://github.com/kubernetes/kubernetes/pull/111411), [@alculquicondor](https://github.com/alculquicondor))
- This release added support for `NodeExpandSecret` for CSI driver client which enables the CSI drivers to make use of this secret while performing node expansion operation based on the user request. Previously there was no secret  provided as part of the `nodeexpansion` call, thus CSI drivers did not make use of the same while expanding the volume at the node side. ([kubernetes/kubernetes#105963](https://github.com/kubernetes/kubernetes/pull/105963), [@zhucan](https://github.com/zhucan))
- [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) are now generally available (GA). The `EphemeralContainers` feature gate is always enabled and should be removed from `--feature-gates` flag on the kube-apiserver and the kubelet command lines. The `EphemeralContainers` feature gate is [deprecated and scheduled for removal](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation)  in a future release. ([kubernetes/kubernetes#111402](https://github.com/kubernetes/kubernetes/pull/111402), [@verb](https://github.com/verb))
- Introduces support for handling pod failures with respect to the configured pod failure policy rules ([kubernetes/kubernetes#111113](https://github.com/kubernetes/kubernetes/pull/111113), [@mimowo](https://github.com/mimowo)) [SIG API Machinery, Apps, Auth, Scheduling and Testing]
- NodeIPAM support for multiple ClusterCIDRs (https://github.com/kubernetes/enhancements/issues/2593) introduced as an alpha feature.
  Setting feature gate MultiCIDRRangeAllocator=true, determines whether the MultiCIDRRangeAllocator controller can be used, while the kube-controller-manager flag below will pick the active controller.
  Enable the MultiCIDRRangeAllocator by setting --cidr-allocator-type=MultiCIDRRangeAllocator flag in kube-controller-manager. ([kubernetes/kubernetes#109090](https://github.com/kubernetes/kubernetes/pull/109090), [@sarveshr7](https://github.com/sarveshr7)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Instrumentation, Network and Testing]
- The CSIInlineVolume feature has moved from beta to GA. ([kubernetes/kubernetes#111258](https://github.com/kubernetes/kubernetes/pull/111258), [@dobsonj](https://github.com/dobsonj)) [SIG API Machinery, Apps, Auth, Instrumentation, Storage and Testing]
- Added alpha support for user namespaces in pods phase 1 (KEP 127, feature gate: UserNamespacesSupport) ([kubernetes/kubernetes#111090](https://github.com/kubernetes/kubernetes/pull/111090), [@rata](https://github.com/rata)) [SIG Apps, Auth, Network, Node, Storage and Testing]
- Adds KMS v2alpha1 support ([kubernetes/kubernetes#111126](https://github.com/kubernetes/kubernetes/pull/111126), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth, Instrumentation and Testing]
- As of v1.25, the PodSecurity `restricted` level no longer requires pods that set .spec.os.name="windows" to also set Linux-specific securityContext fields. If a 1.25+ cluster has unsupported [out-of-skew](https://kubernetes.io/releases/version-skew-policy/#kubelet) nodes prior to v1.23 and wants to ensure namespaces enforcing the `restricted` policy continue to require Linux-specific securityContext fields on all pods, ensure a version of the `restricted` prior to v1.25 is selected by labeling the namespace (for example, `pod-security.kubernetes.io/enforce-version: v1.24`) ([kubernetes/kubernetes#105919](https://github.com/kubernetes/kubernetes/pull/105919), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps, Auth, Testing and Windows]
- Changes ownership semantics of PersistentVolume's spec.claimRef from `atomic` to `granular`. ([kubernetes/kubernetes#110495](https://github.com/kubernetes/kubernetes/pull/110495), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Instrumentation and Testing]
- Extends ContainerStatus CRI API to allow runtime response with container resource requests and limits that are in effect.
  - UpdateContainerResources CRI API now supports both Linux and Windows.
  For details, see KEPs below. ([kubernetes/kubernetes#111645](https://github.com/kubernetes/kubernetes/pull/111645), [@vinaykul](https://github.com/vinaykul)) [SIG Node]
- For v1.25, Kubernetes will be using golang 1.19, In this PR we update to 1.19rc2 as GA is not yet available. ([kubernetes/kubernetes#111254](https://github.com/kubernetes/kubernetes/pull/111254), [@dims](https://github.com/dims)) [SIG Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scheduling, Storage and Testing]
- Introduce PodHasNetwork condition for pods ([kubernetes/kubernetes#111358](https://github.com/kubernetes/kubernetes/pull/111358), [@ddebroy](https://github.com/ddebroy)) [SIG Apps, Node and Testing]
- Introduction of the `DisruptionTarget` pod condition type. Its `reason` field indicates the reason for pod termination:
  - PreemptionByKubeScheduler (Pod preempted by kube-scheduler)
  - DeletionByTaintManager (Pod deleted by taint manager due to NoExecute taint)
  - EvictionByEvictionAPI (Pod evicted by Eviction API)
  - DeletionByPodGC (an orphaned Pod deleted by PodGC) ([kubernetes/kubernetes#110959](https://github.com/kubernetes/kubernetes/pull/110959), [@mimowo](https://github.com/mimowo)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Kube-Scheduler ComponentConfig is graduated to GA, `kubescheduler.config.k8s.io/v1` is available now.
  Plugin `SelectorSpread` is removed in v1. ([kubernetes/kubernetes#110534](https://github.com/kubernetes/kubernetes/pull/110534), [@kerthcet](https://github.com/kerthcet)) [SIG API Machinery, Scheduling and Testing]
- Local Storage Capacity Isolation feature is GA in 1.25 release. For systems (rootless) that cannot check root file system, please use kubelet config --local-storage-capacity-isolation=false to disable this feature. Once disabled, pod cannot set local ephemeral storage request/limit, and emptyDir sizeLimit niether. ([kubernetes/kubernetes#111513](https://github.com/kubernetes/kubernetes/pull/111513), [@jingxu97](https://github.com/jingxu97)) [SIG API Machinery, Node, Scalability and Scheduling]
- PersistentVolumeClaim objects are no longer left with storage class set to `nil` forever, but will be updated retroactively once any StorageClass is set or created as default. ([kubernetes/kubernetes#111467](https://github.com/kubernetes/kubernetes/pull/111467), [@RomanBednar](https://github.com/RomanBednar)) [SIG Apps, Storage and Testing]
- Promote CronJob's TimeZone support to beta ([kubernetes/kubernetes#111435](https://github.com/kubernetes/kubernetes/pull/111435), [@soltysh](https://github.com/soltysh)) [SIG API Machinery, Apps and Testing]
- Promote DaemonSet MaxSurge to GA. This means `--feature-gates=DaemonSetUpdateSurge=true` are not needed on kube-apiserver and kube-controller-manager binaries and they'll be removed soon following policy at https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation ([kubernetes/kubernetes#111194](https://github.com/kubernetes/kubernetes/pull/111194), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps]
- Respect PodTopologySpread after rolling upgrades ([kubernetes/kubernetes#111441](https://github.com/kubernetes/kubernetes/pull/111441), [@denkensk](https://github.com/denkensk)) [SIG API Machinery, Apps, Scheduling and Testing]
- Scheduler: include supported ScoringStrategyType list in error message for NodeResourcesFit plugin ([kubernetes/kubernetes#111206](https://github.com/kubernetes/kubernetes/pull/111206), [@SataQiu](https://github.com/SataQiu)) [SIG Scheduling]
- The Pod `spec.podOS` field is promoted to GA. The `IdentifyPodOS` feature gate unconditionally enabled, and will no longer be accepted as a `--feature-gates` parameter in 1.27. ([kubernetes/kubernetes#111229](https://github.com/kubernetes/kubernetes/pull/111229), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Windows]
- The command line flag `enable-taint-manager` for kube-controller-manager is deprecated and will be removed in 1.26.
  The feature that it supports, taint based eviction, is enabled by default and will continue to be implicitly enabled when the flag is removed. ([kubernetes/kubernetes#111411](https://github.com/kubernetes/kubernetes/pull/111411), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery]
- [Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) are now generally available. The `EphemeralContainers` feature gate is always enabled and should be removed from `--feature-gates` flag on the kube-apiserver and the kubelet command lines. The `EphemeralContainers` feature gate is [deprecated and scheduled for removal](https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation) in a future release. ([kubernetes/kubernetes#111402](https://github.com/kubernetes/kubernetes/pull/111402), [@verb](https://github.com/verb)) [SIG API Machinery, Apps, Node, Storage and Testing]
- Added a new feature gate `CheckpointRestore` to enable support to checkpoint containers. If enabled it is possible to checkpoint a container using the newly kubelet API (/checkpoint/{podNamespace}/{podName}/{containerName}). ([kubernetes/kubernetes#104907](https://github.com/kubernetes/kubernetes/pull/104907), [@adrianreber](https://github.com/adrianreber)) [SIG Node and Testing]
- EndPort field in Network Policy is now promoted to GA
  Network Policy providers that support endPort field now can use it to specify a range of ports to apply a Network Policy.
  Previously, each Network Policy could only target a single port.
  Please be aware that endPort field MUST BE SUPPORTED by the Network Policy provider. In case your provider does not support endPort and this field is specified in a Network Policy, the Network Policy will be created covering only the port field (single port). ([kubernetes/kubernetes#110868](https://github.com/kubernetes/kubernetes/pull/110868), [@rikatz](https://github.com/rikatz)) [SIG API Machinery, Network and Testing]
- Make PodSpec.Ports' description clearer on how this information is only informational and how it can be incorrect. ([kubernetes/kubernetes#110564](https://github.com/kubernetes/kubernetes/pull/110564), [@j4m3s-s](https://github.com/j4m3s-s)) [SIG API Machinery, Network and Node]
- On compatible systems, a mounter's Unmount implementation is changed to not return an error when the specified target can be detected as not a mount point. On Linux, the behavior of detecting a mount point depends on `umount` command is validated when the mounter is created. Additionally, mount point checks will be skipped in CleanupMountPoint/CleanupMountWithForce if the mounter's Unmount having the changed behavior of not returning error when target is not a mount point. ([kubernetes/kubernetes#109676](https://github.com/kubernetes/kubernetes/pull/109676), [@cartermckinnon](https://github.com/cartermckinnon)) [SIG Storage]
- Promote StatefulSet minReadySeconds to GA. This means `--feature-gates=StatefulSetMinReadySeconds=true` are not needed on kube-apiserver and kube-controller-manager binaries and they'll be removed soon following policy at https://kubernetes.io/docs/reference/using-api/deprecation-policy/#deprecation ([kubernetes/kubernetes#110896](https://github.com/kubernetes/kubernetes/pull/110896), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Testing]
- The Pod `spec.podOS` field is promoted to GA. The `IdentifyPodOS` feature gate unconditionally enabled, and will no longer be accepted as a `--feature-gates` parameter in 1.27. ([kubernetes/kubernetes#111229](https://github.com/kubernetes/kubernetes/pull/111229), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Windows]
- The `minDomains` field in Pod Topology Spread is graduated to beta ([kubernetes/kubernetes#110388](https://github.com/kubernetes/kubernetes/pull/110388), [@sanposhiho](https://github.com/sanposhiho)) [SIG API Machinery and Apps]
- The Go API for logging configuration in k8s.io/component-base was moved to k8s.io/component-base/logs/api/v1. The configuration file format and command line flags are the same as before. ([kubernetes/kubernetes#105797](https://github.com/kubernetes/kubernetes/pull/105797), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Cluster Lifecycle, Instrumentation, Node, Scheduling and Testing]
- The PodSecurity admission plugin has graduated to GA and is enabled by default. The admission configuration version has been promoted to `pod-security.admission.config.k8s.io/v1`. ([kubernetes/kubernetes#110459](https://github.com/kubernetes/kubernetes/pull/110459), [@wangyysde](https://github.com/wangyysde)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Storage and Testing]
- Introduce NodeInclusionPolicies to specify nodeAffinity/nodeTaint strategy when calculating pod topology spread skew. ([kubernetes/kubernetes#108492](https://github.com/kubernetes/kubernetes/pull/108492), [@kerthcet](https://github.com/kerthcet)) [SIG API Machinery, Apps, Scheduling and Testing]
- The `metadata.clusterName` field is completely removed. This should not have any user-visible impact. ([kubernetes/kubernetes#109602](https://github.com/kubernetes/kubernetes/pull/109602), [@lavalamp](https://github.com/lavalamp)) [SIG API Machinery, Apps, Auth and Testing]
- This release add support for NodeExpandSecret for CSI driver client which enables the CSI drivers to make use of this secret while performing node expansion operation based on the user request. Previously there was no secret  provided as part of the nodeexpansion call, thus CSI drivers were not make use of the same while expanding the volume at node side. ([kubernetes/kubernetes#105963](https://github.com/kubernetes/kubernetes/pull/105963), [@zhucan](https://github.com/zhucan)) [SIG API Machinery, Apps and Storage]


# v24.2.0

Kubernetes API Version: v1.24.2

### Uncategorized
- The dynamic client now support the `_request_timeout` parameter to configure connection and request timeouts. (#1732, @philipp-sontag-by)

# v24.1.0b1

Kubernetes API Version: v1.24.1

### Uncategorized
- The dynamic client now support the `_request_timeout` parameter to configure connection and request timeouts. (#1732, @philipp-sontag-by)

# v24.1.0a1

Kubernetes API Version: v1.24.1

### API Change
- Add 2 new options for kube-proxy running in winkernel mode. `--forward-healthcheck-vip`, if specified as true, health check traffic whose destination is service VIP will be forwarded to kube-proxy's healthcheck service. `--root-hnsendpoint-name` specifies the name of the hns endpoint for the root network namespace. This option enables the pass-through load balancers like Google's GCLB to correctly health check the backend services. Without this change, the health check packets is dropped, and Windows node will be considered to be unhealthy by those load balancers. ([kubernetes/kubernetes#99287](https://github.com/kubernetes/kubernetes/pull/99287), [@anfernee](https://github.com/anfernee))
- Added CEL runtime cost calculation into CustomerResource validation. CustomerResource validation will fail if runtime cost exceeds the budget. ([kubernetes/kubernetes#108482](https://github.com/kubernetes/kubernetes/pull/108482), [@cici37](https://github.com/cici37))
- Added a new metric `webhook_fail_open_count` to monitor webhooks that fail to open. ([kubernetes/kubernetes#107171](https://github.com/kubernetes/kubernetes/pull/107171), [@ltagliamonte-dd](https://github.com/ltagliamonte-dd))
- Adds a new Status subresource in Network Policy objects ([kubernetes/kubernetes#107963](https://github.com/kubernetes/kubernetes/pull/107963), [@rikatz](https://github.com/rikatz))
- Adds support for `InterfaceNamePrefix` and `BridgeInterface` as arguments to `--detect-local-mode` option and also introduces a new optional `--pod-interface-name-prefix` and `--pod-bridge-interface` flags to kube-proxy. ([kubernetes/kubernetes#95400](https://github.com/kubernetes/kubernetes/pull/95400), [@tssurya](https://github.com/tssurya))
- CEL CRD validation expressions may now reference existing object state using the identifier `oldSelf`. ([kubernetes/kubernetes#108073](https://github.com/kubernetes/kubernetes/pull/108073), [@benluddy](https://github.com/benluddy))
- CRD deep copies should no longer contain shallow copies of `JSONSchemaProps.XValidations`. ([kubernetes/kubernetes#107956](https://github.com/kubernetes/kubernetes/pull/107956), [@benluddy](https://github.com/benluddy))
- CRD writes will generate validation errors if a CEL validation rule references the identifier `oldSelf` on a part of the schema that does not support it. ([kubernetes/kubernetes#108013](https://github.com/kubernetes/kubernetes/pull/108013), [@benluddy](https://github.com/benluddy))
- CSIStorageCapacity.storage.k8s.io: The v1beta1 version of this API is deprecated in favor of v1, and will be removed in v1.27. If a CSI driver supports storage capacity tracking, then it must get deployed with a release of external-provisioner that supports the v1 API. ([kubernetes/kubernetes#108445](https://github.com/kubernetes/kubernetes/pull/108445), [@pohly](https://github.com/pohly))
- Custom resource requests with `fieldValidation=Strict` consistently require `apiVersion` and `kind`, matching non-strict requests ([kubernetes/kubernetes#109019](https://github.com/kubernetes/kubernetes/pull/109019), [@liggitt](https://github.com/liggitt))
- Feature of `DefaultPodTopologySpread` is graduated to GA ([kubernetes/kubernetes#108278](https://github.com/kubernetes/kubernetes/pull/108278), [@kerthcet](https://github.com/kerthcet))
- Feature of `NonPreemptingPriority` is graduated to GA ([kubernetes/kubernetes#107432](https://github.com/kubernetes/kubernetes/pull/107432), [@denkensk](https://github.com/denkensk))
- Feature of `PodOverhead` is graduated to GA ([kubernetes/kubernetes#108441](https://github.com/kubernetes/kubernetes/pull/108441), [@pacoxu](https://github.com/pacoxu))
- Fixed OpenAPI serialization of the x-kubernetes-validations field ([kubernetes/kubernetes#107970](https://github.com/kubernetes/kubernetes/pull/107970), [@liggitt](https://github.com/liggitt))
- Fixed failed flushing logs in defer function when kubelet cmd exit 1. ([kubernetes/kubernetes#104774](https://github.com/kubernetes/kubernetes/pull/104774), [@kerthcet](https://github.com/kerthcet))
- Fixes a regression in v1beta1 PodDisruptionBudget handling of `strategic merge patch`-type API requests for the `selector` field. Prior to 1.21, these requests would merge `matchLabels` content and replace `matchExpressions` content. In 1.21, patch requests touching the `selector` field started replacing the entire selector. This is consistent with server-side apply and the v1 PodDisruptionBudget behavior, but should not have been changed for v1beta1. ([kubernetes/kubernetes#108138](https://github.com/kubernetes/kubernetes/pull/108138), [@liggitt](https://github.com/liggitt))
- Improve kubectl's user help commands readability ([kubernetes/kubernetes#104736](https://github.com/kubernetes/kubernetes/pull/104736), [@lauchokyip](https://github.com/lauchokyip))
- Indexed Jobs graduated to stable. ([kubernetes/kubernetes#107395](https://github.com/kubernetes/kubernetes/pull/107395), [@alculquicondor](https://github.com/alculquicondor))
- Introduce a v1alpha1 networking API for ClusterCIDRConfig ([kubernetes/kubernetes#108290](https://github.com/kubernetes/kubernetes/pull/108290), [@sarveshr7](https://github.com/sarveshr7))
- Introduction of a new "sync_proxy_rules_no_local_endpoints_total" proxy metric. This metric represents the number of services with no internal endpoints. The "traffic_policy" label will contain both "internal" or "external". ([kubernetes/kubernetes#108930](https://github.com/kubernetes/kubernetes/pull/108930), [@MaxRenaud](https://github.com/MaxRenaud))
- JobReadyPods graduates to Beta and it's enabled by default. ([kubernetes/kubernetes#107476](https://github.com/kubernetes/kubernetes/pull/107476), [@alculquicondor](https://github.com/alculquicondor))
- Kube-apiserver: `--audit-log-version` and `--audit-webhook-version` now only support the default value of `audit.k8s.io/v1`. The v1alpha1 and v1beta1 audit log versions, deprecated since 1.13, have been removed. ([kubernetes/kubernetes#108092](https://github.com/kubernetes/kubernetes/pull/108092), [@carlory](https://github.com/carlory))
- Kube-apiserver: the `metadata.selfLink` field can no longer be populated by kube-apiserver; it was deprecated in 1.16 and has not been populated by default since 1.20+. ([kubernetes/kubernetes#107527](https://github.com/kubernetes/kubernetes/pull/107527), [@wojtek-t](https://github.com/wojtek-t))
- Kubelet external Credential Provider feature is moved to Beta. Credential Provider Plugin and Credential Provider Config API's updated from v1alpha1 to v1beta1 with no API changes. ([kubernetes/kubernetes#108847](https://github.com/kubernetes/kubernetes/pull/108847), [@adisky](https://github.com/adisky))
- Make STS available replicas optional again. ([kubernetes/kubernetes#109241](https://github.com/kubernetes/kubernetes/pull/109241), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- MaxUnavailable for StatefulSets, allows faster RollingUpdate by taking down more than 1 pod at a time. The number of pods you want to take down during a RollingUpdate is configurable using maxUnavailable parameter. ([kubernetes/kubernetes#82162](https://github.com/kubernetes/kubernetes/pull/82162), [@krmayankk](https://github.com/krmayankk))
- Non-graceful node shutdown handling is enabled for stateful workload failovers ([kubernetes/kubernetes#108486](https://github.com/kubernetes/kubernetes/pull/108486), [@sonasingh46](https://github.com/sonasingh46))
- Omit enum declarations from the static openapi file captured at https://git.k8s.io/kubernetes/api/openapi-spec. This file is used to generate API clients, and use of enums in those generated clients (rather than strings) can break forward compatibility with additional future values in those fields. See https://issue.k8s.io/109177 for details. ([kubernetes/kubernetes#109178](https://github.com/kubernetes/kubernetes/pull/109178), [@liggitt](https://github.com/liggitt))
- OpenAPI V3 is turned on by default ([kubernetes/kubernetes#109031](https://github.com/kubernetes/kubernetes/pull/109031), [@Jefftree](https://github.com/Jefftree))
- Pod affinity namespace selector and cross-namespace quota graduated to GA. The feature gate `PodAffinityNamespaceSelector` is locked and will be removed in 1.26. ([kubernetes/kubernetes#108136](https://github.com/kubernetes/kubernetes/pull/108136), [@ahg-g](https://github.com/ahg-g))
- Promote IdentifyPodOS feature to beta. ([kubernetes/kubernetes#107859](https://github.com/kubernetes/kubernetes/pull/107859), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Remove a v1alpha1 networking API for ClusterCIDRConfig ([kubernetes/kubernetes#109436](https://github.com/kubernetes/kubernetes/pull/109436), [@JamesLaverack](https://github.com/JamesLaverack))
- Renamed metrics `evictions_number` to `evictions_total` and mark it as stable. The original `evictions_number` metrics name is marked as "Deprecated" and has been removed in kubernetes 1.23 . ([kubernetes/kubernetes#106366](https://github.com/kubernetes/kubernetes/pull/106366), [@cyclinder](https://github.com/cyclinder))
- Skip x-kubernetes-validations rules if having fundamental error against the OpenAPIv3 schema. ([kubernetes/kubernetes#108859](https://github.com/kubernetes/kubernetes/pull/108859), [@cici37](https://github.com/cici37))
- Support for gRPC probes is now in beta. GRPCContainerProbe feature gate is enabled by default. ([kubernetes/kubernetes#108522](https://github.com/kubernetes/kubernetes/pull/108522), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev))
- Suspend job to GA. The feature gate `SuspendJob` is locked and will be removed in 1.26. ([kubernetes/kubernetes#108129](https://github.com/kubernetes/kubernetes/pull/108129), [@ahg-g](https://github.com/ahg-g))
- The AnyVolumeDataSource feature is now beta, and the feature gate is enabled by default. In order to provide user feedback on PVCs with data sources, deployers must install the VolumePopulators CRD and the data-source-validator controller. ([kubernetes/kubernetes#108736](https://github.com/kubernetes/kubernetes/pull/108736), [@bswartz](https://github.com/bswartz))
- The CertificateSigningRequest `spec.expirationSeconds` API field has graduated to GA. The `CSRDuration` feature gate for the field is now unconditionally enabled and will be removed in 1.26. ([kubernetes/kubernetes#108782](https://github.com/kubernetes/kubernetes/pull/108782), [@cfryanr](https://github.com/cfryanr))
- The `ServerSideFieldValidation` feature has graduated to beta and is now enabled by default. Kubectl 1.24 and newer will use server-side validation instead of client-side validation when writing to API servers with the feature enabled. ([kubernetes/kubernetes#108889](https://github.com/kubernetes/kubernetes/pull/108889), [@kevindelgado](https://github.com/kevindelgado))
- The `ServiceLBNodePortControl` feature has graduated to GA. The feature gate will be removed in 1.26. ([kubernetes/kubernetes#107027](https://github.com/kubernetes/kubernetes/pull/107027), [@uablrek](https://github.com/uablrek))
- The deprecated kube-controller-manager flag '--deployment-controller-sync-period' has been removed, it is not used by the deployment controller. ([kubernetes/kubernetes#107178](https://github.com/kubernetes/kubernetes/pull/107178), [@SataQiu](https://github.com/SataQiu))
- The feature `DynamicKubeletConfig` has been removed from the kubelet. ([kubernetes/kubernetes#106932](https://github.com/kubernetes/kubernetes/pull/106932), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev))
- The infrastructure for contextual logging is complete (feature gate implemented, JSON backend ready). ([kubernetes/kubernetes#108995](https://github.com/kubernetes/kubernetes/pull/108995), [@pohly](https://github.com/pohly))
- This adds an optional `timeZone` field as part of the CronJob spec to support running cron jobs in a specific time zone. ([kubernetes/kubernetes#108032](https://github.com/kubernetes/kubernetes/pull/108032), [@deejross](https://github.com/deejross))
- Updated the default API priority-and-fairness config to avoid endpoint/configmaps operations from controller-manager to all match leader-election priority level. ([kubernetes/kubernetes#106725](https://github.com/kubernetes/kubernetes/pull/106725), [@wojtek-t](https://github.com/wojtek-t))
- `topologySpreadConstraints` includes `minDomains` field to limit the minimum number of topology domains. ([kubernetes/kubernetes#107674](https://github.com/kubernetes/kubernetes/pull/107674), [@sanposhiho](https://github.com/sanposhiho))
- Introduce a v1alpha1 networking API for ClusterCIDRConfig ([kubernetes/kubernetes#108290](https://github.com/kubernetes/kubernetes/pull/108290), [@sarveshr7](https://github.com/sarveshr7)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Instrumentation, Network and Testing]
- Introduction of a new "sync_proxy_rules_no_local_endpoints_total" proxy metric. This metric represents the number of services with no internal endpoints. The "traffic_policy" label will contain both "internal" or "external". ([kubernetes/kubernetes#108930](https://github.com/kubernetes/kubernetes/pull/108930), [@MaxRenaud](https://github.com/MaxRenaud)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Instrumentation, Network, Node, Release, Scheduling, Storage, Testing and Windows]
- Make STS available replicas optional again, ([kubernetes/kubernetes#109241](https://github.com/kubernetes/kubernetes/pull/109241), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery and Apps]
- Omit enum declarations from the static openapi file captured at https://git.k8s.io/kubernetes/api/openapi-spec. This file is used to generate API clients, and use of enums in those generated clients (rather than strings) can break forward compatibility with additional future values in those fields. See https://issue.k8s.io/109177 for details. ([kubernetes/kubernetes#109178](https://github.com/kubernetes/kubernetes/pull/109178), [@liggitt](https://github.com/liggitt)) [SIG API Machinery and Auth]
- Remove a v1alpha1 networking API for ClusterCIDRConfig ([kubernetes/kubernetes#109436](https://github.com/kubernetes/kubernetes/pull/109436), [@JamesLaverack](https://github.com/JamesLaverack)) [SIG API Machinery, Apps, Auth, CLI, Network and Testing]
- The deprecated kube-controller-manager flag '--deployment-controller-sync-period' has been removed, it is not used by the deployment controller. ([kubernetes/kubernetes#107178](https://github.com/kubernetes/kubernetes/pull/107178), [@SataQiu](https://github.com/SataQiu)) [SIG API Machinery and Apps]
- Adds a new Status subresource in Network Policy objects ([kubernetes/kubernetes#107963](https://github.com/kubernetes/kubernetes/pull/107963), [@rikatz](https://github.com/rikatz)) [SIG API Machinery, Apps, Network and Testing]
- Adds support for "InterfaceNamePrefix" and "BridgeInterface" as arguments to --detect-local-mode option and also introduces a new optional `--pod-interface-name-prefix` and `--pod-bridge-interface` flags to kube-proxy. ([kubernetes/kubernetes#95400](https://github.com/kubernetes/kubernetes/pull/95400), [@tssurya](https://github.com/tssurya)) [SIG API Machinery and Network]
- CEL CRD validation expressions may now reference existing object state using the identifier `oldSelf`. ([kubernetes/kubernetes#108073](https://github.com/kubernetes/kubernetes/pull/108073), [@benluddy](https://github.com/benluddy)) [SIG API Machinery and Testing]
- CSIStorageCapacity.storage.k8s.io: The v1beta1 version of this API is deprecated in favor of v1, and will be removed in v1.27. If a CSI driver supports storage capacity tracking, then it must get deployed with a release of external-provisioner that supports the v1 API. ([kubernetes/kubernetes#108445](https://github.com/kubernetes/kubernetes/pull/108445), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Auth, Scheduling, Storage and Testing]
- Custom resource requests with fieldValidation=Strict consistently require apiVersion and kind, matching non-strict requests ([kubernetes/kubernetes#109019](https://github.com/kubernetes/kubernetes/pull/109019), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- Improve kubectl's user help commands readability ([kubernetes/kubernetes#104736](https://github.com/kubernetes/kubernetes/pull/104736), [@lauchokyip](https://github.com/lauchokyip)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Contributor Experience, Instrumentation, Network, Node, Release, Scalability, Scheduling, Security, Storage, Testing and Windows]
- Indexed Jobs graduates to stable ([kubernetes/kubernetes#107395](https://github.com/kubernetes/kubernetes/pull/107395), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps, Architecture and Testing]
- Introduce a v1alpha1 networking API for ClusterCIDRConfig ([kubernetes/kubernetes#108290](https://github.com/kubernetes/kubernetes/pull/108290), [@sarveshr7](https://github.com/sarveshr7)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Instrumentation, Network and Testing]
- JobReadyPods graduates to Beta and it's enabled by default. ([kubernetes/kubernetes#107476](https://github.com/kubernetes/kubernetes/pull/107476), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps and Testing]
- Kubelet external Credential Provider feature is moved to Beta.  Credential Provider Plugin and Credential Provider Config API's updated from v1alpha1 to v1beta1 with no API changes. ([kubernetes/kubernetes#108847](https://github.com/kubernetes/kubernetes/pull/108847), [@adisky](https://github.com/adisky)) [SIG API Machinery and Node]
- MaxUnavailable for StatefulSets, allows faster RollingUpdate by taking down more than 1 pod at a time. The number of pods you want to take down during a RollingUpdate is configurable using maxUnavailable parameter. ([kubernetes/kubernetes#82162](https://github.com/kubernetes/kubernetes/pull/82162), [@krmayankk](https://github.com/krmayankk)) [SIG API Machinery and Apps]
- Non graceful node shutdown handling. ([kubernetes/kubernetes#108486](https://github.com/kubernetes/kubernetes/pull/108486), [@sonasingh46](https://github.com/sonasingh46)) [SIG Apps, Node and Storage]
- OpenAPI V3 is turned on by default ([kubernetes/kubernetes#109031](https://github.com/kubernetes/kubernetes/pull/109031), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Scheduling, Storage and Testing]
- Promote IdentifyPodOS feature to beta. ([kubernetes/kubernetes#107859](https://github.com/kubernetes/kubernetes/pull/107859), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps, Node, Testing and Windows]
- Skip x-kubernetes-validations rules if having fundamental error against OpenAPIv3 schema. ([kubernetes/kubernetes#108859](https://github.com/kubernetes/kubernetes/pull/108859), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]
- Support for gRPC probes is now in beta. GRPCContainerProbe feature gate is enabled by default. ([kubernetes/kubernetes#108522](https://github.com/kubernetes/kubernetes/pull/108522), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG API Machinery, Apps, Node and Testing]
- The AnyVolumeDataSource feature is now beta, and the feature gate is enabled by default. In order to provide user feedback on PVCs with data sources, deployers must install the VolumePopulators CRD and the data-source-validator controller. ([kubernetes/kubernetes#108736](https://github.com/kubernetes/kubernetes/pull/108736), [@bswartz](https://github.com/bswartz)) [SIG Apps, Storage and Testing]
- The `ServerSideFieldValidation` feature has graduated to beta and is now enabled by default. Kubectl 1.24 and newer will use server-side validation instead of client-side validation when writing to API servers with the feature enabled. ([kubernetes/kubernetes#108889](https://github.com/kubernetes/kubernetes/pull/108889), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Architecture, CLI and Testing]
- The infrastructure for contextual logging is complete (feature gate implemented, JSON backend ready). ([kubernetes/kubernetes#108995](https://github.com/kubernetes/kubernetes/pull/108995), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Scheduling and Testing]
- This adds an optional `timeZone` field as part of the CronJob spec to support running cron jobs in a specific time zone. ([kubernetes/kubernetes#108032](https://github.com/kubernetes/kubernetes/pull/108032), [@deejross](https://github.com/deejross)) [SIG API Machinery and Apps]
- Add 2 new options for kube-proxy running in winkernel mode. 
  `--forward-healthcheck-vip`, if specified as true, health check traffic whose destination is service VIP will be forwarded to kube-proxy's healthcheck service. `--root-hnsendpoint-name` specifies the name of the hns endpoint for the root network namespace.
  This option enables the pass-through load balancers like Google's GCLB to correctly health check the backend services. Without this change, the health check packets is dropped, and Windows node will be considered to be unhealthy by those load balancers. ([kubernetes/kubernetes#99287](https://github.com/kubernetes/kubernetes/pull/99287), [@anfernee](https://github.com/anfernee)) [SIG API Machinery, Cloud Provider, Network, Testing and Windows]
- Added CEL runtime cost calculation into CustomerResource validation. CustomerResource validation will fail if runtime cost exceeds the budget. ([kubernetes/kubernetes#108482](https://github.com/kubernetes/kubernetes/pull/108482), [@cici37](https://github.com/cici37)) [SIG API Machinery]
- CRD writes will generate validation errors if a CEL validation rule references the identifier "oldSelf" on a part of the schema that does not support it. ([kubernetes/kubernetes#108013](https://github.com/kubernetes/kubernetes/pull/108013), [@benluddy](https://github.com/benluddy)) [SIG API Machinery]
- Feature of `DefaultPodTopologySpread` is graduated to GA ([kubernetes/kubernetes#108278](https://github.com/kubernetes/kubernetes/pull/108278), [@kerthcet](https://github.com/kerthcet)) [SIG Scheduling]
- Feature of `PodOverhead` is graduated to GA ([kubernetes/kubernetes#108441](https://github.com/kubernetes/kubernetes/pull/108441), [@pacoxu](https://github.com/pacoxu)) [SIG API Machinery, Apps, Node and Scheduling]
- Fixes a regression in v1beta1 PodDisruptionBudget handling of "strategic merge patch"-type API requests for the `selector` field. Prior to 1.21, these requests would merge `matchLabels` content and replace `matchExpressions` content. In 1.21, patch requests touching the `selector` field started replacing the entire selector. This is consistent with server-side apply and the v1 PodDisruptionBudget behavior, but should not have been changed for v1beta1. ([kubernetes/kubernetes#108138](https://github.com/kubernetes/kubernetes/pull/108138), [@liggitt](https://github.com/liggitt)) [SIG Apps, Auth and Testing]
- Kube-apiserver: --audit-log-version and --audit-webhook-version now only support the default value of audit.k8s.io/v1. The v1alpha1 and v1beta1 audit log versions, deprecated since 1.13, have been removed. ([kubernetes/kubernetes#108092](https://github.com/kubernetes/kubernetes/pull/108092), [@carlory](https://github.com/carlory)) [SIG API Machinery, Auth and Testing]
- Pod-affinity namespace selector and cross-namespace quota graduated to GA. The feature gate PodAffinityNamespaceSelector is locked and will be removed in 1.26. ([kubernetes/kubernetes#108136](https://github.com/kubernetes/kubernetes/pull/108136), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps, Scheduling and Testing]
- Suspend job to GA. The feature gate SuspendJob is locked and will be removed in 1.26. ([kubernetes/kubernetes#108129](https://github.com/kubernetes/kubernetes/pull/108129), [@ahg-g](https://github.com/ahg-g)) [SIG Apps and Testing]
- The CertificateSigningRequest `spec.expirationSeconds` API field has graduated to GA. The `CSRDuration` feature gate for the field is now unconditionally enabled and will be removed in 1.26. ([kubernetes/kubernetes#108782](https://github.com/kubernetes/kubernetes/pull/108782), [@cfryanr](https://github.com/cfryanr)) [SIG API Machinery, Apps, Auth, Instrumentation and Testing]
- TopologySpreadConstraints includes minDomains field to limit the minimum number of topology domains. ([kubernetes/kubernetes#107674](https://github.com/kubernetes/kubernetes/pull/107674), [@sanposhiho](https://github.com/sanposhiho)) [SIG API Machinery, Apps and Scheduling]
- CRD deep copies should no longer contain shallow copies of JSONSchemaProps.XValidations. ([kubernetes/kubernetes#107956](https://github.com/kubernetes/kubernetes/pull/107956), [@benluddy](https://github.com/benluddy)) [SIG API Machinery]
- Feature of `NonPreemptingPriority` is graduated  to GA ([kubernetes/kubernetes#107432](https://github.com/kubernetes/kubernetes/pull/107432), [@denkensk](https://github.com/denkensk)) [SIG Apps, Scheduling and Testing]
- Fix OpenAPI serialization of the x-kubernetes-validations field ([kubernetes/kubernetes#107970](https://github.com/kubernetes/kubernetes/pull/107970), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- Kube-apiserver: the `metadata.selfLink` field can no longer be populated by kube-apiserver; it was deprecated in 1.16 and has not been populated by default in 1.20+. ([kubernetes/kubernetes#107527](https://github.com/kubernetes/kubernetes/pull/107527), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps, Auth, Autoscaling, CLI, Cloud Provider, Network, Scheduling, Storage and Testing]
- Add a new metric `webhook_fail_open_count` to monitor webhooks that fail open ([kubernetes/kubernetes#107171](https://github.com/kubernetes/kubernetes/pull/107171), [@ltagliamonte-dd](https://github.com/ltagliamonte-dd)) [SIG API Machinery and Instrumentation]
- Fix failed flushing logs in defer function when kubelet cmd exit 1. ([kubernetes/kubernetes#104774](https://github.com/kubernetes/kubernetes/pull/104774), [@kerthcet](https://github.com/kerthcet)) [SIG Node and Scheduling]
- Rename metrics `evictions_number` to `evictions_total` and mark it as stable. The original `evictions_number` metrics name is marked as "Deprecated" and will be removed in kubernetes 1.23 ([kubernetes/kubernetes#106366](https://github.com/kubernetes/kubernetes/pull/106366), [@cyclinder](https://github.com/cyclinder)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- The `ServiceLBNodePortControl` feature graduates to GA. The feature gate will be removed in 1.26. ([kubernetes/kubernetes#107027](https://github.com/kubernetes/kubernetes/pull/107027), [@uablrek](https://github.com/uablrek)) [SIG Network and Testing]
- The feature DynamicKubeletConfig is removed from the kubelet. ([kubernetes/kubernetes#106932](https://github.com/kubernetes/kubernetes/pull/106932), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Apps, Auth, Instrumentation, Node and Testing]
- Update default API priority-and-fairness config to avoid endpoint/configmaps operations from controller-manager to all match leader-election priority level. ([kubernetes/kubernetes#106725](https://github.com/kubernetes/kubernetes/pull/106725), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]


# v23.6.0

Kubernetes API Version: v1.23.6

### API Change
- Omits alpha-level enums from the static openapi file captured in api/openapi-spec ([kubernetes/kubernetes#109179](https://github.com/kubernetes/kubernetes/pull/109179), [@liggitt](https://github.com/liggitt)) [SIG Apps and Auth]
- Fixes a regression in v1beta1 PodDisruptionBudget handling of "strategic merge patch"-type API requests for the `selector` field. Prior to 1.21, these requests would merge `matchLabels` content and replace `matchExpressions` content. In 1.21, patch requests touching the `selector` field started replacing the entire selector. This is consistent with server-side apply and the v1 PodDisruptionBudget behavior, but should not have been changed for v1beta1. ([kubernetes/kubernetes#108139](https://github.com/kubernetes/kubernetes/pull/108139), [@liggitt](https://github.com/liggitt)) [SIG Auth and Testing]


# v23.3.0

Kubernetes API Version: v1.23.4


# v23.3.0b1

Kubernetes API Version: v1.23.4

### API Change
- Fix OpenAPI serialization of the x-kubernetes-validations field ([kubernetes/kubernetes#108030](https://github.com/kubernetes/kubernetes/pull/108030), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]


# v23.3.0a1

Kubernetes API Version: v1.23.3

### API Change
- A new field `omitManagedFields` has been added to both `audit.Policy` and `audit.PolicyRule` 
  so cluster operators can opt in to omit managed fields of the request and response bodies from 
  being written to the API audit log. ([kubernetes/kubernetes#94986](https://github.com/kubernetes/kubernetes/pull/94986), [@tkashem](https://github.com/tkashem)) [SIG API Machinery, Auth, Cloud Provider and Testing]
- A small regression in Service updates was fixed. The circumstances are so unlikely that probably nobody would ever hit it. ([kubernetes/kubernetes#104601](https://github.com/kubernetes/kubernetes/pull/104601), [@thockin](https://github.com/thockin))
- Added a feature gate `StatefulSetAutoDeletePVC`, which allows PVCs automatically created for StatefulSet pods to be automatically deleted. ([kubernetes/kubernetes#99728](https://github.com/kubernetes/kubernetes/pull/99728), [@mattcary](https://github.com/mattcary))
- Client-go impersonation config can specify a UID to pass impersonated uid information through in requests. ([kubernetes/kubernetes#104483](https://github.com/kubernetes/kubernetes/pull/104483), [@margocrawf](https://github.com/margocrawf))
- Create HPA v2 from v2beta2 with some fields changed. ([kubernetes/kubernetes#102534](https://github.com/kubernetes/kubernetes/pull/102534), [@wangyysde](https://github.com/wangyysde)) [SIG API Machinery, Apps, Auth, Autoscaling and Testing]
- Ephemeral containers graduated to beta and are now available by default. ([kubernetes/kubernetes#105405](https://github.com/kubernetes/kubernetes/pull/105405), [@verb](https://github.com/verb))
- Fix kube-proxy regression on UDP services because the logic to detect stale connections was not considering if the endpoint was ready. ([kubernetes/kubernetes#106163](https://github.com/kubernetes/kubernetes/pull/106163), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Contributor Experience, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- If a conflict occurs when creating an object with `generateName`, the server now returns an "AlreadyExists" error with a retry option. ([kubernetes/kubernetes#104699](https://github.com/kubernetes/kubernetes/pull/104699), [@vincepri](https://github.com/vincepri))
- Implement support for recovering from volume expansion failures ([kubernetes/kubernetes#106154](https://github.com/kubernetes/kubernetes/pull/106154), [@gnufied](https://github.com/gnufied)) [SIG API Machinery, Apps and Storage]
- In kubelet, log verbosity and flush frequency can also be configured via the configuration file and not just via command line flags. In other commands (kube-apiserver, kube-controller-manager), the flags are listed in the "Logs flags" group and not under "Global" or "Misc". The type for `-vmodule` was made a bit more descriptive (`pattern=N,...` instead of `moduleSpec`). ([kubernetes/kubernetes#106090](https://github.com/kubernetes/kubernetes/pull/106090), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, CLI, Cluster Lifecycle, Instrumentation, Node and Scheduling]
- Introduce `OS` field in the PodSpec ([kubernetes/kubernetes#104693](https://github.com/kubernetes/kubernetes/pull/104693), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Introduce `v1beta3` API for scheduler. This version 
  - increases the weight of user specifiable priorities.
  The weights of following priority plugins are increased
    - `TaintTolerations` to 3 - as leveraging node tainting to group nodes in the cluster is becoming a widely-adopted practice
    - `NodeAffinity` to 2
    - `InterPodAffinity` to 2
  
  - Won't have `HealthzBindAddress`, `MetricsBindAddress` fields ([kubernetes/kubernetes#104251](https://github.com/kubernetes/kubernetes/pull/104251), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Introduce v1beta2 for Priority and Fairness with no changes in API spec. ([kubernetes/kubernetes#104399](https://github.com/kubernetes/kubernetes/pull/104399), [@tkashem](https://github.com/tkashem))
- JSON log output is configurable and now supports writing info messages to stdout and error messages to stderr. Info messages can be buffered in memory. The default is to write both to stdout without buffering, as before. ([kubernetes/kubernetes#104873](https://github.com/kubernetes/kubernetes/pull/104873), [@pohly](https://github.com/pohly))
- JobTrackingWithFinalizers graduates to beta. Feature is enabled by default. ([kubernetes/kubernetes#105687](https://github.com/kubernetes/kubernetes/pull/105687), [@alculquicondor](https://github.com/alculquicondor))
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums. ([kubernetes/kubernetes#104969](https://github.com/kubernetes/kubernetes/pull/104969), [@liggitt](https://github.com/liggitt))
- Kube-apiserver: The `rbac.authorization.k8s.io/v1alpha1` API version is removed; use the `rbac.authorization.k8s.io/v1` API, available since v1.8. The `scheduling.k8s.io/v1alpha1` API version is removed; use the `scheduling.k8s.io/v1` API, available since v1.14. ([kubernetes/kubernetes#104248](https://github.com/kubernetes/kubernetes/pull/104248), [@liggitt](https://github.com/liggitt))
- Kube-scheduler: support for configuration file version `v1beta1` is removed. Update configuration files to v1beta2(xref: https://github.com/kubernetes/enhancements/issues/2901) or v1beta3 before upgrading to 1.23. ([kubernetes/kubernetes#104782](https://github.com/kubernetes/kubernetes/pull/104782), [@kerthcet](https://github.com/kerthcet))
- KubeSchedulerConfiguration provides a new field `MultiPoint` which will register a plugin for all valid extension points ([kubernetes/kubernetes#105611](https://github.com/kubernetes/kubernetes/pull/105611), [@damemi](https://github.com/damemi)) [SIG Scheduling and Testing]
- Kubelet should reject pods whose OS doesn't match the node's OS label. ([kubernetes/kubernetes#105292](https://github.com/kubernetes/kubernetes/pull/105292), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps and Node]
- Kubelet: turn the KubeletConfiguration v1beta1 `ResolverConfig` field from a `string` to `*string`. ([kubernetes/kubernetes#104624](https://github.com/kubernetes/kubernetes/pull/104624), [@Haleygo](https://github.com/Haleygo))
- Kubernetes is now built using go 1.17. ([kubernetes/kubernetes#103692](https://github.com/kubernetes/kubernetes/pull/103692), [@justaugustus](https://github.com/justaugustus))
- Performs strict server side schema validation requests via the `fieldValidation=[Strict,Warn,Ignore]`. ([kubernetes/kubernetes#105916](https://github.com/kubernetes/kubernetes/pull/105916), [@kevindelgado](https://github.com/kevindelgado))
- Promote `IPv6DualStack` feature to stable.
  Controller Manager flags for the node IPAM controller have slightly changed:
  1. When configuring a dual-stack cluster, the user must specify both `--node-cidr-mask-size-ipv4` and `--node-cidr-mask-size-ipv6` to set the per-node IP mask sizes, instead of the previous `--node-cidr-mask-size` flag.
  2. The `--node-cidr-mask-size` flag is mutually exclusive with `--node-cidr-mask-size-ipv4` and `--node-cidr-mask-size-ipv6`.
  3. Single-stack clusters do not need to change, but may choose to use the more specific flags.  Users can use either the older `--node-cidr-mask-size` flag or one of the newer `--node-cidr-mask-size-ipv4` or `--node-cidr-mask-size-ipv6` flags to configure the per-node IP mask size, provided that the flag's IP family matches the cluster's IP family (--cluster-cidr). ([kubernetes/kubernetes#104691](https://github.com/kubernetes/kubernetes/pull/104691), [@khenidak](https://github.com/khenidak))
- Remove `NodeLease` feature gate that was graduated and locked to stable in 1.17 release. ([kubernetes/kubernetes#105222](https://github.com/kubernetes/kubernetes/pull/105222), [@cyclinder](https://github.com/cyclinder))
- Removed deprecated `--seccomp-profile-root`/`seccompProfileRoot` config. ([kubernetes/kubernetes#103941](https://github.com/kubernetes/kubernetes/pull/103941), [@saschagrunert](https://github.com/saschagrunert))
- Since golang 1.17 both net.ParseIP and net.ParseCIDR rejects leading zeros in the dot-decimal notation of IPv4 addresses,
  Kubernetes will keep allowing leading zeros on IPv4 address to not break the compatibility.
  IMPORTANT: Kubernetes interprets leading zeros on IPv4 addresses as decimal, users must not rely on parser alignment to not being impacted by the associated security advisory:
  CVE-2021-29923 golang standard library "net" - Improper Input Validation of octal literals in golang 1.16.2 and below standard library "net" results in indeterminate SSRF & RFI vulnerabilities.
  Reference: https://nvd.nist.gov/vuln/detail/CVE-2021-29923 ([kubernetes/kubernetes#104368](https://github.com/kubernetes/kubernetes/pull/104368), [@aojea](https://github.com/aojea))
- StatefulSet `minReadySeconds` is promoted to beta. ([kubernetes/kubernetes#104045](https://github.com/kubernetes/kubernetes/pull/104045), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Support pod priority based node graceful shutdown. ([kubernetes/kubernetes#102915](https://github.com/kubernetes/kubernetes/pull/102915), [@wzshiming](https://github.com/wzshiming))
- The "Generic Ephemeral Volume" feature graduates to GA. It is now enabled unconditionally. ([kubernetes/kubernetes#105609](https://github.com/kubernetes/kubernetes/pull/105609), [@pohly](https://github.com/pohly))
- The Kubelet's `--register-with-taints` option is now available via the Kubelet config file field registerWithTaints ([kubernetes/kubernetes#105437](https://github.com/kubernetes/kubernetes/pull/105437), [@cmssczy](https://github.com/cmssczy)) [SIG Node and Scalability]
- The `CSIDriver.Spec.StorageCapacity` can now be modified. ([kubernetes/kubernetes#101789](https://github.com/kubernetes/kubernetes/pull/101789), [@pohly](https://github.com/pohly))
- The `CSIVolumeFSGroupPolicy` feature has moved from beta to GA. ([kubernetes/kubernetes#105940](https://github.com/kubernetes/kubernetes/pull/105940), [@dobsonj](https://github.com/dobsonj))
- The `IngressClass.Spec.Parameters.Namespace` field is now GA. ([kubernetes/kubernetes#104636](https://github.com/kubernetes/kubernetes/pull/104636), [@hbagdi](https://github.com/hbagdi))
- The `Service.spec.ipFamilyPolicy` field is now *required* in order to create or update a Service as dual-stack.  This is a breaking change from the beta behavior.  Previously the server would try to infer the value of that field from either `ipFamilies` or `clusterIPs`, but that caused ambiguity on updates.  Users who want a dual-stack Service MUST specify `ipFamilyPolicy` as either "PreferDualStack" or "RequireDualStack". ([kubernetes/kubernetes#96684](https://github.com/kubernetes/kubernetes/pull/96684), [@thockin](https://github.com/thockin))
- The `TTLAfterFinished` feature gate is now GA and enabled by default. ([kubernetes/kubernetes#105219](https://github.com/kubernetes/kubernetes/pull/105219), [@sahilvv](https://github.com/sahilvv))
- The `kube-controller-manager` supports `--concurrent-ephemeralvolume-syncs` flag to set the number of ephemeral volume controller workers. ([kubernetes/kubernetes#102981](https://github.com/kubernetes/kubernetes/pull/102981), [@SataQiu](https://github.com/SataQiu))
- The legacy scheduler policy config is removed in v1.23, the associated flags `policy-config-file`, `policy-configmap`, `policy-configmap-namespace` and `use-legacy-policy-config` are also removed. Migrate to Component Config instead, see https://kubernetes.io/docs/reference/scheduling/config/ for details. ([kubernetes/kubernetes#105424](https://github.com/kubernetes/kubernetes/pull/105424), [@kerthcet](https://github.com/kerthcet))
- Track the number of Pods with a Ready condition in Job status. The feature is alpha and needs the feature gate JobReadyPods to be enabled. ([kubernetes/kubernetes#104915](https://github.com/kubernetes/kubernetes/pull/104915), [@alculquicondor](https://github.com/alculquicondor))
- Users of `LogFormatRegistry` in component-base must update their code to use the logr v1.0.0 API. The JSON log output now uses the format from go-logr/zapr (no `v` field for error messages, additional information for invalid calls) and has some fixes (correct source code location for warnings about invalid log calls). ([kubernetes/kubernetes#104103](https://github.com/kubernetes/kubernetes/pull/104103), [@pohly](https://github.com/pohly))
- Validation rules for Custom Resource Definitions can be written in the [CEL expression language](https://github.com/google/cel-spec) using the `x-kubernetes-validations` extension in OpenAPIv3 schemas (alpha). This is gated by the alpha "CustomResourceValidationExpressions" feature gate. ([kubernetes/kubernetes#106051](https://github.com/kubernetes/kubernetes/pull/106051), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Storage and Testing]
- Add gRPC probe to Pod.Spec.Container.{Liveness,Readiness,Startup}Probe (#106463, @SergeyKanzhelev) [SIG API Machinery, Apps, CLI, Node and Testing]
- Adds a feature gate StatefulSetAutoDeletePVC, which allows PVCs automatically created for StatefulSet pods to be automatically deleted. (#99728, @mattcary) [SIG API Machinery, Apps, Auth and Testing]
- Performs strict server side schema validation requests via the `fieldValidation=[Strict,Warn,Ignore]` query parameter. (#105916, @kevindelgado) [SIG API Machinery, Apps, Auth, Cloud Provider and Testing]
- Support pod priority based node graceful shutdown (#102915, @wzshiming) [SIG Node and Testing]
- A new field `omitManagedFields` has been added to both `audit.Policy` and `audit.PolicyRule` 
  so cluster operators can opt in to omit managed fields of the request and response bodies from 
  being written to the API audit log. (#94986, @tkashem) [SIG API Machinery, Auth, Cloud Provider and Testing]
- Create HPA v2 from v2beta2 with some fields changed. (#102534, @wangyysde) [SIG API Machinery, Apps, Auth, Autoscaling and Testing]
- Fix kube-proxy regression on UDP services because the logic to detect stale connections was not considering if the endpoint was ready. (#106163, @aojea) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Contributor Experience, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- Implement support for recovering from volume expansion failures (#106154, @gnufied) [SIG API Machinery, Apps and Storage]
- In kubelet, log verbosity and flush frequency can also be configured via the configuration file and not just via command line flags. In other commands (kube-apiserver, kube-controller-manager), the flags are listed in the "Logs flags" group and not under "Global" or "Misc". The type for `-vmodule` was made a bit more descriptive (`pattern=N,...` instead of `moduleSpec`). (#106090, @pohly) [SIG API Machinery, Architecture, CLI, Cluster Lifecycle, Instrumentation, Node and Scheduling]
- IngressClass.Spec.Parameters.Namespace field is now GA. (#104636, @hbagdi) [SIG Network and Testing]
- KubeSchedulerConfiguration provides a new field `MultiPoint` which will register a plugin for all valid extension points (#105611, @damemi) [SIG Scheduling and Testing]
- Kubelet should reject pods whose OS doesn't match the node's OS label. (#105292, @ravisantoshgudimetla) [SIG Apps and Node]
- The CSIVolumeFSGroupPolicy feature has moved from beta to GA. (#105940, @dobsonj) [SIG Storage]
- The Kubelet's `--register-with-taints` option is now available via the Kubelet config file field registerWithTaints (#105437, @cmssczy) [SIG Node and Scalability]
- Validation rules for Custom Resource Definitions can be written in the [CEL expression language](https://github.com/google/cel-spec) using the `x-kubernetes-validations` extension in OpenAPIv3 schemas (alpha). This is gated by the alpha "CustomResourceValidationExpressions" feature gate. (#106051, @jpbetz) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Storage and Testing]
- #### Additional documentation e.g., KEPs (Kubernetes Enhancement Proposals), usage docs, etc.:
  
  <!--
  This section can be blank if this pull request does not require a release note.
  
  When adding links which point to resources within git repositories, like
  KEPs or supporting documentation, please reference a specific commit and avoid
  linking directly to the master branch. This ensures that links reference a
  specific point in time, rather than a document that may change over time.
  
  See here for guidance on getting permanent links to files: https://help.github.com/en/articles/getting-permanent-links-to-files
  
  Please use the following format for linking documentation:
  - [KEP]: <link>
  - [Usage]: <link>
  - [Other doc]: <link>
  --> (#104782, @kerthcet) [SIG Scheduling and Testing]
- Ephemeral containers have reached beta maturity and are now available by default. (#105405, @verb) [SIG API Machinery, Apps, Node and Testing]
- Introduce OS field in the Pod Spec (#104693, @ravisantoshgudimetla) [SIG API Machinery and Apps]
- Introduce v1beta3 api for scheduler. This version 
  - increases the weight of user specifiable priorities.
  The weights of following priority plugins are increased
    - TaintTolerations to 3 - as leveraging node tainting to group nodes in the cluster is becoming a widely-adopted practice
    - NodeAffinity to 2
    - InterPodAffinity to 2
  
  - Won't have HealthzBindAddress, MetricsBindAddress fields (#104251, @ravisantoshgudimetla) [SIG Scheduling and Testing]
- JSON log output is configurable and now supports writing info messages to stdout and error messages to stderr. Info messages can be buffered in memory. The default is to write both to stdout without buffering, as before. (#104873, @pohly) [SIG API Machinery, Architecture, CLI, Cluster Lifecycle, Instrumentation, Node and Scheduling]
- JobTrackingWithFinalizers graduates to beta. Feature is enabled by default. (#105687, @alculquicondor) [SIG Apps and Testing]
- Remove NodeLease feature gate that was graduated and locked to stable in 1.17 release. (#105222, @cyclinder) [SIG Apps, Node and Testing]
- TTLAfterFinished is now GA and enabled by default (#105219, @sahilvv) [SIG API Machinery, Apps, Auth and Testing]
- The "Generic Ephemeral Volume" feature graduates to GA. It is now enabled unconditionally. (#105609, @pohly) [SIG API Machinery, Apps, Auth, Node, Scheduling, Storage and Testing]
- The legacy scheduler policy config is removed in v1.23, the associated flags policy-config-file, policy-configmap, policy-configmap-namespace and use-legacy-policy-config are also removed. Migrate to Component Config instead, see https://kubernetes.io/docs/reference/scheduling/config/ for details. (#105424, @kerthcet) [SIG Scheduling and Testing]
- Track the number of Pods with a Ready condition in Job status. The feature is alpha and needs the feature gate JobReadyPods to be enabled. (#104915, @alculquicondor) [SIG API Machinery, Apps, CLI and Testing]
- Client-go impersonation config can specify a UID to pass impersonated uid information through in requests. ([kubernetes/kubernetes#104483](https://github.com/kubernetes/kubernetes/pull/104483), [@margocrawf](https://github.com/margocrawf)) [SIG API Machinery, Auth and Testing]
- IPv6DualStack feature moved to stable.
  Controller Manager flags for the node IPAM controller have slightly changed:
  1. When configuring a dual-stack cluster, the user must specify both --node-cidr-mask-size-ipv4 and --node-cidr-mask-size-ipv6 to set the per-node IP mask sizes, instead of the previous --node-cidr-mask-size flag.
  2. The --node-cidr-mask-size flag is mutually exclusive with --node-cidr-mask-size-ipv4 and --node-cidr-mask-size-ipv6.
  3. Single-stack clusters do not need to change, but may choose to use the more specific flags.  Users can use either the older --node-cidr-mask-size flag or one of the newer --node-cidr-mask-size-ipv4 or --node-cidr-mask-size-ipv6 flags to configure the per-node IP mask size, provided that the flag's IP family matches the cluster's IP family (--cluster-cidr). ([kubernetes/kubernetes#104691](https://github.com/kubernetes/kubernetes/pull/104691), [@khenidak](https://github.com/khenidak)) [SIG API Machinery, Apps, Auth, Cloud Provider, Cluster Lifecycle, Network, Node and Testing]
- Kubelet: turn the KubeletConfiguration v1beta1 `ResolverConfig` field from a `string` to `*string`. ([kubernetes/kubernetes#104624](https://github.com/kubernetes/kubernetes/pull/104624), [@Haleygo](https://github.com/Haleygo)) [SIG Cluster Lifecycle and Node]
- A small regression in Service updates was fixed.  The circumstances are so unlikely that probably nobody would ever hit it. ([kubernetes/kubernetes#104601](https://github.com/kubernetes/kubernetes/pull/104601), [@thockin](https://github.com/thockin)) [SIG Network]
- Introduce v1beta2 for Priority and Fairness with no changes in API spec ([kubernetes/kubernetes#104399](https://github.com/kubernetes/kubernetes/pull/104399), [@tkashem](https://github.com/tkashem)) [SIG API Machinery and Testing]
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums. ([kubernetes/kubernetes#104969](https://github.com/kubernetes/kubernetes/pull/104969), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps and Network]
- Kubelet: turn the KubeletConfiguration v1beta1 `ResolverConfig` field from a `string` to `*string`. ([kubernetes/kubernetes#104624](https://github.com/kubernetes/kubernetes/pull/104624), [@Haleygo](https://github.com/Haleygo)) [SIG Cluster Lifecycle and Node]
- Kubernetes is now built using go1.17 ([kubernetes/kubernetes#103692](https://github.com/kubernetes/kubernetes/pull/103692), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scheduling, Storage and Testing]
- Removed deprecated `--seccomp-profile-root`/`seccompProfileRoot` config ([kubernetes/kubernetes#103941](https://github.com/kubernetes/kubernetes/pull/103941), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Since golang 1.17 both net.ParseIP and net.ParseCIDR rejects leading zeros in the dot-decimal notation of IPv4 addresses.
  Kubernetes will keep allowing leading zeros on IPv4 address to not break the compatibility.
  IMPORTANT: Kubernetes interprets leading zeros on IPv4 addresses as decimal, users must not rely on parser alignment to not being impacted by the associated security advisory:
  CVE-2021-29923 golang standard library "net" - Improper Input Validation of octal literals in golang 1.16.2 and below standard library "net" results in indeterminate SSRF & RFI vulnerabilities.
  Reference: https://nvd.nist.gov/vuln/detail/CVE-2021-29923 ([kubernetes/kubernetes#104368](https://github.com/kubernetes/kubernetes/pull/104368), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage and Testing]
- StatefulSet minReadySeconds is promoted to beta ([kubernetes/kubernetes#104045](https://github.com/kubernetes/kubernetes/pull/104045), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps and Testing]
- The `Service.spec.ipFamilyPolicy` field is now *required* in order to create or update a Service as dual-stack.  This is a breaking change from the beta behavior.  Previously the server would try to infer the value of that field from either `ipFamilies` or `clusterIPs`, but that caused ambiguity on updates.  Users who want a dual-stack Service MUST specify `ipFamilyPolicy` as either "PreferDualStack" or "RequireDualStack". ([kubernetes/kubernetes#96684](https://github.com/kubernetes/kubernetes/pull/96684), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Network and Testing]
- Users of LogFormatRegistry in component-base must update their code to use the logr v1.0.0 API. The JSON log output now uses the format from go-logr/zapr (no `v` field for error messages, additional information for invalid calls) and has some fixes (correct source code location for warnings about invalid log calls). ([kubernetes/kubernetes#104103](https://github.com/kubernetes/kubernetes/pull/104103), [@pohly](https://github.com/pohly)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation and Storage]
- When creating an object with generateName, if a conflict occurs the server now returns an AlreadyExists error with a retry option. ([kubernetes/kubernetes#104699](https://github.com/kubernetes/kubernetes/pull/104699), [@vincepri](https://github.com/vincepri)) [SIG API Machinery]
- CSIDriver.Spec.StorageCapacity can now be modified. ([kubernetes/kubernetes#101789](https://github.com/kubernetes/kubernetes/pull/101789), [@pohly](https://github.com/pohly)) [SIG Storage]
- Kube-apiserver: The `rbac.authorization.k8s.io/v1alpha1` API version is removed; use the `rbac.authorization.k8s.io/v1` API, available since v1.8. The `scheduling.k8s.io/v1alpha1` API version is removed; use the `scheduling.k8s.io/v1` API, available since v1.14. ([kubernetes/kubernetes#104248](https://github.com/kubernetes/kubernetes/pull/104248), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Network and Testing]
- Kube-controller-manager supports '--concurrent-ephemeralvolume-syncs' flag to set the number of ephemeral volume controller workers. ([kubernetes/kubernetes#102981](https://github.com/kubernetes/kubernetes/pull/102981), [@SataQiu](https://github.com/SataQiu)) [SIG API Machinery and Apps]


# v22.6.0

Kubernetes API Version: v1.22.6

### Bug or Regression
- Notable feature additions for async creation of Custom resources using dynamic Client (#1697, @venukarnati92)

### Feature
- Add `utils.create_from_directory` for creating all yaml files in a directory (#1683, @dingyiyi0226)

# v22.6.0b1

Kubernetes API Version: v1.22.6

### Feature
- Add `utils.create_from_directory` for creating all yaml files in a directory (#1683, @dingyiyi0226)

# v22.6.0a1

Kubernetes API Version: v1.22.6

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104988, @liggitt) [SIG API Machinery, Apps and Network]
- A new score extension for NodeResourcesFit plugin that merges the functionality of `NodeResourcesLeastAllocated`, `NodeResourcesMostAllocated`, `RequestedToCapacityRatio` plugins, which are marked as deprecated as of v1beta2. In v1beta1, the three plugins can still be used in v1beta1 but not at the same time with the score extension of `NodeResourcesFit`. ([kubernetes/kubernetes#101822](https://github.com/kubernetes/kubernetes/pull/101822), [@yuzhiquan](https://github.com/yuzhiquan))
- A value of `Auto` is now a valid for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott))
- Add `DataSourceRef` alpha field to PVC spec, which allows contents other than `PVCs` and `VolumeSnapshots` to be data sources. ([kubernetes/kubernetes#103276](https://github.com/kubernetes/kubernetes/pull/103276), [@bswartz](https://github.com/bswartz))
- Add `PersistentVolumeClaimDeletePoilcy` to StatefulSet API. ([kubernetes/kubernetes#99378](https://github.com/kubernetes/kubernetes/pull/99378), [@mattcary](https://github.com/mattcary))
- Add a new Priority and Fairness rule that exempts all probes (`/readyz`, `/healthz`, `/livez`) to prevent restarting of healthy `kube-apiserver` instance by kubelet. ([kubernetes/kubernetes#100678](https://github.com/kubernetes/kubernetes/pull/100678), [@tkashem](https://github.com/tkashem))
- Add alpha support for HostProcess containers on Windows ([kubernetes/kubernetes#99576](https://github.com/kubernetes/kubernetes/pull/99576), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Node, Testing and Windows]
- Add distributed tracing to the `kube-apiserver`. It is can be enabled with the feature gate `APIServerTracing` ([kubernetes/kubernetes#94942](https://github.com/kubernetes/kubernetes/pull/94942), [@dashpole](https://github.com/dashpole))
- Add three metrics to the job controller to monitor if a job works in healthy condition.
  `IndexedJob` has been promoted to Beta. ([kubernetes/kubernetes#101292](https://github.com/kubernetes/kubernetes/pull/101292), [@AliceZhang2016](https://github.com/AliceZhang2016))
- Added field `.status.uncountedTerminatedPods` to the Job resource. This field is used by the job controller to keep track of finished pods before adding them to the Job status counters. Pods created by the job controller get the finalizer `batch.kubernetes.io/job-tracking`
  Jobs that are tracked using this mechanism get the annotation `batch.kubernetes.io/job-tracking`. This is a temporary measure. Two releases after this feature graduates to beta, the annotation won't be added to Jobs anymore. ([kubernetes/kubernetes#98817](https://github.com/kubernetes/kubernetes/pull/98817), [@alculquicondor](https://github.com/alculquicondor))
- Added new kubelet alpha feature `SeccompDefault`. This feature enables falling back to
  the `RuntimeDefault` (former `runtime/default`) seccomp profile if nothing else is specified
  in the pod/container `SecurityContext` or the pod annotation level. To use the feature, enable
  the feature gate as well as set the kubelet configuration option `SeccompDefault`
  (`--seccomp-default`) to `true`. ([kubernetes/kubernetes#101943](https://github.com/kubernetes/kubernetes/pull/101943), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Adds the `ReadWriteOncePod` access mode for `PersistentVolumes` and `PersistentVolumeClaims`. Restricts volume access to a single pod on a single node. ([kubernetes/kubernetes#102028](https://github.com/kubernetes/kubernetes/pull/102028), [@chrishenzie](https://github.com/chrishenzie))
- Alpha swap support can now be enabled on Kubernetes nodes with the `NodeSwapEnabled` feature flag. See [KEP-2400](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/2400-node-swap/README.md#design-details) for details. ([kubernetes/kubernetes#102823](https://github.com/kubernetes/kubernetes/pull/102823), [@ehashman](https://github.com/ehashman))
- Because of the implementation logic of `time.Format` in golang, the displayed time zone is not consistent. ([kubernetes/kubernetes#102366](https://github.com/kubernetes/kubernetes/pull/102366), [@cndoit18](https://github.com/cndoit18))
- Corrected the documentation for escaping dollar signs in a container's env, command and args property. ([kubernetes/kubernetes#101916](https://github.com/kubernetes/kubernetes/pull/101916), [@MartinKanters](https://github.com/MartinKanters)) [SIG Apps]
- Enable `MaxSurge` for `DaemonSet` by default. ([kubernetes/kubernetes#101742](https://github.com/kubernetes/kubernetes/pull/101742), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Enforce the `ReadWriteOncePod` PVC access mode during scheduling ([kubernetes/kubernetes#103082](https://github.com/kubernetes/kubernetes/pull/103082), [@chrishenzie](https://github.com/chrishenzie))
- Ephemeral containers are now allowed to configure a `securityContext` that differs from that of the Pod. Cluster administrators should ensure that security policy controllers support `EphemeralContainers` before enabling this feature in clusters. ([kubernetes/kubernetes#99023](https://github.com/kubernetes/kubernetes/pull/99023), [@verb](https://github.com/verb))
- Exec plugin authors can override default handling of standard input via new `interactiveMode` kubeconfig field. ([kubernetes/kubernetes#99310](https://github.com/kubernetes/kubernetes/pull/99310), [@ankeesler](https://github.com/ankeesler))
- If someone had the `ProbeTerminationGracePeriod` alpha feature enabled in 1.21, they should update/delete any workloads/pods with probe `terminationGracePeriods` < 1 before upgrading ([kubernetes/kubernetes#103245](https://github.com/kubernetes/kubernetes/pull/103245), [@wzshiming](https://github.com/wzshiming))
- Improved parsing of label selectors ([kubernetes/kubernetes#102188](https://github.com/kubernetes/kubernetes/pull/102188), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery]
- Introduce `minReadySeconds` api to the `StatefulSets`. ([kubernetes/kubernetes#100842](https://github.com/kubernetes/kubernetes/pull/100842), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla))
- Introducing Memory quality of service support with `cgroups v2 (Alpha)`. The `MemoryQoS` feature is now in Alpha. This allows `kubelet` running with `cgroups v2` to set memory QoS at container, pod and QoS level to protect and guarantee better memory quality. This feature can be enabled through feature gate Memory QoS. ([kubernetes/kubernetes#102970](https://github.com/kubernetes/kubernetes/pull/102970), [@borgerli](https://github.com/borgerli))
- Kube API server accepts `Impersonate-Uid` header to impersonate a user with a specific UID, in the same way that you can currently use `Impersonate-User`, `Impersonate-Group` and `Impersonate-Extra`. ([kubernetes/kubernetes#99961](https://github.com/kubernetes/kubernetes/pull/99961), [@margocrawf](https://github.com/margocrawf))
- Kube-apiserver: `--service-account-issuer` can be specified multiple times now, to enable non-disruptive change of issuer. ([kubernetes/kubernetes#101155](https://github.com/kubernetes/kubernetes/pull/101155), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Node and Testing]
- Kube-controller-manager: the `--horizontal-pod-autoscaler-use-rest-clients` flag and Heapster support in the horizontal pod autoscaler, deprecated since 1.12, is removed. ([kubernetes/kubernetes#90368](https://github.com/kubernetes/kubernetes/pull/90368), [@serathius](https://github.com/serathius))
- Kube-scheduler: a plugin enabled in a v1beta2 configuration file takes precedence over the default configuration for that plugin. This simplifies enabling default plugins with custom configuration without needing to explicitly disable those default plugins. ([kubernetes/kubernetes#99582](https://github.com/kubernetes/kubernetes/pull/99582), [@chendave](https://github.com/chendave))
- New `node-high` priority-level has been added to Suggested API Priority and ([kubernetes/kubernetes#101151](https://github.com/kubernetes/kubernetes/pull/101151), [@mborsz](https://github.com/mborsz))
- NodeSwapEnabled feature flag was renamed to NodeSwap
  
  The flag was only available in the 1.22.0-beta.1 release, and the new flag should be used going forward. ([kubernetes/kubernetes#103553](https://github.com/kubernetes/kubernetes/pull/103553), [@ehashman](https://github.com/ehashman)) [SIG Node]
- Omit comparison with boolean constant ([kubernetes/kubernetes#101523](https://github.com/kubernetes/kubernetes/pull/101523), [@chuntaochen](https://github.com/chuntaochen)) [SIG CLI and Cloud Provider]
- Removed the feature flag for probe-level termination grace period from Kubelet. If a user wants to disable this feature on already created pods, they will have to delete and recreate the pods. ([kubernetes/kubernetes#103168](https://github.com/kubernetes/kubernetes/pull/103168), [@raisaat](https://github.com/raisaat)) [SIG Apps and Node]
- Revert addition of Add `PersistentVolumeClaimDeletePoilcy` to `StatefulSet`API. ([kubernetes/kubernetes#103747](https://github.com/kubernetes/kubernetes/pull/103747), [@mattcary](https://github.com/mattcary))
- Scheduler could be configured  to consider new resources beside CPU and memory,  GPU for example, for the score plugin of `NodeResourcesBalancedAllocation`. ([kubernetes/kubernetes#101946](https://github.com/kubernetes/kubernetes/pull/101946), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Server Side Apply now treats all <Some>Selector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#97989](https://github.com/kubernetes/kubernetes/pull/97989), [@Danil-Grigorev](https://github.com/Danil-Grigorev)) [SIG API Machinery]
- Suspend Job feature graduated to beta. Added the `action` label to Job controller sync metrics `job_sync_total` and `job_sync_duration_seconds`. ([kubernetes/kubernetes#102022](https://github.com/kubernetes/kubernetes/pull/102022), [@adtac](https://github.com/adtac))
- The API documentation for the DaemonSet's `spec.updateStrategy.rollingUpdate.maxUnavailable` field was corrected to state that the value is rounded up. ([kubernetes/kubernetes#101296](https://github.com/kubernetes/kubernetes/pull/101296), [@Miciah](https://github.com/Miciah))
- The `CSIServiceAccountToken` graduates to Ga and is unconditionally enabled. ([kubernetes/kubernetes#103001](https://github.com/kubernetes/kubernetes/pull/103001), [@zshihang](https://github.com/zshihang))
- The `CertificateSigningRequest.certificates.k8s.io` API supports an optional expirationSeconds field to allow the client to request a particular duration for the issued certificate.  The default signer implementations provided by the Kubernetes controller manager will honor this field as long as it does not exceed the --cluster-signing-duration flag. ([kubernetes/kubernetes#99494](https://github.com/kubernetes/kubernetes/pull/99494), [@enj](https://github.com/enj))
- The `EndpointSlicen Mirroring controller` no longer mirrors the `last-applied-configuration` annotation created by `kubectl` to update `EndpointSlices`. ([kubernetes/kubernetes#102731](https://github.com/kubernetes/kubernetes/pull/102731), [@sharmarajdaksh](https://github.com/sharmarajdaksh))
- The `NetworkPolicyEndPort` is graduated to beta and is enabled by default. ([kubernetes/kubernetes#102834](https://github.com/kubernetes/kubernetes/pull/102834), [@rikatz](https://github.com/rikatz))
- The `PodDeletionCost` feature has been promoted to beta, and enabled by default. ([kubernetes/kubernetes#101080](https://github.com/kubernetes/kubernetes/pull/101080), [@ahg-g](https://github.com/ahg-g))
- The `Server Side Apply` treats certain structs as atomic. Meaning the entire selector field is managed by a single writer and updated together. ([kubernetes/kubernetes#100684](https://github.com/kubernetes/kubernetes/pull/100684), [@Jefftree](https://github.com/Jefftree))
- The `ServiceAppProtocol` feature gate has been removed. It reached GA in Kubernetes ([kubernetes/kubernetes#103190](https://github.com/kubernetes/kubernetes/pull/103190), [@robscott](https://github.com/robscott))
- The `TerminationGracePeriodSeconds` on pod specs and container probes should not be negative. Negative values of `TerminationGracePeriodSeconds` will be treated as the value `1s` on the delete path. Immutable field validation will be relaxed in order to update negative values. In a future release, negative values will not be permitted. ([kubernetes/kubernetes#98866](https://github.com/kubernetes/kubernetes/pull/98866), [@wzshiming](https://github.com/wzshiming))
- The `kube-scheduler` component config `v1beta2` API available
  Three scheduler plugins deprecated (`NodeLabel`, `ServiceAffinity`, `NodePreferAvoidPods`). ([kubernetes/kubernetes#99597](https://github.com/kubernetes/kubernetes/pull/99597), [@adtac](https://github.com/adtac))
- The `pod/eviction` subresource now accepts `policy/v1` eviction requests in addition to `policy/v1beta1` eviction requests ([kubernetes/kubernetes#100724](https://github.com/kubernetes/kubernetes/pull/100724), [@liggitt](https://github.com/liggitt))
- The `podAffinity`, `NamespaceSelector` and the associated `CrossNamespaceAffinity` quota scope features graduate to Beta and they are now enabled by default. ([kubernetes/kubernetes#101496](https://github.com/kubernetes/kubernetes/pull/101496), [@ahg-g](https://github.com/ahg-g))
- The `pods/ephemeralcontainers` API now returns and expects a `Pod` object instead of `EphemeralContainers`. This is incompatible with the previous alpha-level API. ([kubernetes/kubernetes#101034](https://github.com/kubernetes/kubernetes/pull/101034), [@verb](https://github.com/verb)) [SIG Apps, Auth, CLI and Testing]
- The `v1.Node` and `.status.images[].names` are  now optional. ([kubernetes/kubernetes#102159](https://github.com/kubernetes/kubernetes/pull/102159), [@roycaihw](https://github.com/roycaihw))
- The deprecated flag `--algorithm-provider` has been removed from `kube-scheduler`. Use instead `ComponentConfig` to configure the set of enabled plugins. ([kubernetes/kubernetes#102239](https://github.com/kubernetes/kubernetes/pull/102239), [@Haleygo](https://github.com/Haleygo))
- The options `--ssh-user` and `--ssh-key` are removed. They only functioned on GCE, and only in-tree. Use the apiserver network proxy instead. ([kubernetes/kubernetes#102297](https://github.com/kubernetes/kubernetes/pull/102297), [@deads2k](https://github.com/deads2k))
- Track Job completion through status and Pod finalizers, removing dependency on Pod tombstones. ([kubernetes/kubernetes#98238](https://github.com/kubernetes/kubernetes/pull/98238), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and Testing]
- Track ownership of scale subresource for all scalable resources i.e. Deployment, ReplicaSet, StatefulSet, ReplicationController, and Custom Resources. ([kubernetes/kubernetes#98377](https://github.com/kubernetes/kubernetes/pull/98377), [@nodo](https://github.com/nodo)) [SIG API Machinery and Testing]
- Revert addition of Add PersistentVolumeClaimDeletePoilcy to StatefulSet API. ([kubernetes/kubernetes#103747](https://github.com/kubernetes/kubernetes/pull/103747), [@mattcary](https://github.com/mattcary)) [SIG API Machinery and Apps]
- Added field .status.uncountedTerminatedPods to the Job resource. This field is used by the job controller to keep track of finished pods before adding them to the Job status counters.
  
  Pods created by the job controller get the finalizer batch.kubernetes.io/job-tracking
  
  Jobs that are tracked using this mechanism get the annotation batch.kubernetes.io/job-tracking. This is a temporary measure. Two releases after this feature graduates to beta, the annotation won't be added to Jobs anymore. ([kubernetes/kubernetes#98817](https://github.com/kubernetes/kubernetes/pull/98817), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and CLI]
- Ephemeral containers are now allowed to configure a securityContext that differs from that of the Pod.
  
  Cluster administrators should ensure that security policy controllers support EphemeralContainers before enabling this feature in clusters. ([kubernetes/kubernetes#99023](https://github.com/kubernetes/kubernetes/pull/99023), [@verb](https://github.com/verb)) [SIG API Machinery, Apps, Auth and Node]
- If someone had the ProbeTerminationGracePeriod alpha feature enabled in 1.21, they should update/delete any workloads/pods with probe terminationGracePeriods < 1 before upgrading ([kubernetes/kubernetes#103245](https://github.com/kubernetes/kubernetes/pull/103245), [@wzshiming](https://github.com/wzshiming)) [SIG Apps and Node]
- Introducing Memory QoS support with cgroups v2 (Alpha)
  The MemoryQoS feature is now in Alpha. This allows kubelet running with cgroups v2 to set memory QoS at container, pod and QoS level to protect and guarantee better memory quality. This feature can be enabled through feature gate MemoryQoS. ([kubernetes/kubernetes#102970](https://github.com/kubernetes/kubernetes/pull/102970), [@borgerli](https://github.com/borgerli)) [SIG Node and Storage]
- NodeSwapEnabled feature flag was renamed to NodeSwap
  
  The flag was only available in the 1.22.0-beta.1 release, and the new flag should be used going forward. ([kubernetes/kubernetes#103553](https://github.com/kubernetes/kubernetes/pull/103553), [@ehashman](https://github.com/ehashman)) [SIG Node]
- Removed the feature flag for probe-level termination grace period from Kubelet. If a user wants to disable this feature on already created pods, they will have to delete and recreate the pods. ([kubernetes/kubernetes#103168](https://github.com/kubernetes/kubernetes/pull/103168), [@raisaat](https://github.com/raisaat)) [SIG Apps and Node]
- Track Job completion through status and Pod finalizers, removing dependency on Pod tombstones. ([kubernetes/kubernetes#98238](https://github.com/kubernetes/kubernetes/pull/98238), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery, Apps, Auth and Testing]
- When using `kubectl replace` (or the equivalent API call) on a Service, the caller no longer needs to do a read-modify-write cycle to fetch the allocated values for `.spec.clusterIP` and `.spec.ports[].nodePort`.  Instead the API server will automatically carry these forward from the original object when the new object does not specify them. ([kubernetes/kubernetes#103532](https://github.com/kubernetes/kubernetes/pull/103532), [@thockin](https://github.com/thockin)) [SIG Apps and Network]
- A new score extension for NodeResourcesFit plugin that merges the functionality of NodeResourcesLeastAllocated,NodeResourcesMostAllocated,RequestedToCapacityRatio plugins, which are marked as deprecated as of v1beta2. In v1beta1, the three plugins can still be used in v1beta1 but not at the same time with the score extension of NodeResourcesFit
- Add DataSourceRef alpha field to PVC spec, which allows contents other than PVCs and VolumeSnapshots to be data sources. ([kubernetes/kubernetes#103276](https://github.com/kubernetes/kubernetes/pull/103276), [@bswartz](https://github.com/bswartz)) [SIG API Machinery, Apps and Storage]
- Add PersistentVolumeClaimDeletePoilcy to StatefulSet API. ([kubernetes/kubernetes#99378](https://github.com/kubernetes/kubernetes/pull/99378), [@mattcary](https://github.com/mattcary)) [SIG API Machinery and Apps]
- Add distributed tracing to the kube-apiserver.  It is can be enabled with the feature gate: APIServerTracing=true ([kubernetes/kubernetes#94942](https://github.com/kubernetes/kubernetes/pull/94942), [@dashpole](https://github.com/dashpole)) [SIG API Machinery, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node, Storage and Testing]
- Added new kubelet alpha feature `SeccompDefault`. This feature enables falling back to
  the `RuntimeDefault` (former `runtime/default`) seccomp profile if nothing else is specified
  in the pod/container `SecurityContext` or the pod annotation level. To use the feature, enable
  the feature gate as well as set the kubelet configuration option `SeccompDefault`
  (`--seccomp-default`) to `true`. ([kubernetes/kubernetes#101943](https://github.com/kubernetes/kubernetes/pull/101943), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Adds the ReadWriteOncePod access mode for PersistentVolumes and PersistentVolumeClaims. Restricts volume access to a single pod on a single node. ([kubernetes/kubernetes#102028](https://github.com/kubernetes/kubernetes/pull/102028), [@chrishenzie](https://github.com/chrishenzie)) [SIG Apps, CLI, Node, Scheduling and Storage]
- Alpha swap support can now be enabled on Kubernetes nodes with the NodeSwapEnabled feature flag. See <website link> for details. ([kubernetes/kubernetes#102823](https://github.com/kubernetes/kubernetes/pull/102823), [@ehashman](https://github.com/ehashman)) [SIG Node]
- CSIServiceAccountToken is GA. ([kubernetes/kubernetes#103001](https://github.com/kubernetes/kubernetes/pull/103001), [@zshihang](https://github.com/zshihang)) [SIG Auth and Storage]
- Enforce the ReadWriteOncePod PVC access mode during scheduling ([kubernetes/kubernetes#103082](https://github.com/kubernetes/kubernetes/pull/103082), [@chrishenzie](https://github.com/chrishenzie)) [SIG Apps, CLI, Node, Scheduling and Storage]
- Improved parsing of label selectors ([kubernetes/kubernetes#102188](https://github.com/kubernetes/kubernetes/pull/102188), [@alculquicondor](https://github.com/alculquicondor)) [SIG API Machinery]
- Kube API server accepts Impersonate-Uid header to impersonate a user with a specific UID, in the same way that you can currently use Impersonate-User, Impersonate-Group and Impersonate-Extra ([kubernetes/kubernetes#99961](https://github.com/kubernetes/kubernetes/pull/99961), [@margocrawf](https://github.com/margocrawf)) [SIG API Machinery, Auth and Testing]
- Kube-scheduler: a plugin enabled in a v1beta2 configuration file takes precedence over the default configuration for that plugin; this simplifies enabling default plugins with custom configuration without needing to explicitly disable those default plugins. ([kubernetes/kubernetes#99582](https://github.com/kubernetes/kubernetes/pull/99582), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Scheduler could be configured  to consider new resources beside CPU and memory,  GPU for example, for the score plugin of `NodeResourcesBalancedAllocation`. ([kubernetes/kubernetes#101946](https://github.com/kubernetes/kubernetes/pull/101946), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- Suspend Job feature graduated to beta
  Added the "action" label to Job controller sync metrics job_sync_total and job_sync_duration_seconds ([kubernetes/kubernetes#102022](https://github.com/kubernetes/kubernetes/pull/102022), [@adtac](https://github.com/adtac)) [SIG Apps, Instrumentation and Testing]
- TerminationGracePeriodSeconds on pod specs and container probes should not be negative.
  Negative values of TerminationGracePeriodSeconds will be treated as the value `1s` on the delete path.
  Immutable field validation will be relaxed in order to update negative values. 
  In a future release, negative values will not be permitted. ([kubernetes/kubernetes#98866](https://github.com/kubernetes/kubernetes/pull/98866), [@wzshiming](https://github.com/wzshiming)) [SIG API Machinery, Apps and Node]
- The API documentation for the DaemonSet's spec.updateStrategy.rollingUpdate.maxUnavailable field was corrected to state that the value is rounded up. ([kubernetes/kubernetes#101296](https://github.com/kubernetes/kubernetes/pull/101296), [@Miciah](https://github.com/Miciah)) [SIG Apps and CLI]
- The CertificateSigningRequest.certificates.k8s.io API supports an optional expirationSeconds field to allow the client to request a particular duration for the issued certificate.  The default signer implementations provided by the Kubernetes controller manager will honor this field as long as it does not exceed the --cluster-signing-duration flag. ([kubernetes/kubernetes#99494](https://github.com/kubernetes/kubernetes/pull/99494), [@enj](https://github.com/enj)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Security and Testing]
- The ServiceAppProtocol feature gate has been removed. It reached GA in Kubernetes 1.20. ([kubernetes/kubernetes#103190](https://github.com/kubernetes/kubernetes/pull/103190), [@robscott](https://github.com/robscott)) [SIG Network]
- Because of the implementation logic of time.Format in golang, the displayed time zone is not consistent ([kubernetes/kubernetes#102366](https://github.com/kubernetes/kubernetes/pull/102366), [@cndoit18](https://github.com/cndoit18)) [SIG Apps, Auth, Autoscaling, CLI, Cluster Lifecycle, Instrumentation, Network, Node and Testing]
- Endpoint slices mirroring controller no longer mirrors the last-applied-configuration annotation created by kubectl to updated endpoint slices ([kubernetes/kubernetes#102731](https://github.com/kubernetes/kubernetes/pull/102731), [@sharmarajdaksh](https://github.com/sharmarajdaksh)) [SIG API Machinery, Apps, Cloud Provider, Network, Release, Scheduling, Storage and Testing]
- Exec plugin authors can override default handling of standard input via new interactiveMode kubeconfig field ([kubernetes/kubernetes#99310](https://github.com/kubernetes/kubernetes/pull/99310), [@ankeesler](https://github.com/ankeesler)) [SIG API Machinery, Auth, CLI and Testing]
- Kube-scheduler component config v1beta2 API available
  Three scheduler plugins deprecated (NodeLabel, ServiceAffinity, NodePreferAvoidPods) ([kubernetes/kubernetes#99597](https://github.com/kubernetes/kubernetes/pull/99597), [@adtac](https://github.com/adtac)) [SIG Scheduling]
- Network Policy EndPort is graduated to beta and is enabled by default ([kubernetes/kubernetes#102834](https://github.com/kubernetes/kubernetes/pull/102834), [@rikatz](https://github.com/rikatz)) [SIG Network]
- --ssh-user and --ssh-key options are removed.  They only functioned on GCE, and only in-tree.  Use the apiserver network proxy instead. ([kubernetes/kubernetes#102297](https://github.com/kubernetes/kubernetes/pull/102297), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Cloud Provider and Testing]
- Enable MaxSurge for DS by default ([kubernetes/kubernetes#101742](https://github.com/kubernetes/kubernetes/pull/101742), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG Apps and Testing]
- Introduce minReadySeconds api to the StatefulSets. ([kubernetes/kubernetes#100842](https://github.com/kubernetes/kubernetes/pull/100842), [@ravisantoshgudimetla](https://github.com/ravisantoshgudimetla)) [SIG API Machinery, Apps and Testing]
- Kube-controller-manger: the `--horizontal-pod-autoscaler-use-rest-clients`  flag and Heapster support in the horizontal pod autoscaler, deprecated since 1.12, is removed. ([kubernetes/kubernetes#90368](https://github.com/kubernetes/kubernetes/pull/90368), [@serathius](https://github.com/serathius)) [SIG API Machinery, Apps, Autoscaling, Cloud Provider and Instrumentation]
- The deprecated flag --algorithm-provider has been removed from kube-scheduler. Use instead ComponentConfig to configure the set of enabled plugins ([kubernetes/kubernetes#102239](https://github.com/kubernetes/kubernetes/pull/102239), [@Haleygo](https://github.com/Haleygo)) [SIG Cloud Provider and Scheduling]
- Add alpha support for HostProcess containers on Windows ([kubernetes/kubernetes#99576](https://github.com/kubernetes/kubernetes/pull/99576), [@marosset](https://github.com/marosset)) [SIG API Machinery, Apps, Node, Testing and Windows]
- Add three metrics to job controller to monitor if Job works in a healthy condition.
  IndexedJob promoted to Beta ([kubernetes/kubernetes#101292](https://github.com/kubernetes/kubernetes/pull/101292), [@AliceZhang2016](https://github.com/AliceZhang2016)) [SIG Apps, Instrumentation and Testing]
- Corrected the documentation for escaping dollar signs in a container's env, command and args property. ([kubernetes/kubernetes#101916](https://github.com/kubernetes/kubernetes/pull/101916), [@MartinKanters](https://github.com/MartinKanters)) [SIG Apps]
- Omit comparison with boolean constant ([kubernetes/kubernetes#101523](https://github.com/kubernetes/kubernetes/pull/101523), [@GreenApple10](https://github.com/GreenApple10)) [SIG CLI and Cloud Provider]
- Pod Affinity NamespaceSelector and the associated CrossNamespaceAffinity quota scope graduated to beta ([kubernetes/kubernetes#101496](https://github.com/kubernetes/kubernetes/pull/101496), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps and Testing]
- V1.Node .status.images[].names is now optional ([kubernetes/kubernetes#102159](https://github.com/kubernetes/kubernetes/pull/102159), [@roycaihw](https://github.com/roycaihw)) [SIG Apps and Node]
- "Auto" is now a valid value for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott)) [SIG Apps, Instrumentation and Network]
- Kube-apiserver: `--service-account-issuer` can be specified multiple times now, to enable non-disruptive change of issuer. ([kubernetes/kubernetes#101155](https://github.com/kubernetes/kubernetes/pull/101155), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Node and Testing]
- New "node-high" priority-level has been added to Suggested API Priority and Fairness configuration. ([kubernetes/kubernetes#101151](https://github.com/kubernetes/kubernetes/pull/101151), [@mborsz](https://github.com/mborsz)) [SIG API Machinery]
- PodDeletionCost promoted to Beta ([kubernetes/kubernetes#101080](https://github.com/kubernetes/kubernetes/pull/101080), [@ahg-g](https://github.com/ahg-g)) [SIG Apps]
- SSA treats certain structs as atomic ([kubernetes/kubernetes#100684](https://github.com/kubernetes/kubernetes/pull/100684), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Auth, Node and Storage]
- Server Side Apply now treats all <Some>Selector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#97989](https://github.com/kubernetes/kubernetes/pull/97989), [@Danil-Grigorev](https://github.com/Danil-Grigorev)) [SIG API Machinery]
- The `pods/ephemeralcontainers` API now returns and expects a `Pod` object instead of `EphemeralContainers`. This is incompatible with the previous alpha-level API. ([kubernetes/kubernetes#101034](https://github.com/kubernetes/kubernetes/pull/101034), [@verb](https://github.com/verb)) [SIG Apps, Auth, CLI and Testing]
- The pod/eviction subresource now accepts policy/v1 Eviction requests in addition to policy/v1beta1 Eviction requests ([kubernetes/kubernetes#100724](https://github.com/kubernetes/kubernetes/pull/100724), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Storage and Testing]
- Track ownership of scale subresource for all scalable resources i.e. Deployment, ReplicaSet, StatefulSet, ReplicationController, and Custom Resources. ([kubernetes/kubernetes#98377](https://github.com/kubernetes/kubernetes/pull/98377), [@nodo](https://github.com/nodo)) [SIG API Machinery and Testing]
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#100678](https://github.com/kubernetes/kubernetes/pull/100678), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]


# v21.7.0

Kubernetes API Version: v1.21.7

### Bug or Regression
- Fixed kubernetes-client/python#741, an issue which prevented Kubernetes cluster api-tokens from exec-plugin auth providers from being refreshed after expiry. (#250, @emenendez)
- Use select.poll() for exec on linux/darwin to improve scalability of WSClient (#268, @jsun-splunk)

# v21.7.0b1

Kubernetes API Version: v1.21.7


# v21.7.0a1

Kubernetes API Version: v1.21.7

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104989, @liggitt) [SIG API Machinery, Apps and Network]
- "Auto" is now a valid value for the `service.kubernetes.io/topology-aware-hints` annotation. ([kubernetes/kubernetes#100728](https://github.com/kubernetes/kubernetes/pull/100728), [@robscott](https://github.com/robscott)) [SIG Apps, Instrumentation and Network]
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101111](https://github.com/kubernetes/kubernetes/pull/101111), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- 1. PodAffinityTerm includes a namespaceSelector field to allow selecting eligible namespaces based on their labels. 
  2. A new CrossNamespacePodAffinity quota scope API that allows restricting which namespaces allowed to use PodAffinityTerm with corss-namespace reference via namespaceSelector or namespaces fields. ([kubernetes/kubernetes#98582](https://github.com/kubernetes/kubernetes/pull/98582), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps, Auth and Testing]
- Add Probe-level terminationGracePeriodSeconds field ([kubernetes/kubernetes#99375](https://github.com/kubernetes/kubernetes/pull/99375), [@ehashman](https://github.com/ehashman)) [SIG API Machinery, Apps, Node and Testing]
- Added `.spec.completionMode` field to Job, with accepted values `NonIndexed` (default) and `Indexed`. This is an alpha field and is only honored by servers with the `IndexedJob` feature gate enabled. ([kubernetes/kubernetes#98441](https://github.com/kubernetes/kubernetes/pull/98441), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- Adds support for endPort field in NetworkPolicy ([kubernetes/kubernetes#97058](https://github.com/kubernetes/kubernetes/pull/97058), [@rikatz](https://github.com/rikatz)) [SIG Apps and Network]
- CSIServiceAccountToken graduates to Beta and enabled by default. ([kubernetes/kubernetes#99298](https://github.com/kubernetes/kubernetes/pull/99298), [@zshihang](https://github.com/zshihang))
- Cluster admins can now turn off `/debug/pprof` and `/debug/flags/v` endpoint in kubelet by setting `enableProfilingHandler` and `enableDebugFlagsHandler` to `false` in the Kubelet configuration file. Options `enableProfilingHandler` and `enableDebugFlagsHandler` can be set to `true` only when `enableDebuggingHandlers` is also set to `true`. ([kubernetes/kubernetes#98458](https://github.com/kubernetes/kubernetes/pull/98458), [@SaranBalaji90](https://github.com/SaranBalaji90))
- DaemonSets accept a MaxSurge integer or percent on their rolling update strategy that will launch the updated pod on nodes and wait for those pods to go ready before marking the old out-of-date pods as deleted. This allows workloads to avoid downtime during upgrades when deployed using DaemonSets. This feature is alpha and is behind the DaemonSetUpdateSurge feature gate. ([kubernetes/kubernetes#96441](https://github.com/kubernetes/kubernetes/pull/96441), [@smarterclayton](https://github.com/smarterclayton)) [SIG Apps and Testing]
- Enable SPDY pings to keep connections alive, so that `kubectl exec` and `kubectl portforward` won't be interrupted. ([kubernetes/kubernetes#97083](https://github.com/kubernetes/kubernetes/pull/97083), [@knight42](https://github.com/knight42)) [SIG API Machinery and CLI]
- FieldManager no longer owns fields that get reset before the object is persisted (e.g. "status wiping"). ([kubernetes/kubernetes#99661](https://github.com/kubernetes/kubernetes/pull/99661), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Auth and Testing]
- Fixes server-side apply for APIService resources. ([kubernetes/kubernetes#98576](https://github.com/kubernetes/kubernetes/pull/98576), [@kevindelgado](https://github.com/kevindelgado))
- Generic ephemeral volumes are beta. ([kubernetes/kubernetes#99643](https://github.com/kubernetes/kubernetes/pull/99643), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Storage and Testing]
- Hugepages request values are limited to integer multiples of the page size. ([kubernetes/kubernetes#98515](https://github.com/kubernetes/kubernetes/pull/98515), [@lala123912](https://github.com/lala123912)) [SIG Apps]
- Implement the GetAvailableResources in the podresources API. ([kubernetes/kubernetes#95734](https://github.com/kubernetes/kubernetes/pull/95734), [@fromanirh](https://github.com/fromanirh)) [SIG Instrumentation, Node and Testing]
- IngressClass resource can now reference a resource in a specific namespace 
  for implementation-specific configuration (previously only Cluster-level resources were allowed). 
  This feature can be enabled using the IngressClassNamespacedParams feature gate. ([kubernetes/kubernetes#99275](https://github.com/kubernetes/kubernetes/pull/99275), [@hbagdi](https://github.com/hbagdi))
- Jobs API has a new `.spec.suspend` field that can be used to suspend and resume Jobs. This is an alpha field which is only honored by servers with the `SuspendJob` feature gate enabled. ([kubernetes/kubernetes#98727](https://github.com/kubernetes/kubernetes/pull/98727), [@adtac](https://github.com/adtac))
- Kubelet Graceful Node Shutdown feature graduates to Beta and enabled by default. ([kubernetes/kubernetes#99735](https://github.com/kubernetes/kubernetes/pull/99735), [@bobbypage](https://github.com/bobbypage))
- Kubernetes is now built using go1.15.7 ([kubernetes/kubernetes#98363](https://github.com/kubernetes/kubernetes/pull/98363), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Node, Release and Testing]
- Namespace API objects now have a `kubernetes.io/metadata.name` label matching their metadata.name field to allow selecting any namespace by its name using a label selector. ([kubernetes/kubernetes#96968](https://github.com/kubernetes/kubernetes/pull/96968), [@jayunit100](https://github.com/jayunit100)) [SIG API Machinery, Apps, Cloud Provider, Storage and Testing]
- One new field "InternalTrafficPolicy" in Service is added.
  It specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only.
  "Cluster" routes internal traffic to a Service to all endpoints.
  "Local" routes traffic to node-local endpoints only, and traffic is dropped if no node-local endpoints are ready.
  The default value is "Cluster". ([kubernetes/kubernetes#96600](https://github.com/kubernetes/kubernetes/pull/96600), [@maplain](https://github.com/maplain)) [SIG API Machinery, Apps and Network]
- PodDisruptionBudget API objects can now contain conditions in status. ([kubernetes/kubernetes#98127](https://github.com/kubernetes/kubernetes/pull/98127), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle and Instrumentation]
- PodSecurityPolicy only stores "generic" as allowed volume type if the GenericEphemeralVolume feature gate is enabled ([kubernetes/kubernetes#98918](https://github.com/kubernetes/kubernetes/pull/98918), [@pohly](https://github.com/pohly)) [SIG Auth and Security]
- Promote CronJobs to batch/v1 ([kubernetes/kubernetes#99423](https://github.com/kubernetes/kubernetes/pull/99423), [@soltysh](https://github.com/soltysh)) [SIG API Machinery, Apps, CLI and Testing]
- Promote Immutable Secrets/ConfigMaps feature to Stable. This allows to set `immutable` field in Secret or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#97615](https://github.com/kubernetes/kubernetes/pull/97615), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, Architecture, Node and Testing]
- Remove support for building Kubernetes with bazel. ([kubernetes/kubernetes#99561](https://github.com/kubernetes/kubernetes/pull/99561), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- Scheduler extender filter interface now can report unresolvable failed nodes in the new field `FailedAndUnresolvableNodes` of  `ExtenderFilterResult` struct. Nodes in this map will be skipped in the preemption phase. ([kubernetes/kubernetes#92866](https://github.com/kubernetes/kubernetes/pull/92866), [@cofyc](https://github.com/cofyc)) [SIG Scheduling]
- Services can specify loadBalancerClass to use a custom load balancer ([kubernetes/kubernetes#98277](https://github.com/kubernetes/kubernetes/pull/98277), [@XudongLiuHarold](https://github.com/XudongLiuHarold))
- Storage capacity tracking (= the CSIStorageCapacity feature) graduates to Beta and enabled by default, storage.k8s.io/v1alpha1/VolumeAttachment and storage.k8s.io/v1alpha1/CSIStorageCapacity objects are deprecated ([kubernetes/kubernetes#99641](https://github.com/kubernetes/kubernetes/pull/99641), [@pohly](https://github.com/pohly))
- Support for Indexed Job: a Job that is considered completed when Pods associated to indexes from 0 to (.spec.completions-1) have succeeded. ([kubernetes/kubernetes#98812](https://github.com/kubernetes/kubernetes/pull/98812), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- The BoundServiceAccountTokenVolume feature has been promoted to beta, and enabled by default.
  - This changes the tokens provided to containers at `/var/run/secrets/kubernetes.io/serviceaccount/token` to be time-limited, auto-refreshed, and invalidated when the containing pod is deleted.
  - Clients should reload the token from disk periodically (once per minute is recommended) to ensure they continue to use a valid token. `k8s.io/client-go` version v11.0.0+ and v0.15.0+ reload tokens automatically.
  - By default, injected tokens are given an extended lifetime so they remain valid even after a new refreshed token is provided. The metric `serviceaccount_stale_tokens_total` can be used to monitor for workloads that are depending on the extended lifetime and are continuing to use tokens even after a refreshed token is provided to the container. If that metric indicates no existing workloads are depending on extended lifetimes, injected token lifetime can be shortened to 1 hour by starting `kube-apiserver` with `--service-account-extend-token-expiration=false`. ([kubernetes/kubernetes#95667](https://github.com/kubernetes/kubernetes/pull/95667), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- The EndpointSlice Controllers are now GA. The `EndpointSliceController` will not populate the `deprecatedTopology` field and will only provide topology information through the `zone` and `nodeName` fields. ([kubernetes/kubernetes#99870](https://github.com/kubernetes/kubernetes/pull/99870), [@swetharepakula](https://github.com/swetharepakula))
- The Endpoints controller will now set the `endpoints.kubernetes.io/over-capacity` annotation to "warning" when an Endpoints resource contains more than 1000 addresses. In a future release, the controller will truncate Endpoints that exceed this limit. The EndpointSlice API can be used to support significantly larger number of addresses. ([kubernetes/kubernetes#99975](https://github.com/kubernetes/kubernetes/pull/99975), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The PodDisruptionBudget API has been promoted to policy/v1 with no schema changes. The only functional change is that an empty selector (`{}`) written to a policy/v1 PodDisruptionBudget now selects all pods in the namespace. The behavior of the policy/v1beta1 API remains unchanged. The policy/v1beta1 PodDisruptionBudget API is deprecated and will no longer be served in 1.25+. ([kubernetes/kubernetes#99290](https://github.com/kubernetes/kubernetes/pull/99290), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Scheduling and Testing]
- The `EndpointSlice` API is now GA. The `EndpointSlice` topology field has been removed from the GA API and will be replaced by a new per Endpoint Zone field. If the topology field was previously used, it will be converted into an annotation in the v1 Resource. The `discovery.k8s.io/v1alpha1` API is removed. ([kubernetes/kubernetes#99662](https://github.com/kubernetes/kubernetes/pull/99662), [@swetharepakula](https://github.com/swetharepakula))
- The `controller.kubernetes.io/pod-deletion-cost` annotation can be set to offer a hint on the cost of deleting a `Pod` compared to other pods belonging to the same ReplicaSet. Pods with lower deletion cost are deleted first. This is an alpha feature. ([kubernetes/kubernetes#99163](https://github.com/kubernetes/kubernetes/pull/99163), [@ahg-g](https://github.com/ahg-g))
- The kube-apiserver now resets `managedFields` that got corrupted by a mutating admission controller. ([kubernetes/kubernetes#98074](https://github.com/kubernetes/kubernetes/pull/98074), [@kwiesmueller](https://github.com/kwiesmueller))
- Topology Aware Hints are now available in alpha and can be enabled with the `TopologyAwareHints` feature gate. ([kubernetes/kubernetes#99522](https://github.com/kubernetes/kubernetes/pull/99522), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Instrumentation, Network and Testing]
- Users might specify the `kubectl.kubernetes.io/default-exec-container` annotation in a Pod to preselect container for kubectl commands. ([kubernetes/kubernetes#97099](https://github.com/kubernetes/kubernetes/pull/97099), [@pacoxu](https://github.com/pacoxu)) [SIG CLI]
- Add Probe-level terminationGracePeriodSeconds field ([kubernetes/kubernetes#99375](https://github.com/kubernetes/kubernetes/pull/99375), [@ehashman](https://github.com/ehashman)) [SIG API Machinery, Apps, Node and Testing]
- CSIServiceAccountToken is Beta now ([kubernetes/kubernetes#99298](https://github.com/kubernetes/kubernetes/pull/99298), [@zshihang](https://github.com/zshihang)) [SIG Auth, Storage and Testing]
- Discovery.k8s.io/v1beta1 EndpointSlices are deprecated in favor of discovery.k8s.io/v1, and will no longer be served in Kubernetes v1.25. ([kubernetes/kubernetes#100472](https://github.com/kubernetes/kubernetes/pull/100472), [@liggitt](https://github.com/liggitt)) [SIG Network]
- FieldManager no longer owns fields that get reset before the object is persisted (e.g. "status wiping"). ([kubernetes/kubernetes#99661](https://github.com/kubernetes/kubernetes/pull/99661), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Auth and Testing]
- Generic ephemeral volumes are beta. ([kubernetes/kubernetes#99643](https://github.com/kubernetes/kubernetes/pull/99643), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Node, Storage and Testing]
- Implement the GetAvailableResources in the podresources API. ([kubernetes/kubernetes#95734](https://github.com/kubernetes/kubernetes/pull/95734), [@fromanirh](https://github.com/fromanirh)) [SIG Instrumentation, Node and Testing]
- The Endpoints controller will now set the `endpoints.kubernetes.io/over-capacity` annotation to "warning" when an Endpoints resource contains more than 1000 addresses. In a future release, the controller will truncate Endpoints that exceed this limit. The EndpointSlice API can be used to support significantly larger number of addresses. ([kubernetes/kubernetes#99975](https://github.com/kubernetes/kubernetes/pull/99975), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The PodDisruptionBudget API has been promoted to policy/v1 with no schema changes. The only functional change is that an empty selector (`{}`) written to a policy/v1 PodDisruptionBudget now selects all pods in the namespace. The behavior of the policy/v1beta1 API remains unchanged. The policy/v1beta1 PodDisruptionBudget API is deprecated and will no longer be served in 1.25+. ([kubernetes/kubernetes#99290](https://github.com/kubernetes/kubernetes/pull/99290), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Scheduling and Testing]
- Topology Aware Hints are now available in alpha and can be enabled with the `TopologyAwareHints` feature gate. ([kubernetes/kubernetes#99522](https://github.com/kubernetes/kubernetes/pull/99522), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Instrumentation, Network and Testing]
- 1. PodAffinityTerm includes a namespaceSelector field to allow selecting eligible namespaces based on their labels. 
  2. A new CrossNamespacePodAffinity quota scope API that allows restricting which namespaces allowed to use PodAffinityTerm with corss-namespace reference via namespaceSelector or namespaces fields. ([kubernetes/kubernetes#98582](https://github.com/kubernetes/kubernetes/pull/98582), [@ahg-g](https://github.com/ahg-g)) [SIG API Machinery, Apps, Auth and Testing]
- Add a default metadata name labels for selecting any namespace by its name. ([kubernetes/kubernetes#96968](https://github.com/kubernetes/kubernetes/pull/96968), [@jayunit100](https://github.com/jayunit100)) [SIG API Machinery, Apps, Cloud Provider, Storage and Testing]
- Added `.spec.completionMode` field to Job, with accepted values `NonIndexed` (default) and `Indexed` ([kubernetes/kubernetes#98441](https://github.com/kubernetes/kubernetes/pull/98441), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- Clarified NetworkPolicy policyTypes documentation ([kubernetes/kubernetes#97216](https://github.com/kubernetes/kubernetes/pull/97216), [@joejulian](https://github.com/joejulian)) [SIG Network]
- DaemonSets accept a MaxSurge integer or percent on their rolling update strategy that will launch the updated pod on nodes and wait for those pods to go ready before marking the old out-of-date pods as deleted. This allows workloads to avoid downtime during upgrades when deployed using DaemonSets. This feature is alpha and is behind the DaemonSetUpdateSurge feature gate. ([kubernetes/kubernetes#96441](https://github.com/kubernetes/kubernetes/pull/96441), [@smarterclayton](https://github.com/smarterclayton)) [SIG Apps and Testing]
- EndpointSlice API is now GA. The EndpointSlice topology field has been removed from the GA API and will be replaced by a new per Endpoint Zone field. If the topology field was previously used, it will be converted into an annotation in the v1 Resource. The discovery.k8s.io/v1alpha1 API is removed. ([kubernetes/kubernetes#99662](https://github.com/kubernetes/kubernetes/pull/99662), [@swetharepakula](https://github.com/swetharepakula)) [SIG API Machinery, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network and Testing]
- EndpointSlice Controllers are now GA. The EndpointSlice Controller will not populate the `deprecatedTopology` field and will only provide topology information through the `zone` and `nodeName` fields. ([kubernetes/kubernetes#99870](https://github.com/kubernetes/kubernetes/pull/99870), [@swetharepakula](https://github.com/swetharepakula)) [SIG API Machinery, Apps, Auth, Network and Testing]
- IngressClass resource can now reference a resource in a specific namespace 
  for implementation-specific configuration(previously only Cluster-level resources were allowed). 
  This feature can be enabled using the IngressClassNamespacedParams feature gate. ([kubernetes/kubernetes#99275](https://github.com/kubernetes/kubernetes/pull/99275), [@hbagdi](https://github.com/hbagdi)) [SIG API Machinery, CLI and Network]
- Introduce conditions for PodDisruptionBudget ([kubernetes/kubernetes#98127](https://github.com/kubernetes/kubernetes/pull/98127), [@mortent](https://github.com/mortent)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle and Instrumentation]
- Jobs API has a new .spec.suspend field that can be used to suspend and resume Jobs ([kubernetes/kubernetes#98727](https://github.com/kubernetes/kubernetes/pull/98727), [@adtac](https://github.com/adtac)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Kubelet Graceful Node Shutdown feature is now beta. ([kubernetes/kubernetes#99735](https://github.com/kubernetes/kubernetes/pull/99735), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- Limit the quest value of hugepage to integer multiple of page size. ([kubernetes/kubernetes#98515](https://github.com/kubernetes/kubernetes/pull/98515), [@lala123912](https://github.com/lala123912)) [SIG Apps]
- One new field "InternalTrafficPolicy" in Service is added.
  It specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only.
  "Cluster" routes internal traffic to a Service to all endpoints.
  "Local" routes traffic to node-local endpoints only, and traffic is dropped if no node-local endpoints are ready.
  The default value is "Cluster". ([kubernetes/kubernetes#96600](https://github.com/kubernetes/kubernetes/pull/96600), [@maplain](https://github.com/maplain)) [SIG API Machinery, Apps and Network]
- PodSecurityPolicy only stores "generic" as allowed volume type if the GenericEphemeralVolume feature gate is enabled ([kubernetes/kubernetes#98918](https://github.com/kubernetes/kubernetes/pull/98918), [@pohly](https://github.com/pohly)) [SIG Auth and Security]
- Promote CronJobs to batch/v1 ([kubernetes/kubernetes#99423](https://github.com/kubernetes/kubernetes/pull/99423), [@soltysh](https://github.com/soltysh)) [SIG API Machinery, Apps, CLI and Testing]
- Remove support for building Kubernetes with bazel. ([kubernetes/kubernetes#99561](https://github.com/kubernetes/kubernetes/pull/99561), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Scheduling, Storage, Testing and Windows]
- Setting loadBalancerClass in load balancer type of service is available with this PR. 
  Users who want to use a custom load balancer can specify loadBalancerClass to achieve it. ([kubernetes/kubernetes#98277](https://github.com/kubernetes/kubernetes/pull/98277), [@XudongLiuHarold](https://github.com/XudongLiuHarold)) [SIG API Machinery, Apps, Cloud Provider and Network]
- Storage capacity tracking (= the CSIStorageCapacity feature) is beta, storage.k8s.io/v1alpha1/VolumeAttachment and storage.k8s.io/v1alpha1/CSIStorageCapacity objects are deprecated ([kubernetes/kubernetes#99641](https://github.com/kubernetes/kubernetes/pull/99641), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Scheduling, Storage and Testing]
- Support for Indexed Job: a Job that is considered completed when Pods associated to indexes from 0 to (.spec.completions-1) have succeeded. ([kubernetes/kubernetes#98812](https://github.com/kubernetes/kubernetes/pull/98812), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps and CLI]
- The apiserver now resets managedFields that got corrupted by a mutating admission controller. ([kubernetes/kubernetes#98074](https://github.com/kubernetes/kubernetes/pull/98074), [@kwiesmueller](https://github.com/kwiesmueller)) [SIG API Machinery and Testing]
- `controller.kubernetes.io/pod-deletion-cost` annotation can be set to offer a hint on the cost of deleting a pod compared to other pods belonging to the same ReplicaSet. Pods with lower deletion cost are deleted first. This is an alpha feature. ([kubernetes/kubernetes#99163](https://github.com/kubernetes/kubernetes/pull/99163), [@ahg-g](https://github.com/ahg-g)) [SIG Apps]
- Cluster admins can now turn off /debug/pprof and /debug/flags/v endpoint in kubelet by setting enableProfilingHandler and enableDebugFlagsHandler to false in their kubelet configuration file. enableProfilingHandler and enableDebugFlagsHandler can be set to true only when enableDebuggingHandlers is also set to true. ([kubernetes/kubernetes#98458](https://github.com/kubernetes/kubernetes/pull/98458), [@SaranBalaji90](https://github.com/SaranBalaji90)) [SIG Node]
- The BoundServiceAccountTokenVolume feature has been promoted to beta, and enabled by default.
  - This changes the tokens provided to containers at `/var/run/secrets/kubernetes.io/serviceaccount/token` to be time-limited, auto-refreshed, and invalidated when the containing pod is deleted.
  - Clients should reload the token from disk periodically (once per minute is recommended) to ensure they continue to use a valid token. `k8s.io/client-go` version v11.0.0+ and v0.15.0+ reload tokens automatically.
  - By default, injected tokens are given an extended lifetime so they remain valid even after a new refreshed token is provided. The metric `serviceaccount_stale_tokens_total` can be used to monitor for workloads that are depending on the extended lifetime and are continuing to use tokens even after a refreshed token is provided to the container. If that metric indicates no existing workloads are depending on extended lifetimes, injected token lifetime can be shortened to 1 hour by starting `kube-apiserver` with `--service-account-extend-token-expiration=false`. ([kubernetes/kubernetes#95667](https://github.com/kubernetes/kubernetes/pull/95667), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- Adds support for portRange / EndPort in Network Policy ([kubernetes/kubernetes#97058](https://github.com/kubernetes/kubernetes/pull/97058), [@rikatz](https://github.com/rikatz)) [SIG Apps and Network]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#98576](https://github.com/kubernetes/kubernetes/pull/98576), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps and Testing]
- Kubernetes is now built using go1.15.7 ([kubernetes/kubernetes#98363](https://github.com/kubernetes/kubernetes/pull/98363), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Node, Release and Testing]
- Scheduler extender filter interface now can report unresolvable failed nodes in the new field `FailedAndUnresolvableNodes` of  `ExtenderFilterResult` struct. Nodes in this map will be skipped in the preemption phase. ([kubernetes/kubernetes#92866](https://github.com/kubernetes/kubernetes/pull/92866), [@cofyc](https://github.com/cofyc)) [SIG Scheduling]
- Enable SPDY pings to keep connections alive, so that `kubectl exec` and `kubectl port-forward` won't be interrupted. ([kubernetes/kubernetes#97083](https://github.com/kubernetes/kubernetes/pull/97083), [@knight42](https://github.com/knight42)) [SIG API Machinery and CLI]
- Change the APIVersion proto name of BoundObjectRef from aPIVersion to apiVersion. ([kubernetes/kubernetes#97379](https://github.com/kubernetes/kubernetes/pull/97379), [@kebe7jun](https://github.com/kebe7jun)) [SIG Auth]
- Promote Immutable Secrets/ConfigMaps feature to Stable.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#97615](https://github.com/kubernetes/kubernetes/pull/97615), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, Architecture, Node and Testing]


# v20.13.0

Kubernetes API Version: v1.20.13


# v20.12.0b1

Kubernetes API Version: v1.20.12

### API Change
- Kube-apiserver: Fixes handling of CRD schemas containing literal null values in enums (#104990, @liggitt) [SIG API Machinery, Apps and Network]


# v20.11.0a1

Kubernetes API Version: v1.20.11

### API Change
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101112](https://github.com/kubernetes/kubernetes/pull/101112), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#100714](https://github.com/kubernetes/kubernetes/pull/100714), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps and Testing]
- Regenerate protobuf code to fix CVE-2021-3121 ([kubernetes/kubernetes#100501](https://github.com/kubernetes/kubernetes/pull/100501), [@joelsmith](https://github.com/joelsmith)) [SIG API Machinery, Apps, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node and Storage]
- Kubernetes is now built using go1.15.8 ([kubernetes/kubernetes#98962](https://github.com/kubernetes/kubernetes/pull/98962), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Release and Testing]
- `TokenRequest` and `TokenRequestProjection` features have been promoted to GA. This feature allows generating service account tokens that are not visible in Secret objects and are tied to the lifetime of a Pod object. See https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection for details on configuring and using this feature. The `TokenRequest` and `TokenRequestProjection` feature gates will be removed in v1.21.
  - kubeadm's kube-apiserver Pod manifest now includes the following flags by default "--service-account-key-file", "--service-account-signing-key-file", "--service-account-issuer". ([kubernetes/kubernetes#93258](https://github.com/kubernetes/kubernetes/pull/93258), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle, Storage and Testing]
- A new `nofuzz` go build tag now disables gofuzz support. Release binaries enable this. ([kubernetes/kubernetes#92491](https://github.com/kubernetes/kubernetes/pull/92491), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery]
- Add WindowsContainerResources and Annotations to CRI-API UpdateContainerResourcesRequest ([kubernetes/kubernetes#95741](https://github.com/kubernetes/kubernetes/pull/95741), [@katiewasnothere](https://github.com/katiewasnothere)) [SIG Node]
- Add a `serving` and `terminating` condition to the EndpointSlice API.
  `serving` tracks the readiness of endpoints regardless of their terminating state. This is distinct from `ready` since `ready` is only true when pods are not terminating. 
  `terminating` is true when an endpoint is terminating. For pods this is any endpoint with a deletion timestamp. ([kubernetes/kubernetes#92968](https://github.com/kubernetes/kubernetes/pull/92968), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps and Network]
- Add dual-stack Services (alpha).  This is a BREAKING CHANGE to an alpha API.
  It changes the dual-stack API wrt Service from a single ipFamily field to 3
  fields: ipFamilyPolicy (SingleStack, PreferDualStack, RequireDualStack),
  ipFamilies (a list of families assigned), and clusterIPs (inclusive of
  clusterIP).  Most users do not need to set anything at all, defaulting will
  handle it for them.  Services are single-stack unless the user asks for
  dual-stack.  This is all gated by the "IPv6DualStack" feature gate. ([kubernetes/kubernetes#91824](https://github.com/kubernetes/kubernetes/pull/91824), [@khenidak](https://github.com/khenidak)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Add support for hugepages to downward API ([kubernetes/kubernetes#86102](https://github.com/kubernetes/kubernetes/pull/86102), [@derekwaynecarr](https://github.com/derekwaynecarr)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Adds kubelet alpha feature, `GracefulNodeShutdown` which makes kubelet aware of node system shutdowns and result in graceful termination of pods during a system shutdown. ([kubernetes/kubernetes#96129](https://github.com/kubernetes/kubernetes/pull/96129), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- AppProtocol is now GA for Endpoints and Services. The ServiceAppProtocol feature gate will be deprecated in 1.21. ([kubernetes/kubernetes#96327](https://github.com/kubernetes/kubernetes/pull/96327), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- Automatic allocation of NodePorts for services with type LoadBalancer can now be disabled by setting the (new) parameter
  Service.spec.allocateLoadBalancerNodePorts=false. The default is to allocate NodePorts for services with type LoadBalancer which is the existing behavior. ([kubernetes/kubernetes#92744](https://github.com/kubernetes/kubernetes/pull/92744), [@uablrek](https://github.com/uablrek)) [SIG Apps and Network]
- Certain fields on  Service objects will be automatically cleared when changing the service's `type` to a mode that does not need those fields.  For example, changing from type=LoadBalancer to type=ClusterIP will clear the NodePort assignments, rather than forcing the user to clear them. ([kubernetes/kubernetes#95196](https://github.com/kubernetes/kubernetes/pull/95196), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Network and Testing]
- Document that ServiceTopology feature is required to use `service.spec.topologyKeys`. ([kubernetes/kubernetes#96528](https://github.com/kubernetes/kubernetes/pull/96528), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- EndpointSlice has a new NodeName field guarded by the EndpointSliceNodeName feature gate.
  - EndpointSlice topology field will be deprecated in an upcoming release.
  - EndpointSlice "IP" address type is formally removed after being deprecated in Kubernetes 1.17.
  - The discovery.k8s.io/v1alpha1 API is deprecated and will be removed in Kubernetes 1.21. ([kubernetes/kubernetes#96440](https://github.com/kubernetes/kubernetes/pull/96440), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps and Network]
- External facing API podresources is now available under k8s.io/kubelet/pkg/apis/ ([kubernetes/kubernetes#92632](https://github.com/kubernetes/kubernetes/pull/92632), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node and Testing]
- Fewer candidates are enumerated for preemption to improve performance in large clusters. ([kubernetes/kubernetes#94814](https://github.com/kubernetes/kubernetes/pull/94814), [@adtac](https://github.com/adtac))
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94481](https://github.com/kubernetes/kubernetes/pull/94481), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Instrumentation]
- GPU metrics provided by kubelet are now disabled by default. ([kubernetes/kubernetes#95184](https://github.com/kubernetes/kubernetes/pull/95184), [@RenaudWasTaken](https://github.com/RenaudWasTaken))
- If BoundServiceAccountTokenVolume is enabled, cluster admins can use metric `serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with flag `--service-account-extend-token-expiration=false` ([kubernetes/kubernetes#96273](https://github.com/kubernetes/kubernetes/pull/96273), [@zshihang](https://github.com/zshihang)) [SIG API Machinery and Auth]
- Introduce alpha support for exec-based container registry credential provider plugins in the kubelet. ([kubernetes/kubernetes#94196](https://github.com/kubernetes/kubernetes/pull/94196), [@andrewsykim](https://github.com/andrewsykim)) [SIG Node and Release]
- Introduces a metric source for HPAs which allows scaling based on container resource usage. ([kubernetes/kubernetes#90691](https://github.com/kubernetes/kubernetes/pull/90691), [@arjunrn](https://github.com/arjunrn)) [SIG API Machinery, Apps, Autoscaling and CLI]
- Kube-apiserver now deletes expired kube-apiserver Lease objects:
  - The feature is under feature gate `APIServerIdentity`.
  - A flag is added to kube-apiserver: `identity-lease-garbage-collection-check-period-seconds` ([kubernetes/kubernetes#95895](https://github.com/kubernetes/kubernetes/pull/95895), [@roycaihw](https://github.com/roycaihw)) [SIG API Machinery, Apps, Auth and Testing]
- Kube-controller-manager: volume plugins can be restricted from contacting local and loopback addresses by setting `--volume-host-allow-local-loopback=false`, or from contacting specific CIDR ranges by setting `--volume-host-cidr-denylist` (for example, `--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`) ([kubernetes/kubernetes#91785](https://github.com/kubernetes/kubernetes/pull/91785), [@mattcary](https://github.com/mattcary)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Migrate scheduler, controller-manager and cloud-controller-manager to use LeaseLock ([kubernetes/kubernetes#94603](https://github.com/kubernetes/kubernetes/pull/94603), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps, Cloud Provider and Scheduling]
- Modify DNS-1123 error messages to indicate that RFC 1123 is not followed exactly ([kubernetes/kubernetes#94182](https://github.com/kubernetes/kubernetes/pull/94182), [@mattfenwick](https://github.com/mattfenwick)) [SIG API Machinery, Apps, Auth, Network and Node]
- Move configurable fsgroup change policy for pods to beta ([kubernetes/kubernetes#96376](https://github.com/kubernetes/kubernetes/pull/96376), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- New flag is introduced, i.e. --topology-manager-scope=container|pod. 
  The default value is the "container" scope. ([kubernetes/kubernetes#92967](https://github.com/kubernetes/kubernetes/pull/92967), [@cezaryzukowski](https://github.com/cezaryzukowski)) [SIG Instrumentation, Node and Testing]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- NodeAffinity plugin can be configured with AddedAffinity. ([kubernetes/kubernetes#96202](https://github.com/kubernetes/kubernetes/pull/96202), [@alculquicondor](https://github.com/alculquicondor)) [SIG Node, Scheduling and Testing]
- Promote RuntimeClass feature to GA.
  Promote node.k8s.io API groups from v1beta1 to v1. ([kubernetes/kubernetes#95718](https://github.com/kubernetes/kubernetes/pull/95718), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Reminder: The labels "failure-domain.beta.kubernetes.io/zone" and "failure-domain.beta.kubernetes.io/region" are deprecated in favor of "topology.kubernetes.io/zone" and "topology.kubernetes.io/region" respectively.  All users of the "failure-domain.beta..." labels should switch to the "topology..." equivalents. ([kubernetes/kubernetes#96033](https://github.com/kubernetes/kubernetes/pull/96033), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, CLI, Cloud Provider, Network, Node, Scheduling, Storage and Testing]
- Server Side Apply now treats LabelSelector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#93901](https://github.com/kubernetes/kubernetes/pull/93901), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Storage and Testing]
- Services will now have a `clusterIPs` field to go with `clusterIP`.  `clusterIPs[0]` is a synonym for `clusterIP` and will be synchronized on create and update operations. ([kubernetes/kubernetes#95894](https://github.com/kubernetes/kubernetes/pull/95894), [@thockin](https://github.com/thockin)) [SIG Network]
- The ServiceAccountIssuerDiscovery feature gate is now Beta and enabled by default. ([kubernetes/kubernetes#91921](https://github.com/kubernetes/kubernetes/pull/91921), [@mtaufen](https://github.com/mtaufen)) [SIG Auth]
- The status of v1beta1 CRDs without "preserveUnknownFields:false" now shows a violation, "spec.preserveUnknownFields: Invalid value: true: must be false". ([kubernetes/kubernetes#93078](https://github.com/kubernetes/kubernetes/pull/93078), [@vareti](https://github.com/vareti))
- The usage of mixed protocol values in the same LoadBalancer Service is possible if the new feature gate MixedProtocolLBService is enabled. The feature gate is disabled by default. The user has to enable it for the API Server. ([kubernetes/kubernetes#94028](https://github.com/kubernetes/kubernetes/pull/94028), [@janosi](https://github.com/janosi)) [SIG API Machinery and Apps]
- This PR will introduce a feature gate CSIServiceAccountToken with two additional fields in `CSIDriverSpec`. ([kubernetes/kubernetes#93130](https://github.com/kubernetes/kubernetes/pull/93130), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Users can try the CronJob controller v2 using the feature gate. This will be the default controller in future releases. ([kubernetes/kubernetes#93370](https://github.com/kubernetes/kubernetes/pull/93370), [@alaypatel07](https://github.com/alaypatel07)) [SIG API Machinery, Apps, Auth and Testing]
- VolumeSnapshotDataSource moves to GA in 1.20 release ([kubernetes/kubernetes#95282](https://github.com/kubernetes/kubernetes/pull/95282), [@xing-yang](https://github.com/xing-yang)) [SIG Apps]
- WinOverlay feature graduated to beta ([kubernetes/kubernetes#94807](https://github.com/kubernetes/kubernetes/pull/94807), [@ksubrmnn](https://github.com/ksubrmnn)) [SIG Windows]
- API priority and fairness graduated to beta
  1.19 servers with APF turned on should not be run in a multi-server cluster with 1.20+ servers. ([kubernetes/kubernetes#96527](https://github.com/kubernetes/kubernetes/pull/96527), [@adtac](https://github.com/adtac)) [SIG API Machinery and Testing]
- Add LoadBalancerIPMode feature gate ([kubernetes/kubernetes#92312](https://github.com/kubernetes/kubernetes/pull/92312), [@Sh4d1](https://github.com/Sh4d1)) [SIG Apps, CLI, Cloud Provider and Network]
- Add WindowsContainerResources and Annotations to CRI-API UpdateContainerResourcesRequest ([kubernetes/kubernetes#95741](https://github.com/kubernetes/kubernetes/pull/95741), [@katiewasnothere](https://github.com/katiewasnothere)) [SIG Node]
- Add a 'serving' and `terminating` condition to the EndpointSlice API.
  
  `serving` tracks the readiness of endpoints regardless of their terminating state. This is distinct from `ready` since `ready` is only true when pods are not terminating. 
  `terminating` is true when an endpoint is terminating. For pods this is any endpoint with a deletion timestamp. ([kubernetes/kubernetes#92968](https://github.com/kubernetes/kubernetes/pull/92968), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps and Network]
- Add support for hugepages to downward API ([kubernetes/kubernetes#86102](https://github.com/kubernetes/kubernetes/pull/86102), [@derekwaynecarr](https://github.com/derekwaynecarr)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Adds kubelet alpha feature, `GracefulNodeShutdown` which makes kubelet aware of node system shutdowns and result in graceful termination of pods during a system shutdown. ([kubernetes/kubernetes#96129](https://github.com/kubernetes/kubernetes/pull/96129), [@bobbypage](https://github.com/bobbypage)) [SIG Node]
- AppProtocol is now GA for Endpoints and Services. The ServiceAppProtocol feature gate will be deprecated in 1.21. ([kubernetes/kubernetes#96327](https://github.com/kubernetes/kubernetes/pull/96327), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- Automatic allocation of NodePorts for services with type LoadBalancer can now be disabled by setting the (new) parameter
  Service.spec.allocateLoadBalancerNodePorts=false. The default is to allocate NodePorts for services with type LoadBalancer which is the existing behavior. ([kubernetes/kubernetes#92744](https://github.com/kubernetes/kubernetes/pull/92744), [@uablrek](https://github.com/uablrek)) [SIG Apps and Network]
- Document that ServiceTopology feature is required to use `service.spec.topologyKeys`. ([kubernetes/kubernetes#96528](https://github.com/kubernetes/kubernetes/pull/96528), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- EndpointSlice has a new NodeName field guarded by the EndpointSliceNodeName feature gate.
  - EndpointSlice topology field will be deprecated in an upcoming release.
  - EndpointSlice "IP" address type is formally removed after being deprecated in Kubernetes 1.17.
  - The discovery.k8s.io/v1alpha1 API is deprecated and will be removed in Kubernetes 1.21. ([kubernetes/kubernetes#96440](https://github.com/kubernetes/kubernetes/pull/96440), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps and Network]
- Fewer candidates are enumerated for preemption to improve performance in large clusters ([kubernetes/kubernetes#94814](https://github.com/kubernetes/kubernetes/pull/94814), [@adtac](https://github.com/adtac)) [SIG Scheduling]
- If BoundServiceAccountTokenVolume is enabled, cluster admins can use metric `serviceaccount_stale_tokens_total` to monitor workloads that are depending on the extended tokens. If there are no such workloads, turn off extended tokens by starting `kube-apiserver` with flag `--service-account-extend-token-expiration=false` ([kubernetes/kubernetes#96273](https://github.com/kubernetes/kubernetes/pull/96273), [@zshihang](https://github.com/zshihang)) [SIG API Machinery and Auth]
- Introduce alpha support for exec-based container registry credential provider plugins in the kubelet. ([kubernetes/kubernetes#94196](https://github.com/kubernetes/kubernetes/pull/94196), [@andrewsykim](https://github.com/andrewsykim)) [SIG Node and Release]
- Kube-apiserver now deletes expired kube-apiserver Lease objects:
  - The feature is under feature gate `APIServerIdentity`.
  - A flag is added to kube-apiserver: `identity-lease-garbage-collection-check-period-seconds` ([kubernetes/kubernetes#95895](https://github.com/kubernetes/kubernetes/pull/95895), [@roycaihw](https://github.com/roycaihw)) [SIG API Machinery, Apps, Auth and Testing]
- Move configurable fsgroup change policy for pods to beta ([kubernetes/kubernetes#96376](https://github.com/kubernetes/kubernetes/pull/96376), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- New flag is introduced, i.e. --topology-manager-scope=container|pod. 
  The default value is the "container" scope. ([kubernetes/kubernetes#92967](https://github.com/kubernetes/kubernetes/pull/92967), [@cezaryzukowski](https://github.com/cezaryzukowski)) [SIG Instrumentation, Node and Testing]
- NodeAffinity plugin can be configured with AddedAffinity. ([kubernetes/kubernetes#96202](https://github.com/kubernetes/kubernetes/pull/96202), [@alculquicondor](https://github.com/alculquicondor)) [SIG Node, Scheduling and Testing]
- Promote RuntimeClass feature to GA.
  Promote node.k8s.io API groups from v1beta1 to v1. ([kubernetes/kubernetes#95718](https://github.com/kubernetes/kubernetes/pull/95718), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Reminder: The labels "failure-domain.beta.kubernetes.io/zone" and "failure-domain.beta.kubernetes.io/region" are deprecated in favor of "topology.kubernetes.io/zone" and "topology.kubernetes.io/region" respectively.  All users of the "failure-domain.beta..." labels should switch to the "topology..." equivalents. ([kubernetes/kubernetes#96033](https://github.com/kubernetes/kubernetes/pull/96033), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, CLI, Cloud Provider, Network, Node, Scheduling, Storage and Testing]
- The usage of mixed protocol values in the same LoadBalancer Service is possible if the new feature gate MixedProtocolLBSVC is enabled.
  "action required"
  The feature gate is disabled by default. The user has to enable it for the API Server. ([kubernetes/kubernetes#94028](https://github.com/kubernetes/kubernetes/pull/94028), [@janosi](https://github.com/janosi)) [SIG API Machinery and Apps]
- This PR will introduce a feature gate CSIServiceAccountToken with two additional fields in `CSIDriverSpec`. ([kubernetes/kubernetes#93130](https://github.com/kubernetes/kubernetes/pull/93130), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Users can try the CronJob controller v2 using the feature gate. This will be the default controller in future releases. ([kubernetes/kubernetes#93370](https://github.com/kubernetes/kubernetes/pull/93370), [@alaypatel07](https://github.com/alaypatel07)) [SIG API Machinery, Apps, Auth and Testing]
- VolumeSnapshotDataSource moves to GA in 1.20 release ([kubernetes/kubernetes#95282](https://github.com/kubernetes/kubernetes/pull/95282), [@xing-yang](https://github.com/xing-yang)) [SIG Apps]
- + `TokenRequest` and `TokenRequestProjection` features have been promoted to GA. This feature allows generating service account tokens that are not visible in Secret objects and are tied to the lifetime of a Pod object. See https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection for details on configuring and using this feature. The `TokenRequest` and `TokenRequestProjection` feature gates will be removed in v1.21.
  + kubeadm's kube-apiserver Pod manifest now includes the following flags by default "--service-account-key-file", "--service-account-signing-key-file", "--service-account-issuer". ([kubernetes/kubernetes#93258](https://github.com/kubernetes/kubernetes/pull/93258), [@zshihang](https://github.com/zshihang)) [SIG API Machinery, Auth, Cluster Lifecycle, Storage and Testing]
- Certain fields on  Service objects will be automatically cleared when changing the service's `type` to a mode that does not need those fields.  For example, changing from type=LoadBalancer to type=ClusterIP will clear the NodePort assignments, rather than forcing the user to clear them. ([kubernetes/kubernetes#95196](https://github.com/kubernetes/kubernetes/pull/95196), [@thockin](https://github.com/thockin)) [SIG API Machinery, Apps, Network and Testing]
- Services will now have a `clusterIPs` field to go with `clusterIP`.  `clusterIPs[0]` is a synonym for `clusterIP` and will be synchronized on create and update operations. ([kubernetes/kubernetes#95894](https://github.com/kubernetes/kubernetes/pull/95894), [@thockin](https://github.com/thockin)) [SIG Network]
- Add dual-stack Services (alpha).  This is a BREAKING CHANGE to an alpha API.
  It changes the dual-stack API wrt Service from a single ipFamily field to 3
  fields: ipFamilyPolicy (SingleStack, PreferDualStack, RequireDualStack),
  ipFamilies (a list of families assigned), and clusterIPs (inclusive of
  clusterIP).  Most users do not need to set anything at all, defaulting will
  handle it for them.  Services are single-stack unless the user asks for
  dual-stack.  This is all gated by the "IPv6DualStack" feature gate. ([kubernetes/kubernetes#91824](https://github.com/kubernetes/kubernetes/pull/91824), [@khenidak](https://github.com/khenidak)) [SIG API Machinery, Apps, CLI, Network, Node, Scheduling and Testing]
- Introduces a metric source for HPAs which allows scaling based on container resource usage. ([kubernetes/kubernetes#90691](https://github.com/kubernetes/kubernetes/pull/90691), [@arjunrn](https://github.com/arjunrn)) [SIG API Machinery, Apps, Autoscaling and CLI]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user-provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- GPU metrics provided by kubelet are now disabled by default ([kubernetes/kubernetes#95184](https://github.com/kubernetes/kubernetes/pull/95184), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- New parameter `defaultingType` for `PodTopologySpread` plugin allows to use k8s defined or user provided default constraints ([kubernetes/kubernetes#95048](https://github.com/kubernetes/kubernetes/pull/95048), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling]
- Server Side Apply now treats LabelSelector fields as atomic (meaning the entire selector is managed by a single writer and updated together), since they contain interrelated and inseparable fields that do not merge in intuitive ways. ([kubernetes/kubernetes#93901](https://github.com/kubernetes/kubernetes/pull/93901), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Storage and Testing]
- Status of v1beta1 CRDs without "preserveUnknownFields:false" will show violation "spec.preserveUnknownFields: Invalid value: true: must be false" ([kubernetes/kubernetes#93078](https://github.com/kubernetes/kubernetes/pull/93078), [@vareti](https://github.com/vareti)) [SIG API Machinery]
- A new `nofuzz` go build tag now disables gofuzz support. Release binaries enable this. ([kubernetes/kubernetes#92491](https://github.com/kubernetes/kubernetes/pull/92491), [@BenTheElder](https://github.com/BenTheElder)) [SIG API Machinery]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/135-seccomp/README.md#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- External facing API podresources is now available under k8s.io/kubelet/pkg/apis/ ([kubernetes/kubernetes#92632](https://github.com/kubernetes/kubernetes/pull/92632), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node and Testing]
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94481](https://github.com/kubernetes/kubernetes/pull/94481), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Instrumentation]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empty; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Kube-controller-manager: volume plugins can be restricted from contacting local and loopback addresses by setting `--volume-host-allow-local-loopback=false`, or from contacting specific CIDR ranges by setting `--volume-host-cidr-denylist` (for example, `--volume-host-cidr-denylist=127.0.0.1/28,feed::/16`) ([kubernetes/kubernetes#91785](https://github.com/kubernetes/kubernetes/pull/91785), [@mattcary](https://github.com/mattcary)) [SIG API Machinery, Apps, Auth, CLI, Network, Node, Storage and Testing]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- Migrate scheduler, controller-manager and cloud-controller-manager to use LeaseLock ([kubernetes/kubernetes#94603](https://github.com/kubernetes/kubernetes/pull/94603), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps, Cloud Provider and Scheduling]
- Modify DNS-1123 error messages to indicate that RFC 1123 is not followed exactly ([kubernetes/kubernetes#94182](https://github.com/kubernetes/kubernetes/pull/94182), [@mattfenwick](https://github.com/mattfenwick)) [SIG API Machinery, Apps, Auth, Network and Node]
- The ServiceAccountIssuerDiscovery feature gate is now Beta and enabled by default. ([kubernetes/kubernetes#91921](https://github.com/kubernetes/kubernetes/pull/91921), [@mtaufen](https://github.com/mtaufen)) [SIG Auth]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- When creating a networking.k8s.io/v1 Ingress API object, `spec.tls[*].secretName` values are required to pass validation rules for Secret API object names. ([kubernetes/kubernetes#93929](https://github.com/kubernetes/kubernetes/pull/93929), [@liggitt](https://github.com/liggitt)) [SIG Network]
- WinOverlay feature graduated to beta ([kubernetes/kubernetes#94807](https://github.com/kubernetes/kubernetes/pull/94807), [@ksubrmnn](https://github.com/ksubrmnn)) [SIG Windows]


# v19.15.0

Kubernetes API Version: v1.19.15

### Feature
- The new parameter 'no_proxy' has been added to configuration for the REST and websocket client. ([kubernetes-client/python#1579](https://github.com/kubernetes-client/python/pull/1579), [@itaru2622](https://github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))//github.com/itaru2622))

# v19.15.0b1

Kubernetes API Version: v1.19.15

- No changes. The same as `v19.15.0a1`.

# v19.15.0a1

Kubernetes API Version: v1.19.15

### Bug Fix
- Type checking in `Client.serialize_body()` was made more restrictive and robust. ([kubernetes-client/python-base#241](https://github.com/kubernetes-client/python-base/pull/241), [@piglei](https://github.com/piglei))

### Feature
- Support Proxy Authentication in websocket client(stream/ws_client) like REST client. ([kubernetes-client/python-base#256](https://github.com/kubernetes-client/python-base/pull/256), [@itaru2622](https://github.com/itaru2622))
- Support for the dryRun parameter has been added to the dynamic client. ([kubernetes-client/python-base#247](https://github.com/kubernetes-client/python-base/pull/247), [@gravesm](https://github.com/gravesm))

### API Change
- We have added a new Priority & Fairness rule that exempts all probes (/readyz, /healthz, /livez) to prevent 
  restarting of "healthy" kube-apiserver instance(s) by kubelet. ([kubernetes/kubernetes#101113](https://github.com/kubernetes/kubernetes/pull/101113), [@tkashem](https://github.com/tkashem)) [SIG API Machinery]
- Fixes using server-side apply with APIService resources ([kubernetes/kubernetes#100713](https://github.com/kubernetes/kubernetes/pull/100713), [@kevindelgado](https://github.com/kevindelgado)) [SIG API Machinery, Apps, Scheduling and Testing]
- Regenerate protobuf code to fix CVE-2021-3121 ([kubernetes/kubernetes#100515](https://github.com/kubernetes/kubernetes/pull/100515), [@joelsmith](https://github.com/joelsmith)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Node and Storage]
- Kubernetes is now built using go1.15.8 ([kubernetes/kubernetes#99093](https://github.com/kubernetes/kubernetes/pull/99093), [@cpanato](https://github.com/cpanato)) [SIG Cloud Provider, Instrumentation, Release and Testing]
- Fix conversions for custom metrics. ([kubernetes/kubernetes#94654](https://github.com/kubernetes/kubernetes/pull/94654), [@wojtek-t](https://github.com/wojtek-t)) [SIG Instrumentation]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/135-seccomp/README.md#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Admission webhooks can now return warning messages that are surfaced to API clients, using the `.response.warnings` field in the admission review response. ([kubernetes/kubernetes#92667](https://github.com/kubernetes/kubernetes/pull/92667), [@liggitt](https://github.com/liggitt)) [SIG API Machinery and Testing]
- CertificateSigningRequest API conditions were updated:
  - a `status` field was added; this field defaults to `True`, and may only be set to `True` for `Approved`, `Denied`, and `Failed` conditions
  - a `lastTransitionTime` field was added
  - a `Failed` condition type was added to allow signers to indicate permanent failure; this condition can be added via the `certificatesigningrequests/status` subresource.
  - `Approved` and `Denied` conditions are mutually exclusive
  - `Approved`, `Denied`, and `Failed` conditions can no longer be removed from a CSR ([kubernetes/kubernetes#90191](https://github.com/kubernetes/kubernetes/pull/90191), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Auth, CLI and Node]
- Cluster admins can now turn off /logs endpoint in kubelet by setting enableSystemLogHandler to false in their kubelet configuration file. enableSystemLogHandler can be set to true only when enableDebuggingHandlers is also set to true. ([kubernetes/kubernetes#87273](https://github.com/kubernetes/kubernetes/pull/87273), [@SaranBalaji90](https://github.com/SaranBalaji90)) [SIG Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- CustomResourceDefinitions added support for marking versions as deprecated by setting `spec.versions[*].deprecated` to `true`, and for optionally overriding the default deprecation warning with a `spec.versions[*].deprecationWarning` field. ([kubernetes/kubernetes#92329](https://github.com/kubernetes/kubernetes/pull/92329), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
- Fix bug in reflector that couldn't recover from "Too large resource version" errors ([kubernetes/kubernetes#92537](https://github.com/kubernetes/kubernetes/pull/92537), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([kubernetes/kubernetes#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empt; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Go1.14.4 is now the minimum version required for building Kubernetes ([kubernetes/kubernetes#92438](https://github.com/kubernetes/kubernetes/pull/92438), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Storage and Testing]
- Hide managedFields from kubectl edit command ([kubernetes/kubernetes#91946](https://github.com/kubernetes/kubernetes/pull/91946), [@soltysh](https://github.com/soltysh)) [SIG CLI]
- K8s.io/apimachinery - scheme.Convert() now uses only explicitly registered conversions - default reflection based conversion is no longer available. `+k8s:conversion-gen` tags can be used with the `k8s.io/code-generator` component to generate conversions. ([kubernetes/kubernetes#90018](https://github.com/kubernetes/kubernetes/pull/90018), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps and Testing]
- Kube-proxy: add `--bind-address-hard-fail` flag to treat failure to bind to a port as fatal ([kubernetes/kubernetes#89350](https://github.com/kubernetes/kubernetes/pull/89350), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle and Network]
- Kubebuilder validation tags are set on metav1.Condition for CRD generation ([kubernetes/kubernetes#92660](https://github.com/kubernetes/kubernetes/pull/92660), [@damemi](https://github.com/damemi)) [SIG API Machinery]
- Kubelet's --runonce option is now also available in Kubelet's config file as `runOnce`. ([kubernetes/kubernetes#89128](https://github.com/kubernetes/kubernetes/pull/89128), [@vincent178](https://github.com/vincent178)) [SIG Node]
- Kubelet: add '--logging-format' flag to support structured logging ([kubernetes/kubernetes#91532](https://github.com/kubernetes/kubernetes/pull/91532), [@afrouzMashaykhi](https://github.com/afrouzMashaykhi)) [SIG API Machinery, Cluster Lifecycle, Instrumentation and Node]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- Promote Immutable Secrets/ConfigMaps feature to Beta and enable the feature by default.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#89594](https://github.com/kubernetes/kubernetes/pull/89594), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps and Testing]
- Remove `BindTimeoutSeconds` from schedule configuration `KubeSchedulerConfiguration` ([kubernetes/kubernetes#91580](https://github.com/kubernetes/kubernetes/pull/91580), [@cofyc](https://github.com/cofyc)) [SIG Scheduling and Testing]
- Remove kubescheduler.config.k8s.io/v1alpha1 ([kubernetes/kubernetes#89298](https://github.com/kubernetes/kubernetes/pull/89298), [@gavinfish](https://github.com/gavinfish)) [SIG Scheduling]
- Reserve plugins that fail to reserve will trigger the unreserve extension point ([kubernetes/kubernetes#92391](https://github.com/kubernetes/kubernetes/pull/92391), [@adtac](https://github.com/adtac)) [SIG Scheduling and Testing]
- Resolve regression in `metadata.managedFields` handling in update/patch requests submitted by older API clients ([kubernetes/kubernetes#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse))
- Scheduler: optionally check for available storage capacity before scheduling pods which have unbound volumes (alpha feature with the new `CSIStorageCapacity` feature gate, only works for CSI drivers and depends on support for the feature in a CSI driver deployment) ([kubernetes/kubernetes#92387](https://github.com/kubernetes/kubernetes/pull/92387), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Scheduling, Storage and Testing]
- Seccomp support has graduated to GA. A new `seccompProfile` field is added to pod and container securityContext objects. Support for `seccomp.security.alpha.kubernetes.io/pod` and `container.seccomp.security.alpha.kubernetes.io/...` annotations is deprecated, and will be removed in v1.22. ([kubernetes/kubernetes#91381](https://github.com/kubernetes/kubernetes/pull/91381), [@pjbgf](https://github.com/pjbgf)) [SIG Apps, Auth, Node, Release, Scheduling and Testing]
- ServiceAppProtocol feature gate is now beta and enabled by default, adding new AppProtocol field to Services and Endpoints. ([kubernetes/kubernetes#90023](https://github.com/kubernetes/kubernetes/pull/90023), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- SetHostnameAsFQDN is a new field in PodSpec. When set to true, the fully 
  qualified domain name (FQDN) of a Pod is set as hostname of its containers. 
  In Linux containers, this means setting the FQDN in the hostname field of the 
  kernel (the nodename field of struct utsname).  In Windows containers, this
  means setting the this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. 
  If a pod does not have FQDN, this has no effect. ([kubernetes/kubernetes#91699](https://github.com/kubernetes/kubernetes/pull/91699), [@javidiaz](https://github.com/javidiaz)) [SIG Apps, Network, Node and Testing]
- The CertificateSigningRequest API is promoted to certificates.k8s.io/v1 with the following changes:
  - `spec.signerName` is now required, and requests for `kubernetes.io/legacy-unknown` are not allowed to be created via the `certificates.k8s.io/v1` API
  - `spec.usages` is now required, may not contain duplicate values, and must only contain known usages
  - `status.conditions` may not contain duplicate types
  - `status.conditions[*].status` is now required
  - `status.certificate` must be PEM-encoded, and contain only CERTIFICATE blocks ([kubernetes/kubernetes#91685](https://github.com/kubernetes/kubernetes/pull/91685), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Architecture, Auth, CLI and Testing]
- The HugePageStorageMediumSize feature gate is now on by default allowing usage of multiple sizes huge page resources on a container level. ([kubernetes/kubernetes#90592](https://github.com/kubernetes/kubernetes/pull/90592), [@bart0sh](https://github.com/bart0sh)) [SIG Node]
- The Kubelet's --node-status-max-images option is now available via the Kubelet config file field nodeStatusMaxImage ([kubernetes/kubernetes#91275](https://github.com/kubernetes/kubernetes/pull/91275), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's --seccomp-profile-root option is now marked as deprecated. ([kubernetes/kubernetes#91182](https://github.com/kubernetes/kubernetes/pull/91182), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--bootstrap-checkpoint-path` option is now removed. ([kubernetes/kubernetes#91577](https://github.com/kubernetes/kubernetes/pull/91577), [@knabben](https://github.com/knabben)) [SIG Apps and Node]
- The Kubelet's `--cloud-provider` and `--cloud-config` options are now marked as deprecated. ([kubernetes/kubernetes#90408](https://github.com/kubernetes/kubernetes/pull/90408), [@knabben](https://github.com/knabben)) [SIG Cloud Provider and Node]
- The Kubelet's `--enable-server` and `--provider-id` option is now available via the Kubelet config file field `enableServer` and `providerID` respectively. ([kubernetes/kubernetes#90494](https://github.com/kubernetes/kubernetes/pull/90494), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--kernel-memcg-notification` option is now available via the Kubelet config file field kernelMemcgNotification ([kubernetes/kubernetes#91863](https://github.com/kubernetes/kubernetes/pull/91863), [@knabben](https://github.com/knabben)) [SIG Cloud Provider, Node and Testing]
- The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--volume-plugin-dir` option is now available via the Kubelet config file field `VolumePluginDir`. ([kubernetes/kubernetes#88480](https://github.com/kubernetes/kubernetes/pull/88480), [@savitharaghunathan](https://github.com/savitharaghunathan)) [SIG Node]
- The `DefaultIngressClass` feature is now GA. The `--feature-gate` parameter will be removed in 1.20. ([kubernetes/kubernetes#91957](https://github.com/kubernetes/kubernetes/pull/91957), [@cmluciano](https://github.com/cmluciano)) [SIG API Machinery, Apps, Network and Testing]
- The alpha `DynamicAuditing` feature gate and `auditregistration.k8s.io/v1alpha1` API have been removed and are no longer supported. ([kubernetes/kubernetes#91502](https://github.com/kubernetes/kubernetes/pull/91502), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Auth and Testing]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- The unused `series.state` field, deprecated since v1.14, is removed from the `events.k8s.io/v1beta1` and `v1` Event types. ([kubernetes/kubernetes#90449](https://github.com/kubernetes/kubernetes/pull/90449), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps]
- Unreserve extension point for scheduler plugins is merged into Reserve extension point ([kubernetes/kubernetes#92200](https://github.com/kubernetes/kubernetes/pull/92200), [@adtac](https://github.com/adtac)) [SIG Scheduling and Testing]
- Update Golang to v1.14.4 ([kubernetes/kubernetes#88638](https://github.com/kubernetes/kubernetes/pull/88638), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Cloud Provider, Release and Testing]
- Updated the API documentation for Service.Spec.IPFamily to warn that its exact
  semantics will probably change before the dual-stack feature goes GA, and users
  should look at ClusterIP or Endpoints, not IPFamily, to figure out if an existing
  Service is IPv4, IPv6, or dual-stack. ([kubernetes/kubernetes#91527](https://github.com/kubernetes/kubernetes/pull/91527), [@danwinship](https://github.com/danwinship)) [SIG Apps and Network]
- Users can configure a resource prefix to ignore a group of resources. ([kubernetes/kubernetes#88842](https://github.com/kubernetes/kubernetes/pull/88842), [@angao](https://github.com/angao)) [SIG Node and Scheduling]
- `Ingress` and `IngressClass` resources have graduated to `networking.k8s.io/v1`. Ingress and IngressClass types in the `extensions/v1beta1` and `networking.k8s.io/v1beta1` API versions are deprecated and will no longer be served in 1.22+. Persisted objects can be accessed via the `networking.k8s.io/v1` API. Notable changes in v1 Ingress objects (v1beta1 field names are unchanged):
  - `spec.backend` -> `spec.defaultBackend`
  - `serviceName` -> `service.name`
  - `servicePort` -> `service.port.name` (for string values)
  - `servicePort` -> `service.port.number` (for numeric values)
  - `pathType` no longer has a default value in v1; "Exact", "Prefix", or "ImplementationSpecific" must be specified
  Other Ingress API updates:
  - backends can now be resource or service backends
  - `path` is no longer required to be a valid regular expression ([kubernetes/kubernetes#89778](https://github.com/kubernetes/kubernetes/pull/89778), [@cmluciano](https://github.com/cmluciano)) [SIG API Machinery, Apps, CLI, Network and Testing]
- `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- `PostFilter` type is added to scheduler component config API on version v1beta1. ([kubernetes/kubernetes#91547](https://github.com/kubernetes/kubernetes/pull/91547), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- `RequestedToCapacityRatioArgs` encoding is now strict ([kubernetes/kubernetes#91603](https://github.com/kubernetes/kubernetes/pull/91603), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
- `v1beta1` Scheduler `Extender` encoding is case-sensitive (`v1alpha1`/`v1alpha2` was case-insensitive), its `httpTimeout` field uses duration encoding (for example, one second is specified as `"1s"`), and the `enableHttps` field in `v1alpha1`/`v1alpha2` was renamed to `enableHTTPS`. ([kubernetes/kubernetes#91625](https://github.com/kubernetes/kubernetes/pull/91625), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
- Adds the ability to disable Accelerator/GPU metrics collected by Kubelet ([kubernetes/kubernetes#91930](https://github.com/kubernetes/kubernetes/pull/91930), [@RenaudWasTaken](https://github.com/RenaudWasTaken)) [SIG Node]
- Kubernetes is now built with golang 1.15.0-rc.1.
  - The deprecated, legacy behavior of treating the CommonName field on X.509 serving certificates as a host name when no Subject Alternative Names are present is now disabled by default. It can be temporarily re-enabled by adding the value x509ignoreCN=0 to the GODEBUG environment variable. ([kubernetes/kubernetes#93264](https://github.com/kubernetes/kubernetes/pull/93264), [@justaugustus](https://github.com/justaugustus)) [SIG API Machinery, Auth, CLI, Cloud Provider, Cluster Lifecycle, Instrumentation, Network, Node, Release, Scalability, Storage and Testing]
- A new alpha-level field, `SupportsFsGroup`, has been introduced for CSIDrivers to allow them to specify whether they support volume ownership and permission modifications. The `CSIVolumeSupportFSGroup` feature gate must be enabled to allow this field to be used. ([kubernetes/kubernetes#92001](https://github.com/kubernetes/kubernetes/pull/92001), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, CLI and Storage]
- The kube-controller-manager managed signers can now have distinct signing certificates and keys.  See the help about `--cluster-signing-[signer-name]-{cert,key}-file`.  `--cluster-signing-{cert,key}-file` is still the default. ([kubernetes/kubernetes#90822](https://github.com/kubernetes/kubernetes/pull/90822), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Apps and Auth]
- Added pod version skew strategy for seccomp profile to synchronize the deprecated annotations with the new API Server fields. Please see the corresponding section [in the KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/135-seccomp#version-skew-strategy) for more detailed explanations. ([kubernetes/kubernetes#91408](https://github.com/kubernetes/kubernetes/pull/91408), [@saschagrunert](https://github.com/saschagrunert)) [SIG Apps, Auth, CLI and Node]
- Custom Endpoints are now mirrored to EndpointSlices by a new EndpointSliceMirroring controller. ([kubernetes/kubernetes#91637](https://github.com/kubernetes/kubernetes/pull/91637), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, Auth, Cloud Provider, Instrumentation, Network and Testing]
- Generic ephemeral volumes, a new alpha feature under the `GenericEphemeralVolume` feature gate, provide a more flexible alternative to `EmptyDir` volumes: as with `EmptyDir`, volumes are created and deleted for each pod automatically by Kubernetes. But because the normal provisioning process is used (`PersistentVolumeClaim`), storage can be provided by third-party storage vendors and all of the usual volume features work. Volumes don't need to be empt; for example, restoring from snapshot is supported. ([kubernetes/kubernetes#92784](https://github.com/kubernetes/kubernetes/pull/92784), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, CLI, Instrumentation, Node, Scheduling, Storage and Testing]
- Remove `BindTimeoutSeconds` from schedule configuration `KubeSchedulerConfiguration` ([kubernetes/kubernetes#91580](https://github.com/kubernetes/kubernetes/pull/91580), [@cofyc](https://github.com/cofyc)) [SIG Scheduling and Testing]
- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([kubernetes/kubernetes#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- The CertificateSigningRequest API is promoted to certificates.k8s.io/v1 with the following changes:
  - `spec.signerName` is now required, and requests for `kubernetes.io/legacy-unknown` are not allowed to be created via the `certificates.k8s.io/v1` API
  - `spec.usages` is now required, may not contain duplicate values, and must only contain known usages
  - `status.conditions` may not contain duplicate types
  - `status.conditions[*].status` is now required
  - `status.certificate` must be PEM-encoded, and contain only CERTIFICATE blocks ([kubernetes/kubernetes#91685](https://github.com/kubernetes/kubernetes/pull/91685), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Architecture, Auth, CLI and Testing]
- The Kubelet's `--cloud-provider` and `--cloud-config` options are now marked as deprecated. ([kubernetes/kubernetes#90408](https://github.com/kubernetes/kubernetes/pull/90408), [@knabben](https://github.com/knabben)) [SIG Cloud Provider and Node]
- CertificateSigningRequest API conditions were updated:
  - a `status` field was added; this field defaults to `True`, and may only be set to `True` for `Approved`, `Denied`, and `Failed` conditions
  - a `lastTransitionTime` field was added
  - a `Failed` condition type was added to allow signers to indicate permanent failure; this condition can be added via the `certificatesigningrequests/status` subresource.
  - `Approved` and `Denied` conditions are mutually exclusive
  - `Approved`, `Denied`, and `Failed` conditions can no longer be removed from a CSR ([kubernetes/kubernetes#90191](https://github.com/kubernetes/kubernetes/pull/90191), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Auth, CLI and Node]
- EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([kubernetes/kubernetes#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- The Kubelet's --node-status-max-images option is now available via the Kubelet config file field nodeStatusMaxImage ([kubernetes/kubernetes#91275](https://github.com/kubernetes/kubernetes/pull/91275), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's --seccomp-profile-root option is now available via the Kubelet config file field seccompProfileRoot. ([kubernetes/kubernetes#91182](https://github.com/kubernetes/kubernetes/pull/91182), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--enable-server` and `--provider-id` option is now available via the Kubelet config file field `enableServer` and `providerID` respectively. ([kubernetes/kubernetes#90494](https://github.com/kubernetes/kubernetes/pull/90494), [@knabben](https://github.com/knabben)) [SIG Node]
- The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
- The alpha `DynamicAuditing` feature gate and `auditregistration.k8s.io/v1alpha1` API have been removed and are no longer supported. ([kubernetes/kubernetes#91502](https://github.com/kubernetes/kubernetes/pull/91502), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Auth and Testing]
- `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- `PostFilter` type is added to scheduler component config API on version v1beta1. ([kubernetes/kubernetes#91547](https://github.com/kubernetes/kubernetes/pull/91547), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- `kubescheduler.config.k8s.io` is now beta ([kubernetes/kubernetes#91420](https://github.com/kubernetes/kubernetes/pull/91420), [@pancernik](https://github.com/pancernik)) [SIG Scheduling]
 - EnvVarSource api doc bug fixes ([kubernetes/kubernetes#91194](https://github.com/kubernetes/kubernetes/pull/91194), [@wawa0210](https://github.com/wawa0210)) [SIG Apps]
 - The Kubelet's `--really-crash-for-testing` and  `--chaos-chance` options are now marked as deprecated. ([kubernetes/kubernetes#90499](https://github.com/kubernetes/kubernetes/pull/90499), [@knabben](https://github.com/knabben)) [SIG Node]
 - `NodeResourcesLeastAllocated` and `NodeResourcesMostAllocated` plugins now support customized weight on the CPU and memory. ([kubernetes/kubernetes#90544](https://github.com/kubernetes/kubernetes/pull/90544), [@chendave](https://github.com/chendave)) [SIG Scheduling]
- K8s.io/apimachinery - scheme.Convert() now uses only explicitly registered conversions - default reflection based conversion is no longer available. `+k8s:conversion-gen` tags can be used with the `k8s.io/code-generator` component to generate conversions. ([kubernetes/kubernetes#90018](https://github.com/kubernetes/kubernetes/pull/90018), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery, Apps and Testing]
- Kubelet's --runonce option is now also available in Kubelet's config file as `runOnce`. ([kubernetes/kubernetes#89128](https://github.com/kubernetes/kubernetes/pull/89128), [@vincent178](https://github.com/vincent178)) [SIG Node]
- Promote Immutable Secrets/ConfigMaps feature to Beta and enable the feature by default.
  This allows to set `Immutable` field in Secrets or ConfigMap object to mark their contents as immutable. ([kubernetes/kubernetes#89594](https://github.com/kubernetes/kubernetes/pull/89594), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps and Testing]
- The unused `series.state` field, deprecated since v1.14, is removed from the `events.k8s.io/v1beta1` and `v1` Event types. ([kubernetes/kubernetes#90449](https://github.com/kubernetes/kubernetes/pull/90449), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps]
- Kube-proxy: add `--bind-address-hard-fail` flag to treat failure to bind to a port as fatal ([kubernetes/kubernetes#89350](https://github.com/kubernetes/kubernetes/pull/89350), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle and Network]
- Remove kubescheduler.config.k8s.io/v1alpha1 ([kubernetes/kubernetes#89298](https://github.com/kubernetes/kubernetes/pull/89298), [@gavinfish](https://github.com/gavinfish)) [SIG Scheduling]
- ServiceAppProtocol feature gate is now beta and enabled by default, adding new AppProtocol field to Services and Endpoints. ([kubernetes/kubernetes#90023](https://github.com/kubernetes/kubernetes/pull/90023), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The Kubelet's `--volume-plugin-dir` option is now available via the Kubelet config file field `VolumePluginDir`. ([kubernetes/kubernetes#88480](https://github.com/kubernetes/kubernetes/pull/88480), [@savitharaghunathan](https://github.com/savitharaghunathan)) [SIG Node]
- A new IngressClass resource has been added to enable better Ingress configuration. ([kubernetes/kubernetes#88509](https://github.com/kubernetes/kubernetes/pull/88509), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, CLI, Network, Node and Testing]
- API additions to apiserver types ([kubernetes/kubernetes#87179](https://github.com/kubernetes/kubernetes/pull/87179), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery, Cloud Provider and Cluster Lifecycle]
- Add Scheduling Profiles to kubescheduler.config.k8s.io/v1alpha2 ([kubernetes/kubernetes#88087](https://github.com/kubernetes/kubernetes/pull/88087), [@alculquicondor](https://github.com/alculquicondor)) [SIG Scheduling and Testing]
- Added GenericPVCDataSource feature gate to enable using arbitrary custom resources as the data source for a PVC. ([kubernetes/kubernetes#88636](https://github.com/kubernetes/kubernetes/pull/88636), [@bswartz](https://github.com/bswartz)) [SIG Apps and Storage]
- Added support for multiple sizes huge pages on a container level ([kubernetes/kubernetes#84051](https://github.com/kubernetes/kubernetes/pull/84051), [@bart0sh](https://github.com/bart0sh)) [SIG Apps, Node and Storage]
- Allow user to specify fsgroup permission change policy for pods ([kubernetes/kubernetes#88488](https://github.com/kubernetes/kubernetes/pull/88488), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- AppProtocol is a new field on Service and Endpoints resources, enabled with the ServiceAppProtocol feature gate. ([kubernetes/kubernetes#88503](https://github.com/kubernetes/kubernetes/pull/88503), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- BlockVolume and CSIBlockVolume features are now GA. ([kubernetes/kubernetes#88673](https://github.com/kubernetes/kubernetes/pull/88673), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Node and Storage]
- Consumers of the 'certificatesigningrequests/approval' API must now grant permission to 'approve' CSRs for the 'signerName' specified on the CSR. More information on the new signerName field can be found at https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/1513-certificate-signing-request/README.md/#signers ([kubernetes/kubernetes#88246](https://github.com/kubernetes/kubernetes/pull/88246), [@munnerz](https://github.com/munnerz)) [SIG API Machinery, Apps, Auth, CLI, Node and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-map-keys` to specify properties that uniquely identify list items must make those properties required or have a default value, to ensure those properties are present for all list items. See https://kubernetes.io/docs/reference/using-api/api-concepts/#merge-strategy for details. ([kubernetes/kubernetes#88076](https://github.com/kubernetes/kubernetes/pull/88076), [@eloyekunle](https://github.com/eloyekunle)) [SIG API Machinery and Testing]
- Fixed missing validation of uniqueness of list items in lists with `x-kubernetes-list-type: map` or `x-kubernetes-list-type: set` in CustomResources. ([kubernetes/kubernetes#84920](https://github.com/kubernetes/kubernetes/pull/84920), [@sttts](https://github.com/sttts)) [SIG API Machinery]
- Fixes a regression with clients prior to 1.15 not being able to update podIP in pod status, or podCIDR in node spec, against >= 1.16 API servers ([kubernetes/kubernetes#88505](https://github.com/kubernetes/kubernetes/pull/88505), [@liggitt](https://github.com/liggitt)) [SIG Apps and Network]
- Ingress: Add Exact and Prefix matching to Ingress PathTypes ([kubernetes/kubernetes#88587](https://github.com/kubernetes/kubernetes/pull/88587), [@cmluciano](https://github.com/cmluciano)) [SIG Apps, Cluster Lifecycle and Network]
- Ingress: Add alternate backends via TypedLocalObjectReference ([kubernetes/kubernetes#88775](https://github.com/kubernetes/kubernetes/pull/88775), [@cmluciano](https://github.com/cmluciano)) [SIG Apps and Network]
- Ingress: allow wildcard hosts in IngressRule ([kubernetes/kubernetes#88858](https://github.com/kubernetes/kubernetes/pull/88858), [@cmluciano](https://github.com/cmluciano)) [SIG Network]
- Introduces optional --detect-local flag to kube-proxy. 
  Currently the only supported value is "cluster-cidr", 
  which is the default if not specified. ([kubernetes/kubernetes#87748](https://github.com/kubernetes/kubernetes/pull/87748), [@satyasm](https://github.com/satyasm)) [SIG Cluster Lifecycle, Network and Scheduling]
- Kube-controller-manager and kube-scheduler expose profiling by default to match the kube-apiserver.  Use `--profiling=false` to disable. ([kubernetes/kubernetes#88663](https://github.com/kubernetes/kubernetes/pull/88663), [@deads2k](https://github.com/deads2k)) [SIG API Machinery, Cloud Provider and Scheduling]
- Kube-scheduler can run more than one scheduling profile. Given a pod, the profile is selected by using its `.spec.SchedulerName`. ([kubernetes/kubernetes#88285](https://github.com/kubernetes/kubernetes/pull/88285), [@alculquicondor](https://github.com/alculquicondor)) [SIG Apps, Scheduling and Testing]
- Move TaintBasedEvictions feature gates to GA ([kubernetes/kubernetes#87487](https://github.com/kubernetes/kubernetes/pull/87487), [@skilxn-go](https://github.com/skilxn-go)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Moving Windows RunAsUserName feature to GA ([kubernetes/kubernetes#87790](https://github.com/kubernetes/kubernetes/pull/87790), [@marosset](https://github.com/marosset)) [SIG Apps and Windows]
- New flag --endpointslice-updates-batch-period in kube-controller-manager can be used to reduce number of endpointslice updates generated by pod changes. ([kubernetes/kubernetes#88745](https://github.com/kubernetes/kubernetes/pull/88745), [@mborsz](https://github.com/mborsz)) [SIG API Machinery, Apps and Network]
- New flag `--show-hidden-metrics-for-version` in kubelet can be used to show all hidden metrics that deprecated in the previous minor release. ([kubernetes/kubernetes#85282](https://github.com/kubernetes/kubernetes/pull/85282), [@serathius](https://github.com/serathius)) [SIG Node]
- Removes ConfigMap as suggestion for IngressClass parameters ([kubernetes/kubernetes#89093](https://github.com/kubernetes/kubernetes/pull/89093), [@robscott](https://github.com/robscott)) [SIG Network]
- Scheduler Extenders can now be configured in the v1alpha2 component config ([kubernetes/kubernetes#88768](https://github.com/kubernetes/kubernetes/pull/88768), [@damemi](https://github.com/damemi)) [SIG Release, Scheduling and Testing]
- The apiserver/v1alph1 #EgressSelectorConfiguration API is now beta. ([kubernetes/kubernetes#88502](https://github.com/kubernetes/kubernetes/pull/88502), [@caesarxuchao](https://github.com/caesarxuchao)) [SIG API Machinery]
- The storage.k8s.io/CSIDriver has moved to GA, and is now available for use. ([kubernetes/kubernetes#84814](https://github.com/kubernetes/kubernetes/pull/84814), [@huffmanca](https://github.com/huffmanca)) [SIG API Machinery, Apps, Auth, Node, Scheduling, Storage and Testing]
- VolumePVCDataSource moves to GA in 1.18 release ([kubernetes/kubernetes#88686](https://github.com/kubernetes/kubernetes/pull/88686), [@j-griffith](https://github.com/j-griffith)) [SIG Apps, CLI and Cluster Lifecycle]


# v18.20.0

Kubernetes API Version: 1.18.20

### Feature
- Support for the dryRun parameter has been added to the dynamic client. ([kubernetes-client/python-base#247](https://github.com/kubernetes-client/python-base/pull/247), [@gravesm](https://github.com/gravesm))
- The `python2` support will be removed in 18.0.0 beta release. All the tests will use `python3` versions. ([kubernetes-client/python-base#238](https://github.com/kubernetes-client/python-base/pull/238), [@Priyankasaggu11929](https://github.com/Priyankasaggu11929))
- The dynamic client now supports customizing http "Accept" header through the `header_params` parameter, which can be used to customizing API server response, e.g. retrieving object metadata only. ([kubernetes-client/python-base#236](https://github.com/kubernetes-client/python-base/pull/236), [@Yashks1994](https://github.com/Yashks1994))

# v18.20.0b1

Kubernetes API Version: 1.18.20

**Important Information:**

- Python 2 had reached [End of Life](https://www.python.org/doc/sunset-python-2/) on January 1, 2020. The Kubernetes Python Client has dropped support for Python 2 from this release (v18.20.0b1) and will no longer provide support to older clients as per the [Kubernetes support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions).

# v18.17.0a1

Kubernetes API Version: 1.18.17

**Important Information:**

- The Kubernetes Python client versioning scheme has changed. The version numbers used till Kubernetes Python Client v12.y.z lagged behind the actual Kubernetes minor version numbers. From this release, the client is moving a version format `vY.Z.P` where `Y` and `Z` are respectively from the Kubernetes version `v1.Y.Z` and `P` would incremented due to changes on the Python client side itself. Ref: https://github.com/kubernetes-client/python/issues/1244
- Python 2 had reached [End of Life](https://www.python.org/doc/sunset-python-2/) on January 1, 2020. The Kubernetes Python Client has dropped support for Python 2 from this release (v18.0.0) and will no longer provide support to older clients as per the [Kubernetes support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions).

**Deprecations:**
- The following deprecated APIs can no longer be served:
  - All resources under `apps/v1beta1` and `apps/v1beta2` - use `apps/v1` instead
  - `daemonsets`, `deployments`, `replicasets` resources under `extensions/v1beta1` - use `apps/v1` instead
  - `networkpolicies` resources under `extensions/v1beta1` - use `networking.k8s.io/v1` instead
  - `podsecuritypolicies` resources under `extensions/v1beta1` - use `policy/v1beta1` instead ([#85903](https://github.com/kubernetes/kubernetes/pull/85903), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Cluster Lifecycle, Instrumentation and Testing]

**New Feature:**
- Support leader election. [kubernetes-client/python-base#206](https://github.com/kubernetes-client/python-base/pull/206)

**Bug Fix:**
- Raise exception when an empty config file is passed to load_kube_config. [kubernetes-client/python-base#223](https://github.com/kubernetes-client/python-base/pull/223)
- fix: load cache error when CacheDecoder object is not callable. [kubernetes-client/python-base#226](https://github.com/kubernetes-client/python-base/pull/226)
- Fix Watch retries with 410 errors. [kubernetes-client/python-base#227](https://github.com/kubernetes-client/python-base/pull/227)
- Automatically handles chunked or non-chunked responses. Fix ResponseNotChunked error from watch. [kubernetes-client/python-base#231](https://github.com/kubernetes-client/python-base/pull/231)

**API Change:**
- Add allowWatchBookmarks, resoureVersionMatch parameters to custom objects. [kubernetes-client/gen#180](https://github.com/kubernetes-client/gen/pull/180)
- Fix bug in reflector that couldn't recover from "Too large resource version" errors ([#92537](https://github.com/kubernetes/kubernetes/pull/92537), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([#92007](https://github.com/kubernetes/kubernetes/pull/92007), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- A new IngressClass resource has been added to enable better Ingress configuration. ([#88509](https://github.com/kubernetes/kubernetes/pull/88509), [@robscott](https://github.com/robscott)) [SIG API Machinery, Apps, CLI, Network, Node and Testing]
- The CSIDriver API has graduated to storage.k8s.io/v1, and is now available for use. ([#84814](https://github.com/kubernetes/kubernetes/pull/84814), [@huffmanca](https://github.com/huffmanca)) [SIG Storage]
- autoscaling/v2beta2 HorizontalPodAutoscaler added a `spec.behavior` field that allows scale behavior to be configured. Behaviors are specified separately for scaling up and down. In each direction a stabilization window can be specified as well as a list of policies and how to select amongst them. Policies can limit the absolute number of pods added or removed, or the percentage of pods added or removed. ([#74525](https://github.com/kubernetes/kubernetes/pull/74525), [@gliush](https://github.com/gliush)) [SIG API Machinery, Apps, Autoscaling and CLI]
- Ingress:
  - `spec.ingressClassName` replaces the deprecated `kubernetes.io/ingress.class` annotation, and allows associating an Ingress object with a particular controller.
  - path definitions added a `pathType` field to allow indicating how the specified path should be matched against incoming requests. Valid values are `Exact`, `Prefix`, and `ImplementationSpecific` ([#88587](https://github.com/kubernetes/kubernetes/pull/88587), [@cmluciano](https://github.com/cmluciano)) [SIG Apps, Cluster Lifecycle and Network]
- The alpha feature `AnyVolumeDataSource` enables PersistentVolumeClaim objects to use the spec.dataSource field to reference a custom type as a data source ([#88636](https://github.com/kubernetes/kubernetes/pull/88636), [@bswartz](https://github.com/bswartz)) [SIG Apps and Storage]
- The alpha feature `ConfigurableFSGroupPolicy` enables v1 Pods to specify a spec.securityContext.fsGroupChangePolicy policy to control how file permissions are applied to volumes mounted into the pod. ([#88488](https://github.com/kubernetes/kubernetes/pull/88488), [@gnufied](https://github.com/gnufied)) [SIG  Storage]
- The alpha feature `ServiceAppProtocol` enables setting an `appProtocol` field in ServicePort and EndpointPort definitions. ([#88503](https://github.com/kubernetes/kubernetes/pull/88503), [@robscott](https://github.com/robscott)) [SIG Apps and Network]
- The alpha feature `ImmutableEphemeralVolumes` enables an `immutable` field in both Secret and ConfigMap objects to mark their contents as immutable. ([#86377](https://github.com/kubernetes/kubernetes/pull/86377), [@wojtek-t](https://github.com/wojtek-t)) [SIG Apps, CLI and Testing]
- The beta feature `ServerSideApply` enables tracking and managing changed fields for all new objects, which means there will be `managedFields` in `metadata` with the list of managers and their owned fields.
- The alpha feature `ServiceAccountIssuerDiscovery` enables publishing OIDC discovery information and service account token verification keys at `/.well-known/openid-configuration` and `/openid/v1/jwks` endpoints by API servers configured to issue service account tokens. ([#80724](https://github.com/kubernetes/kubernetes/pull/80724), [@cceckman](https://github.com/cceckman)) [SIG API Machinery, Auth, Cluster Lifecycle and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-map-keys` to specify properties that uniquely identify list items must make those properties required or have a default value, to ensure those properties are present for all list items. See https://kubernetes.io/docs/reference/using-api/api-concepts/&#35;merge-strategy for details. ([#88076](https://github.com/kubernetes/kubernetes/pull/88076), [@eloyekunle](https://github.com/eloyekunle)) [SIG API Machinery and Testing]
- CustomResourceDefinition schemas that use `x-kubernetes-list-type: map` or `x-kubernetes-list-type: set` now enable validation that the list items in the corresponding custom resources are unique. ([#84920](https://github.com/kubernetes/kubernetes/pull/84920), [@sttts](https://github.com/sttts)) [SIG API Machinery]


To read the full CHANGELOG visit [here](https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.18.md).

# v17.17.0

Kubernetes API Version: 1.17.17

Changelog since v17.17.0b1:

### Bug or Regression
- Fix watch stream non-chunked response handling ([kubernetes-client/python-base#231](https://github.com/kubernetes-client/python-base/pull/231), [@dhague](https://github.com/dhague))
- Fixed a decoding error for BOOTMARK watch events ([kubernetes-client/python-base#234](https://github.com/kubernetes-client/python-base/pull/234), [@yliaog](https://github.com/yliaog))

### Feature
- Load_kube_config_from_dict() support define custom temp files path ([kubernetes-client/python-base#233](https://github.com/kubernetes-client/python-base/pull/233), [@onecer](https://github.com/onecer))
- The dynamic client now supports customizing http "Accept" header through the `header_params` parameter, which can be used to customizing API server response, e.g. retrieving object metadata only. ([kubernetes-client/python-base#236](https://github.com/kubernetes-client/python-base/pull/236), [@Yashks1994](https://github.com/Yashks1994))

# v17.17.0b1

Kubernetes API Version: 1.17.17

Changelog since v17.14.0a1:

**New Feature:**
- Add Python 3.9 to build [kubernetes-client/python#1311](https://github.com/kubernetes-client/python/pull/1311)
- Enable leaderelection [kubernetes-client/python#1363](https://github.com/kubernetes-client/python/pull/1363)

**API Change:**
- Add allowWatchBookmarks, resoureVersionMatch parameters to custom objects. [kubernetes-client/gen#180](https://github.com/kubernetes-client/gen/pull/180)

**Bug Fix:**
- fix: load cache error when CacheDecoder object is not callable [kubernetes-client/python-base#226](https://github.com/kubernetes-client/python-base/pull/226)
- raise exception when an empty config file is passed to load_kube_config [kubernetes-client/python-base#223](https://github.com/kubernetes-client/python-base/pull/223)
- Fix bug with Watch and 410 retries [kubernetes-client/python-base#227](https://github.com/kubernetes-client/python-base/pull/227)

# v17.14.0a1

Kubernetes API Version: 1.17.14

**Important Information:**

- The Kubernetes Python client versioning scheme has changed. The version numbers used till Kubernetes Python Client v12.y.z lagged behind the actual Kubernetes minor version numbers. From this release, the client is moving a version format `vY.Z.P` where `Y` and `Z` are respectively from the Kubernetes version `v1.Y.Z` and `P` would incremented due to changes on the Python client side itself. Ref: https://github.com/kubernetes-client/python/issues/1244
- Python 2 had reached [End of Life](https://www.python.org/doc/sunset-python-2/) on January 1, 2020. The Kubernetes Python Client will drop support for Python 2 from the next release (v18.0.0) and will no longer provide support to older clients as per the [Kubernetes support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions).


**API Change:**
- Fixed: log timestamps now include trailing zeros to maintain a fixed width ([#91207](https://github.com/kubernetes/kubernetes/pull/91207), [@iamchuckss](https://github.com/iamchuckss)) [SIG Apps and Node]
- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([#92008](https://github.com/kubernetes/kubernetes/pull/92008), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
 - Fix bug where sending a status update completely wipes managedFields for some types. ([#90032](https://github.com/kubernetes/kubernetes/pull/90032), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
 - Fixes a regression with clients prior to 1.15 not being able to update podIP in pod status, or podCIDR in node spec, against >= 1.16 API servers ([#88505](https://github.com/kubernetes/kubernetes/pull/88505), [@liggitt](https://github.com/liggitt)) [SIG Apps and Network]
 - CustomResourceDefinitions now validate documented API semantics of `x-kubernetes-list-type` and `x-kubernetes-map-type` atomic to reject non-atomic sub-types. ([#84722](https://github.com/kubernetes/kubernetes/pull/84722), [@sttts](https://github.com/sttts))
- Kube-apiserver: The `AdmissionConfiguration` type accepted by `--admission-control-config-file` has been promoted to `apiserver.config.k8s.io/v1` with no schema changes. ([#85098](https://github.com/kubernetes/kubernetes/pull/85098), [@liggitt](https://github.com/liggitt))
- Fixed EndpointSlice port name validation to match Endpoint port name validation (allowing port names longer than 15 characters) ([#84481](https://github.com/kubernetes/kubernetes/pull/84481), [@robscott](https://github.com/robscott))
- CustomResourceDefinitions introduce `x-kubernetes-map-type` annotation as a CRD API extension. Enables this particular validation for server-side apply. ([#84113](https://github.com/kubernetes/kubernetes/pull/84113), [@enxebre](https://github.com/enxebre))

To read the full CHANGELOG visit [here](https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.17.md).

# v12.0.1

Kubernetes API Version: 1.16.15

**Breaking Change:**

- `kubernetes.config.Configuration()` will now return the default "initial" configuration, `kubernetes.config.Configuration.get_default_copy()` will return the default configuration if there is a default set via `Configuration.set_default(c)`, otherwise, it will also return the default "initial" configuration. [OpenAPITools/openapi-generator#4485](https://github.com/OpenAPITools/openapi-generator/pull/4485), [OpenAPITools/openapi-generator#5315](https://github.com/OpenAPITools/openapi-generator/pull/5315). **Note: ** This change also affects v12.0.0a1, v12.0.0b1 and v12.0.0.

**Bug Fix:**
- Prevent 503s from killing the client during discovery [kubernetes-client/python-base#187](https://github.com/kubernetes-client/python-base/pull/187)


# v12.0.0

Kubernetes API Version: 1.16.15

**New Feature:**
- Implement Port Forwarding [kubernetes-client/python-base#210](https://github.com/kubernetes-client/python-base/pull/210), [kubernetes-client/python-base#211](https://github.com/kubernetes-client/python-base/pull/211), [kubernetes-client/python#1237](https://github.com/kubernetes-client/python/pull/1237)
- Support loading configuration from file-like objects [kubernetes-client/python-base#208](https://github.com/kubernetes-client/python-base/pull/208)
- Returns the created k8s objects in `create_from_{dict,yaml}` [kubernetes-client/python#1262](https://github.com/kubernetes-client/python/pull/1262)


# v12.0.0b1

Kubernetes API Version: 1.16.14

**New Feature:**
- Accept and use client certificates from authentication plugins [kubernetes-client/python-base#205](https://github.com/kubernetes-client/python-base/pull/205)

**Bug Fix:**
- Return when object is None in FileOrData class [kubernetes-client/python-base#201](https://github.com/kubernetes-client/python-base/pull/201)

# v12.0.0a1

Kubernetes API Version: 1.16.14

**API Change:**

- Resolve regression in metadata.managedFields handling in update/patch requests submitted by older API clients ([#91748](https://github.com/kubernetes/kubernetes/pull/91748), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- Fix bug where sending a status update completely wipes managedFields for some types. ([#90033](https://github.com/kubernetes/kubernetes/pull/90033), [@apelisse](https://github.com/apelisse)) [SIG API Machinery and Testing]
- The `MutatingWebhookConfiguration` and `ValidatingWebhookConfiguration` APIs have been promoted to `admissionregistration.k8s.io/v1`:
  - `failurePolicy` default changed from `Ignore` to `Fail` for v1
  - `matchPolicy` default changed from `Exact` to `Equivalent` for v1
  - `timeout` default changed from `30s` to `10s` for v1
  - `sideEffects` default value is removed, and the field made required, and only `None` and `NoneOnDryRun` are permitted for v1
  - `admissionReviewVersions` default value is removed and the field made required for v1 (supported versions for AdmissionReview are `v1` and `v1beta1`)
  - The `name` field for specified webhooks must be unique for `MutatingWebhookConfiguration` and `ValidatingWebhookConfiguration` objects created via `admissionregistration.k8s.io/v1`
- The `AdmissionReview` API sent to and received from admission webhooks has been promoted to `admission.k8s.io/v1`. Webhooks can specify a preference for receiving `v1` AdmissionReview objects with `admissionReviewVersions: ["v1","v1beta1"]`, and must respond with an API object in the same `apiVersion` they are sent. When webhooks use `admission.k8s.io/v1`, the following additional validation is performed on their responses:
  - `response.patch` and `response.patchType` are not permitted from validating admission webhooks
  - `apiVersion: "admission.k8s.io/v1"` is required
  - `kind: "AdmissionReview"` is required
  - `response.uid: "<value of request.uid>"` is required
  - `response.patchType: "JSONPatch"` is required (if `response.patch` is set) ([#80231](https://github.com/kubernetes/kubernetes/pull/80231), [@liggitt](https://github.com/liggitt))
- The `CustomResourceDefinition` API type is promoted to `apiextensions.k8s.io/v1` with the following changes:
  - Use of the new `default` feature in validation schemas is limited to v1
  - `spec.scope` is no longer defaulted to `Namespaced` and must be explicitly specified
  - `spec.version` is removed in v1; use `spec.versions` instead
  - `spec.validation` is removed in v1; use `spec.versions[*].schema` instead
  - `spec.subresources` is removed in v1; use `spec.versions[*].subresources` instead
  - `spec.additionalPrinterColumns` is removed in v1; use `spec.versions[*].additionalPrinterColumns` instead
  - `spec.conversion.webhookClientConfig` is moved to `spec.conversion.webhook.clientConfig` in v1
  - `spec.conversion.conversionReviewVersions` is moved to `spec.conversion.webhook.conversionReviewVersions` in v1
  - `spec.versions[*].schema.openAPIV3Schema` is now required when creating v1 CustomResourceDefinitions
  - `spec.preserveUnknownFields: true` is disallowed when creating v1 CustomResourceDefinitions; it must be specified within schema definitions as `x-kubernetes-preserve-unknown-fields: true`
  - In `additionalPrinterColumns` items, the `JSONPath` field was renamed to `jsonPath` in v1 (fixes https://github.com/kubernetes/kubernetes/issues/66531)
    The `apiextensions.k8s.io/v1beta1` version of `CustomResourceDefinition` is deprecated and will no longer be served in v1.19. ([#79604](https://github.com/kubernetes/kubernetes/pull/79604), [@liggitt](https://github.com/liggitt))
- The `ConversionReview` API sent to and received from custom resource CustomResourceDefinition conversion webhooks has been promoted to `apiextensions.k8s.io/v1`. CustomResourceDefinition conversion webhooks can now indicate they support receiving and responding with `ConversionReview` API objects in the `apiextensions.k8s.io/v1` version by including `v1` in the `conversionReviewVersions` list in their CustomResourceDefinition. Conversion webhooks must respond with a ConversionReview object in the same apiVersion they receive. `apiextensions.k8s.io/v1` `ConversionReview` responses must specify a `response.uid` that matches the `request.uid` of the object they were sent. ([#81476](https://github.com/kubernetes/kubernetes/pull/81476), [@liggitt](https://github.com/liggitt))
- Add scheduling support for RuntimeClasses. RuntimeClasses can now specify nodeSelector constraints & tolerations, which are merged into the PodSpec for pods using that RuntimeClass. ([#80825](https://github.com/kubernetes/kubernetes/pull/80825), [@tallclair](https://github.com/tallclair))
- Kubelet should now more reliably report the same primary node IP even if the set of node IPs reported by the CloudProvider changes. ([#79391](https://github.com/kubernetes/kubernetes/pull/79391), [@danwinship](https://github.com/danwinship))
- Omit nil or empty field when calculating container hash value to avoid hash changed. For a new field with a non-nil default value in the container spec, the hash would still get changed. ([#57741](https://github.com/kubernetes/kubernetes/pull/57741), [@dixudx](https://github.com/dixudx))
- Property `conditions` in `apiextensions.v1beta1.CustomResourceDefinitionStatus` and `apiextensions.v1.CustomResourceDefinitionStatus` is now optional instead of required. ([#64996](https://github.com/kubernetes/kubernetes/pull/64996), [@roycaihw](https://github.com/roycaihw))
- When the status of a CustomResourceDefinition condition changes, its corresponding `lastTransitionTime` is now updated. ([#69655](https://github.com/kubernetes/kubernetes/pull/69655), [@CaoShuFeng](https://github.com/CaoShuFeng))

**New Feature:**

- Adds the ability to load kubeconfig from a dictionary [kubernetes-client/python-base#195](https://github.com/kubernetes-client/python-base/pull/195)
- Allow incluster to accept pass-in config [kubernetes-client/python-base#193](https://github.com/kubernetes-client/python-base/pull/193)
- Set expiration on token of incluster config and reload the token if it expires [kubernetes-client/python-base#191](https://github.com/kubernetes-client/python-base/pull/191)

**Bug Fix:**

- Fixes a bug in loading kubeconfig when there are no users in the config [kubernetes-client/python-base#198](https://github.com/kubernetes-client/python-base/pull/198)
- Retry expired watches [kubernetes-client/python-base#133](https://github.com/kubernetes-client/python-base/pull/133)

**OpenAPI Generator Changes:**

OpenAPI Generator has been updated to v4.3.0 from v3.3.4. Following are links to Python client related changes throughout the OpenAPI releases above v3.3.4 to v4.3.0:

- [v4.3.0](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.3.0+label%3A%22Client%3A+Python%22)
- [v4.2.3](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.2.3+label%3A%22Client%3A+Python%22)
- [v4.2.2](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.2.2+label%3A%22Client%3A+Python%22)
- [v4.2.1](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.2.1+label%3A%22Client%3A+Python%22)
- [v4.2.0](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.2.0+label%3A%22Client%3A+Python%22)
- [v4.1.3](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.1.3+label%3A%22Client%3A+Python%22)
- [v4.1.2](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.1.2+label%3A%22Client%3A+Python%22)
- [v4.1.1](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.1.1+label%3A%22Client%3A+Python%22)
- [v4.1.0](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.1.0+label%3A%22Client%3A+Python%22)
- [v4.0.3](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.0.3+label%3A%22Client%3A+Python%22)
- [v4.0.2](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Amerged+is%3Apr+milestone%3A4.0.2+label%3A%22Client%3A+Python%22)
- [v4.0.1](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Apr+milestone%3A4.0.1+is%3Amerged+label%3A%22Client%3A+Python%22)
- [v4.0.0](https://github.com/OpenAPITools/openapi-generator/pulls?q=is%3Apr+milestone%3A4.0.0+is%3Amerged+label%3A%22Client%3A+Python%22)


# v11.0.0

Kubernetes API Version: 1.15.10

**API Change:**

- Deleting CustomObjects doesn't require passing in the body anymore [kubernetes-client/gen#142](https://github.com/kubernetes-client/gen/pull/142)

**New Feature:**

- Add ability to the client to be used as Context Manager [kubernetes-client/python#1073](https://github.com/kubernetes-client/python/pull/1073)
- Enable the use of dynamic client [kubernetes-client/python#1035](https://github.com/kubernetes-client/python/pull/1035)
- Add option to refresh gcp token when config is cmd-path [kubernetes-client/python-base#175](https://github.com/kubernetes-client/python-base/pull/175)

**Bug Fix:**

- Add kubernetes.dynamic to setup.py pkg list [kubernetes-client/python#1096](https://github.com/kubernetes-client/python/pull/1096)
- Fixed issue in `__del__` method of the `ApiClient` that caused an indefinite hang during garbage collection. [kubernetes-client/python#1073](https://github.com/kubernetes-client/python/pull/1073)
- Fix custom object API example [kubernetes-client/python#1049](https://github.com/kubernetes-client/python/pull/1049)
- Fix deprecation warning in E2E tests [kubernetes-client/python#1036](https://github.com/kubernetes-client/python/pull/1036)
- Use `==/!=` to compare str, bytes, and int literals [kubernetes-client/python#1007](https://github.com/kubernetes-client/python/pull/1007)
- Fix apiserver_id 'get' method [kubernetes-client/python-base#184](https://github.com/kubernetes-client/python-base/pull/184)
- Fix persist_config flag and function calls [kubernetes-client/python-base#169](https://github.com/kubernetes-client/python-base/pull/169)
- Fix memory inneficiencies in the WebSocket client [kubernetes-client/python-base#178](https://github.com/kubernetes-client/python-base/pull/178)
- Fix functionality to watch logs when log line is not a JSON-serialized object [kubernetes-client/python-base#171](https://github.com/kubernetes-client/python-base/pull/171)
- Detect binary payloads and send the correct opcode [kubernetes-client/python-base#152](https://github.com/kubernetes-client/python-base/pull/152)

**Deprecation Notice**
v11.0.0 of the client follows the Kubernetes [deprecation policy](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md#supported-releases-and-component-skew) and will
be deprecated as and when Kubernetes version v1.15 gets deprecated.

# v11.0.0b2
**Bug Fix:**
- Fix a fatal bug in package setup [kubernetes-client/python#1011](https://github.com/kubernetes-client/python/pull/1011)

# v11.0.0b1
**Bug Fix:**
- Fix a bug in kubeconfig loader where NoneType gets iterated [kubernetes-client/python-base#158](https://github.com/kubernetes-client/python-base/pull/158)
- Fix a bug in kubeconfig loader that False value gets treated as absence [kubernetes-client/python-base#161](https://github.com/kubernetes-client/python-base/pull/161)
- Fix a bug in kubeconfig loader where merging valid configs fails if fields are missing [kubernetes-client/python-base#163](https://github.com/kubernetes-client/python-base/pull/163)
- Fix azure refresh token apiserver id [kubernetes-client/python-base#170](https://github.com/kubernetes-client/python-base/pull/170)
- Support chunked listing to custom object API [kubernetes-client/gen#130](https://github.com/kubernetes-client/gen/pull/130)

**New Feature:**
- Add returncode method to WSClient [kubernetes-client/python-base#160](https://github.com/kubernetes-client/python-base/pull/160)
- Add proxy support to WSClient [kubernetes-client/python-base#157](https://github.com/kubernetes-client/python-base/pull/157)
- Add util function to parse canonical quantities [kubernetes-client/python#855](https://github.com/kubernetes-client/python/pull/855)

# v11.0.0a1
**New Feature:**
- Add dynamic client [kubernetes-client/python-base#56](https://github.com/kubernetes-client/python-base/pull/56)
- `create_from_yaml` supports creation from dict and namespace option [kubernetes-client/python#795](https://github.com/kubernetes-client/python/pull/795)

**Breaking Change:**
- The Python client will be generated by openapi-generator, with the following breaking changes [kubernetes-client/gen#97](https://github.com/kubernetes-client/gen/pull/97)
- `kubernetes.client.apis` package is renamed to `kubernetes.client.api`
- `kubernetes` package code now uses absolute import instead of relative import
- The `swagger_types` attribute in all models is renamed to `openapi_types`
- Python3.4 is no longer supported [kubernetes-client/python#807](https://github.com/kubernetes-client/python/pull/807)

**API Change:**
- Introduce `ExtensionsV1beta1RuntimeClassStrategyOptions` and `PolicyV1beta1RuntimeClassStrategyOptions`. Add RuntimeClass restrictions & defaulting to PodSecurityPolicy [kubernetes/kubernetes#73795](https://github.com/kubernetes/kubernetes/pull/73795)
- Introduce `V1WindowsSecurityContextOptions`. Add Windows specific options in Pod Security Context and Container Security Context [kubernetes/kubernetes#77147](https://github.com/kubernetes/kubernetes/pull/77147)
- Split `V1beta1Webhook` into `V1beta1MutatingWebhook` and `V1beta1ValidatingWebhook` [kubernetes/kubernetes#78491](https://github.com/kubernetes/kubernetes/pull/78491)
- Introduce parameter `allow_watch_bookmarks` in list options for requesting watch bookmarks from apiserver. The implementation in apiserver is hidden behind feature gate `WatchBookmark` (currently in Alpha stage) [kubernetes/kubernetes#74074](https://github.com/kubernetes/kubernetes/pull/74074)
- Add `V1DeleteOptions` parameters (`dry_run`, `grace_period_seconds`, `orphan_dependents`, `propagation_policy`) to delete collection APIs [kubernetes/kubernetes#77843](https://github.com/kubernetes/kubernetes/pull/77843)
- Add ListMeta.RemainingItemCount. When responding a LIST request, if the server has more data available, and if the request does not contain label selectors or field selectors, the server sets the ListOptions.RemainingItemCount to the number of remaining objects [kubernetes/kubernetes#75993](https://github.com/kubernetes/kubernetes/pull/75993)
- Add `controller_expand_secret_ref` in `V1SecretReference` to store CSI volume expansion secrets [kubernetes/kubernetes#77516](https://github.com/kubernetes/kubernetes/pull/77516)
- Introduce `preemption_policy` field to V1PriorityClass [kubernetes/kubernetes#74614](https://github.com/kubernetes/kubernetes/pull/74614)
- Add `port` configuration to service reference in Admission webhook configuration, AuditSink webhook configuration, CRD Conversion webhook configuration and kube-aggregator [kubernetes/kubernetes#74855](https://github.com/kubernetes/kubernetes/pull/74855)
- Introduce `inline_volume_spec` to `V1PersistentVolumeSpec` [kubernetes/kubernetes#77703](https://github.com/kubernetes/kubernetes/pull/77703)
- Add fields `x_kubernetes_embedded_resource`, `x_kubernetes_int_or_string`, `x_kubernetes_preserve_unknown_fields` to V1beta1JSONSchemaProps [kubernetes/kubernetes#77207](https://github.com/kubernetes/kubernetes/pull/77207)

**Bug Fix:**
- Update `_load_azure_token` to handle str and int [kubernetes-client/python-base#141](https://github.com/kubernetes-client/python-base/pull/141)
- Correct regex to properly parse rfc3339 microseconds [kubernetes-client/python-base#150](https://github.com/kubernetes-client/python-base/pull/150)

# v10.1.0
**Bug Fix:**
- Fixed issue in `__del__` method of the `ApiClient` that caused an indefinite hang during garbage collection. *Note* The `ApiClient` `ThreadPool` will no longer be cleaned up automatically during garbage collection, instead the `close` method must be invoked directly, or the `ApiClient` can be used as a context manager. [kubernetes-client/python#1073](https://github.com/kubernetes-client/python/pull/1073)

# v10.0.1
**Bug Fix:**
- Fix content type regression in custom object patch API [kubernetes-client/python#866](https://github.com/kubernetes-client/python/issues/866)

**Security Fix:**
- Bump urllib3 version to pick up security fix for CVE-2019-11324 [kubernetes-client/python#897](https://github.com/kubernetes-client/python/pull/897)

# v10.0.0
**Bug Fix:**
- Fix base64 padding for kube config [kubernetes-client/python-base#79](https://github.com/kubernetes-client/python-base/pull/79)
- Fix websocket client decoding binary message. Replace non-utf8 data instead of failing [kubernetes-client/python-base#104](https://github.com/kubernetes-client/python-base/pull/104)
- Add email scope to GCP provided credential refresh [kubernetes-client/python-base#110](https://github.com/kubernetes-client/python-base/pull/110)
- Fix broken urllib3 dependencies [kubernetes-client/python#816](https://github.com/kubernetes-client/python/pull/816)

**New Feature:**
- Add method to dynamically set namespace in yaml utility [kubernetes-client/python#782](https://github.com/kubernetes-client/python/pull/782)

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
- The alpha Initializers feature, `admissionregistration.k8s.io/v1alpha1` API version, `Initializers` admission plugin, and use of the `metadata.initializers` API field have been removed. Discontinue use of the alpha feature and delete any existing `InitializerConfiguration` API objects before upgrading. The `metadata.initializers` field will be removed in a future release. The parameter `include_uninitialized` has been removed. [kubernetes/kubernetes#72972](https://github.com/kubernetes/kubernetes/pull/72972)

# v9.0.0
**Bug Fix:**
- Add fieldSelector parameter to list/watch methods in custom objects spec [kubernetes-client/gen#106](https://github.com/kubernetes-client/gen/pull/106)

# v9.0.0b1
**Breaking Change:**
- Move dependency adal under extra require [kubernetes-client/python-base#108](https://github.com/kubernetes-client/python-base/pull/108)

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
- Configuration is not a singleton object anymore. Please use Configuration.set_default to change default configuration.
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
- Add support for accessing multiple clusters #7
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
