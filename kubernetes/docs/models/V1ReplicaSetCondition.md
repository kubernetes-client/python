# kubernetes.client.model.v1_replica_set_condition.V1ReplicaSetCondition

ReplicaSetCondition describes the state of a replica set at a certain point.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ReplicaSetCondition describes the state of a replica set at a certain point. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Type of replica set condition. | 
**status** | str,  | str,  | Status of the condition, one of True, False, Unknown. | 
**lastTransitionTime** | str, datetime,  | str,  | The last time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | A human readable message indicating details about the transition. | [optional] 
**reason** | str,  | str,  | The reason for the condition&#x27;s last transition. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

