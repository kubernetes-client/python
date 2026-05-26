# V1alpha1StorageVersionCondition

Describes the state of the storageVersion at a certain point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | message is a human readable string indicating details about the transition. | 
**observed_generation** | **int** | observedGeneration represents the .metadata.generation that the condition was set based upon, if field is set. | [optional] 
**reason** | **str** | reason for the condition&#39;s last transition. | 
**status** | **str** | status of the condition, one of True, False, Unknown. | 
**type** | **str** | type of the condition. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


