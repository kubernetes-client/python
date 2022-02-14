# V2HorizontalPodAutoscalerCondition

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the last time the condition transitioned from one status to another | [optional] 
**message** | **str** | message is a human-readable explanation containing details about the transition | [optional] 
**reason** | **str** | reason is the reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | status is the status of the condition (True, False, Unknown) | 
**type** | **str** | type describes the current condition | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


