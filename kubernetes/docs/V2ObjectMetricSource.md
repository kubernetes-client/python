# V2ObjectMetricSource

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**described_object** | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


