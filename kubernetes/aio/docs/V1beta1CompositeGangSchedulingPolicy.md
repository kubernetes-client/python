# V1beta1CompositeGangSchedulingPolicy

CompositeGangSchedulingPolicy indicates that the groups belonging to the composite group should be scheduled using all-or-nothing semantics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_group_count** | **int** | minGroupCount is the minimum number of child groups that must be schedulable or scheduled at the same time for the scheduler to admit the entire group. It must be a positive integer. |

## Example

```python
from kubernetes.aio.client.models.v1beta1_composite_gang_scheduling_policy import V1beta1CompositeGangSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CompositeGangSchedulingPolicy from a JSON string
v1beta1_composite_gang_scheduling_policy_instance = V1beta1CompositeGangSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta1CompositeGangSchedulingPolicy.to_json())

# convert the object into a dict
v1beta1_composite_gang_scheduling_policy_dict = v1beta1_composite_gang_scheduling_policy_instance.to_dict()
# create an instance of V1beta1CompositeGangSchedulingPolicy from a dict
v1beta1_composite_gang_scheduling_policy_from_dict = V1beta1CompositeGangSchedulingPolicy.from_dict(v1beta1_composite_gang_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
