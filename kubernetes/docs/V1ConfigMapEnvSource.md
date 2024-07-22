# V1ConfigMapEnvSource

ConfigMapEnvSource selects a ConfigMap to populate the environment variables with.  The contents of the target ConfigMap's Data field will represent the key-value pairs as environment variables.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the ConfigMap must be defined | [optional] 

## Example

```python
from kubernetes.client.models.v1_config_map_env_source import V1ConfigMapEnvSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1ConfigMapEnvSource from a JSON string
v1_config_map_env_source_instance = V1ConfigMapEnvSource.from_json(json)
# print the JSON string representation of the object
print V1ConfigMapEnvSource.to_json()

# convert the object into a dict
v1_config_map_env_source_dict = v1_config_map_env_source_instance.to_dict()
# create an instance of V1ConfigMapEnvSource from a dict
v1_config_map_env_source_form_dict = v1_config_map_env_source.from_dict(v1_config_map_env_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


