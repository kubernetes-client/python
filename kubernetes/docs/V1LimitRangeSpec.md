# V1LimitRangeSpec

LimitRangeSpec defines a min/max usage limit for resources that match on kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**List[V1LimitRangeItem]**](V1LimitRangeItem.md) | Limits is the list of LimitRangeItem objects that are enforced. | 

## Example

```python
from kubernetes.client.models.v1_limit_range_spec import V1LimitRangeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1LimitRangeSpec from a JSON string
v1_limit_range_spec_instance = V1LimitRangeSpec.from_json(json)
# print the JSON string representation of the object
print V1LimitRangeSpec.to_json()

# convert the object into a dict
v1_limit_range_spec_dict = v1_limit_range_spec_instance.to_dict()
# create an instance of V1LimitRangeSpec from a dict
v1_limit_range_spec_form_dict = v1_limit_range_spec.from_dict(v1_limit_range_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


