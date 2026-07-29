# V1beta1Device

Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | [**V1beta1BasicDevice**](V1beta1BasicDevice.md) |  | [optional]
**name** | **str** | Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label. |

## Example

```python
from kubernetes.client.models.v1beta1_device import V1beta1Device

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Device from a JSON string
v1beta1_device_instance = V1beta1Device.from_json(json)
# print the JSON string representation of the object
print(V1beta1Device.to_json())

# convert the object into a dict
v1beta1_device_dict = v1beta1_device_instance.to_dict()
# create an instance of V1beta1Device from a dict
v1beta1_device_from_dict = V1beta1Device.from_dict(v1beta1_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
