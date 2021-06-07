# V2beta2MetricStatus

MetricStatus describes the last-read state of a single metric.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type is the type of metric source.  It will be one of \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. | 
**external** | [**V2beta2ExternalMetricStatus**](V2beta2ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2beta2ObjectMetricStatus**](V2beta2ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2beta2PodsMetricStatus**](V2beta2PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2beta2ResourceMetricStatus**](V2beta2ResourceMetricStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


