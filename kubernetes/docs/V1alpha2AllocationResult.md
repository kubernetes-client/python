# V1alpha2AllocationResult

AllocationResult contains attributes of an allocated resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_on_nodes** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**resource_handles** | [**list[V1alpha2ResourceHandle]**](V1alpha2ResourceHandle.md) | ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  Setting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in. | [optional] 
**shareable** | **bool** | Shareable determines whether the resource supports more than one consumer at a time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


