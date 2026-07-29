# V1ReplicaSetStatus

ReplicaSetStatus represents the current status of a ReplicaSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | The number of available non-terminating pods (ready for at least minReadySeconds) for this replica set. | [optional]
**conditions** | [**List[V1ReplicaSetCondition]**](V1ReplicaSetCondition.md) | Represents the latest available observations of a replica set&#39;s current state. | [optional]
**fully_labeled_replicas** | **int** | The number of non-terminating pods that have labels matching the labels of the pod template of the replicaset. | [optional]
**observed_generation** | **int** | ObservedGeneration reflects the generation of the most recently observed ReplicaSet. | [optional]
**ready_replicas** | **int** | The number of non-terminating pods targeted by this ReplicaSet with a Ready Condition. | [optional]
**replicas** | **int** | Replicas is the most recently observed number of non-terminating pods. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset |
**terminating_replicas** | **int** | The number of terminating pods for this replica set. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.  This is a beta field and requires enabling DeploymentReplicaSetTerminatingReplicas feature (enabled by default). | [optional]

## Example

```python
from kubernetes.client.models.v1_replica_set_status import V1ReplicaSetStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ReplicaSetStatus from a JSON string
v1_replica_set_status_instance = V1ReplicaSetStatus.from_json(json)
# print the JSON string representation of the object
print(V1ReplicaSetStatus.to_json())

# convert the object into a dict
v1_replica_set_status_dict = v1_replica_set_status_instance.to_dict()
# create an instance of V1ReplicaSetStatus from a dict
v1_replica_set_status_from_dict = V1ReplicaSetStatus.from_dict(v1_replica_set_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
