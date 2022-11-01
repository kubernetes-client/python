# kubernetes.client.model.v1_custom_resource_definition_names.V1CustomResourceDefinitionNames

CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**plural** | str,  | str,  | plural is the plural name of the resource to serve. The custom resources are served under &#x60;/apis/&lt;group&gt;/&lt;version&gt;/.../&lt;plural&gt;&#x60;. Must match the name of the CustomResourceDefinition (in the form &#x60;&lt;names.plural&gt;.&lt;group&gt;&#x60;). Must be all lowercase. | 
**kind** | str,  | str,  | kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the &#x60;kind&#x60; attribute in API calls. | 
**[categories](#categories)** | list, tuple,  | tuple,  | categories is a list of grouped resources this custom resource belongs to (e.g. &#x27;all&#x27;). This is published in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get all&#x60;. | [optional] 
**listKind** | str,  | str,  | listKind is the serialized kind of the list for this resource. Defaults to \&quot;&#x60;kind&#x60;List\&quot;. | [optional] 
**[shortNames](#shortNames)** | list, tuple,  | tuple,  | shortNames are short names for the resource, exposed in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get &lt;shortname&gt;&#x60;. It must be all lowercase. | [optional] 
**singular** | str,  | str,  | singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased &#x60;kind&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by kubernetes.clients to support invocations like `kubectl get all`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | categories is a list of grouped resources this custom resource belongs to (e.g. &#x27;all&#x27;). This is published in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get all&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# shortNames

shortNames are short names for the resource, exposed in API discovery documents, and used by kubernetes.clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | shortNames are short names for the resource, exposed in API discovery documents, and used by kubernetes.clients to support invocations like &#x60;kubectl get &lt;shortname&gt;&#x60;. It must be all lowercase. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

