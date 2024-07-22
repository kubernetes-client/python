# V1FCVolumeSource

Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**lun** | **int** | lun is Optional: FC target lun number | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**target_wwns** | **List[str]** | targetWWNs is Optional: FC target worldwide names (WWNs) | [optional] 
**wwids** | **List[str]** | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. | [optional] 

## Example

```python
from kubernetes.client.models.v1_fc_volume_source import V1FCVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1FCVolumeSource from a JSON string
v1_fc_volume_source_instance = V1FCVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1FCVolumeSource.to_json()

# convert the object into a dict
v1_fc_volume_source_dict = v1_fc_volume_source_instance.to_dict()
# create an instance of V1FCVolumeSource from a dict
v1_fc_volume_source_form_dict = v1_fc_volume_source.from_dict(v1_fc_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


