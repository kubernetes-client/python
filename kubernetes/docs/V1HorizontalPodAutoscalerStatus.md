# V1HorizontalPodAutoscalerStatus

current status of a horizontal pod autoscaler

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_cpu_utilization_percentage** | **int** | currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU. | [optional] 
**current_replicas** | **int** | currentReplicas is the current number of replicas of pods managed by this autoscaler. | 
**desired_replicas** | **int** | desiredReplicas is the  desired number of replicas of pods managed by this autoscaler. | 
**last_scale_time** | **datetime** | lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed. | [optional] 
**observed_generation** | **int** | observedGeneration is the most recent generation observed by this autoscaler. | [optional] 

## Example

```python
from kubernetes.client.models.v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1HorizontalPodAutoscalerStatus from a JSON string
v1_horizontal_pod_autoscaler_status_instance = V1HorizontalPodAutoscalerStatus.from_json(json)
# print the JSON string representation of the object
print V1HorizontalPodAutoscalerStatus.to_json()

# convert the object into a dict
v1_horizontal_pod_autoscaler_status_dict = v1_horizontal_pod_autoscaler_status_instance.to_dict()
# create an instance of V1HorizontalPodAutoscalerStatus from a dict
v1_horizontal_pod_autoscaler_status_form_dict = v1_horizontal_pod_autoscaler_status.from_dict(v1_horizontal_pod_autoscaler_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


