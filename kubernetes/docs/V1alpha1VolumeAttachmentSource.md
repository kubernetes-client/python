# V1alpha1VolumeAttachmentSource

VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_volume_spec** | [**V1PersistentVolumeSpec**](V1PersistentVolumeSpec.md) |  | [optional] 
**persistent_volume_name** | **str** | Name of the persistent volume to attach. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


