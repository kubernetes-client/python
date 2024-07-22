# V2MetricStatus

MetricStatus describes the last-read state of a single metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**V2ContainerResourceMetricStatus**](V2ContainerResourceMetricStatus.md) |  | [optional] 
**external** | [**V2ExternalMetricStatus**](V2ExternalMetricStatus.md) |  | [optional] 
**object** | [**V2ObjectMetricStatus**](V2ObjectMetricStatus.md) |  | [optional] 
**pods** | [**V2PodsMetricStatus**](V2PodsMetricStatus.md) |  | [optional] 
**resource** | [**V2ResourceMetricStatus**](V2ResourceMetricStatus.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It will be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each corresponds to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 

## Example

```python
from kubernetes.client.models.v2_metric_status import V2MetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricStatus from a JSON string
v2_metric_status_instance = V2MetricStatus.from_json(json)
# print the JSON string representation of the object
print V2MetricStatus.to_json()

# convert the object into a dict
v2_metric_status_dict = v2_metric_status_instance.to_dict()
# create an instance of V2MetricStatus from a dict
v2_metric_status_form_dict = v2_metric_status.from_dict(v2_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


