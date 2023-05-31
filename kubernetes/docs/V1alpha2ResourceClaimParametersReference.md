# V1alpha2ResourceClaimParametersReference

ResourceClaimParametersReference contains enough information to let you locate the parameters for a ResourceClaim. The object must be in the same namespace as the ResourceClaim.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced. This is the same value as in the parameter object&#39;s metadata, for example \&quot;ConfigMap\&quot;. | 
**name** | **str** | Name is the name of resource being referenced. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


