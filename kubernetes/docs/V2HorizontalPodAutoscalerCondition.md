# V2HorizontalPodAutoscalerCondition

HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the last time the condition transitioned from one status to another | [optional] 
**message** | **str** | message is a human-readable explanation containing details about the transition | [optional] 
**reason** | **str** | reason is the reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | status is the status of the condition (True, False, Unknown) | 
**type** | **str** | type describes the current condition | 

## Example

```python
from kubernetes.client.models.v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerCondition from a JSON string
v2_horizontal_pod_autoscaler_condition_instance = V2HorizontalPodAutoscalerCondition.from_json(json)
# print the JSON string representation of the object
print V2HorizontalPodAutoscalerCondition.to_json()

# convert the object into a dict
v2_horizontal_pod_autoscaler_condition_dict = v2_horizontal_pod_autoscaler_condition_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerCondition from a dict
v2_horizontal_pod_autoscaler_condition_form_dict = v2_horizontal_pod_autoscaler_condition.from_dict(v2_horizontal_pod_autoscaler_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


