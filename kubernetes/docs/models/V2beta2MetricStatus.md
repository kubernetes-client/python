# kubernetes.client.model.v2beta2_metric_status.V2beta2MetricStatus

MetricStatus describes the last-read state of a single metric.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MetricStatus describes the last-read state of a single metric. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type is the type of metric source.  It will be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 
**containerResource** | [**V2beta2ContainerResourceMetricStatus**](V2beta2ContainerResourceMetricStatus.md) | [**V2beta2ContainerResourceMetricStatus**](V2beta2ContainerResourceMetricStatus.md) |  | [optional] 
**external** | [**V2beta2ExternalMetricStatus**](V2beta2ExternalMetricStatus.md) | [**V2beta2ExternalMetricStatus**](V2beta2ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2beta2ObjectMetricStatus**](V2beta2ObjectMetricStatus.md) | [**V2beta2ObjectMetricStatus**](V2beta2ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2beta2PodsMetricStatus**](V2beta2PodsMetricStatus.md) | [**V2beta2PodsMetricStatus**](V2beta2PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2beta2ResourceMetricStatus**](V2beta2ResourceMetricStatus.md) | [**V2beta2ResourceMetricStatus**](V2beta2ResourceMetricStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

