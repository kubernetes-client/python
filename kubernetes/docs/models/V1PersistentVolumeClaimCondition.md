# kubernetes.client.model.v1_persistent_volume_claim_condition.V1PersistentVolumeClaimCondition

PersistentVolumeClaimCondition contails details about state of pvc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PersistentVolumeClaimCondition contails details about state of pvc | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | 
**status** | str,  | str,  |  | 
**lastProbeTime** | str, datetime,  | str,  | lastProbeTime is the time we probed the condition. | [optional] value must conform to RFC-3339 date-time
**lastTransitionTime** | str, datetime,  | str,  | lastTransitionTime is the time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | message is the human-readable message indicating details about last transition. | [optional] 
**reason** | str,  | str,  | reason is a unique, this should be a short, machine understandable string that gives the reason for condition&#x27;s last transition. If it reports \&quot;ResizeStarted\&quot; that means the underlying persistent volume is being resized. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

