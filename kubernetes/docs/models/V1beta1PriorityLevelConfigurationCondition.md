# kubernetes.client.model.v1beta1_priority_level_configuration_condition.V1beta1PriorityLevelConfigurationCondition

PriorityLevelConfigurationCondition defines the condition of priority level.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PriorityLevelConfigurationCondition defines the condition of priority level. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lastTransitionTime** | str, datetime,  | str,  | &#x60;lastTransitionTime&#x60; is the last time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | &#x60;message&#x60; is a human-readable message indicating details about last transition. | [optional] 
**reason** | str,  | str,  | &#x60;reason&#x60; is a unique, one-word, CamelCase reason for the condition&#x27;s last transition. | [optional] 
**status** | str,  | str,  | &#x60;status&#x60; is the status of the condition. Can be True, False, Unknown. Required. | [optional] 
**type** | str,  | str,  | &#x60;type&#x60; is the type of the condition. Required. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

