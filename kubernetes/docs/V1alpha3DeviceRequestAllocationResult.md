# V1alpha3DeviceRequestAllocationResult

DeviceRequestAllocationResult contains the allocation result for one request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_access** | **bool** | AdminAccess indicates that this device was allocated for administrative access. See the corresponding request field for a definition of mode.  This is an alpha field and requires enabling the DRAAdminAccess feature gate. Admin access is disabled if this field is unset or set to false, otherwise it is enabled. | [optional] 
**device** | **str** | Device references one device instance via its name in the driver&#39;s resource pool. It must be a DNS label. | 
**driver** | **str** | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. | 
**pool** | **str** | This name together with the driver name and the device name field identify which device was allocated (&#x60;&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;&#x60;).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. | 
**request** | **str** | Request is the name of the request in the claim which caused this device to be allocated. Multiple devices may have been allocated per request. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


