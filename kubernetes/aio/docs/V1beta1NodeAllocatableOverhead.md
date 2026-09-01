# V1beta1NodeAllocatableOverhead

NodeAllocatableOverhead defines auxiliary resource overheads incurred when allocating a device. Overheads can be specified as a fixed cost per pod referencing the claim, a variable cost per container reference, or both. Kubelet accounts for this overhead by adding it to both the pod-level and container-level cgroups of referencing containers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_container** | **str** | PerContainer is applied per container reference to the claim. This models overhead scaling linearly with the number of containers actively using the device. When both PerPod and PerContainer are specified, the total overhead allocated for each pod referencing the claim is computed as: Quantity &#x3D; PerPod + (PerContainer * NumReferences) Kubelet accounts for this overhead in cgroups: - Pod-level cgroup (requests and limits): Kubelet adds PerPod + (PerContainer * NumReferences). - Container-level cgroup (limits only): Kubelet adds PerPod + PerContainer for each referencing container. This allows any single container to access the pod-level overhead, while the parent cgroup caps the total usage to account for PerPod exactly once. | [optional]
**per_pod** | **str** | PerPod is overhead applied once per pod referencing the claim on this node. This is a flat overhead incurred for every pod referencing the claim. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_node_allocatable_overhead import V1beta1NodeAllocatableOverhead

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1NodeAllocatableOverhead from a JSON string
v1beta1_node_allocatable_overhead_instance = V1beta1NodeAllocatableOverhead.from_json(json)
# print the JSON string representation of the object
print(V1beta1NodeAllocatableOverhead.to_json())

# convert the object into a dict
v1beta1_node_allocatable_overhead_dict = v1beta1_node_allocatable_overhead_instance.to_dict()
# create an instance of V1beta1NodeAllocatableOverhead from a dict
v1beta1_node_allocatable_overhead_from_dict = V1beta1NodeAllocatableOverhead.from_dict(v1beta1_node_allocatable_overhead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
