# V1NodeAllocatableMapping

NodeAllocatableMapping defines how a DRA allocation directly translates into a node allocatable resource quantity. The mapping can be derived from either the count of allocated devices (via deviceMultiplier) or the specific capacity consumed (via capacityKey and capacityMultiplier). These options are mutually exclusive. Kubelet adds this mapped resource quantity from claim to both requests and limits at the pod-level cgroup, and to limits at the container-level cgroup for each container referencing the claim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_key** | **str** | CapacityKey references a capacity name defined as a key in the &#x60;spec.devices[*].capacity&#x60; map. When this field is set, the value associated with this key in the &#x60;status.allocation.devices.results[*].consumedCapacity&#x60; map (for a specific claim allocation) determines the base quantity for the node allocatable resource. &#x60;capacityMultiplier&#x60; must also be set and is multiplied with the base quantity. For example, if &#x60;spec.devices[*].capacity&#x60; has an entry \&quot;dra.example.com/memory\&quot;: \&quot;128Gi\&quot;, and this field is set to \&quot;dra.example.com/memory\&quot;, then for a claim allocation that consumes { \&quot;dra.example.com/memory\&quot;: \&quot;4Gi\&quot; } the base quantity for the node allocatable resource mapping will be \&quot;4Gi\&quot;. The final node allocatable resource amount is &#x60;consumedCapacity[capacityKey]&#x60; * &#x60;capacityMultiplier&#x60;. | [optional]
**capacity_multiplier** | **str** | CapacityMultiplier is used as a multiplier for the allocated capacity consumed. It is only valid if &#x60;capacityKey&#x60; is set. The final node allocatable resource amount is &#x60;consumedCapacity[capacityKey]&#x60; * &#x60;capacityMultiplier&#x60;. For example, if a Device&#39;s capacity \&quot;dra.example.com/cores\&quot; is consumed, and each \&quot;core\&quot; provides 2 \&quot;cpu\&quot;s, the mapping would be: {ResourceName: \&quot;cpu\&quot;, capacityKey: \&quot;dra.example.com/cores\&quot;, capacityMultiplier: \&quot;2\&quot;}. If a claim consumes 8 \&quot;dra.example.com/cores\&quot;, the CPU footprint is 8 * 2 &#x3D; 16. | [optional]
**device_multiplier** | **str** | DeviceMultiplier is used as a multiplier for the allocated device count in the claim. The final node allocatable resource amount is &#x60;deviceCount&#x60; * &#x60;deviceMultiplier&#x60;. For example, a DRA driver representing each cache complex (CCX) as a device would have {ResourceName: \&quot;cpu\&quot;, deviceMultiplier: \&quot;8\&quot;} in its &#x60;nodeAllocatableResources&#x60;. If 2 devices (CCX) are allocated to the claim, 2 * 8 &#x3D; 16 CPUs would be considered as allocated. It is only valid when &#x60;capacityKey&#x60; and &#x60;capacityMultiplier&#x60; are not set. | [optional]

## Example

```python
from kubernetes.client.models.v1_node_allocatable_mapping import V1NodeAllocatableMapping

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAllocatableMapping from a JSON string
v1_node_allocatable_mapping_instance = V1NodeAllocatableMapping.from_json(json)
# print the JSON string representation of the object
print(V1NodeAllocatableMapping.to_json())

# convert the object into a dict
v1_node_allocatable_mapping_dict = v1_node_allocatable_mapping_instance.to_dict()
# create an instance of V1NodeAllocatableMapping from a dict
v1_node_allocatable_mapping_from_dict = V1NodeAllocatableMapping.from_dict(v1_node_allocatable_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
