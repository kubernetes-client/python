# V2beta1MetricStatus

MetricStatus describes the last-read state of a single metric.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**V2beta1ContainerResourceMetricStatus**](V2beta1ContainerResourceMetricStatus.md) |  | [optional] 
**external** | [**V2beta1ExternalMetricStatus**](V2beta1ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2beta1ObjectMetricStatus**](V2beta1ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2beta1PodsMetricStatus**](V2beta1PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2beta1ResourceMetricStatus**](V2beta1ResourceMetricStatus.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It will be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


