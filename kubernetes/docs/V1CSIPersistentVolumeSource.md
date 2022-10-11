# V1CSIPersistentVolumeSource

Represents storage that is managed by an external CSI volume driver (Beta feature)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_expand_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**controller_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**driver** | **str** | driver is the name of the driver to use for this volume. Required. | 
**fs_type** | **str** | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. | [optional] 
**node_expand_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**node_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**node_stage_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**read_only** | **bool** | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**volume_attributes** | **dict(str, str)** | volumeAttributes of the volume to publish. | [optional] 
**volume_handle** | **str** | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


