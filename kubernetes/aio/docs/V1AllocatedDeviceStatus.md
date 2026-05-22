# V1AllocatedDeviceStatus

AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.  The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1Condition]**](V1Condition.md) | Conditions contains the latest observation of the device&#39;s state. If the device has been configured according to the class and claim config references, the &#x60;Ready&#x60; condition should be True.  Must not contain more than 8 entries. | [optional] 
**data** | **object** | Data contains arbitrary driver-specific data.  The length of the raw data must be smaller or equal to 10 Ki. | [optional] 
**device** | **str** | Device references one device instance via its name in the driver&#39;s resource pool. It must be a DNS label. | 
**driver** | **str** | Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. | 
**network_data** | [**V1NetworkDeviceData**](V1NetworkDeviceData.md) |  | [optional] 
**pool** | **str** | This name together with the driver name and the device name field identify which device was allocated (&#x60;&lt;driver name&gt;/&lt;pool name&gt;/&lt;device name&gt;&#x60;).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes. | 
**share_id** | **str** | ShareID uniquely identifies an individual allocation share of the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


