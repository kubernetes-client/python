# V2ExternalMetricSource

ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) |  | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) |  | 

## Example

```python
from kubernetes.client.models.v2_external_metric_source import V2ExternalMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExternalMetricSource from a JSON string
v2_external_metric_source_instance = V2ExternalMetricSource.from_json(json)
# print the JSON string representation of the object
print V2ExternalMetricSource.to_json()

# convert the object into a dict
v2_external_metric_source_dict = v2_external_metric_source_instance.to_dict()
# create an instance of V2ExternalMetricSource from a dict
v2_external_metric_source_form_dict = v2_external_metric_source.from_dict(v2_external_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


