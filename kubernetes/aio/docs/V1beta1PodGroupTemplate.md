# V1beta1PodGroupTemplate

PodGroupTemplate represents a template for a set of pods with a scheduling policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_mode** | [**V1beta1DisruptionMode**](V1beta1DisruptionMode.md) |  | [optional]
**name** | **str** | name is a unique identifier for the PodGroupTemplate within the Workload. It must be a DNS label. This field is immutable. |
**preemption_policy** | **str** | preemptionPolicy is the Policy for preempting pods/podgroups with lower priority. One of Never, PreemptLowerPriority. This field is immutable. This field is available only when the PodGroupPreemptionPolicy feature gate is enabled. | [optional]
**priority** | **int** | priority is the value of priority of pod groups created from this template. Various system components use this field to find the priority of the pod group. The higher the value, the higher the priority. This field is immutable. | [optional]
**priority_class_name** | **str** | priorityClassName indicates the priority that should be considered when scheduling a pod group created from this template. This field is immutable. | [optional]
**resource_claims** | [**List[V1beta1PodGroupResourceClaim]**](V1beta1PodGroupResourceClaim.md) | resourceClaims defines which ResourceClaims may be shared among Pods in the group. Pods consume the devices allocated to a PodGroup&#39;s claim by defining a claim in its own Spec.ResourceClaims that matches the PodGroup&#39;s claim exactly. The claim must have the same name and refer to the same ResourceClaim or ResourceClaimTemplate.  This is a beta-level field and requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable. | [optional]
**scheduling_constraints** | [**V1beta1PodGroupSchedulingConstraints**](V1beta1PodGroupSchedulingConstraints.md) |  | [optional]
**scheduling_policy** | [**V1beta1PodGroupSchedulingPolicy**](V1beta1PodGroupSchedulingPolicy.md) |  |

## Example

```python
from kubernetes.aio.client.models.v1beta1_pod_group_template import V1beta1PodGroupTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodGroupTemplate from a JSON string
v1beta1_pod_group_template_instance = V1beta1PodGroupTemplate.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodGroupTemplate.to_json())

# convert the object into a dict
v1beta1_pod_group_template_dict = v1beta1_pod_group_template_instance.to_dict()
# create an instance of V1beta1PodGroupTemplate from a dict
v1beta1_pod_group_template_from_dict = V1beta1PodGroupTemplate.from_dict(v1beta1_pod_group_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
