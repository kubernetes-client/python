# V1CustomResourceValidation

CustomResourceValidation is a list of validation methods for CustomResources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_apiv3_schema** | [**V1JSONSchemaProps**](V1JSONSchemaProps.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_validation import V1CustomResourceValidation

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceValidation from a JSON string
v1_custom_resource_validation_instance = V1CustomResourceValidation.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceValidation.to_json()

# convert the object into a dict
v1_custom_resource_validation_dict = v1_custom_resource_validation_instance.to_dict()
# create an instance of V1CustomResourceValidation from a dict
v1_custom_resource_validation_form_dict = v1_custom_resource_validation.from_dict(v1_custom_resource_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


