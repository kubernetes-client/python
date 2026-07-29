# V1beta2DeviceTaintRuleSpec

DeviceTaintRuleSpec specifies the selector and one taint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_selector** | [**V1beta2DeviceTaintSelector**](V1beta2DeviceTaintSelector.md) |  | [optional]
**taint** | [**V1beta2DeviceTaint**](V1beta2DeviceTaint.md) |  |

## Example

```python
from kubernetes.client.models.v1beta2_device_taint_rule_spec import V1beta2DeviceTaintRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceTaintRuleSpec from a JSON string
v1beta2_device_taint_rule_spec_instance = V1beta2DeviceTaintRuleSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceTaintRuleSpec.to_json())

# convert the object into a dict
v1beta2_device_taint_rule_spec_dict = v1beta2_device_taint_rule_spec_instance.to_dict()
# create an instance of V1beta2DeviceTaintRuleSpec from a dict
v1beta2_device_taint_rule_spec_from_dict = V1beta2DeviceTaintRuleSpec.from_dict(v1beta2_device_taint_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
