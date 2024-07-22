# V2HorizontalPodAutoscalerStatus

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V2HorizontalPodAutoscalerCondition]**](V2HorizontalPodAutoscalerCondition.md) | conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. | [optional] 
**current_metrics** | [**List[V2MetricStatus]**](V2MetricStatus.md) | currentMetrics is the last read state of the metrics used by this autoscaler. | [optional] 
**current_replicas** | **int** | currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler. | [optional] 
**desired_replicas** | **int** | desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler. | 
**last_scale_time** | **datetime** | lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed. | [optional] 
**observed_generation** | **int** | observedGeneration is the most recent generation observed by this autoscaler. | [optional] 

## Example

```python
from kubernetes.client.models.v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerStatus from a JSON string
v2_horizontal_pod_autoscaler_status_instance = V2HorizontalPodAutoscalerStatus.from_json(json)
# print the JSON string representation of the object
print V2HorizontalPodAutoscalerStatus.to_json()

# convert the object into a dict
v2_horizontal_pod_autoscaler_status_dict = v2_horizontal_pod_autoscaler_status_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerStatus from a dict
v2_horizontal_pod_autoscaler_status_form_dict = v2_horizontal_pod_autoscaler_status.from_dict(v2_horizontal_pod_autoscaler_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


