# V2MetricSpec

MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**V2ContainerResourceMetricSource**](V2ContainerResourceMetricSource.md) |  | [optional] 
**external** | [**V2ExternalMetricSource**](V2ExternalMetricSource.md) |  | [optional] 
**object** | [**V2ObjectMetricSource**](V2ObjectMetricSource.md) |  | [optional] 
**pods** | [**V2PodsMetricSource**](V2PodsMetricSource.md) |  | [optional] 
**resource** | [**V2ResourceMetricSource**](V2ResourceMetricSource.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It should be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


