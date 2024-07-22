# V2HorizontalPodAutoscalerSpec

HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | [**V2HorizontalPodAutoscalerBehavior**](V2HorizontalPodAutoscalerBehavior.md) |  | [optional] 
**max_replicas** | **int** | maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas. | 
**metrics** | [**List[V2MetricSpec]**](V2MetricSpec.md) | metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization. | [optional] 
**min_replicas** | **int** | minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. | [optional] 
**scale_target_ref** | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) |  | 

## Example

```python
from kubernetes.client.models.v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerSpec from a JSON string
v2_horizontal_pod_autoscaler_spec_instance = V2HorizontalPodAutoscalerSpec.from_json(json)
# print the JSON string representation of the object
print V2HorizontalPodAutoscalerSpec.to_json()

# convert the object into a dict
v2_horizontal_pod_autoscaler_spec_dict = v2_horizontal_pod_autoscaler_spec_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerSpec from a dict
v2_horizontal_pod_autoscaler_spec_form_dict = v2_horizontal_pod_autoscaler_spec.from_dict(v2_horizontal_pod_autoscaler_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


