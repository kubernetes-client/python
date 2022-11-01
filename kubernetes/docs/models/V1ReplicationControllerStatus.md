# kubernetes.client.model.v1_replication_controller_status.V1ReplicationControllerStatus

ReplicationControllerStatus represents the current status of a replication controller.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ReplicationControllerStatus represents the current status of a replication controller. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller | value must be a 32 bit integer
**availableReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | The number of available replicas (ready for at least minReadySeconds) for this replication controller. | [optional] value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | Represents the latest available observations of a replication controller&#x27;s current state. | [optional] 
**fullyLabeledReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | The number of pods that have labels matching the labels of the pod template of the replication controller. | [optional] value must be a 32 bit integer
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | ObservedGeneration reflects the generation of the most recently observed replication controller. | [optional] value must be a 64 bit integer
**readyReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | The number of ready replicas for this replication controller. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Represents the latest available observations of a replication controller's current state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Represents the latest available observations of a replication controller&#x27;s current state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ReplicationControllerCondition**](V1ReplicationControllerCondition.md) | [**V1ReplicationControllerCondition**](V1ReplicationControllerCondition.md) | [**V1ReplicationControllerCondition**](V1ReplicationControllerCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

