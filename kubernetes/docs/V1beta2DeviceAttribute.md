# V1beta2DeviceAttribute

DeviceAttribute must have exactly one field set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** | BoolValue is a true/false value. | [optional]
**bools** | **List[bool]** | BoolValues is a non-empty list of true/false values. | [optional]
**int** | **int** | IntValue is a number. | [optional]
**ints** | **List[int]** | IntValues is a non-empty list of numbers.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional]
**string** | **str** | StringValue is a string. Must not be longer than 64 characters. | [optional]
**strings** | **List[str]** | StringValues is a non-empty list of strings. Each string must not be longer than 64 characters.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional]
**version** | **str** | VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters. | [optional]
**versions** | **List[str]** | VersionValues is a non-empty list of semantic versions according to semver.org spec 2.0.0. Each version string must not be longer than 64 characters.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional]

## Example

```python
from kubernetes.client.models.v1beta2_device_attribute import V1beta2DeviceAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceAttribute from a JSON string
v1beta2_device_attribute_instance = V1beta2DeviceAttribute.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceAttribute.to_json())

# convert the object into a dict
v1beta2_device_attribute_dict = v1beta2_device_attribute_instance.to_dict()
# create an instance of V1beta2DeviceAttribute from a dict
v1beta2_device_attribute_from_dict = V1beta2DeviceAttribute.from_dict(v1beta2_device_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
