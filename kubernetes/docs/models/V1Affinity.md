# kubernetes.client.model.v1_affinity.V1Affinity

Affinity is a group of affinity scheduling rules.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Affinity is a group of affinity scheduling rules. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nodeAffinity** | [**V1NodeAffinity**](V1NodeAffinity.md) | [**V1NodeAffinity**](V1NodeAffinity.md) |  | [optional] 
**podAffinity** | [**V1PodAffinity**](V1PodAffinity.md) | [**V1PodAffinity**](V1PodAffinity.md) |  | [optional] 
**podAntiAffinity** | [**V1PodAntiAffinity**](V1PodAntiAffinity.md) | [**V1PodAntiAffinity**](V1PodAntiAffinity.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

