# V1CustomResourceDefinitionSpec

CustomResourceDefinitionSpec describes how a user wants their resource to appear
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion** | [**V1CustomResourceConversion**](V1CustomResourceConversion.md) |  | [optional] 
**group** | **str** | group is the API group of the defined custom resource. The custom resources are served under &#x60;/apis/&lt;group&gt;/...&#x60;. Must match the name of the CustomResourceDefinition (in the form &#x60;&lt;names.plural&gt;.&lt;group&gt;&#x60;). | 
**names** | [**V1CustomResourceDefinitionNames**](V1CustomResourceDefinitionNames.md) |  | 
**preserve_unknown_fields** | **bool** | preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting &#x60;x-preserve-unknown-fields&#x60; to true in &#x60;spec.versions[*].schema.openAPIV3Schema&#x60;. See https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#pruning-versus-preserving-unknown-fields for details. | [optional] 
**scope** | **str** | scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are &#x60;Cluster&#x60; and &#x60;Namespaced&#x60;. | 
**versions** | [**list[V1CustomResourceDefinitionVersion]**](V1CustomResourceDefinitionVersion.md) | versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is \&quot;kube-like\&quot;, it will sort above non \&quot;kube-like\&quot; version strings, which are ordered lexicographically. \&quot;Kube-like\&quot; versions start with a \&quot;v\&quot;, then are followed by a number (the major version), then optionally the string \&quot;alpha\&quot; or \&quot;beta\&quot; and another number (the minor version). These are sorted first by GA &gt; beta &gt; alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


