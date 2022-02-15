# V1NamespaceCondition

NamespaceCondition contains details about state of namespace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of namespace controller condition.  Possible enum values:  - &#x60;\&quot;NamespaceContentRemaining\&quot;&#x60; contains information about resources remaining in a namespace.  - &#x60;\&quot;NamespaceDeletionContentFailure\&quot;&#x60; contains information about namespace deleter errors during deletion of resources.  - &#x60;\&quot;NamespaceDeletionDiscoveryFailure\&quot;&#x60; contains information about namespace deleter errors during resource discovery.  - &#x60;\&quot;NamespaceDeletionGroupVersionParsingFailure\&quot;&#x60; contains information about namespace deleter errors parsing GV for legacy types.  - &#x60;\&quot;NamespaceFinalizersRemaining\&quot;&#x60; contains information about which finalizers are on resources remaining in a namespace. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


