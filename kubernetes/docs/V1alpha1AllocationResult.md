# V1alpha1AllocationResult

AllocationResult contains attributed of an allocated resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_on_nodes** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**resource_handle** | **str** | ResourceHandle contains arbitrary data returned by the driver after a successful allocation. This is opaque for Kubernetes. Driver documentation may explain to users how to interpret this data if needed.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. | [optional] 
**shareable** | **bool** | Shareable determines whether the resource supports more than one consumer at a time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


