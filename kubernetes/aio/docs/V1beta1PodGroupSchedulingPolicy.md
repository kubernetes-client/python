# V1beta1PodGroupSchedulingPolicy

PodGroupSchedulingPolicy defines the scheduling configuration for a PodGroup. Exactly one policy must be set. The policy is chosen at creation time by setting either the Basic or Gang field. The PodGroup may not change policy after creation. Fields within chosen policy may be updated after creation when their individual fields allow it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic** | **object** | basic specifies that the pods in this group should be scheduled using standard Kubernetes scheduling behavior. Setting this field at group creation time opts this group to basic scheduling; this field cannot be changed afterward. | [optional]
**gang** | [**V1beta1GangSchedulingPolicy**](V1beta1GangSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_pod_group_scheduling_policy import V1beta1PodGroupSchedulingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodGroupSchedulingPolicy from a JSON string
v1beta1_pod_group_scheduling_policy_instance = V1beta1PodGroupSchedulingPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodGroupSchedulingPolicy.to_json())

# convert the object into a dict
v1beta1_pod_group_scheduling_policy_dict = v1beta1_pod_group_scheduling_policy_instance.to_dict()
# create an instance of V1beta1PodGroupSchedulingPolicy from a dict
v1beta1_pod_group_scheduling_policy_from_dict = V1beta1PodGroupSchedulingPolicy.from_dict(v1beta1_pod_group_scheduling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
