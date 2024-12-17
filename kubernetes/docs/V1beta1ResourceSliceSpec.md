# V1beta1ResourceSliceSpec

ResourceSliceSpec contains the information published by the driver in one ResourceSlice.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | AllNodes indicates that all nodes have access to the resources in the pool.  Exactly one of NodeName, NodeSelector and AllNodes must be set. | [optional] 
**devices** | [**list[V1beta1Device]**](V1beta1Device.md) | Devices lists some or all of the devices in this pool.  Must not have more than 128 entries. | [optional] 
**driver** | **str** | Driver identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. This field is immutable. | 
**node_name** | **str** | NodeName identifies the node which provides the resources in this pool. A field selector can be used to list only ResourceSlice objects belonging to a certain node.  This field can be used to limit access from nodes to ResourceSlices with the same node name. It also indicates to autoscalers that adding new nodes of the same type as some old node might also make new resources available.  Exactly one of NodeName, NodeSelector and AllNodes must be set. This field is immutable. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**pool** | [**V1beta1ResourcePool**](V1beta1ResourcePool.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


