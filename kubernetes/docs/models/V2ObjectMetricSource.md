# kubernetes.client.model.v2_object_metric_source.V2ObjectMetricSource

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**describedObject** | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) | [**V2MetricTarget**](V2MetricTarget.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

