# V1ReplicaSetCondition

ReplicaSetCondition describes the state of a replica set at a certain point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of replica set condition. | 
**last_transition_time** | **datetime** | The last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


