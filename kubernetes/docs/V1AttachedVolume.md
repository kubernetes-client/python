# V1AttachedVolume

AttachedVolume describes a volume attached to a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | DevicePath represents the device path where the volume should be available | 
**name** | **str** | Name of the attached volume | 

## Example

```python
from kubernetes.client.models.v1_attached_volume import V1AttachedVolume

# TODO update the JSON string below
json = "{}"
# create an instance of V1AttachedVolume from a JSON string
v1_attached_volume_instance = V1AttachedVolume.from_json(json)
# print the JSON string representation of the object
print V1AttachedVolume.to_json()

# convert the object into a dict
v1_attached_volume_dict = v1_attached_volume_instance.to_dict()
# create an instance of V1AttachedVolume from a dict
v1_attached_volume_form_dict = v1_attached_volume.from_dict(v1_attached_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


