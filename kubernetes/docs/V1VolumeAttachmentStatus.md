# V1VolumeAttachmentStatus

VolumeAttachmentStatus is the status of a VolumeAttachment request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached** | **bool** | Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | 
**attach_error** | [**V1VolumeError**](V1VolumeError.md) |  | [optional] 
**attachment_metadata** | **{str: (str,)}** | Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | [optional] 
**detach_error** | [**V1VolumeError**](V1VolumeError.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


