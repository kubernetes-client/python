# V1beta1DeviceSelector

DeviceSelector must have exactly one field set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cel** | [**V1beta1CELDeviceSelector**](V1beta1CELDeviceSelector.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_device_selector import V1beta1DeviceSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceSelector from a JSON string
v1beta1_device_selector_instance = V1beta1DeviceSelector.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceSelector.to_json())

# convert the object into a dict
v1beta1_device_selector_dict = v1beta1_device_selector_instance.to_dict()
# create an instance of V1beta1DeviceSelector from a dict
v1beta1_device_selector_from_dict = V1beta1DeviceSelector.from_dict(v1beta1_device_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
