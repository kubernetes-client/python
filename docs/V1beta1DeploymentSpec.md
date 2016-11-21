# V1beta1DeploymentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] 
**paused** | **bool** | Indicates that the deployment is paused and will not be processed by the deployment controller. | [optional] 
**progress_deadline_seconds** | **int** | The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Once autoRollback is implemented, the deployment controller will automatically rollback failed deployments. Note that progress will not be estimated during the time a deployment is paused. This is not set by default. | [optional] 
**replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**revision_history_limit** | **int** | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**rollback_to** | [**V1beta1RollbackConfig**](V1beta1RollbackConfig.md) | The config this deployment is rolling back to. Will be cleared after rollback is done. | [optional] 
**selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. | [optional] 
**strategy** | [**V1beta1DeploymentStrategy**](V1beta1DeploymentStrategy.md) | The deployment strategy to use to replace existing pods with new ones. | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template describes the pods that will be created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


