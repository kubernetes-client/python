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
**format** | **str** | format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like \&quot;0321751043\&quot; or \&quot;978-0321751041\&quot; - isbn10: an ISBN10 number string like \&quot;0321751043\&quot; - isbn13: an ISBN13 number string like \&quot;978-0321751041\&quot; - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like \&quot;#FFFFFF: following the regex ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like \&quot;rgb(255,255,2559\&quot; - byte: base64 encoded binary data - password: any kind of string - date: a date string like \&quot;2006-01-02\&quot; as defined by full-date in RFC3339 - duration: a duration string like \&quot;22 ns\&quot; as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like \&quot;2014-12-15T19:30:20.000Z\&quot; as defined by date-time in RFC3339. | [optional] 
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
**x_kubernetes_list_map_keys** | **list[str]** | x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type &#x60;map&#x60; by specifying the keys used as the index of the map.  This tag MUST only be used on lists that have the \&quot;x-kubernetes-list-type\&quot; extension set to \&quot;map\&quot;. Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).  The properties specified must either be required or have a default value, to ensure those properties are present for all list items. | [optional] 
**x_kubernetes_list_type** | **str** | x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:  1) &#x60;atomic&#x60;: the list is treated as a single entity, like a scalar.      Atomic lists will be entirely replaced when updated. This extension      may be used on any type of list (struct, scalar, ...). 2) &#x60;set&#x60;:      Sets are lists that must not have multiple items with the same value. Each      value must be a scalar, an object with x-kubernetes-map-type &#x60;atomic&#x60; or an      array with x-kubernetes-list-type &#x60;atomic&#x60;. 3) &#x60;map&#x60;:      These lists are like maps in that their elements have a non-index key      used to identify them. Order is preserved upon merge. The map tag      must only be used on a list with elements of type object. Defaults to atomic for arrays. | [optional] 
**x_kubernetes_map_type** | **str** | x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:  1) &#x60;granular&#x60;:      These maps are actual maps (key-value pairs) and each fields are independent      from each other (they can each be manipulated by separate actors). This is      the default behaviour for all maps. 2) &#x60;atomic&#x60;: the list is treated as a single entity, like a scalar.      Atomic maps will be entirely replaced when updated. | [optional] 
**x_kubernetes_preserve_unknown_fields** | **bool** | x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


