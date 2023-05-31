# V2ResourceMetricStatus

ResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) |  | 
**name** | **str** | name is the name of the resource in question. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


