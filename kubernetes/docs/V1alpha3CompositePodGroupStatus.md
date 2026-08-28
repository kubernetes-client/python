# V1alpha3CompositePodGroupStatus

CompositePodGroupStatus represents information about the status of a composite pod group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | conditions represent the latest observations of the CompositePodGroup&#39;s state.  Known condition types: - \&quot;CompositePodGroupInitiallyScheduled\&quot;: Indicates whether the overall scheduling requirement   for the subtree under this CompositePodGroup has been satisfied. Once this condition   transitions to True, it serves as a terminal state and will never revert to False,   even if pods are subsequently deleted and group constraints are no longer met. - \&quot;DisruptionTarget\&quot;: Indicates whether the CompositePodGroup is about to be terminated   due to disruption such as preemption.  Known reasons for the CompositePodGroupInitiallyScheduled condition: - \&quot;Unschedulable\&quot;: The CompositePodGroup&#39;s subtree could not be placed due to resource constraints,   affinity/anti-affinity, or topological constraints. - \&quot;SchedulerError\&quot;: The CompositePodGroup cannot be scheduled due to some internal error   that occurred during scheduling. - \&quot;Invalid\&quot;: Set to True when kube-scheduler detects an invalid group layout during   runtime validation. The &#x60;message&#x60; field details the specific layout violation (such as   a detected cycle, exceeding the maximum depth of 4, or referencing multiple distinct Workloads).  Known reasons for the DisruptionTarget condition: - \&quot;PreemptionByScheduler\&quot;: The CompositePodGroup was targeted by the scheduler&#39;s preemption loop   to free up capacity for higher-priority preemptors. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_composite_pod_group_status import V1alpha3CompositePodGroupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CompositePodGroupStatus from a JSON string
v1alpha3_composite_pod_group_status_instance = V1alpha3CompositePodGroupStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CompositePodGroupStatus.to_json())

# convert the object into a dict
v1alpha3_composite_pod_group_status_dict = v1alpha3_composite_pod_group_status_instance.to_dict()
# create an instance of V1alpha3CompositePodGroupStatus from a dict
v1alpha3_composite_pod_group_status_from_dict = V1alpha3CompositePodGroupStatus.from_dict(v1alpha3_composite_pod_group_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
