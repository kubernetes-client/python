# V1DeploymentCondition

DeploymentCondition describes the state of a deployment at a certain point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**last_update_time** | **datetime** | The last time this condition was updated. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of deployment condition. | 

## Example

```python
from kubernetes.client.models.v1_deployment_condition import V1DeploymentCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeploymentCondition from a JSON string
v1_deployment_condition_instance = V1DeploymentCondition.from_json(json)
# print the JSON string representation of the object
print V1DeploymentCondition.to_json()

# convert the object into a dict
v1_deployment_condition_dict = v1_deployment_condition_instance.to_dict()
# create an instance of V1DeploymentCondition from a dict
v1_deployment_condition_form_dict = v1_deployment_condition.from_dict(v1_deployment_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


