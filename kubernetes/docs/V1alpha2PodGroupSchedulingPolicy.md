# V1alpha2PodGroupSchedulingPolicy

PodGroupSchedulingPolicy defines the scheduling configuration for a PodGroup. Exactly one policy must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | Basic specifies that the pods in this group should be scheduled using standard Kubernetes scheduling behavior. | [optional]
**gang** | [**V1alpha2GangSchedulingPolicy**](V1alpha2GangSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group_scheduling_policy import V1alpha2PodGroupSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroupSchedulingPolicy from a JSON string
v1alpha2_pod_group_scheduling_policy_instance = V1alpha2PodGroupSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroupSchedulingPolicy.to_json())

# convert the object into a dict
v1alpha2_pod_group_scheduling_policy_dict = v1alpha2_pod_group_scheduling_policy_instance.to_dict()
# create an instance of V1alpha2PodGroupSchedulingPolicy from a dict
v1alpha2_pod_group_scheduling_policy_from_dict = V1alpha2PodGroupSchedulingPolicy.from_dict(v1alpha2_pod_group_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
