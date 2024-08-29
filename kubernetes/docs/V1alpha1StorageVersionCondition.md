# V1alpha1StorageVersionCondition

Describes the state of the storageVersion at a certain point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | 
**observed_generation** | **int** | If set, this represents the .metadata.generation that the condition was set based upon. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of the condition. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


