# V1DeviceClass

DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1DeviceClassSpec**](V1DeviceClassSpec.md) |  |

## Example

```python
from kubernetes.client.models.v1_device_class import V1DeviceClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceClass from a JSON string
v1_device_class_instance = V1DeviceClass.from_json(json)
# print the JSON string representation of the object
print(V1DeviceClass.to_json())

# convert the object into a dict
v1_device_class_dict = v1_device_class_instance.to_dict()
# create an instance of V1DeviceClass from a dict
v1_device_class_from_dict = V1DeviceClass.from_dict(v1_device_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
