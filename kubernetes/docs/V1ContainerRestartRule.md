# V1ContainerRestartRule

ContainerRestartRule describes how a container exit is handled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is \&quot;Restart\&quot; to restart the container. |
**exit_codes** | [**V1ContainerRestartRuleOnExitCodes**](V1ContainerRestartRuleOnExitCodes.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1_container_restart_rule import V1ContainerRestartRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerRestartRule from a JSON string
v1_container_restart_rule_instance = V1ContainerRestartRule.from_json(json)
# print the JSON string representation of the object
print(V1ContainerRestartRule.to_json())

# convert the object into a dict
v1_container_restart_rule_dict = v1_container_restart_rule_instance.to_dict()
# create an instance of V1ContainerRestartRule from a dict
v1_container_restart_rule_from_dict = V1ContainerRestartRule.from_dict(v1_container_restart_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
