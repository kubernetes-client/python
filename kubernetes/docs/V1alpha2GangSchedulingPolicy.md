# V1alpha2GangSchedulingPolicy

GangSchedulingPolicy defines the parameters for gang scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_count** | **int** | MinCount is the minimum number of pods that must be schedulable or scheduled at the same time for the scheduler to admit the entire group. It must be a positive integer. |

## Example

```python
from kubernetes.client.models.v1alpha2_gang_scheduling_policy import V1alpha2GangSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2GangSchedulingPolicy from a JSON string
v1alpha2_gang_scheduling_policy_instance = V1alpha2GangSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1alpha2GangSchedulingPolicy.to_json())

# convert the object into a dict
v1alpha2_gang_scheduling_policy_dict = v1alpha2_gang_scheduling_policy_instance.to_dict()
# create an instance of V1alpha2GangSchedulingPolicy from a dict
v1alpha2_gang_scheduling_policy_from_dict = V1alpha2GangSchedulingPolicy.from_dict(v1alpha2_gang_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
