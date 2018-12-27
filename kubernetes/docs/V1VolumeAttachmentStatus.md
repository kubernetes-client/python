# V1VolumeAttachmentStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_error** | [**V1VolumeError**](V1VolumeError.md) | The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | [optional] 
**attached** | **bool** | Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | 
**attachment_metadata** | **dict(str, str)** | Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher. | [optional] 
**detach_error** | [**V1VolumeError**](V1VolumeError.md) | The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


