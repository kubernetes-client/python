# V2PodsMetricSource

PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) |  | 

## Example

```python
from kubernetes.client.models.v2_pods_metric_source import V2PodsMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2PodsMetricSource from a JSON string
v2_pods_metric_source_instance = V2PodsMetricSource.from_json(json)
# print the JSON string representation of the object
print V2PodsMetricSource.to_json()

# convert the object into a dict
v2_pods_metric_source_dict = v2_pods_metric_source_instance.to_dict()
# create an instance of V2PodsMetricSource from a dict
v2_pods_metric_source_form_dict = v2_pods_metric_source.from_dict(v2_pods_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


