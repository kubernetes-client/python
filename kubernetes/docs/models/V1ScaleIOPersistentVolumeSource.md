# kubernetes.client.model.v1_scale_io_persistent_volume_source.V1ScaleIOPersistentVolumeSource

ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ScaleIOPersistentVolumeSource represents a persistent ScaleIO volume | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**system** | str,  | str,  | system is the name of the storage system as configured in ScaleIO. | 
**secretRef** | [**V1SecretReference**](V1SecretReference.md) | [**V1SecretReference**](V1SecretReference.md) |  | 
**gateway** | str,  | str,  | gateway is the host address of the ScaleIO API Gateway. | 
**fsType** | str,  | str,  | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot; | [optional] 
**protectionDomain** | str,  | str,  | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. | [optional] 
**readOnly** | bool,  | BoolClass,  | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**sslEnabled** | bool,  | BoolClass,  | sslEnabled is the flag to enable/disable SSL communication with Gateway, default false | [optional] 
**storageMode** | str,  | str,  | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. | [optional] 
**storagePool** | str,  | str,  | storagePool is the ScaleIO Storage Pool associated with the protection domain. | [optional] 
**volumeName** | str,  | str,  | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

