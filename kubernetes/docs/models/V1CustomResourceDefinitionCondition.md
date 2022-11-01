# kubernetes.client.model.v1_custom_resource_definition_condition.V1CustomResourceDefinitionCondition

CustomResourceDefinitionCondition contains details for the current condition of this pod.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CustomResourceDefinitionCondition contains details for the current condition of this pod. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type is the type of the condition. Types include Established, NamesAccepted and Terminating. | 
**status** | str,  | str,  | status is the status of the condition. Can be True, False, Unknown. | 
**lastTransitionTime** | str, datetime,  | str,  | lastTransitionTime last time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | message is a human-readable message indicating details about last transition. | [optional] 
**reason** | str,  | str,  | reason is a unique, one-word, CamelCase reason for the condition&#x27;s last transition. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

