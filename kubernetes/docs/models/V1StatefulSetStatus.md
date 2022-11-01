# kubernetes.client.model.v1_stateful_set_status.V1StatefulSetStatus

StatefulSetStatus represents the current state of a StatefulSet.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | StatefulSetStatus represents the current state of a StatefulSet. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | replicas is the number of Pods created by the StatefulSet controller. | value must be a 32 bit integer
**availableReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset. | [optional] value must be a 32 bit integer
**collisionCount** | decimal.Decimal, int,  | decimal.Decimal,  | collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | Represents the latest available observations of a statefulset&#x27;s current state. | [optional] 
**currentReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. | [optional] value must be a 32 bit integer
**currentRevision** | str,  | str,  | currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). | [optional] 
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet&#x27;s generation, which is updated on mutation by the API Server. | [optional] value must be a 64 bit integer
**readyReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | readyReplicas is the number of pods created for this StatefulSet with a Ready Condition. | [optional] value must be a 32 bit integer
**updateRevision** | str,  | str,  | updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) | [optional] 
**updatedReplicas** | decimal.Decimal, int,  | decimal.Decimal,  | updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Represents the latest available observations of a statefulset's current state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Represents the latest available observations of a statefulset&#x27;s current state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1StatefulSetCondition**](V1StatefulSetCondition.md) | [**V1StatefulSetCondition**](V1StatefulSetCondition.md) | [**V1StatefulSetCondition**](V1StatefulSetCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

