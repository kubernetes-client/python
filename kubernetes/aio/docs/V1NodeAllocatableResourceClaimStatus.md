# V1NodeAllocatableResourceClaimStatus

NodeAllocatableResourceClaimStatus describes the status of node allocatable resources allocated via DRA.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | **list[str]** | Containers lists the names of all containers in this pod that reference the claim. | [optional] 
**resource_claim_name** | **str** | ResourceClaimName is the resource claim referenced by the pod that resulted in this node allocatable resource allocation. | 
**resources** | **dict[str, str]** | Resources is a map of the node-allocatable resource name to the aggregate quantity allocated to the claim. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


