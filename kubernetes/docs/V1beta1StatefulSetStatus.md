# V1beta1StatefulSetStatus

StatefulSetStatus represents the current state of a StatefulSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collision_count** | **int** | collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision. | [optional] 
**conditions** | [**list[V1beta1StatefulSetCondition]**](V1beta1StatefulSetCondition.md) | Represents the latest available observations of a statefulset&#39;s current state. | [optional] 
**current_replicas** | **int** | currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision. | [optional] 
**current_revision** | **str** | currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas). | [optional] 
**observed_generation** | **int** | observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet&#39;s generation, which is updated on mutation by the API Server. | [optional] 
**ready_replicas** | **int** | readyReplicas is the number of Pods created by the StatefulSet controller that have a Ready Condition. | [optional] 
**replicas** | **int** | replicas is the number of Pods created by the StatefulSet controller. | 
**update_revision** | **str** | updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas) | [optional] 
**updated_replicas** | **int** | updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


