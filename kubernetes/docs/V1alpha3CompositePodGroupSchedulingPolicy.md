# V1alpha3CompositePodGroupSchedulingPolicy

CompositePodGroupSchedulingPolicy defines the scheduling configuration for a CompositePodGroup. Exactly one policy must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | basic specifies that the groups of this composite group should be scheduled independently. This field is immutable. | [optional]
**gang** | [**V1alpha3CompositeGangSchedulingPolicy**](V1alpha3CompositeGangSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_composite_pod_group_scheduling_policy import V1alpha3CompositePodGroupSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CompositePodGroupSchedulingPolicy from a JSON string
v1alpha3_composite_pod_group_scheduling_policy_instance = V1alpha3CompositePodGroupSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CompositePodGroupSchedulingPolicy.to_json())

# convert the object into a dict
v1alpha3_composite_pod_group_scheduling_policy_dict = v1alpha3_composite_pod_group_scheduling_policy_instance.to_dict()
# create an instance of V1alpha3CompositePodGroupSchedulingPolicy from a dict
v1alpha3_composite_pod_group_scheduling_policy_from_dict = V1alpha3CompositePodGroupSchedulingPolicy.from_dict(v1alpha3_composite_pod_group_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
