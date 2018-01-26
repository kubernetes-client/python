# V1alpha1VolumeAttachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata | [optional] 
**spec** | [**V1alpha1VolumeAttachmentSpec**](V1alpha1VolumeAttachmentSpec.md) | Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system. | 
**status** | [**V1alpha1VolumeAttachmentStatus**](V1alpha1VolumeAttachmentStatus.md) | Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


