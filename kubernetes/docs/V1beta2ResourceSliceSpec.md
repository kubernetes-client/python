# V1beta2ResourceSliceSpec

ResourceSliceSpec contains the information published by the driver in one ResourceSlice.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional] 
**devices** | [**list[V1beta2Device]**](V1beta2Device.md) | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. | [optional] 
**driver** | **str** | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. This field is immutable. | 
**node_name** | **str** | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. This field is immutable. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**per_device_node_selection** | **bool** | PerDeviceNodeSelection defines whether the access from nodes to resources in the pool is set on the ResourceSlice level or on each device. If it is set to true, every device defined the ResourceSlice must specify this individually.  Exactly one of NodeName, NodeSelector, AllNodes, and PerDeviceNodeSelection must be set. | [optional] 
**pool** | [**V1beta2ResourcePool**](V1beta2ResourcePool.md) |  | 
**shared_counters** | [**list[V1beta2CounterSet]**](V1beta2CounterSet.md) | SharedCounters defines a list of counter sets, each of which has a name and a list of counters available.  The names of the SharedCounters must be unique in the ResourceSlice.  The maximum number of counters in all sets is 32. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


