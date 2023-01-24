# V1alpha1ResourceClaimConsumerReference

ResourceClaimConsumerReference contains enough information to let you locate the consumer of a ResourceClaim. The user must be a resource in the same namespace as the ResourceClaim.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. | [optional] 
**name** | **str** | Name is the name of resource being referenced. | 
**resource** | **str** | Resource is the type of resource being referenced, for example \&quot;pods\&quot;. | 
**uid** | **str** | UID identifies exactly one incarnation of the resource. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


