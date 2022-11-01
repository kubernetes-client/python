# kubernetes.client.model.v1_volume_projection.V1VolumeProjection

Projection that may be projected along with other supported volume types

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Projection that may be projected along with other supported volume types | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configMap** | [**V1ConfigMapProjection**](V1ConfigMapProjection.md) | [**V1ConfigMapProjection**](V1ConfigMapProjection.md) |  | [optional] 
**downwardAPI** | [**V1DownwardAPIProjection**](V1DownwardAPIProjection.md) | [**V1DownwardAPIProjection**](V1DownwardAPIProjection.md) |  | [optional] 
**secret** | [**V1SecretProjection**](V1SecretProjection.md) | [**V1SecretProjection**](V1SecretProjection.md) |  | [optional] 
**serviceAccountToken** | [**V1ServiceAccountTokenProjection**](V1ServiceAccountTokenProjection.md) | [**V1ServiceAccountTokenProjection**](V1ServiceAccountTokenProjection.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

