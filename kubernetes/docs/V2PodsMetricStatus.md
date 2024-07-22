# V2PodsMetricStatus

PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) |  | 
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 

## Example

```python
from kubernetes.client.models.v2_pods_metric_status import V2PodsMetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2PodsMetricStatus from a JSON string
v2_pods_metric_status_instance = V2PodsMetricStatus.from_json(json)
# print the JSON string representation of the object
print V2PodsMetricStatus.to_json()

# convert the object into a dict
v2_pods_metric_status_dict = v2_pods_metric_status_instance.to_dict()
# create an instance of V2PodsMetricStatus from a dict
v2_pods_metric_status_form_dict = v2_pods_metric_status.from_dict(v2_pods_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


