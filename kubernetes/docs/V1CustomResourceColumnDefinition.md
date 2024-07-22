# V1CustomResourceColumnDefinition

CustomResourceColumnDefinition specifies a column for server side printing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description is a human readable description of this column. | [optional] 
**format** | **str** | format is an optional OpenAPI type definition for this column. The &#39;name&#39; format is applied to the primary identifier column to assist in kubernetes.clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. | [optional] 
**json_path** | **str** | jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column. | 
**name** | **str** | name is a human readable name for the column. | 
**priority** | **int** | priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0. | [optional] 
**type** | **str** | type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details. | 

## Example

```python
from kubernetes.client.models.v1_custom_resource_column_definition import V1CustomResourceColumnDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceColumnDefinition from a JSON string
v1_custom_resource_column_definition_instance = V1CustomResourceColumnDefinition.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceColumnDefinition.to_json()

# convert the object into a dict
v1_custom_resource_column_definition_dict = v1_custom_resource_column_definition_instance.to_dict()
# create an instance of V1CustomResourceColumnDefinition from a dict
v1_custom_resource_column_definition_form_dict = v1_custom_resource_column_definition.from_dict(v1_custom_resource_column_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


