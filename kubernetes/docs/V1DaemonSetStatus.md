# V1DaemonSetStatus

DaemonSetStatus represents the current status of a daemon set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_count** | **int** | Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] 
**conditions** | [**list[V1DaemonSetCondition]**](V1DaemonSetCondition.md) | Represents the latest available observations of a DaemonSet&#39;s current state. | [optional] 
**current_number_scheduled** | **int** | The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**desired_number_scheduled** | **int** | The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**number_available** | **int** | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**number_misscheduled** | **int** | The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**number_ready** | **int** | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready. | 
**number_unavailable** | **int** | The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**observed_generation** | **int** | The most recent generation observed by the daemon set controller. | [optional] 
**updated_number_scheduled** | **int** | The total number of nodes that are running updated daemon pod | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


