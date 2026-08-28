# V1beta1CompositePodGroupTemplate

CompositePodGroupTemplate represents a template for a CompositePodGroup with a scheduling policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_pod_group_templates** | [**List[V1beta1CompositePodGroupTemplate]**](V1beta1CompositePodGroupTemplate.md) | compositePodGroupTemplates is the list of templates for children CompositePodGroups. The maximum number of templates is 8. At least one entry in CompositePodGroupTemplates or PodGroupTemplates must be set. | [optional]
**disruption_mode** | [**V1beta1CompositeDisruptionMode**](V1beta1CompositeDisruptionMode.md) |  | [optional]
**name** | **str** | name is a unique identifier for the CompositePodGroupTemplate within the Workload. It must be a DNS label. This field is required. |
**pod_group_templates** | [**List[V1beta1PodGroupTemplate]**](V1beta1PodGroupTemplate.md) | podGroupTemplates is the list of templates for children PodGroups. The maximum number of templates is 8. At least one entry in CompositePodGroupTemplates or PodGroupTemplates must be set. | [optional]
**preemption_policy** | **str** | preemptionPolicy is the Policy for preempting pods/podgroups with lower priority. One of Never, PreemptLowerPriority. This field is immutable. This field is available only when the PodGroupPreemptionPolicy feature gate is enabled. | [optional]
**priority** | **int** | priority is the value of priority of composite pod groups created from this template. Various system components use this field to find the priority of the composite pod group. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority. This field is immutable. | [optional]
**priority_class_name** | **str** | priorityClassName indicates the priority that should be considered when scheduling a composite pod group created from this template. If no priority class is specified, admission control can set this to the global default priority class if it exists. Otherwise, composite pod groups created from this template will have the priority set to zero. This field is immutable. | [optional]
**scheduling_constraints** | [**V1beta1CompositePodGroupSchedulingConstraints**](V1beta1CompositePodGroupSchedulingConstraints.md) |  | [optional]
**scheduling_policy** | [**V1beta1CompositePodGroupSchedulingPolicy**](V1beta1CompositePodGroupSchedulingPolicy.md) |  |

## Example

```python
from kubernetes.client.models.v1beta1_composite_pod_group_template import V1beta1CompositePodGroupTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CompositePodGroupTemplate from a JSON string
v1beta1_composite_pod_group_template_instance = V1beta1CompositePodGroupTemplate.from_json(json)
# print the JSON string representation of the object
print(V1beta1CompositePodGroupTemplate.to_json())

# convert the object into a dict
v1beta1_composite_pod_group_template_dict = v1beta1_composite_pod_group_template_instance.to_dict()
# create an instance of V1beta1CompositePodGroupTemplate from a dict
v1beta1_composite_pod_group_template_from_dict = V1beta1CompositePodGroupTemplate.from_dict(v1beta1_composite_pod_group_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
