# V1SecretKeySelector

SecretKeySelector selects a key of a Secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the secret to select from.  Must be a valid secret key. | 
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the Secret or its key must be defined | [optional] 

## Example

```python
from kubernetes.client.models.v1_secret_key_selector import V1SecretKeySelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1SecretKeySelector from a JSON string
v1_secret_key_selector_instance = V1SecretKeySelector.from_json(json)
# print the JSON string representation of the object
print V1SecretKeySelector.to_json()

# convert the object into a dict
v1_secret_key_selector_dict = v1_secret_key_selector_instance.to_dict()
# create an instance of V1SecretKeySelector from a dict
v1_secret_key_selector_form_dict = v1_secret_key_selector.from_dict(v1_secret_key_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


