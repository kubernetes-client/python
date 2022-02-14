# V1Taint

The node this Taint is attached to has the \"effect\" on any pod that does not tolerate the Taint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  Possible enum values:  - &#x60;\&quot;NoExecute\&quot;&#x60; Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController.  - &#x60;\&quot;NoSchedule\&quot;&#x60; Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler.  - &#x60;\&quot;PreferNoSchedule\&quot;&#x60; Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler. | 
**key** | **str** | Required. The taint key to be applied to a node. | 
**time_added** | **datetime** | TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. | [optional] 
**value** | **str** | The taint value corresponding to the taint key. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


