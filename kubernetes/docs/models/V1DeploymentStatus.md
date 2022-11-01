# kubernetes.client.model.v1_deployment_status.V1DeploymentStatus

DeploymentStatus is the most recently observed status of the Deployment.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeploymentStatus is the most recently observed status of the Deployment. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**availableReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of available pods (ready for at least minReadySeconds) targeted by this deployment. | [optional] value must be a 32 bit integer
**collisionCount** | decimal.Decimal, int,  | decimal.Decimal,  | Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet. | [optional] value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | Represents the latest available observations of a deployment&#x27;s current state. | [optional] 
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | The generation observed by the deployment controller. | [optional] value must be a 64 bit integer
**readyReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | readyReplicas is the number of pods targeted by this Deployment with a Ready Condition. | [optional] value must be a 32 bit integer
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of non-terminated pods targeted by this deployment (their labels match the selector). | [optional] value must be a 32 bit integer
**unavailableReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created. | [optional] value must be a 32 bit integer
**updatedReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of non-terminated pods targeted by this deployment that have the desired template spec. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Represents the latest available observations of a deployment's current state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Represents the latest available observations of a deployment&#x27;s current state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1DeploymentCondition**](V1DeploymentCondition.md) | [**V1DeploymentCondition**](V1DeploymentCondition.md) | [**V1DeploymentCondition**](V1DeploymentCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

