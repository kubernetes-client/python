# V1beta3PriorityLevelConfigurationReference

PriorityLevelConfigurationReference contains information that points to the \"request-priority\" being used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#x60;name&#x60; is the name of the priority level configuration being referenced Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_priority_level_configuration_reference import V1beta3PriorityLevelConfigurationReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3PriorityLevelConfigurationReference from a JSON string
v1beta3_priority_level_configuration_reference_instance = V1beta3PriorityLevelConfigurationReference.from_json(json)
# print the JSON string representation of the object
print V1beta3PriorityLevelConfigurationReference.to_json()

# convert the object into a dict
v1beta3_priority_level_configuration_reference_dict = v1beta3_priority_level_configuration_reference_instance.to_dict()
# create an instance of V1beta3PriorityLevelConfigurationReference from a dict
v1beta3_priority_level_configuration_reference_form_dict = v1beta3_priority_level_configuration_reference.from_dict(v1beta3_priority_level_configuration_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


