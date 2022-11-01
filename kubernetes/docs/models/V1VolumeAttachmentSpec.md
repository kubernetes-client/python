# kubernetes.client.model.v1_volume_attachment_spec.V1VolumeAttachmentSpec

VolumeAttachmentSpec is the specification of a VolumeAttachment request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | VolumeAttachmentSpec is the specification of a VolumeAttachment request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nodeName** | str,  | str,  | The node that the volume should be attached to. | 
**source** | [**V1VolumeAttachmentSource**](V1VolumeAttachmentSource.md) | [**V1VolumeAttachmentSource**](V1VolumeAttachmentSource.md) |  | 
**attacher** | str,  | str,  | Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName(). | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

