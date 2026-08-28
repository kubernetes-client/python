# V1DeviceTaintRuleSpec

DeviceTaintRuleSpec specifies the selector and one taint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_selector** | [**V1DeviceTaintSelector**](V1DeviceTaintSelector.md) |  | [optional]
**taint** | [**V1DeviceTaint**](V1DeviceTaint.md) |  |

## Example

```python
from kubernetes.client.models.v1_device_taint_rule_spec import V1DeviceTaintRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceTaintRuleSpec from a JSON string
v1_device_taint_rule_spec_instance = V1DeviceTaintRuleSpec.from_json(json)
# print the JSON string representation of the object
print(V1DeviceTaintRuleSpec.to_json())

# convert the object into a dict
v1_device_taint_rule_spec_dict = v1_device_taint_rule_spec_instance.to_dict()
# create an instance of V1DeviceTaintRuleSpec from a dict
v1_device_taint_rule_spec_from_dict = V1DeviceTaintRuleSpec.from_dict(v1_device_taint_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
