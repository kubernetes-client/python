# kubernetes.client.model.v1_horizontal_pod_autoscaler_spec.V1HorizontalPodAutoscalerSpec

specification of a horizontal pod autoscaler.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | specification of a horizontal pod autoscaler. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas. | value must be a 32 bit integer
**scaleTargetRef** | [**V1CrossVersionObjectReference**](V1CrossVersionObjectReference.md) | [**V1CrossVersionObjectReference**](V1CrossVersionObjectReference.md) |  | 
**minReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. | [optional] value must be a 32 bit integer
**targetCPUUtilizationPercentage** | decimal.Decimal, int,  | decimal.Decimal,  | target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

