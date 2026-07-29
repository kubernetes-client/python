# V1VolumeStatus

VolumeStatus represents the status of a mounted volume. At most one of its members must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**V1ImageVolumeStatus**](V1ImageVolumeStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1_volume_status import V1VolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeStatus from a JSON string
v1_volume_status_instance = V1VolumeStatus.from_json(json)
# print the JSON string representation of the object
print(V1VolumeStatus.to_json())

# convert the object into a dict
v1_volume_status_dict = v1_volume_status_instance.to_dict()
# create an instance of V1VolumeStatus from a dict
v1_volume_status_from_dict = V1VolumeStatus.from_dict(v1_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
