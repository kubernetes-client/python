# kubernetes.client.model.v1_scope_selector.V1ScopeSelector

A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[matchExpressions](#matchExpressions)** | list, tuple,  | tuple,  | A list of scope selector requirements by scope of the resources. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# matchExpressions

A list of scope selector requirements by scope of the resources.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of scope selector requirements by scope of the resources. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ScopedResourceSelectorRequirement**](V1ScopedResourceSelectorRequirement.md) | [**V1ScopedResourceSelectorRequirement**](V1ScopedResourceSelectorRequirement.md) | [**V1ScopedResourceSelectorRequirement**](V1ScopedResourceSelectorRequirement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

