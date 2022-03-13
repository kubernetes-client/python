# V1ReplicationControllerStatus

ReplicationControllerStatus represents the current status of a replication controller.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller | 
**available_replicas** | **int** | The number of available replicas (ready for at least minReadySeconds) for this replication controller. | [optional] 
**conditions** | [**[V1ReplicationControllerCondition]**](V1ReplicationControllerCondition.md) | Represents the latest available observations of a replication controller&#39;s current state. | [optional] 
**fully_labeled_replicas** | **int** | The number of pods that have labels matching the labels of the pod template of the replication controller. | [optional] 
**observed_generation** | **int** | ObservedGeneration reflects the generation of the most recently observed replication controller. | [optional] 
**ready_replicas** | **int** | The number of ready replicas for this replication controller. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


