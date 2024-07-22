# V2ExternalMetricStatus

ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 

## Example

```python
from kubernetes.client.models.v2_external_metric_status import V2ExternalMetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExternalMetricStatus from a JSON string
v2_external_metric_status_instance = V2ExternalMetricStatus.from_json(json)
# print the JSON string representation of the object
print V2ExternalMetricStatus.to_json()

# convert the object into a dict
v2_external_metric_status_dict = v2_external_metric_status_instance.to_dict()
# create an instance of V2ExternalMetricStatus from a dict
v2_external_metric_status_form_dict = v2_external_metric_status.from_dict(v2_external_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


