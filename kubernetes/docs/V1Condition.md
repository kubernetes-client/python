# V1Condition

Condition contains details for one aspect of the current state of this API Resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | 
**message** | **str** | message is a human readable message indicating details about the transition. This may be an empty string. | 
**observed_generation** | **int** | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | [optional] 
**reason** | **str** | reason contains a programmatic identifier indicating the reason for the condition&#39;s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | 
**status** | **str** | status of the condition, one of True, False, Unknown. | 
**type** | **str** | type of condition in CamelCase or in foo.example.com/CamelCase. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


