# V1alpha3WorkloadPodGroupGangSchedulingPolicy

WorkloadPodGroupGangSchedulingPolicy defines the parameters for gang (all-or-nothing) scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_count** | **int** | minCount is the minimum number of pods that must be scheduled at the same time for the scheduler to admit the entire group. This field is optional. If it is not specified, the controller should inject a context-specific sane default (e.g., parallelism for a Job). If set, it must be a positive integer. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_workload_pod_group_gang_scheduling_policy import V1alpha3WorkloadPodGroupGangSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3WorkloadPodGroupGangSchedulingPolicy from a JSON string
v1alpha3_workload_pod_group_gang_scheduling_policy_instance = V1alpha3WorkloadPodGroupGangSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1alpha3WorkloadPodGroupGangSchedulingPolicy.to_json())

# convert the object into a dict
v1alpha3_workload_pod_group_gang_scheduling_policy_dict = v1alpha3_workload_pod_group_gang_scheduling_policy_instance.to_dict()
# create an instance of V1alpha3WorkloadPodGroupGangSchedulingPolicy from a dict
v1alpha3_workload_pod_group_gang_scheduling_policy_from_dict = V1alpha3WorkloadPodGroupGangSchedulingPolicy.from_dict(v1alpha3_workload_pod_group_gang_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
