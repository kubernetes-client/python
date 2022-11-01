# kubernetes.client.model.v1_api_resource.V1APIResource

APIResource specifies the name of a resource and whether it is namespaced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | APIResource specifies the name of a resource and whether it is namespaced. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kind** | str,  | str,  | kind is the kind for the resource (e.g. &#x27;Foo&#x27; is the kind for a resource &#x27;foo&#x27;) | 
**name** | str,  | str,  | name is the plural name of the resource. | 
**[verbs](#verbs)** | list, tuple,  | tuple,  | verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy) | 
**namespaced** | bool,  | BoolClass,  | namespaced indicates if a resource is namespaced or not. | 
**singularName** | str,  | str,  | singularName is the singular name of the resource.  This allows kubernetes.clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface. | 
**[categories](#categories)** | list, tuple,  | tuple,  | categories is a list of the grouped resources this resource belongs to (e.g. &#x27;all&#x27;) | [optional] 
**group** | str,  | str,  | group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\&quot;. | [optional] 
**[shortNames](#shortNames)** | list, tuple,  | tuple,  | shortNames is a list of suggested short names of the resource. | [optional] 
**storageVersionHash** | str,  | str,  | The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by kubernetes.clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates. | [optional] 
**version** | str,  | str,  | version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource&#x27;s group)\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# verbs

verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# categories

categories is a list of the grouped resources this resource belongs to (e.g. 'all')

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | categories is a list of the grouped resources this resource belongs to (e.g. &#x27;all&#x27;) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# shortNames

shortNames is a list of suggested short names of the resource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | shortNames is a list of suggested short names of the resource. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

