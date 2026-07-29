# V1beta2Counter

Counter describes a quantity associated with a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value defines how much of a certain device counter is available. |

## Example

```python
from kubernetes.client.models.v1beta2_counter import V1beta2Counter

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2Counter from a JSON string
v1beta2_counter_instance = V1beta2Counter.from_json(json)
# print the JSON string representation of the object
print(V1beta2Counter.to_json())

# convert the object into a dict
v1beta2_counter_dict = v1beta2_counter_instance.to_dict()
# create an instance of V1beta2Counter from a dict
v1beta2_counter_from_dict = V1beta2Counter.from_dict(v1beta2_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
