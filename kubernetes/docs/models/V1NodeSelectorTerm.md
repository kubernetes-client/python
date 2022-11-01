# kubernetes.client.model.v1_node_selector_term.V1NodeSelectorTerm

A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[matchExpressions](#matchExpressions)** | list, tuple,  | tuple,  | A list of node selector requirements by node&#x27;s labels. | [optional] 
**[matchFields](#matchFields)** | list, tuple,  | tuple,  | A list of node selector requirements by node&#x27;s fields. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# matchExpressions

A list of node selector requirements by node's labels.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of node selector requirements by node&#x27;s labels. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) | [**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) | [**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) |  | 

# matchFields

A list of node selector requirements by node's fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of node selector requirements by node&#x27;s fields. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) | [**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) | [**V1NodeSelectorRequirement**](V1NodeSelectorRequirement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

