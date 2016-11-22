# V1beta1ReplicaSet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object&#39;s metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata | [optional] 
**spec** | [**V1beta1ReplicaSetSpec**](V1beta1ReplicaSetSpec.md) | Spec defines the specification of the desired behavior of the ReplicaSet. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status | [optional] 
**status** | [**V1beta1ReplicaSetStatus**](V1beta1ReplicaSetStatus.md) | Status is the most recently observed status of the ReplicaSet. This data may be out of date by some window of time. Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


