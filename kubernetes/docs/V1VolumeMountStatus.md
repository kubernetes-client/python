# V1VolumeMountStatus

VolumeMountStatus shows status of volume mounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | MountPath corresponds to the original VolumeMount. | 
**name** | **str** | Name corresponds to the name of the original VolumeMount. | 
**read_only** | **bool** | ReadOnly corresponds to the original VolumeMount. | [optional] 
**recursive_read_only** | **str** | RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result. | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_mount_status import V1VolumeMountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeMountStatus from a JSON string
v1_volume_mount_status_instance = V1VolumeMountStatus.from_json(json)
# print the JSON string representation of the object
print V1VolumeMountStatus.to_json()

# convert the object into a dict
v1_volume_mount_status_dict = v1_volume_mount_status_instance.to_dict()
# create an instance of V1VolumeMountStatus from a dict
v1_volume_mount_status_form_dict = v1_volume_mount_status.from_dict(v1_volume_mount_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


