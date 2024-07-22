# V1DeploymentSpec

DeploymentSpec is the specification of the desired behavior of the Deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] 
**paused** | **bool** | Indicates that the deployment is paused. | [optional] 
**progress_deadline_seconds** | **int** | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. | [optional] 
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**revision_history_limit** | **int** | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**strategy** | [**V1DeploymentStrategy**](V1DeploymentStrategy.md) |  | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1_deployment_spec import V1DeploymentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeploymentSpec from a JSON string
v1_deployment_spec_instance = V1DeploymentSpec.from_json(json)
# print the JSON string representation of the object
print V1DeploymentSpec.to_json()

# convert the object into a dict
v1_deployment_spec_dict = v1_deployment_spec_instance.to_dict()
# create an instance of V1DeploymentSpec from a dict
v1_deployment_spec_form_dict = v1_deployment_spec.from_dict(v1_deployment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


