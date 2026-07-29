# V1alpha2PodGroupTemplateReference

PodGroupTemplateReference references a PodGroup template defined in some object (e.g. Workload). Exactly one reference must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload** | [**V1alpha2WorkloadPodGroupTemplateReference**](V1alpha2WorkloadPodGroupTemplateReference.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group_template_reference import V1alpha2PodGroupTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroupTemplateReference from a JSON string
v1alpha2_pod_group_template_reference_instance = V1alpha2PodGroupTemplateReference.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroupTemplateReference.to_json())

# convert the object into a dict
v1alpha2_pod_group_template_reference_dict = v1alpha2_pod_group_template_reference_instance.to_dict()
# create an instance of V1alpha2PodGroupTemplateReference from a dict
v1alpha2_pod_group_template_reference_from_dict = V1alpha2PodGroupTemplateReference.from_dict(v1alpha2_pod_group_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
