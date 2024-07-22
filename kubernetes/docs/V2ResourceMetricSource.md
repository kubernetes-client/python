# V2ResourceMetricSource

ResourceMetricSource indicates how to scale on a resource metric known to Kubernetes, as specified in requests and limits, describing each pod in the current scale target (e.g. CPU or memory).  The values will be averaged together before being compared to the target.  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  Only one \"target\" type should be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the resource in question. | 
**target** | [**V2MetricTarget**](V2MetricTarget.md) |  | 

## Example

```python
from kubernetes.client.models.v2_resource_metric_source import V2ResourceMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ResourceMetricSource from a JSON string
v2_resource_metric_source_instance = V2ResourceMetricSource.from_json(json)
# print the JSON string representation of the object
print V2ResourceMetricSource.to_json()

# convert the object into a dict
v2_resource_metric_source_dict = v2_resource_metric_source_instance.to_dict()
# create an instance of V2ResourceMetricSource from a dict
v2_resource_metric_source_form_dict = v2_resource_metric_source.from_dict(v2_resource_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


