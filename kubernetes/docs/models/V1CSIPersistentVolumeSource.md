# kubernetes.client.model.v1_csi_persistent_volume_source.V1CSIPersistentVolumeSource

Represents storage that is managed by an external CSI volume driver (Beta feature)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents storage that is managed by an external CSI volume driver (Beta feature) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**driver** | str,  | str,  | driver is the name of the driver to use for this volume. Required. | 
**volumeHandle** | str,  | str,  | volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | 
**controllerExpandSecretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**controllerPublishSecretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**fsType** | str,  | str,  | fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. | [optional] 
**nodeExpandSecretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**nodePublishSecretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**nodeStageSecretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | [optional] 
**readOnly** | bool,  | BoolClass,  | readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**[volumeAttributes](#volumeAttributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | volumeAttributes of the volume to publish. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# volumeAttributes

volumeAttributes of the volume to publish.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | volumeAttributes of the volume to publish. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

