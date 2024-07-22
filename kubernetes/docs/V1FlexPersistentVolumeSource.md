# V1FlexPersistentVolumeSource

FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | driver is the name of the driver to use for this volume. | 
**fs_type** | **str** | fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. The default filesystem depends on FlexVolume script. | [optional] 
**options** | **Dict[str, str]** | options is Optional: this field holds extra command options if any. | [optional] 
**read_only** | **bool** | readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_flex_persistent_volume_source import V1FlexPersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlexPersistentVolumeSource from a JSON string
v1_flex_persistent_volume_source_instance = V1FlexPersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1FlexPersistentVolumeSource.to_json()

# convert the object into a dict
v1_flex_persistent_volume_source_dict = v1_flex_persistent_volume_source_instance.to_dict()
# create an instance of V1FlexPersistentVolumeSource from a dict
v1_flex_persistent_volume_source_form_dict = v1_flex_persistent_volume_source.from_dict(v1_flex_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


