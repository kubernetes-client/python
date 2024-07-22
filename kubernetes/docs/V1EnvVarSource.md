# V1EnvVarSource

EnvVarSource represents a source for the value of an EnvVar.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**field_ref** | [**V1ObjectFieldSelector**](V1ObjectFieldSelector.md) |  | [optional] 
**resource_field_ref** | [**V1ResourceFieldSelector**](V1ResourceFieldSelector.md) |  | [optional] 
**secret_key_ref** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_env_var_source import V1EnvVarSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnvVarSource from a JSON string
v1_env_var_source_instance = V1EnvVarSource.from_json(json)
# print the JSON string representation of the object
print V1EnvVarSource.to_json()

# convert the object into a dict
v1_env_var_source_dict = v1_env_var_source_instance.to_dict()
# create an instance of V1EnvVarSource from a dict
v1_env_var_source_form_dict = v1_env_var_source.from_dict(v1_env_var_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


