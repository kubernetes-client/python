# kubernetes.client.model.v1_deployment_spec.V1DeploymentSpec

DeploymentSpec is the specification of the desired behavior of the Deployment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeploymentSpec is the specification of the desired behavior of the Deployment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**minReadySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] value must be a 32 bit integer
**paused** | bool,  | BoolClass,  | Indicates that the deployment is paused. | [optional] 
**progressDeadlineSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s. | [optional] value must be a 32 bit integer
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] value must be a 32 bit integer
**revisionHistoryLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. | [optional] value must be a 32 bit integer
**strategy** | [**V1DeploymentStrategy**](V1DeploymentStrategy.md) | [**V1DeploymentStrategy**](V1DeploymentStrategy.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

