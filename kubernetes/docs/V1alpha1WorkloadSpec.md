# V1alpha1WorkloadSpec

WorkloadSpec defines the desired state of a Workload.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_ref** | [**V1alpha1TypedLocalObjectReference**](V1alpha1TypedLocalObjectReference.md) |  | [optional] 
**pod_groups** | [**list[V1alpha1PodGroup]**](V1alpha1PodGroup.md) | PodGroups is the list of pod groups that make up the Workload. The maximum number of pod groups is 8. This field is immutable. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


