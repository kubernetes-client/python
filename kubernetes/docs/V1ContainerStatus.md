# V1ContainerStatus

ContainerStatus contains details for the current status of this container.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | Container&#39;s ID in the format &#39;docker://&lt;container_id&gt;&#39;. | [optional] 
**image** | **str** | The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images. | 
**image_id** | **str** | ImageID of the container&#39;s image. | 
**last_state** | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 
**name** | **str** | This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated. | 
**ready** | **bool** | Specifies whether the container has passed its readiness probe. | 
**restart_count** | **int** | The number of times the container has been restarted. | 
**started** | **bool** | Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined. | [optional] 
**state** | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


