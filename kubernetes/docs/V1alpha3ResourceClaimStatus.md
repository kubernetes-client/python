# V1alpha3ResourceClaimStatus

ResourceClaimStatus tracks whether the resource has been allocated and what the result of that was.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation** | [**V1alpha3AllocationResult**](V1alpha3AllocationResult.md) |  | [optional] 
**deallocation_requested** | **bool** | Indicates that a claim is to be deallocated. While this is set, no new consumers may be added to ReservedFor.  This is only used if the claim needs to be deallocated by a DRA driver. That driver then must deallocate this claim and reset the field together with clearing the Allocation field.  This is an alpha field and requires enabling the DRAControlPlaneController feature gate. | [optional] 
**reserved_for** | [**list[V1alpha3ResourceClaimConsumerReference]**](V1alpha3ResourceClaimConsumerReference.md) | ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started. A claim that is in use or might be in use because it has been reserved must not get deallocated.  In a cluster with multiple scheduler instances, two pods might get scheduled concurrently by different schedulers. When they reference the same ResourceClaim which already has reached its maximum number of consumers, only one pod can be scheduled.  Both schedulers try to add their pod to the claim.status.reservedFor field, but only the update that reaches the API server first gets stored. The other one fails with an error and the scheduler which issued it knows that it must put the pod back into the queue, waiting for the ResourceClaim to become usable again.  There can be at most 32 such reservations. This may get increased in the future, but not reduced. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


