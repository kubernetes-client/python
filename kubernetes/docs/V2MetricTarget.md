# V2MetricTarget

MetricTarget defines the target value, average value, or average utilization of a specific metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_utilization** | **int** | averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type | [optional] 
**average_value** | **str** | averageValue is the target value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**type** | **str** | type represents whether the metric type is Utilization, Value, or AverageValue | 
**value** | **str** | value is the target value of the metric (as a quantity). | [optional] 

## Example

```python
from kubernetes.client.models.v2_metric_target import V2MetricTarget

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricTarget from a JSON string
v2_metric_target_instance = V2MetricTarget.from_json(json)
# print the JSON string representation of the object
print V2MetricTarget.to_json()

# convert the object into a dict
v2_metric_target_dict = v2_metric_target_instance.to_dict()
# create an instance of V2MetricTarget from a dict
v2_metric_target_form_dict = v2_metric_target.from_dict(v2_metric_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


