# V1alpha2PodGroupSchedulingPolicy

PodGroupSchedulingPolicy defines the scheduling configuration for a PodGroup. Exactly one policy must be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | Basic specifies that the pods in this group should be scheduled using standard Kubernetes scheduling behavior. | [optional] 
**gang** | [**V1alpha2GangSchedulingPolicy**](V1alpha2GangSchedulingPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


