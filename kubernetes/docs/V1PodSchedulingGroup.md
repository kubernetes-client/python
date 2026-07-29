# V1PodSchedulingGroup

PodSchedulingGroup identifies the runtime scheduling group instance that a Pod belongs to. The scheduler uses this information to apply workload-aware scheduling semantics. Exactly one field must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_group_name** | **str** | PodGroupName specifies the name of the standalone PodGroup object that represents the runtime instance of this group. Must be a DNS subdomain. | [optional]

## Example

```python
from kubernetes.client.models.v1_pod_scheduling_group import V1PodSchedulingGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodSchedulingGroup from a JSON string
v1_pod_scheduling_group_instance = V1PodSchedulingGroup.from_json(json)
# print the JSON string representation of the object
print(V1PodSchedulingGroup.to_json())

# convert the object into a dict
v1_pod_scheduling_group_dict = v1_pod_scheduling_group_instance.to_dict()
# create an instance of V1PodSchedulingGroup from a dict
v1_pod_scheduling_group_from_dict = V1PodSchedulingGroup.from_dict(v1_pod_scheduling_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
