# V1alpha2PodGroupSpec

PodGroupSpec defines the desired state of a PodGroup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_mode** | **str** | DisruptionMode defines the mode in which a given PodGroup can be disrupted. Controllers are expected to fill this field by copying it from a PodGroupTemplate. One of Pod, PodGroup. Defaults to Pod if unset. This field is immutable. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional] 
**pod_group_template_ref** | [**V1alpha2PodGroupTemplateReference**](V1alpha2PodGroupTemplateReference.md) |  | [optional] 
**priority** | **int** | Priority is the value of priority of this pod group. Various system components use this field to find the priority of the pod group. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. This field is immutable. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional] 
**priority_class_name** | **str** | PriorityClassName defines the priority that should be considered when scheduling this pod group. Controllers are expected to fill this field by copying it from a PodGroupTemplate. Otherwise, it is validated and resolved similarly to the PriorityClassName on PodGroupTemplate (i.e. if no priority class is specified, admission control can set this to the global default priority class if it exists. Otherwise, the pod group&#39;s priority will be zero). This field is immutable. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional] 
**resource_claims** | [**list[V1alpha2PodGroupResourceClaim]**](V1alpha2PodGroupResourceClaim.md) | ResourceClaims defines which ResourceClaims may be shared among Pods in the group. Pods consume the devices allocated to a PodGroup&#39;s claim by defining a claim in its own Spec.ResourceClaims that matches the PodGroup&#39;s claim exactly. The claim must have the same name and refer to the same ResourceClaim or ResourceClaimTemplate.  This is an alpha-level field and requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable. | [optional] 
**scheduling_constraints** | [**V1alpha2PodGroupSchedulingConstraints**](V1alpha2PodGroupSchedulingConstraints.md) |  | [optional] 
**scheduling_policy** | [**V1alpha2PodGroupSchedulingPolicy**](V1alpha2PodGroupSchedulingPolicy.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


