# V1ResourceSliceSpec

ResourceSliceSpec contains the information published by the driver in one ResourceSlice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional]
**devices** | [**List[V1Device]**](V1Device.md) | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. If any device uses taints or consumes counters the limit is 64.  Only one of Devices and SharedCounters can be set in a ResourceSlice. | [optional]
**driver** | **str** | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. This field is immutable. |
**node_name** | **str** | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable. | [optional]
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional]
**partition_type_attribute** | **str** | PartitionTypeAttribute names a string device attribute (by fully qualified name, e.g. \&quot;gpu.example.com/profile\&quot;) whose value labels each device with its partition type, such as \&quot;Full\&quot; or \&quot;Half\&quot; for a MIG-style GPU.  When set, every partitionable device in the slice must carry the attribute and devices sharing a value must share the same ConsumesCounters cost. | [optional]
**per_device_node_selection** | **bool** | PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional]
**pool** | [**V1ResourcePool**](V1ResourcePool.md) |  |
**shared_counters** | [**List[V1CounterSet]**](V1CounterSet.md) | SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the counter sets must be unique in the ResourcePool.  Only one of Devices and SharedCounters can be set in a ResourceSlice.  The maximum number of counter sets is 8. | [optional]
**skip_node_operations** | **List[str]** | SkipNodeOperations lists node-local resource operations (gRPC calls) that will be skipped for the devices in this slice when determining whether operations are necessary on the node. If all allocated devices for a driver in a claim skip an operation, that gRPC call will be skipped. Valid values are:  - \&quot;NodePrepareResources\&quot;: NodePrepareResources gRPC calls are skipped. This   value cannot be specified unless \&quot;NodeUnprepareResources\&quot; is also listed   (or \&quot;*\&quot; is specified). - \&quot;NodeUnprepareResources\&quot;: NodeUnprepareResources gRPC calls are skipped. - \&quot;*\&quot;: All node-local resource operations are skipped.  Other values may be added in the future. The kubelet must ignore unknown values. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_resource_slice_spec import V1ResourceSliceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceSliceSpec from a JSON string
v1_resource_slice_spec_instance = V1ResourceSliceSpec.from_json(json)
# print the JSON string representation of the object
print(V1ResourceSliceSpec.to_json())

# convert the object into a dict
v1_resource_slice_spec_dict = v1_resource_slice_spec_instance.to_dict()
# create an instance of V1ResourceSliceSpec from a dict
v1_resource_slice_spec_from_dict = V1ResourceSliceSpec.from_dict(v1_resource_slice_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
