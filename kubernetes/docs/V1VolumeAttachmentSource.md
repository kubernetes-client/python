# V1VolumeAttachmentSource

VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_volume_spec** | [**V1PersistentVolumeSpec**](V1PersistentVolumeSpec.md) |  | [optional] 
**persistent_volume_name** | **str** | persistentVolumeName represents the name of the persistent volume to attach. | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_attachment_source import V1VolumeAttachmentSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeAttachmentSource from a JSON string
v1_volume_attachment_source_instance = V1VolumeAttachmentSource.from_json(json)
# print the JSON string representation of the object
print V1VolumeAttachmentSource.to_json()

# convert the object into a dict
v1_volume_attachment_source_dict = v1_volume_attachment_source_instance.to_dict()
# create an instance of V1VolumeAttachmentSource from a dict
v1_volume_attachment_source_form_dict = v1_volume_attachment_source.from_dict(v1_volume_attachment_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


