# V2MetricIdentifier

MetricIdentifier defines the name and optionally selector for a metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the given metric | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v2_metric_identifier import V2MetricIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of V2MetricIdentifier from a JSON string
v2_metric_identifier_instance = V2MetricIdentifier.from_json(json)
# print the JSON string representation of the object
print V2MetricIdentifier.to_json()

# convert the object into a dict
v2_metric_identifier_dict = v2_metric_identifier_instance.to_dict()
# create an instance of V2MetricIdentifier from a dict
v2_metric_identifier_form_dict = v2_metric_identifier.from_dict(v2_metric_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


