# V2MetricValueStatus

MetricValueStatus holds the current value for a metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_utilization** | **int** | currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. | [optional] 
**average_value** | **str** | averageValue is the current value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**value** | **str** | value is the current value of the metric (as a quantity). | [optional] 

## Example

```python
from kubernetes.client.models.v2_metric_value_status import V2MetricValueStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricValueStatus from a JSON string
v2_metric_value_status_instance = V2MetricValueStatus.from_json(json)
# print the JSON string representation of the object
print V2MetricValueStatus.to_json()

# convert the object into a dict
v2_metric_value_status_dict = v2_metric_value_status_instance.to_dict()
# create an instance of V2MetricValueStatus from a dict
v2_metric_value_status_form_dict = v2_metric_value_status.from_dict(v2_metric_value_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


