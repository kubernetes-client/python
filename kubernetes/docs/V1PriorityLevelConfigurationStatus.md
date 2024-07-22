# V1PriorityLevelConfigurationStatus

PriorityLevelConfigurationStatus represents the current state of a \"request-priority\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1PriorityLevelConfigurationCondition]**](V1PriorityLevelConfigurationCondition.md) | &#x60;conditions&#x60; is the current state of \&quot;request-priority\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_priority_level_configuration_status import V1PriorityLevelConfigurationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PriorityLevelConfigurationStatus from a JSON string
v1_priority_level_configuration_status_instance = V1PriorityLevelConfigurationStatus.from_json(json)
# print the JSON string representation of the object
print V1PriorityLevelConfigurationStatus.to_json()

# convert the object into a dict
v1_priority_level_configuration_status_dict = v1_priority_level_configuration_status_instance.to_dict()
# create an instance of V1PriorityLevelConfigurationStatus from a dict
v1_priority_level_configuration_status_form_dict = v1_priority_level_configuration_status.from_dict(v1_priority_level_configuration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


