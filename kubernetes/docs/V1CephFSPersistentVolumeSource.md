# V1CephFSPersistentVolumeSource

Represents a Ceph Filesystem mount that lasts the lifetime of a pod Cephfs volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | **List[str]** | monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | 
**path** | **str** | path is Optional: Used as the mounted root, rather than the full Ceph tree, default is / | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_file** | **str** | secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**user** | **str** | user is Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it | [optional] 

## Example

```python
from kubernetes.client.models.v1_ceph_fs_persistent_volume_source import V1CephFSPersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1CephFSPersistentVolumeSource from a JSON string
v1_ceph_fs_persistent_volume_source_instance = V1CephFSPersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1CephFSPersistentVolumeSource.to_json()

# convert the object into a dict
v1_ceph_fs_persistent_volume_source_dict = v1_ceph_fs_persistent_volume_source_instance.to_dict()
# create an instance of V1CephFSPersistentVolumeSource from a dict
v1_ceph_fs_persistent_volume_source_form_dict = v1_ceph_fs_persistent_volume_source.from_dict(v1_ceph_fs_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


