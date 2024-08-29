# V1alpha3DeviceAllocationConfiguration

DeviceAllocationConfiguration gets embedded in an AllocationResult.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque** | [**V1alpha3OpaqueDeviceConfiguration**](V1alpha3OpaqueDeviceConfiguration.md) |  | [optional] 
**requests** | **list[str]** | Requests lists the names of requests where the configuration applies. If empty, its applies to all requests. | [optional] 
**source** | **str** | Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


