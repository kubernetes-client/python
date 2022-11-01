# kubernetes.client.model.v1_pod_condition.V1PodCondition

PodCondition contains details for the current condition of this pod.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PodCondition contains details for the current condition of this pod. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions | 
**status** | str,  | str,  | Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions | 
**lastProbeTime** | str, datetime,  | str,  | Last time we probed the condition. | [optional] value must conform to RFC-3339 date-time
**lastTransitionTime** | str, datetime,  | str,  | Last time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | Human-readable message indicating details about last transition. | [optional] 
**reason** | str,  | str,  | Unique, one-word, CamelCase reason for the condition&#x27;s last transition. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

