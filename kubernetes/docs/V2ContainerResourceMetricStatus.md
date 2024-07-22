# V2ContainerResourceMetricStatus

ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | container is the name of the container in the pods of the scaling target | 
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) |  | 
**name** | **str** | name is the name of the resource in question. | 

## Example

```python
from kubernetes.client.models.v2_container_resource_metric_status import V2ContainerResourceMetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2ContainerResourceMetricStatus from a JSON string
v2_container_resource_metric_status_instance = V2ContainerResourceMetricStatus.from_json(json)
# print the JSON string representation of the object
print V2ContainerResourceMetricStatus.to_json()

# convert the object into a dict
v2_container_resource_metric_status_dict = v2_container_resource_metric_status_instance.to_dict()
# create an instance of V2ContainerResourceMetricStatus from a dict
v2_container_resource_metric_status_form_dict = v2_container_resource_metric_status.from_dict(v2_container_resource_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


