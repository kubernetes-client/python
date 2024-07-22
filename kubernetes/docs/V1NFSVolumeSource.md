# V1NFSVolumeSource

Represents an NFS mount that lasts the lifetime of a pod. NFS volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | 
**read_only** | **bool** | readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | [optional] 
**server** | **str** | server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | 

## Example

```python
from kubernetes.client.models.v1_nfs_volume_source import V1NFSVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1NFSVolumeSource from a JSON string
v1_nfs_volume_source_instance = V1NFSVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1NFSVolumeSource.to_json()

# convert the object into a dict
v1_nfs_volume_source_dict = v1_nfs_volume_source_instance.to_dict()
# create an instance of V1NFSVolumeSource from a dict
v1_nfs_volume_source_form_dict = v1_nfs_volume_source.from_dict(v1_nfs_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


