# V1beta1WorkloadSpec

WorkloadSpec defines the desired state of a Workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_pod_group_templates** | [**List[V1beta1CompositePodGroupTemplate]**](V1beta1CompositePodGroupTemplate.md) | compositePodGroupTemplates is the list of CompositePodGroup templates that make up the Workload. The maximum number of templates is 8. This field is immutable. Exactly one of CompositePodGroupTemplates and PodGroupTemplates must be set.  This field is used only when the CompositePodGroup feature gate is enabled. | [optional]
**controller_ref** | [**V1beta1TypedLocalObjectReference**](V1beta1TypedLocalObjectReference.md) |  | [optional]
**pod_group_templates** | [**List[V1beta1PodGroupTemplate]**](V1beta1PodGroupTemplate.md) | podGroupTemplates is the list of templates that make up the Workload. The maximum number of templates is 8. Templates cannot be added or removed after the workload is created. Existing templates may still be updated where their individual fields allow it. Exactly one of CompositePodGroupTemplates and PodGroupTemplates must be set. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_workload_spec import V1beta1WorkloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1WorkloadSpec from a JSON string
v1beta1_workload_spec_instance = V1beta1WorkloadSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1WorkloadSpec.to_json())

# convert the object into a dict
v1beta1_workload_spec_dict = v1beta1_workload_spec_instance.to_dict()
# create an instance of V1beta1WorkloadSpec from a dict
v1beta1_workload_spec_from_dict = V1beta1WorkloadSpec.from_dict(v1beta1_workload_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
