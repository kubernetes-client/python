# kubernetes.client.model.v1_env_from_source.V1EnvFromSource

EnvFromSource represents the source of a set of ConfigMaps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EnvFromSource represents the source of a set of ConfigMaps | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configMapRef** | [**V1ConfigMapEnvSource**](V1ConfigMapEnvSource.md) | [**V1ConfigMapEnvSource**](V1ConfigMapEnvSource.md) |  | [optional] 
**prefix** | str,  | str,  | An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. | [optional] 
**secretRef** | [**V1SecretEnvSource**](V1SecretEnvSource.md) | [**V1SecretEnvSource**](V1SecretEnvSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

