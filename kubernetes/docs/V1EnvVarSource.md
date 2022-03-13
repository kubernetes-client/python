# V1EnvVarSource

EnvVarSource represents a source for the value of an EnvVar.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**field_ref** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) |  | [optional] 
**resource_field_ref** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) |  | [optional] 
**secret_key_ref** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


