# V1DeploymentStrategy

DeploymentStrategy describes how to replace existing pods with new ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**V1RollingUpdateDeployment**](V1RollingUpdateDeployment.md) |  | [optional] 
**type** | **str** | Type of deployment. Can be \&quot;Recreate\&quot; or \&quot;RollingUpdate\&quot;. Default is RollingUpdate. | [optional] 

## Example

```python
from kubernetes.client.models.v1_deployment_strategy import V1DeploymentStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeploymentStrategy from a JSON string
v1_deployment_strategy_instance = V1DeploymentStrategy.from_json(json)
# print the JSON string representation of the object
print V1DeploymentStrategy.to_json()

# convert the object into a dict
v1_deployment_strategy_dict = v1_deployment_strategy_instance.to_dict()
# create an instance of V1DeploymentStrategy from a dict
v1_deployment_strategy_form_dict = v1_deployment_strategy.from_dict(v1_deployment_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


