# AppsV1beta1DeploymentStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. | [optional] 
**collision_count** | **int** | Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. | [optional] 
**conditions** | [**list[AppsV1beta1DeploymentCondition]**](AppsV1beta1DeploymentCondition.md) | Represents the latest available observations of a deployment&#39;s current state. | [optional] 
**observed_generation** | **int** | The generation observed by the deployment controller. | [optional] 
**ready_replicas** | **int** | Total number of ready pods targeted by this deployment. | [optional] 
**replicas** | **int** | Total number of non-terminated pods targeted by this deployment (their labels match the selector). | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable pods targeted by this deployment. | [optional] 
**updated_replicas** | **int** | Total number of non-terminated pods targeted by this deployment that have the desired template spec. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


