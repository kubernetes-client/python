# V1LocalVolumeSource

Local represents directly-attached storage with node affinity (Beta feature)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. It applies only when the Path is a block device. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. The default value is to auto-select a filesystem if unspecified. | [optional] 
**path** | **str** | path of the full path to the volume on the node. It can be either a directory or block device (disk, partition, ...). | 

## Example

```python
from kubernetes.client.models.v1_local_volume_source import V1LocalVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1LocalVolumeSource from a JSON string
v1_local_volume_source_instance = V1LocalVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1LocalVolumeSource.to_json()

# convert the object into a dict
v1_local_volume_source_dict = v1_local_volume_source_instance.to_dict()
# create an instance of V1LocalVolumeSource from a dict
v1_local_volume_source_form_dict = v1_local_volume_source.from_dict(v1_local_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


