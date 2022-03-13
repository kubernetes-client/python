# V1CustomResourceDefinitionNames

CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the &#x60;kind&#x60; attribute in API calls. | 
**plural** | **str** | plural is the plural name of the resource to serve. The custom resources are served under &#x60;/apis/&lt;group&gt;/&lt;version&gt;/.../&lt;plural&gt;&#x60;. Must match the name of the CustomResourceDefinition (in the form &#x60;&lt;names.plural&gt;.&lt;group&gt;&#x60;). Must be all lowercase. | 
**categories** | **[str]** | categories is a list of grouped resources this custom resource belongs to (e.g. &#39;all&#39;). This is published in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get all&#x60;. | [optional] 
**list_kind** | **str** | listKind is the serialized kind of the list for this resource. Defaults to \&quot;&#x60;kind&#x60;List\&quot;. | [optional] 
**short_names** | **[str]** | shortNames are short names for the resource, exposed in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get &lt;shortname&gt;&#x60;. It must be all lowercase. | [optional] 
**singular** | **str** | singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased &#x60;kind&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


