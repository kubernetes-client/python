# V1alpha2DriverRequests

DriverRequests describes all resources that are needed from one particular driver.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_name** | **str** | DriverName is the name used by the DRA driver kubelet plugin. | [optional] 
**requests** | [**list[V1alpha2ResourceRequest]**](V1alpha2ResourceRequest.md) | Requests describes all resources that are needed from the driver. | [optional] 
**vendor_parameters** | [**object**](.md) | VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


