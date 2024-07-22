# V1EnvFromSource

EnvFromSource represents the source of a set of ConfigMaps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_ref** | [**V1ConfigMapEnvSource**](V1ConfigMapEnvSource.md) |  | [optional] 
**prefix** | **str** | An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. | [optional] 
**secret_ref** | [**V1SecretEnvSource**](V1SecretEnvSource.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_env_from_source import V1EnvFromSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EnvFromSource from a JSON string
v1_env_from_source_instance = V1EnvFromSource.from_json(json)
# print the JSON string representation of the object
print V1EnvFromSource.to_json()

# convert the object into a dict
v1_env_from_source_dict = v1_env_from_source_instance.to_dict()
# create an instance of V1EnvFromSource from a dict
v1_env_from_source_form_dict = v1_env_from_source.from_dict(v1_env_from_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


