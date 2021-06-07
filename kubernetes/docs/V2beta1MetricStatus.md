# V2beta1MetricStatus

MetricStatus describes the last-read state of a single metric.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type is the type of metric source.  It will be one of \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. | 
**external** | [**V2beta1ExternalMetricStatus**](V2beta1ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2beta1ObjectMetricStatus**](V2beta1ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2beta1PodsMetricStatus**](V2beta1PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2beta1ResourceMetricStatus**](V2beta1ResourceMetricStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


