# V2ObjectMetricStatus

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) |  | 
**described_object** | [**V2CrossVersionObjectReference**](V2CrossVersionObjectReference.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 

## Example

```python
from kubernetes.client.models.v2_object_metric_status import V2ObjectMetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2ObjectMetricStatus from a JSON string
v2_object_metric_status_instance = V2ObjectMetricStatus.from_json(json)
# print the JSON string representation of the object
print V2ObjectMetricStatus.to_json()

# convert the object into a dict
v2_object_metric_status_dict = v2_object_metric_status_instance.to_dict()
# create an instance of V2ObjectMetricStatus from a dict
v2_object_metric_status_form_dict = v2_object_metric_status.from_dict(v2_object_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


