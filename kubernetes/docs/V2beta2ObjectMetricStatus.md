# V2beta2ObjectMetricStatus

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**V2beta2MetricValueStatus**](V2beta2MetricValueStatus.md) |  | 
**described_object** | [**V2beta2CrossVersionObjectReference**](V2beta2CrossVersionObjectReference.md) |  | 
**metric** | [**V2beta2MetricIdentifier**](V2beta2MetricIdentifier.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


