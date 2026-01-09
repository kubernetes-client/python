# V1beta1DeviceClassSpec

DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**list[V1beta1DeviceClassConfiguration]**](V1beta1DeviceClassConfiguration.md) | Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim. | [optional] 
**extended_resource_name** | **str** | ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod&#39;s extended resource requests. It has the same format as the name of a pod&#39;s extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod&#39;s extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is an alpha field. | [optional] 
**selectors** | [**list[V1beta1DeviceSelector]**](V1beta1DeviceSelector.md) | Each selector must be satisfied by a device which is claimed via this class. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


