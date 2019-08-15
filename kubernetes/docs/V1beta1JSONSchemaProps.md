# V1beta1JSONSchemaProps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | [optional] 
**schema** | **str** |  | [optional] 
**additional_items** | [**object**](.md) | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**additional_properties** | [**object**](.md) | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**all_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**any_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**default** | [**object**](.md) | default is a default value for undefined object fields. Defaulting is an alpha feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false. | [optional] 
**definitions** | [**dict(str, V1beta1JSONSchemaProps)**](V1beta1JSONSchemaProps.md) |  | [optional] 
**dependencies** | **dict(str, object)** |  | [optional] 
**description** | **str** |  | [optional] 
**enum** | **list[object]** |  | [optional] 
**example** | [**object**](.md) | JSON represents any valid JSON value. These types are supported: bool, int64, float64, string, []interface{}, map[string]interface{} and nil. | [optional] 
**exclusive_maximum** | **bool** |  | [optional] 
**exclusive_minimum** | **bool** |  | [optional] 
**external_docs** | [**V1beta1ExternalDocumentation**](V1beta1ExternalDocumentation.md) |  | [optional] 
**format** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**object**](.md) | JSONSchemaPropsOrArray represents a value that can either be a JSONSchemaProps or an array of JSONSchemaProps. Mainly here for serialization purposes. | [optional] 
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
**x_kubernetes_embedded_resource** | **bool** | x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata). | [optional] 
**x_kubernetes_int_or_string** | **bool** | x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:  1) anyOf:    - type: integer    - type: string 2) allOf:    - anyOf:      - type: integer      - type: string    - ... zero or more | [optional] 
**x_kubernetes_preserve_unknown_fields** | **bool** | x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


