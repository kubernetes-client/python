# V1beta1DeviceClassSpec

DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1beta1DeviceClassConfiguration]**](V1beta1DeviceClassConfiguration.md) | Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.  They are passed to the driver, but are not considered while allocating the claim. | [optional]
**extended_resource_name** | **str** | ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod&#39;s extended resource requests. It has the same format as the name of a pod&#39;s extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod&#39;s extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.  This is a beta field. | [optional]
**selectors** | [**List[V1beta1DeviceSelector]**](V1beta1DeviceSelector.md) | Each selector must be satisfied by a device which is claimed via this class. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_device_class_spec import V1beta1DeviceClassSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceClassSpec from a JSON string
v1beta1_device_class_spec_instance = V1beta1DeviceClassSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceClassSpec.to_json())

# convert the object into a dict
v1beta1_device_class_spec_dict = v1beta1_device_class_spec_instance.to_dict()
# create an instance of V1beta1DeviceClassSpec from a dict
v1beta1_device_class_spec_from_dict = V1beta1DeviceClassSpec.from_dict(v1beta1_device_class_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
