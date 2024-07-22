# V1HostPathVolumeSource

Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | 
**type** | **str** | type for HostPath Volume Defaults to \&quot;\&quot; More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | [optional] 

## Example

```python
from kubernetes.client.models.v1_host_path_volume_source import V1HostPathVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1HostPathVolumeSource from a JSON string
v1_host_path_volume_source_instance = V1HostPathVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1HostPathVolumeSource.to_json()

# convert the object into a dict
v1_host_path_volume_source_dict = v1_host_path_volume_source_instance.to_dict()
# create an instance of V1HostPathVolumeSource from a dict
v1_host_path_volume_source_form_dict = v1_host_path_volume_source.from_dict(v1_host_path_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


