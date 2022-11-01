# kubernetes.client.model.v1_env_var_source.V1EnvVarSource

EnvVarSource represents a source for the value of an EnvVar.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EnvVarSource represents a source for the value of an EnvVar. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configMapKeyRef** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**fieldRef** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) |  | [optional] 
**resourceFieldRef** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) |  | [optional] 
**secretKeyRef** | [**V1SecretKeySelector**](V1SecretKeySelector.md) | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

