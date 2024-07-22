# V1CinderPersistentVolumeSource

Represents a cinder volume resource in Openstack. A Cinder volume must exist before mounting to a container. The volume must also be in the same region as the kubelet. Cinder volumes support ownership management and SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | [optional] 
**secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**volume_id** | **str** | volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md | 

## Example

```python
from kubernetes.client.models.v1_cinder_persistent_volume_source import V1CinderPersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1CinderPersistentVolumeSource from a JSON string
v1_cinder_persistent_volume_source_instance = V1CinderPersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1CinderPersistentVolumeSource.to_json()

# convert the object into a dict
v1_cinder_persistent_volume_source_dict = v1_cinder_persistent_volume_source_instance.to_dict()
# create an instance of V1CinderPersistentVolumeSource from a dict
v1_cinder_persistent_volume_source_form_dict = v1_cinder_persistent_volume_source.from_dict(v1_cinder_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


