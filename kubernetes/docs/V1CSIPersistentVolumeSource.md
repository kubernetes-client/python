# V1CSIPersistentVolumeSource

Represents storage that is managed by an external CSI volume driver (Beta feature)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is the name of the driver to use for this volume. Required. | 
**volume_handle** | **str** | VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | 
**controller_expand_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**controller_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**fs_type** | **str** | Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. | [optional] 
**node_publish_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**node_stage_secret_ref** | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**read_only** | **bool** | Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**volume_attributes** | **{str: (str,)}** | Attributes of the volume to publish. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


