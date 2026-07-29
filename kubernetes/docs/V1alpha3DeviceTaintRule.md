# V1alpha3DeviceTaintRule

DeviceTaintRule adds one taint to all devices which match the selector. This has the same effect as if the taint was specified directly in the ResourceSlice by the DRA driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1alpha3DeviceTaintRuleSpec**](V1alpha3DeviceTaintRuleSpec.md) |  |
**status** | [**V1alpha3DeviceTaintRuleStatus**](V1alpha3DeviceTaintRuleStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_device_taint_rule import V1alpha3DeviceTaintRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceTaintRule from a JSON string
v1alpha3_device_taint_rule_instance = V1alpha3DeviceTaintRule.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceTaintRule.to_json())

# convert the object into a dict
v1alpha3_device_taint_rule_dict = v1alpha3_device_taint_rule_instance.to_dict()
# create an instance of V1alpha3DeviceTaintRule from a dict
v1alpha3_device_taint_rule_from_dict = V1alpha3DeviceTaintRule.from_dict(v1alpha3_device_taint_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
