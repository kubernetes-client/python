# kubernetes.client.model.v2beta2_horizontal_pod_autoscaler_status.V2beta2HorizontalPodAutoscalerStatus

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**desiredReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler. | value must be a 32 bit integer
**currentReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler. | value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. | [optional] 
**[currentMetrics](#currentMetrics)** | list, tuple,  | tuple,  | currentMetrics is the last read state of the metrics used by this autoscaler. | [optional] 
**lastScaleTime** | str, datetime,  | str,  | lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed. | [optional] value must conform to RFC-3339 date-time
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | observedGeneration is the most recent generation observed by this autoscaler. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V2beta2HorizontalPodAutoscalerCondition**](V2beta2HorizontalPodAutoscalerCondition.md) | [**V2beta2HorizontalPodAutoscalerCondition**](V2beta2HorizontalPodAutoscalerCondition.md) | [**V2beta2HorizontalPodAutoscalerCondition**](V2beta2HorizontalPodAutoscalerCondition.md) |  | 

# currentMetrics

currentMetrics is the last read state of the metrics used by this autoscaler.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | currentMetrics is the last read state of the metrics used by this autoscaler. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V2beta2MetricStatus**](V2beta2MetricStatus.md) | [**V2beta2MetricStatus**](V2beta2MetricStatus.md) | [**V2beta2MetricStatus**](V2beta2MetricStatus.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

