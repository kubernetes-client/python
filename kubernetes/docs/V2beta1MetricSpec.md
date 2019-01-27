# V2beta1MetricSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external** | [**V2beta1ExternalMetricSource**](V2beta1ExternalMetricSource.md) |  | [optional] 
**object** | [**V2beta1ObjectMetricSource**](V2beta1ObjectMetricSource.md) |  | [optional] 
**pods** | [**V2beta1PodsMetricSource**](V2beta1PodsMetricSource.md) |  | [optional] 
**resource** | [**V2beta1ResourceMetricSource**](V2beta1ResourceMetricSource.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It should be one of \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


