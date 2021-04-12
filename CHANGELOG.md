# v18

**New Feature:**
- Support leader election. [kubernetes-client/python-base#206](https://github.com/kubernetes-client/python-base/pull/206)

**Bug Fix:**
- Raise exception when an empty config file is passed to load_kube_config. [kubernetes-client/python-base#223](https://github.com/kubernetes-client/python-base/pull/223)
- fix: load cache error when CacheDecoder object is not callable. [kubernetes-client/python-base#226](https://github.com/kubernetes-client/python-base/pull/226)
- Fix Watch retries with 410 errors. [kubernetes-client/python-base#227](https://github.com/kubernetes-client/python-base/pull/227)
- Automatically handles chunked or non-chunked responses. Fix ResponseNotChunked error from watch. [kubernetes-client/python-base#231](https://github.com/kubernetes-client/python-base/pull/231)

**API Change:**
- Add allowWatchBookmarks, resoureVersionMatch parameters to custom objects. [kubernetes-client/gen#180](https://github.com/kubernetes-client/gen/pull/180)


# v18.0.0-snapshot

Kubernetes API Version: 1.18.12

**Important Information:**

- The Kubernetes Python client versioning scheme has changed. The version numbers used till Kubernetes Python Client v12.y.z lagged behind the actual Kubernetes minor version numbers. From this release, the client is moving a version format `vY.Z.P` where `Y` and `Z` are respectively from the Kubernetes version `v1.Y.Z` and `P` would incremented due to changes on the Python client side itself. Ref: https://github.com/kubernetes-client/python/issues/1244
- Python 2 had reached [End of Life](https://www.python.org/doc/sunset-python-2/) on January 1, 2020. The Kubernetes Python Client has dropped support for Python 2 from this release (v18.0.0) and will no longer provide support to older clients as per the [Kubernetes support policy](https://kubernetes.io/docs/setup/release/version-skew-policy/#supported-versions).

**Deprecations:**
- The following deprecated APIs can no longer be served:
  - All resources under `apps/v1beta1` and `apps/v1beta2` - use `apps/v1` instead
  - `daemonsets`, `deployments`, `replicasets` resources under `extensions/v1beta1` - use `apps/v1` instead
  - `networkpolicies` resources under `extensions/v1beta1` - use `networking.k8s.io/v1` instead
  - `podsecuritypolicies` resources under `extensions/v1beta1` - use `policy/v1beta1` instead ([#85903](https://github.com/kubernetes/kubernetes/pull/85903), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Apps, Cluster Lifecycle, Instrumentation and Testing]

**API Change:**
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


# v17.0.0-snapshot

Kubernetes API Version: 1.17.13

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
