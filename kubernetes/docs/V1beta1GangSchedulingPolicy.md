# V1beta1GangSchedulingPolicy

GangSchedulingPolicy defines the parameters for gang scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_count** | **int** | minCount is the minimum number of pods that must be schedulable or scheduled at the same time for the scheduler to admit the entire group. It must be a positive integer. This field is mutable to support workload scaling.  Note that the scheduler operates on an eventually consistent model. Updates to minCount may not be immediately reflected in scheduling decisions due to propagation delays. If minCount is updated while a scheduling cycle is in progress for that group, the new value may not take effect until the next cycle. Moreover, minCount is only enforced during scheduling, meaning that modifications to this field do not affect already-scheduled pods, applying only to those evaluated in future cycles. |

## Example

```python
from kubernetes.client.models.v1beta1_gang_scheduling_policy import V1beta1GangSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1GangSchedulingPolicy from a JSON string
v1beta1_gang_scheduling_policy_instance = V1beta1GangSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta1GangSchedulingPolicy.to_json())

# convert the object into a dict
v1beta1_gang_scheduling_policy_dict = v1beta1_gang_scheduling_policy_instance.to_dict()
# create an instance of V1beta1GangSchedulingPolicy from a dict
v1beta1_gang_scheduling_policy_from_dict = V1beta1GangSchedulingPolicy.from_dict(v1beta1_gang_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
