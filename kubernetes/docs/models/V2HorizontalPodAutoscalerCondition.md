# kubernetes.client.model.v2_horizontal_pod_autoscaler_condition.V2HorizontalPodAutoscalerCondition

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type describes the current condition | 
**status** | str,  | str,  | status is the status of the condition (True, False, Unknown) | 
**lastTransitionTime** | str, datetime,  | str,  | lastTransitionTime is the last time the condition transitioned from one status to another | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | message is a human-readable explanation containing details about the transition | [optional] 
**reason** | str,  | str,  | reason is the reason for the condition&#x27;s last transition. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

