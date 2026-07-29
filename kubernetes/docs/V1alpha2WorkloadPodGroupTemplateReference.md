# V1alpha2WorkloadPodGroupTemplateReference

WorkloadPodGroupTemplateReference references the PodGroupTemplate within the Workload object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_group_template_name** | **str** | PodGroupTemplateName defines the PodGroupTemplate name within the Workload object. |
**workload_name** | **str** | WorkloadName defines the name of the Workload object. |

## Example

```python
from kubernetes.client.models.v1alpha2_workload_pod_group_template_reference import V1alpha2WorkloadPodGroupTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2WorkloadPodGroupTemplateReference from a JSON string
v1alpha2_workload_pod_group_template_reference_instance = V1alpha2WorkloadPodGroupTemplateReference.from_json(json)
# print the JSON string representation of the object
print(V1alpha2WorkloadPodGroupTemplateReference.to_json())

# convert the object into a dict
v1alpha2_workload_pod_group_template_reference_dict = v1alpha2_workload_pod_group_template_reference_instance.to_dict()
# create an instance of V1alpha2WorkloadPodGroupTemplateReference from a dict
v1alpha2_workload_pod_group_template_reference_from_dict = V1alpha2WorkloadPodGroupTemplateReference.from_dict(v1alpha2_workload_pod_group_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
