# V1beta1JSONSchemaProps

JSONSchemaProps is a JSON-Schema following Specification Draft 4 (http://json-schema.org/).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | [optional] 
**schema** | **str** |  | [optional] 
**additional_items** | [**object**](.md) | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**additional_properties** | [**object**](.md) | JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value. Defaults to true for the boolean property. | [optional] 
**all_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**any_of** | [**list[V1beta1JSONSchemaProps]**](V1beta1JSONSchemaProps.md) |  | [optional] 
**default** | [**object**](.md) | default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. CustomResourceDefinitions with defaults must be created using the v1 (or newer) CustomResourceDefinition API. | [optional] 
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
**x_kubernetes_list_map_keys** | **list[str]** | x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type &#x60;map&#x60; by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the \&quot;x-kubernetes-list-type\&quot; extension set to \&quot;map\&quot;. Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported). | [optional] 
**x_kubernetes_list_type** | **str** | x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) &#x60;atomic&#x60;: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) &#x60;set&#x60;:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x-kubernetes-map-type &#x60;atomic&#x60; or an      array with x-kubernetes-list-type &#x60;atomic&#x60;. 3) &#x60;map&#x60;:      These lists are like maps in that their elements have a non-index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays. | [optional] 
**x_kubernetes_preserve_unknown_fields** | **bool** | x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


