# V2alpha1HorizontalPodAutoscaler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | metadata is the standard object metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata | [optional] 
**spec** | [**V2alpha1HorizontalPodAutoscalerSpec**](V2alpha1HorizontalPodAutoscalerSpec.md) | spec is the specification for the behaviour of the autoscaler. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status. | [optional] 
**status** | [**V2alpha1HorizontalPodAutoscalerStatus**](V2alpha1HorizontalPodAutoscalerStatus.md) | status is the current information about the autoscaler. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


