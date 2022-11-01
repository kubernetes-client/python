# kubernetes.client.model.v1_replica_set_status.V1ReplicaSetStatus

ReplicaSetStatus represents the current status of a ReplicaSet.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ReplicaSetStatus represents the current status of a ReplicaSet. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller | value must be a 32 bit integer
**availableReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | The number of available replicas (ready for at least minReadySeconds) for this replica set. | [optional] value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | Represents the latest available observations of a replica set&#x27;s current state. | [optional] 
**fullyLabeledReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | The number of pods that have labels matching the labels of the pod template of the replicaset. | [optional] value must be a 32 bit integer
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | ObservedGeneration reflects the generation of the most recently observed ReplicaSet. | [optional] value must be a 64 bit integer
**readyReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Represents the latest available observations of a replica set's current state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Represents the latest available observations of a replica set&#x27;s current state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ReplicaSetCondition**](V1ReplicaSetCondition.md) | [**V1ReplicaSetCondition**](V1ReplicaSetCondition.md) | [**V1ReplicaSetCondition**](V1ReplicaSetCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

