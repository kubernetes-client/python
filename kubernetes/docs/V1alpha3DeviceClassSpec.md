# V1alpha3DeviceClassSpec

DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**list[V1alpha3DeviceClassConfiguration]**](V1alpha3DeviceClassConfiguration.md) | Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim. | [optional] 
**selectors** | [**list[V1alpha3DeviceSelector]**](V1alpha3DeviceSelector.md) | Each selector must be satisfied by a device which is claimed via this class. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


