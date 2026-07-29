# V1ContainerRestartRuleOnExitCodes

ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the   set of specified values. - NotIn: the requirement is satisfied if the container exit code is   not in the set of specified values. |
**values** | **List[int]** | Specifies the set of values to check for container exit codes. At most 255 elements are allowed. | [optional]

## Example

```python
from kubernetes.client.models.v1_container_restart_rule_on_exit_codes import V1ContainerRestartRuleOnExitCodes

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerRestartRuleOnExitCodes from a JSON string
v1_container_restart_rule_on_exit_codes_instance = V1ContainerRestartRuleOnExitCodes.from_json(json)
# print the JSON string representation of the object
print(V1ContainerRestartRuleOnExitCodes.to_json())

# convert the object into a dict
v1_container_restart_rule_on_exit_codes_dict = v1_container_restart_rule_on_exit_codes_instance.to_dict()
# create an instance of V1ContainerRestartRuleOnExitCodes from a dict
v1_container_restart_rule_on_exit_codes_from_dict = V1ContainerRestartRuleOnExitCodes.from_dict(v1_container_restart_rule_on_exit_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
