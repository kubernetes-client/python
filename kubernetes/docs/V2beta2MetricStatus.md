# V2beta2MetricStatus

MetricStatus describes the last-read state of a single metric.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type is the type of metric source.  It will be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 
**container_resource** | [**V2beta2ContainerResourceMetricStatus**](V2beta2ContainerResourceMetricStatus.md) |  | [optional] 
**external** | [**V2beta2ExternalMetricStatus**](V2beta2ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2beta2ObjectMetricStatus**](V2beta2ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2beta2PodsMetricStatus**](V2beta2PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2beta2ResourceMetricStatus**](V2beta2ResourceMetricStatus.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


