# V1NodeAllocatableOverheadResources

NodeAllocatableOverheadResources describes auxiliary overhead resource allocations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the resource (e.g., cpu, memory). |
**per_container** | **str** | PerContainer is the variable overhead quantity applied for each container referencing the claim. The container references are recorded in &#x60;nodeAllocatableResourceClaimStatuses.containers&#x60;. The total overhead quantity allocated for the claim is computed as: Quantity &#x3D; PerPod + (PerContainer * NumReferences) Kubelet accounts for this overhead in cgroups: - Pod-level cgroup (requests and limits): Kubelet adds PerPod + (PerContainer * NumReferences). - Container-level cgroup (limits only): Kubelet adds PerPod + PerContainer for each referencing container. This allows any single container to access the pod-level overhead, while the parent cgroup caps the total usage to account for PerPod exactly once. At least one of PerPod or PerContainer must be specified. Specifying neither is an invalid configuration. | [optional]
**per_pod** | **str** | PerPod is the flat overhead quantity allocated per pod. Adding to each container limit allows individual containers to utilize the overhead, while the parent pod-level cgroup limit caps the total usage at the pod boundary where the overhead is accounted for exactly once. At least one of PerPod or PerContainer must be specified. Specifying neither is an invalid configuration. | [optional]

## Example

```python
from kubernetes.client.models.v1_node_allocatable_overhead_resources import V1NodeAllocatableOverheadResources

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAllocatableOverheadResources from a JSON string
v1_node_allocatable_overhead_resources_instance = V1NodeAllocatableOverheadResources.from_json(json)
# print the JSON string representation of the object
print(V1NodeAllocatableOverheadResources.to_json())

# convert the object into a dict
v1_node_allocatable_overhead_resources_dict = v1_node_allocatable_overhead_resources_instance.to_dict()
# create an instance of V1NodeAllocatableOverheadResources from a dict
v1_node_allocatable_overhead_resources_from_dict = V1NodeAllocatableOverheadResources.from_dict(v1_node_allocatable_overhead_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
