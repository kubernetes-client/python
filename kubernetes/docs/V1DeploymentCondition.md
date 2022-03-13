# V1DeploymentCondition

DeploymentCondition describes the state of a deployment at a certain point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of deployment condition. | 
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**last_update_time** | **datetime** | The last time this condition was updated. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


