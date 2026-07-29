# V1alpha2PodGroupTemplate

PodGroupTemplate represents a template for a set of pods with a scheduling policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_mode** | **str** | DisruptionMode defines the mode in which a given PodGroup can be disrupted. One of Pod, PodGroup. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional]
**name** | **str** | Name is a unique identifier for the PodGroupTemplate within the Workload. It must be a DNS label. This field is immutable. |
**priority** | **int** | Priority is the value of priority of pod groups created from this template. Various system components use this field to find the priority of the pod group. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional]
**priority_class_name** | **str** | PriorityClassName indicates the priority that should be considered when scheduling a pod group created from this template. If no priority class is specified, admission control can set this to the global default priority class if it exists. Otherwise, pod groups created from this template will have the priority set to zero. This field is available only when the WorkloadAwarePreemption feature gate is enabled. | [optional]
**resource_claims** | [**List[V1alpha2PodGroupResourceClaim]**](V1alpha2PodGroupResourceClaim.md) | ResourceClaims defines which ResourceClaims may be shared among Pods in the group. Pods consume the devices allocated to a PodGroup&#39;s claim by defining a claim in its own Spec.ResourceClaims that matches the PodGroup&#39;s claim exactly. The claim must have the same name and refer to the same ResourceClaim or ResourceClaimTemplate.  This is an alpha-level field and requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable. | [optional]
**scheduling_constraints** | [**V1alpha2PodGroupSchedulingConstraints**](V1alpha2PodGroupSchedulingConstraints.md) |  | [optional]
**scheduling_policy** | [**V1alpha2PodGroupSchedulingPolicy**](V1alpha2PodGroupSchedulingPolicy.md) |  |

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group_template import V1alpha2PodGroupTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroupTemplate from a JSON string
v1alpha2_pod_group_template_instance = V1alpha2PodGroupTemplate.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroupTemplate.to_json())

# convert the object into a dict
v1alpha2_pod_group_template_dict = v1alpha2_pod_group_template_instance.to_dict()
# create an instance of V1alpha2PodGroupTemplate from a dict
v1alpha2_pod_group_template_from_dict = V1alpha2PodGroupTemplate.from_dict(v1alpha2_pod_group_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
