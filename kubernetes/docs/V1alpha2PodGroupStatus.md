# V1alpha2PodGroupStatus

PodGroupStatus represents information about the status of a pod group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | Conditions represent the latest observations of the PodGroup&#39;s state.  Known condition types: - \&quot;PodGroupScheduled\&quot;: Indicates whether the scheduling requirement has been satisfied. - \&quot;DisruptionTarget\&quot;: Indicates whether the PodGroup is about to be terminated   due to disruption such as preemption.  Known reasons for the PodGroupScheduled condition: - \&quot;Unschedulable\&quot;: The PodGroup cannot be scheduled due to resource constraints,   affinity/anti-affinity rules, or insufficient capacity for the gang. - \&quot;SchedulerError\&quot;: The PodGroup cannot be scheduled due to some internal error   that happened during scheduling, for example due to nodeAffinity parsing errors.  Known reasons for the DisruptionTarget condition: - \&quot;PreemptionByScheduler\&quot;: The PodGroup was preempted by the scheduler to make room for   higher-priority PodGroups or Pods. | [optional]
**resource_claim_statuses** | [**List[V1alpha2PodGroupResourceClaimStatus]**](V1alpha2PodGroupResourceClaimStatus.md) | Status of resource claims. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group_status import V1alpha2PodGroupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroupStatus from a JSON string
v1alpha2_pod_group_status_instance = V1alpha2PodGroupStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroupStatus.to_json())

# convert the object into a dict
v1alpha2_pod_group_status_dict = v1alpha2_pod_group_status_instance.to_dict()
# create an instance of V1alpha2PodGroupStatus from a dict
v1alpha2_pod_group_status_from_dict = V1alpha2PodGroupStatus.from_dict(v1alpha2_pod_group_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
