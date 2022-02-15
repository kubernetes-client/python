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
**type** | **str** | Type of node condition.  Possible enum values:  - &#x60;\&quot;DiskPressure\&quot;&#x60; means the kubelet is under pressure due to insufficient available disk.  - &#x60;\&quot;MemoryPressure\&quot;&#x60; means the kubelet is under pressure due to insufficient available memory.  - &#x60;\&quot;NetworkUnavailable\&quot;&#x60; means that network for the node is not correctly configured.  - &#x60;\&quot;PIDPressure\&quot;&#x60; means the kubelet is under pressure due to insufficient available PID.  - &#x60;\&quot;Ready\&quot;&#x60; means kubelet is healthy and ready to accept pods. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


