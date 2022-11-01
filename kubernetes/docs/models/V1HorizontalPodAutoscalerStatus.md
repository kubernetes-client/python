# kubernetes.client.model.v1_horizontal_pod_autoscaler_status.V1HorizontalPodAutoscalerStatus

current status of a horizontal pod autoscaler

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | current status of a horizontal pod autoscaler | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**desiredReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | desired number of replicas of pods managed by this autoscaler. | value must be a 32 bit integer
**currentReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | current number of replicas of pods managed by this autoscaler. | value must be a 32 bit integer
**currentCPUUtilizationPercentage** | decimal.Decimal, int,  | decimal.Decimal,  | current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU. | [optional] value must be a 32 bit integer
**lastScaleTime** | str, datetime,  | str,  | last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed. | [optional] value must conform to RFC-3339 date-time
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | most recent generation observed by this autoscaler. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

