# V1PodCondition

PodCondition contains details for the current condition of this pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | Last time we probed the condition. | [optional] 
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | Human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions | 
**type** | **str** | Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions  Possible enum values:  - &#x60;\&quot;ContainersReady\&quot;&#x60; indicates whether all containers in the pod are ready.  - &#x60;\&quot;Initialized\&quot;&#x60; means that all init containers in the pod have started successfully.  - &#x60;\&quot;PodScheduled\&quot;&#x60; represents status of the scheduling process for this pod.  - &#x60;\&quot;Ready\&quot;&#x60; means the pod is able to service requests and should be added to the load balancing pools of all matching services. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


