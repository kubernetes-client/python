# V1beta1DaemonSetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_number_scheduled** | **int** | The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 
**desired_number_scheduled** | **int** | The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 
**number_available** | **int** | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**number_misscheduled** | **int** | The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 
**number_ready** | **int** | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready. | 
**number_unavailable** | **int** | The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**observed_generation** | **int** | The most recent generation observed by the daemon set controller. | [optional] 
**updated_number_scheduled** | **int** | The total number of nodes that are running updated daemon pod | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


