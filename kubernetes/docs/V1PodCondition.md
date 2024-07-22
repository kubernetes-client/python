# V1PodCondition

PodCondition contains details for the current condition of this pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | Last time we probed the condition. | [optional] 
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | Human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions | 
**type** | **str** | Type is the type of the condition. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions | 

## Example

```python
from kubernetes.client.models.v1_pod_condition import V1PodCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodCondition from a JSON string
v1_pod_condition_instance = V1PodCondition.from_json(json)
# print the JSON string representation of the object
print V1PodCondition.to_json()

# convert the object into a dict
v1_pod_condition_dict = v1_pod_condition_instance.to_dict()
# create an instance of V1PodCondition from a dict
v1_pod_condition_form_dict = v1_pod_condition.from_dict(v1_pod_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


