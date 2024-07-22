# V1VolumeAttachmentSpec

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacher** | **str** | attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). | 
**node_name** | **str** | nodeName represents the node that the volume should be attached to. | 
**source** | [**V1VolumeAttachmentSource**](V1VolumeAttachmentSource.md) |  | 

## Example

```python
from kubernetes.client.models.v1_volume_attachment_spec import V1VolumeAttachmentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeAttachmentSpec from a JSON string
v1_volume_attachment_spec_instance = V1VolumeAttachmentSpec.from_json(json)
# print the JSON string representation of the object
print V1VolumeAttachmentSpec.to_json()

# convert the object into a dict
v1_volume_attachment_spec_dict = v1_volume_attachment_spec_instance.to_dict()
# create an instance of V1VolumeAttachmentSpec from a dict
v1_volume_attachment_spec_form_dict = v1_volume_attachment_spec.from_dict(v1_volume_attachment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


