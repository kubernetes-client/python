# V1beta1JSONSchemaProps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | [optional] 
**schema** | **str** |  | [optional] 
**additional_items** | **object** | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**additional_properties** | **object** | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**all_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**any_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**default** | **object** | JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil. | [optional] 
**definitions** | [**dict(str, V1beta1JSONSchemaProps)**](V1beta1JSONSchemaProps.md) |  | [optional] 
**dependencies** | **dict(str, object)** |  | [optional] 
**description** | **str** |  | [optional] 
**enum** | **list[object]** |  | [optional] 
**example** | **object** | JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil. | [optional] 
**exclusive_maximum** | **bool** |  | [optional] 
**exclusive_minimum** | **bool** |  | [optional] 
**external_docs** | [**V1beta1ExternalDocumentation**](V1beta1ExternalDocumentation.md) |  | [optional] 
**format** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | **object** | JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes. | [optional] 
**max_items** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**max_properties** | **int** |  | [optional] 
**maximum** | **float** |  | [optional] 
**min_items** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] 
**min_properties** | **int** |  | [optional] 
**minimum** | **float** |  | [optional] 
**multiple_of** | **float** |  | [optional] 
**_not** | [**V1beta1JSONSchemaProps**](V1beta1JSONSchemaProps.md) |  | [optional] 
**nullable** | **bool** |  | [optional] 
**one_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**pattern** | **str** |  | [optional] 
**pattern_properties** | [**dict(str, V1beta1JSONSchemaProps)**](V1beta1JSONSchemaProps.md) |  | [optional] 
**properties** | [**dict(str, V1beta1JSONSchemaProps)**](V1beta1JSONSchemaProps.md) |  | [optional] 
**required** | **list[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unique_items** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


