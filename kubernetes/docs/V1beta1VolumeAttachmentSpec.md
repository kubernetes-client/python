# V1beta1VolumeAttachmentSpec

VolumeAttachmentSpec is the specification of a VolumeAttachment request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacher** | **str** | Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). | 
**node_name** | **str** | The node that the volume should be attached to. | 
**source** | [**V1beta1VolumeAttachmentSource**](V1beta1VolumeAttachmentSource.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


