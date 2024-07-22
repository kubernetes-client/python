# V1ExternalDocumentation

ExternalDocumentation allows referencing an external resource for extended documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_external_documentation import V1ExternalDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of V1ExternalDocumentation from a JSON string
v1_external_documentation_instance = V1ExternalDocumentation.from_json(json)
# print the JSON string representation of the object
print V1ExternalDocumentation.to_json()

# convert the object into a dict
v1_external_documentation_dict = v1_external_documentation_instance.to_dict()
# create an instance of V1ExternalDocumentation from a dict
v1_external_documentation_form_dict = v1_external_documentation.from_dict(v1_external_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


