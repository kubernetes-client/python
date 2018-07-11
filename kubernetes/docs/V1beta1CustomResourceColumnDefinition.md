# V1beta1CustomResourceColumnDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_path** | **str** | JSONPath is a simple JSON path, i.e. with array notation. | 
**description** | **str** | description is a human readable description of this column. | [optional] 
**format** | **str** | format is an optional OpenAPI type definition for this column. The &#39;name&#39; format is applied to the primary identifier column to assist in kubernetes.clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more. | [optional] 
**name** | **str** | name is a human readable name for the column. | 
**priority** | **int** | priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a higher priority. | [optional] 
**type** | **str** | type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


