# V1EmptyDirVolumeSource

Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **str** | medium represents what type of storage medium should back this directory. The default is \&quot;\&quot; which means to use the node&#39;s default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 
**size_limit** | **str** | sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 

## Example

```python
from kubernetes.client.models.v1_empty_dir_volume_source import V1EmptyDirVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EmptyDirVolumeSource from a JSON string
v1_empty_dir_volume_source_instance = V1EmptyDirVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1EmptyDirVolumeSource.to_json()

# convert the object into a dict
v1_empty_dir_volume_source_dict = v1_empty_dir_volume_source_instance.to_dict()
# create an instance of V1EmptyDirVolumeSource from a dict
v1_empty_dir_volume_source_form_dict = v1_empty_dir_volume_source.from_dict(v1_empty_dir_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


