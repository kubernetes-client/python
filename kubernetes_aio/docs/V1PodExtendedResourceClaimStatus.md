# V1PodExtendedResourceClaimStatus

PodExtendedResourceClaimStatus is stored in the PodStatus for the extended resource requests backed by DRA. It stores the generated name for the corresponding special ResourceClaim created by the scheduler.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_mappings** | [**list[V1ContainerExtendedResourceRequest]**](V1ContainerExtendedResourceRequest.md) | RequestMappings identifies the mapping of &lt;container, extended resource backed by DRA&gt; to  device request in the generated ResourceClaim. | 
**resource_claim_name** | **str** | ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


