# V1PhotonPersistentDiskVolumeSource

Represents a Photon Controller persistent disk resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**pd_id** | **str** | pdID is the ID that identifies Photon Controller persistent disk | 

## Example

```python
from kubernetes.client.models.v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1PhotonPersistentDiskVolumeSource from a JSON string
v1_photon_persistent_disk_volume_source_instance = V1PhotonPersistentDiskVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1PhotonPersistentDiskVolumeSource.to_json()

# convert the object into a dict
v1_photon_persistent_disk_volume_source_dict = v1_photon_persistent_disk_volume_source_instance.to_dict()
# create an instance of V1PhotonPersistentDiskVolumeSource from a dict
v1_photon_persistent_disk_volume_source_form_dict = v1_photon_persistent_disk_volume_source.from_dict(v1_photon_persistent_disk_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


