# V1VolumeAttachmentStatus

VolumeAttachmentStatus is the status of a VolumeAttachment request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_error** | [**V1VolumeError**](V1VolumeError.md) |  | [optional] 
**attached** | **bool** | attached indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | 
**attachment_metadata** | **Dict[str, str]** | attachmentMetadata is populated with any information returned by the attach operation, upon successful attach, that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | [optional] 
**detach_error** | [**V1VolumeError**](V1VolumeError.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_attachment_status import V1VolumeAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeAttachmentStatus from a JSON string
v1_volume_attachment_status_instance = V1VolumeAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print V1VolumeAttachmentStatus.to_json()

# convert the object into a dict
v1_volume_attachment_status_dict = v1_volume_attachment_status_instance.to_dict()
# create an instance of V1VolumeAttachmentStatus from a dict
v1_volume_attachment_status_form_dict = v1_volume_attachment_status.from_dict(v1_volume_attachment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


