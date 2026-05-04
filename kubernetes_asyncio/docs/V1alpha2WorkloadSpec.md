# V1alpha2WorkloadSpec

WorkloadSpec defines the desired state of a Workload.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_ref** | [**V1alpha2TypedLocalObjectReference**](V1alpha2TypedLocalObjectReference.md) |  | [optional] 
**pod_group_templates** | [**list[V1alpha2PodGroupTemplate]**](V1alpha2PodGroupTemplate.md) | PodGroupTemplates is the list of templates that make up the Workload. The maximum number of templates is 8. This field is immutable. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


