# kubernetes.client.model.v1_ephemeral_volume_source.V1EphemeralVolumeSource

Represents an ephemeral volume that is handled by a normal storage driver.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents an ephemeral volume that is handled by a normal storage driver. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**volumeClaimTemplate** | [**V1PersistentVolumeClaimTemplate**](V1PersistentVolumeClaimTemplate.md) | [**V1PersistentVolumeClaimTemplate**](V1PersistentVolumeClaimTemplate.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

