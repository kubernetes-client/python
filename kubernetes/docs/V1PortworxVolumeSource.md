# V1PortworxVolumeSource

PortworxVolumeSource represents a Portworx volume resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**volume_id** | **str** | volumeID uniquely identifies a Portworx volume | 

## Example

```python
from kubernetes.client.models.v1_portworx_volume_source import V1PortworxVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortworxVolumeSource from a JSON string
v1_portworx_volume_source_instance = V1PortworxVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1PortworxVolumeSource.to_json()

# convert the object into a dict
v1_portworx_volume_source_dict = v1_portworx_volume_source_instance.to_dict()
# create an instance of V1PortworxVolumeSource from a dict
v1_portworx_volume_source_form_dict = v1_portworx_volume_source.from_dict(v1_portworx_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


