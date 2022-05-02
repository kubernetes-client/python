# V1NodeCondition

NodeCondition contains condition information for a node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_heartbeat_time** | **datetime** | Last time we got an update on a given condition. | [optional] 
**last_transition_time** | **datetime** | Last time the condition transit from one status to another. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of node condition. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


