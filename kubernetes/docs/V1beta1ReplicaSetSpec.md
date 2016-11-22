# V1beta1ReplicaSetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] 
**replicas** | **int** | Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: http://kubernetes.io/docs/user-guide/replication-controller#what-is-a-replication-controller | [optional] 
**selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | Selector is a label query over pods that should match the replica count. If the selector is empty, it is defaulted to the labels present on the pod template. Label keys and values that must match in order to be controlled by this replica set. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: http://kubernetes.io/docs/user-guide/replication-controller#pod-template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


