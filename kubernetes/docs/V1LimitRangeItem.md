# V1LimitRangeItem

LimitRangeItem defines a min/max usage limit for any resource that matches on kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **Dict[str, str]** | Default resource requirement limit value by resource name if resource limit is omitted. | [optional] 
**default_request** | **Dict[str, str]** | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. | [optional] 
**max** | **Dict[str, str]** | Max usage constraints on this kind by resource name. | [optional] 
**max_limit_request_ratio** | **Dict[str, str]** | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. | [optional] 
**min** | **Dict[str, str]** | Min usage constraints on this kind by resource name. | [optional] 
**type** | **str** | Type of resource that this limit applies to. | 

## Example

```python
from kubernetes.client.models.v1_limit_range_item import V1LimitRangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of V1LimitRangeItem from a JSON string
v1_limit_range_item_instance = V1LimitRangeItem.from_json(json)
# print the JSON string representation of the object
print V1LimitRangeItem.to_json()

# convert the object into a dict
v1_limit_range_item_dict = v1_limit_range_item_instance.to_dict()
# create an instance of V1LimitRangeItem from a dict
v1_limit_range_item_form_dict = v1_limit_range_item.from_dict(v1_limit_range_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


