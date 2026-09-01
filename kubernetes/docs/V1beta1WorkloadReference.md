# V1beta1WorkloadReference

WorkloadReference references the Workload object together with the template that was used to create a particular PodGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_name** | **str** | templateName is the name of a template within the Workload object that was used to create a pod group. It must be a DNS label. This field is required. |
**workload_name** | **str** | workloadName is the name of the Workload object that contains a template that was used when creating a pod group. It must be a DNS name. This field is required. |

## Example

```python
from kubernetes.client.models.v1beta1_workload_reference import V1beta1WorkloadReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1WorkloadReference from a JSON string
v1beta1_workload_reference_instance = V1beta1WorkloadReference.from_json(json)
# print the JSON string representation of the object
print(V1beta1WorkloadReference.to_json())

# convert the object into a dict
v1beta1_workload_reference_dict = v1beta1_workload_reference_instance.to_dict()
# create an instance of V1beta1WorkloadReference from a dict
v1beta1_workload_reference_from_dict = V1beta1WorkloadReference.from_dict(v1beta1_workload_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
