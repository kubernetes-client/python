# V1alpha3WorkloadPodGroupSchedulingPolicy

WorkloadPodGroupSchedulingPolicy defines the scheduling policy for a group of pods managed by a workload controller. Exactly one policy must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | basic specifies that standard, pod-by-pod Kubernetes scheduling behavior should be used. | [optional]
**gang** | [**V1alpha3WorkloadPodGroupGangSchedulingPolicy**](V1alpha3WorkloadPodGroupGangSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha3_workload_pod_group_scheduling_policy import V1alpha3WorkloadPodGroupSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3WorkloadPodGroupSchedulingPolicy from a JSON string
v1alpha3_workload_pod_group_scheduling_policy_instance = V1alpha3WorkloadPodGroupSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1alpha3WorkloadPodGroupSchedulingPolicy.to_json())

# convert the object into a dict
v1alpha3_workload_pod_group_scheduling_policy_dict = v1alpha3_workload_pod_group_scheduling_policy_instance.to_dict()
# create an instance of V1alpha3WorkloadPodGroupSchedulingPolicy from a dict
v1alpha3_workload_pod_group_scheduling_policy_from_dict = V1alpha3WorkloadPodGroupSchedulingPolicy.from_dict(v1alpha3_workload_pod_group_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
