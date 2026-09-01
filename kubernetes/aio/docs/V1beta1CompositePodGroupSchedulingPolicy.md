# V1beta1CompositePodGroupSchedulingPolicy

CompositePodGroupSchedulingPolicy defines the scheduling configuration for a CompositePodGroup. Exactly one policy must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | basic specifies that the groups of this composite group should be scheduled independently. This field is immutable. | [optional]
**gang** | [**V1beta1CompositeGangSchedulingPolicy**](V1beta1CompositeGangSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_composite_pod_group_scheduling_policy import V1beta1CompositePodGroupSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CompositePodGroupSchedulingPolicy from a JSON string
v1beta1_composite_pod_group_scheduling_policy_instance = V1beta1CompositePodGroupSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta1CompositePodGroupSchedulingPolicy.to_json())

# convert the object into a dict
v1beta1_composite_pod_group_scheduling_policy_dict = v1beta1_composite_pod_group_scheduling_policy_instance.to_dict()
# create an instance of V1beta1CompositePodGroupSchedulingPolicy from a dict
v1beta1_composite_pod_group_scheduling_policy_from_dict = V1beta1CompositePodGroupSchedulingPolicy.from_dict(v1beta1_composite_pod_group_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
