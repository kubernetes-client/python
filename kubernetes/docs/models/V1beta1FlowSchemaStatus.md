# kubernetes.client.model.v1beta1_flow_schema_status.V1beta1FlowSchemaStatus

FlowSchemaStatus represents the current state of a FlowSchema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | FlowSchemaStatus represents the current state of a FlowSchema. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[conditions](#conditions)** | list, tuple,  | tuple,  | &#x60;conditions&#x60; is a list of the current states of FlowSchema. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

`conditions` is a list of the current states of FlowSchema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | &#x60;conditions&#x60; is a list of the current states of FlowSchema. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1beta1FlowSchemaCondition**](V1beta1FlowSchemaCondition.md) | [**V1beta1FlowSchemaCondition**](V1beta1FlowSchemaCondition.md) | [**V1beta1FlowSchemaCondition**](V1beta1FlowSchemaCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

