# V1ReplicationControllerStatus

ReplicationControllerStatus represents the current status of a replication controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | The number of available replicas (ready for at least minReadySeconds) for this replication controller. | [optional] 
**conditions** | [**List[V1ReplicationControllerCondition]**](V1ReplicationControllerCondition.md) | Represents the latest available observations of a replication controller&#39;s current state. | [optional] 
**fully_labeled_replicas** | **int** | The number of pods that have labels matching the labels of the pod template of the replication controller. | [optional] 
**observed_generation** | **int** | ObservedGeneration reflects the generation of the most recently observed replication controller. | [optional] 
**ready_replicas** | **int** | The number of ready replicas for this replication controller. | [optional] 
**replicas** | **int** | Replicas is the most recently observed number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller | 

## Example

```python
from kubernetes.client.models.v1_replication_controller_status import V1ReplicationControllerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ReplicationControllerStatus from a JSON string
v1_replication_controller_status_instance = V1ReplicationControllerStatus.from_json(json)
# print the JSON string representation of the object
print V1ReplicationControllerStatus.to_json()

# convert the object into a dict
v1_replication_controller_status_dict = v1_replication_controller_status_instance.to_dict()
# create an instance of V1ReplicationControllerStatus from a dict
v1_replication_controller_status_form_dict = v1_replication_controller_status.from_dict(v1_replication_controller_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


