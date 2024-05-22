# V1alpha2ResourceHandle

ResourceHandle holds opaque resource data for processing by a specific kubelet plugin.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. | [optional] 
**driver_name** | **str** | DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle&#39;s data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in. | [optional] 
**structured_data** | [**V1alpha2StructuredResourceHandle**](V1alpha2StructuredResourceHandle.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


