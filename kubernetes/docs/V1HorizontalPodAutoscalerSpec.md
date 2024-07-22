# V1HorizontalPodAutoscalerSpec

specification of a horizontal pod autoscaler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_replicas** | **int** | maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas. | 
**min_replicas** | **int** | minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. | [optional] 
**scale_target_ref** | [**V1CrossVersionObjectReference**](V1CrossVersionObjectReference.md) |  | 
**target_cpu_utilization_percentage** | **int** | targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used. | [optional] 

## Example

```python
from kubernetes.client.models.v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1HorizontalPodAutoscalerSpec from a JSON string
v1_horizontal_pod_autoscaler_spec_instance = V1HorizontalPodAutoscalerSpec.from_json(json)
# print the JSON string representation of the object
print V1HorizontalPodAutoscalerSpec.to_json()

# convert the object into a dict
v1_horizontal_pod_autoscaler_spec_dict = v1_horizontal_pod_autoscaler_spec_instance.to_dict()
# create an instance of V1HorizontalPodAutoscalerSpec from a dict
v1_horizontal_pod_autoscaler_spec_form_dict = v1_horizontal_pod_autoscaler_spec.from_dict(v1_horizontal_pod_autoscaler_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


