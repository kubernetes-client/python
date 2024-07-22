# V1SecretEnvSource

SecretEnvSource selects a Secret to populate the environment variables with.  The contents of the target Secret's Data field will represent the key-value pairs as environment variables.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the Secret must be defined | [optional] 

## Example

```python
from kubernetes.client.models.v1_secret_env_source import V1SecretEnvSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1SecretEnvSource from a JSON string
v1_secret_env_source_instance = V1SecretEnvSource.from_json(json)
# print the JSON string representation of the object
print V1SecretEnvSource.to_json()

# convert the object into a dict
v1_secret_env_source_dict = v1_secret_env_source_instance.to_dict()
# create an instance of V1SecretEnvSource from a dict
v1_secret_env_source_form_dict = v1_secret_env_source.from_dict(v1_secret_env_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


