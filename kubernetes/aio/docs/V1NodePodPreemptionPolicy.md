# V1NodePodPreemptionPolicy

NodePodPreemptionPolicy defines the node-level policies governing preemption for pods on this node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_resize_preemption** | **List[str]** | DisableResizePreemption lists the owners (e.g., autoscalers, operators, administrators) that have requested to disable scheduler and Kubelet preemption for in-place pod resize on this node. If this list is non-empty, resize-induced preemption is disabled on this node. This is an alpha field and requires enabling the InPlacePodVerticalScalingSchedulerPreemption feature gate. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_node_pod_preemption_policy import V1NodePodPreemptionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodePodPreemptionPolicy from a JSON string
v1_node_pod_preemption_policy_instance = V1NodePodPreemptionPolicy.from_json(json)
# print the JSON string representation of the object
print(V1NodePodPreemptionPolicy.to_json())

# convert the object into a dict
v1_node_pod_preemption_policy_dict = v1_node_pod_preemption_policy_instance.to_dict()
# create an instance of V1NodePodPreemptionPolicy from a dict
v1_node_pod_preemption_policy_from_dict = V1NodePodPreemptionPolicy.from_dict(v1_node_pod_preemption_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
