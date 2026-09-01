# V1alpha3PodGroupTemplate

PodGroupTemplate represents a template for a set of pods with a scheduling policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_mode** | [**V1alpha3DisruptionMode**](V1alpha3DisruptionMode.md) |  | [optional]
**name** | **str** | name is a unique identifier for the PodGroupTemplate within the Workload. It must be a DNS label. This field is immutable. |
**preemption_policy** | **str** | preemptionPolicy is the Policy for preempting pods/podgroups with lower priority. One of Never, PreemptLowerPriority. This field is immutable. This field is available only when the PodGroupPreemptionPolicy feature gate is enabled. | [optional]
**priority** | **int** | priority is the value of priority of pod groups created from this template. Various system components use this field to find the priority of the pod group. The higher the value, the higher the priority. This field is immutable. | [optional]
**priority_class_name** | **str** | priorityClassName indicates the priority that should be considered when scheduling a pod group created from this template. This field is immutable. | [optional]
**resource_claims** | [**List[V1alpha3PodGroupResourceClaim]**](V1alpha3PodGroupResourceClaim.md) | resourceClaims defines which ResourceClaims may be shared among Pods in the group. Pods consume the devices allocated to a PodGroup&#39;s claim by defining a claim in its own Spec.ResourceClaims that matches the PodGroup&#39;s claim exactly. The claim must have the same name and refer to the same ResourceClaim or ResourceClaimTemplate.  This is a beta-level field and requires that the DRAWorkloadResourceClaims feature gate is enabled.  This field is immutable. | [optional]
**scheduling_constraints** | [**V1alpha3PodGroupSchedulingConstraints**](V1alpha3PodGroupSchedulingConstraints.md) |  | [optional]
**scheduling_policy** | [**V1alpha3PodGroupSchedulingPolicy**](V1alpha3PodGroupSchedulingPolicy.md) |  |

## Example

```python
from kubernetes.aio.client.models.v1alpha3_pod_group_template import V1alpha3PodGroupTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3PodGroupTemplate from a JSON string
v1alpha3_pod_group_template_instance = V1alpha3PodGroupTemplate.from_json(json)
# print the JSON string representation of the object
print(V1alpha3PodGroupTemplate.to_json())

# convert the object into a dict
v1alpha3_pod_group_template_dict = v1alpha3_pod_group_template_instance.to_dict()
# create an instance of V1alpha3PodGroupTemplate from a dict
v1alpha3_pod_group_template_from_dict = V1alpha3PodGroupTemplate.from_dict(v1alpha3_pod_group_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
