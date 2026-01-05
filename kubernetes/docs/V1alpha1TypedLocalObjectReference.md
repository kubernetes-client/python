# V1alpha1TypedLocalObjectReference

TypedLocalObjectReference allows to reference typed object inside the same namespace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is empty, the specified Kind must be in the core API group. For any other third-party types, setting APIGroup is required. It must be a DNS subdomain. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced. It must be a path segment name. | 
**name** | **str** | Name is the name of resource being referenced. It must be a path segment name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


