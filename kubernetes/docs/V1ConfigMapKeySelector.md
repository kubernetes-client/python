# V1ConfigMapKeySelector

Selects a key from a ConfigMap.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key to select. | 
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the ConfigMap or its key must be defined | [optional] 

## Example

```python
from kubernetes.client.models.v1_config_map_key_selector import V1ConfigMapKeySelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1ConfigMapKeySelector from a JSON string
v1_config_map_key_selector_instance = V1ConfigMapKeySelector.from_json(json)
# print the JSON string representation of the object
print V1ConfigMapKeySelector.to_json()

# convert the object into a dict
v1_config_map_key_selector_dict = v1_config_map_key_selector_instance.to_dict()
# create an instance of V1ConfigMapKeySelector from a dict
v1_config_map_key_selector_form_dict = v1_config_map_key_selector.from_dict(v1_config_map_key_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


