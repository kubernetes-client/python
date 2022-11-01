# kubernetes.client.model.v1_resource_field_selector.V1ResourceFieldSelector

ResourceFieldSelector represents container resources (cpu, memory) and their output format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ResourceFieldSelector represents container resources (cpu, memory) and their output format | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource** | str,  | str,  | Required: resource to select | 
**containerName** | str,  | str,  | Container name: required for volumes, optional for env vars | [optional] 
**divisor** | str,  | str,  | Specifies the output format of the exposed resources, defaults to \&quot;1\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

