# kubernetes.client.model.v1_topology_selector_label_requirement.V1TopologySelectorLabelRequirement

A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[values](#values)** | list, tuple,  | tuple,  | An array of string values. One value must match the label to be selected. Each entry in Values is ORed. | 
**key** | str,  | str,  | The label key that the selector applies to. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

An array of string values. One value must match the label to be selected. Each entry in Values is ORed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of string values. One value must match the label to be selected. Each entry in Values is ORed. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

