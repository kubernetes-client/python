# V1alpha2WorkloadSpec

WorkloadSpec defines the desired state of a Workload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_ref** | [**V1alpha2TypedLocalObjectReference**](V1alpha2TypedLocalObjectReference.md) |  | [optional]
**pod_group_templates** | [**List[V1alpha2PodGroupTemplate]**](V1alpha2PodGroupTemplate.md) | PodGroupTemplates is the list of templates that make up the Workload. The maximum number of templates is 8. This field is immutable. |

## Example

```python
from kubernetes.client.models.v1alpha2_workload_spec import V1alpha2WorkloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2WorkloadSpec from a JSON string
v1alpha2_workload_spec_instance = V1alpha2WorkloadSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha2WorkloadSpec.to_json())

# convert the object into a dict
v1alpha2_workload_spec_dict = v1alpha2_workload_spec_instance.to_dict()
# create an instance of V1alpha2WorkloadSpec from a dict
v1alpha2_workload_spec_from_dict = V1alpha2WorkloadSpec.from_dict(v1alpha2_workload_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
