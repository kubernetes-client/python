# V1alpha3OpaqueDeviceConfiguration

OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. | 
**parameters** | [**object**](.md) | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version (\&quot;kind\&quot; + \&quot;apiVersion\&quot; for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


