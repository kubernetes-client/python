# V1DaemonSetStatus

DaemonSetStatus represents the current status of a daemon set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_count** | **int** | Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] 
**conditions** | [**List[V1DaemonSetCondition]**](V1DaemonSetCondition.md) | Represents the latest available observations of a DaemonSet&#39;s current state. | [optional] 
**current_number_scheduled** | **int** | The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**desired_number_scheduled** | **int** | The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**number_available** | **int** | The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**number_misscheduled** | **int** | The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/ | 
**number_ready** | **int** | numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition. | 
**number_unavailable** | **int** | The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds) | [optional] 
**observed_generation** | **int** | The most recent generation observed by the daemon set controller. | [optional] 
**updated_number_scheduled** | **int** | The total number of nodes that are running updated daemon pod | [optional] 

## Example

```python
from kubernetes.client.models.v1_daemon_set_status import V1DaemonSetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1DaemonSetStatus from a JSON string
v1_daemon_set_status_instance = V1DaemonSetStatus.from_json(json)
# print the JSON string representation of the object
print V1DaemonSetStatus.to_json()

# convert the object into a dict
v1_daemon_set_status_dict = v1_daemon_set_status_instance.to_dict()
# create an instance of V1DaemonSetStatus from a dict
v1_daemon_set_status_form_dict = v1_daemon_set_status.from_dict(v1_daemon_set_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


