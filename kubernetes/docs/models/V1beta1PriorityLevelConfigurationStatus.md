# kubernetes.client.model.v1beta1_priority_level_configuration_status.V1beta1PriorityLevelConfigurationStatus

PriorityLevelConfigurationStatus represents the current state of a \"request-priority\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PriorityLevelConfigurationStatus represents the current state of a \&quot;request-priority\&quot;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[conditions](#conditions)** | list, tuple,  | tuple,  | &#x60;conditions&#x60; is the current state of \&quot;request-priority\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

`conditions` is the current state of \"request-priority\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | &#x60;conditions&#x60; is the current state of \&quot;request-priority\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationCondition**](V1beta1PriorityLevelConfigurationCondition.md) | [**V1beta1PriorityLevelConfigurationCondition**](V1beta1PriorityLevelConfigurationCondition.md) | [**V1beta1PriorityLevelConfigurationCondition**](V1beta1PriorityLevelConfigurationCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

