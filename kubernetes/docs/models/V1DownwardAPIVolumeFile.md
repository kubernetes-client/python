# kubernetes.client.model.v1_downward_api_volume_file.V1DownwardAPIVolumeFile

DownwardAPIVolumeFile represents information to create the file containing the pod field

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DownwardAPIVolumeFile represents information to create the file containing the pod field | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**path** | str,  | str,  | Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the &#x27;..&#x27; path. Must be utf-8 encoded. The first item of the relative path must not start with &#x27;..&#x27; | 
**fieldRef** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) |  | [optional] 
**mode** | decimal.Decimal, int,  | decimal.Decimal,  | Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] value must be a 32 bit integer
**resourceFieldRef** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

