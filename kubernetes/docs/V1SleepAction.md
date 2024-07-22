# V1SleepAction

SleepAction describes a \"sleep\" action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | Seconds is the number of seconds to sleep. | 

## Example

```python
from kubernetes.client.models.v1_sleep_action import V1SleepAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1SleepAction from a JSON string
v1_sleep_action_instance = V1SleepAction.from_json(json)
# print the JSON string representation of the object
print V1SleepAction.to_json()

# convert the object into a dict
v1_sleep_action_dict = v1_sleep_action_instance.to_dict()
# create an instance of V1SleepAction from a dict
v1_sleep_action_form_dict = v1_sleep_action.from_dict(v1_sleep_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


