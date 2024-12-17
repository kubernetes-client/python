# V1beta1BasicDevice

BasicDevice defines one device instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**dict(str, V1beta1DeviceAttribute)**](V1beta1DeviceAttribute.md) | Attributes defines the set of attributes for this device. The name of each attribute must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 
**capacity** | [**dict(str, V1beta1DeviceCapacity)**](V1beta1DeviceCapacity.md) | Capacity defines the set of capacities for this device. The name of each capacity must be unique in that set.  The maximum number of attributes and capacities combined is 32. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


