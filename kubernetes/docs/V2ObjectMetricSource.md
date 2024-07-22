# V2ObjectMetricSource

ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**described_object** | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) |  | 

## Example

```python
from kubernetes.client.models.v2_object_metric_source import V2ObjectMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ObjectMetricSource from a JSON string
v2_object_metric_source_instance = V2ObjectMetricSource.from_json(json)
# print the JSON string representation of the object
print V2ObjectMetricSource.to_json()

# convert the object into a dict
v2_object_metric_source_dict = v2_object_metric_source_instance.to_dict()
# create an instance of V2ObjectMetricSource from a dict
v2_object_metric_source_form_dict = v2_object_metric_source.from_dict(v2_object_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


