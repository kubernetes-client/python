# V1ServiceAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_pull_secrets** | [**list[V1LocalObjectReference]**](V1LocalObjectReference.md) | ImagePullSecrets is a list of references to secrets in the same namespace to use for pulling any images in pods that reference this ServiceAccount. ImagePullSecrets are distinct from Secrets because Secrets can be mounted in the pod, but ImagePullSecrets are only accessed by the kubelet. More info: http://kubernetes.io/docs/user-guide/secrets#manually-specifying-an-imagepullsecret | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata | [optional] 
**secrets** | [**list[V1ObjectReference]**](V1ObjectReference.md) | Secrets is the list of secrets allowed to be used by pods running using this ServiceAccount. More info: http://kubernetes.io/docs/user-guide/secrets | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


