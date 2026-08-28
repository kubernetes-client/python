# V1alpha3WorkloadPodGroupDisruptionMode

WorkloadPodGroupDisruptionMode defines how individual pods within a group can be disrupted. Exactly one mode must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | all specifies that all pods in the group must be disrupted together. | [optional]
**single** | **object** | single specifies that pods can be disrupted independently from each other. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_workload_pod_group_disruption_mode import V1alpha3WorkloadPodGroupDisruptionMode

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3WorkloadPodGroupDisruptionMode from a JSON string
v1alpha3_workload_pod_group_disruption_mode_instance = V1alpha3WorkloadPodGroupDisruptionMode.from_json(json)
# print the JSON string representation of the object
print(V1alpha3WorkloadPodGroupDisruptionMode.to_json())

# convert the object into a dict
v1alpha3_workload_pod_group_disruption_mode_dict = v1alpha3_workload_pod_group_disruption_mode_instance.to_dict()
# create an instance of V1alpha3WorkloadPodGroupDisruptionMode from a dict
v1alpha3_workload_pod_group_disruption_mode_from_dict = V1alpha3WorkloadPodGroupDisruptionMode.from_dict(v1alpha3_workload_pod_group_disruption_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
