# V1IngressClassParametersReference

IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is the type of resource being referenced. | 
**name** | **str** | Name is the name of resource being referenced. | 
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**namespace** | **str** | Namespace is the namespace of the resource being referenced. This field is required when scope is set to \&quot;Namespace\&quot; and must be unset when scope is set to \&quot;Cluster\&quot;. | [optional] 
**scope** | **str** | Scope represents if this refers to a cluster or namespace scoped resource. This may be set to \&quot;Cluster\&quot; (default) or \&quot;Namespace\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


