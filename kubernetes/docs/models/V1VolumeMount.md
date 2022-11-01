# kubernetes.client.model.v1_volume_mount.V1VolumeMount

VolumeMount describes a mounting of a Volume within a container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | VolumeMount describes a mounting of a Volume within a container. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mountPath** | str,  | str,  | Path within the container at which the volume should be mounted.  Must not contain &#x27;:&#x27;. | 
**name** | str,  | str,  | This must match the Name of a Volume. | 
**mountPropagation** | str,  | str,  | mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. | [optional] 
**readOnly** | bool,  | BoolClass,  | Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false. | [optional] 
**subPath** | str,  | str,  | Path within the volume from which the container&#x27;s volume should be mounted. Defaults to \&quot;\&quot; (volume&#x27;s root). | [optional] 
**subPathExpr** | str,  | str,  | Expanded path within the volume from which the container&#x27;s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container&#x27;s environment. Defaults to \&quot;\&quot; (volume&#x27;s root). SubPathExpr and SubPath are mutually exclusive. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

