# V1GlusterfsVolumeSource

Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | **str** | endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**path** | **str** | path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | 
**read_only** | **bool** | readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod | [optional] 

## Example

```python
from kubernetes.client.models.v1_glusterfs_volume_source import V1GlusterfsVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1GlusterfsVolumeSource from a JSON string
v1_glusterfs_volume_source_instance = V1GlusterfsVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1GlusterfsVolumeSource.to_json()

# convert the object into a dict
v1_glusterfs_volume_source_dict = v1_glusterfs_volume_source_instance.to_dict()
# create an instance of V1GlusterfsVolumeSource from a dict
v1_glusterfs_volume_source_form_dict = v1_glusterfs_volume_source.from_dict(v1_glusterfs_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


