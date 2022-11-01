# kubernetes.client.model.v1_daemon_set_status.V1DaemonSetStatus

DaemonSetStatus represents the current status of a daemon set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DaemonSetStatus represents the current status of a daemon set. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**numberMisscheduled** | decimal.Decimal, int,  | decimal.Decimal,  | The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | value must be a 32 bit integer
**numberReady** | decimal.Decimal, int,  | decimal.Decimal,  | numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition. | value must be a 32 bit integer
**currentNumberScheduled** | decimal.Decimal, int,  | decimal.Decimal,  | The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | value must be a 32 bit integer
**desiredNumberScheduled** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | value must be a 32 bit integer
**collisionCount** | decimal.Decimal, int,  | decimal.Decimal,  | Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] value must be a 32 bit integer
**[conditions](#conditions)** | list, tuple,  | tuple,  | Represents the latest available observations of a DaemonSet&#x27;s current state. | [optional] 
**numberAvailable** | decimal.Decimal, int,  | decimal.Decimal,  | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] value must be a 32 bit integer
**numberUnavailable** | decimal.Decimal, int,  | decimal.Decimal,  | The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] value must be a 32 bit integer
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | The most recent generation observed by the daemon set controller. | [optional] value must be a 64 bit integer
**updatedNumberScheduled** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of nodes that are running updated daemon pod | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Represents the latest available observations of a DaemonSet's current state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Represents the latest available observations of a DaemonSet&#x27;s current state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1DaemonSetCondition**](V1DaemonSetCondition.md) | [**V1DaemonSetCondition**](V1DaemonSetCondition.md) | [**V1DaemonSetCondition**](V1DaemonSetCondition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

