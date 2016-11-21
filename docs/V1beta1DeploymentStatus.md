# V1beta1DeploymentStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. | [optional] 
**conditions** | [**list[V1beta1DeploymentCondition]**](V1beta1DeploymentCondition.md) | Represents the latest available observations of a deployment&#39;s current state. | [optional] 
**observed_generation** | **int** | The generation observed by the deployment controller. | [optional] 
**replicas** | **int** | Total number of non-terminated pods targeted by this deployment (their labels match the selector). | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable pods targeted by this deployment. | [optional] 
**updated_replicas** | **int** | Total number of non-terminated pods targeted by this deployment that have the desired template spec. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


