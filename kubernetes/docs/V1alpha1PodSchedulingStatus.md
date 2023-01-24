# V1alpha1PodSchedulingStatus

PodSchedulingStatus describes where resources for the Pod can be allocated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_claims** | [**list[V1alpha1ResourceClaimSchedulingStatus]**](V1alpha1ResourceClaimSchedulingStatus.md) | ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \&quot;WaitForFirstConsumer\&quot; allocation mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


