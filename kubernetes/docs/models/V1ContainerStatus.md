# kubernetes.client.model.v1_container_status.V1ContainerStatus

ContainerStatus contains details for the current status of this container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ContainerStatus contains details for the current status of this container. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image** | str,  | str,  | The image the container is running. More info: https://kubernetes.io/docs/concepts/containers/images. | 
**imageID** | str,  | str,  | ImageID of the container&#x27;s image. | 
**restartCount** | decimal.Decimal, int,  | decimal.Decimal,  | The number of times the container has been restarted. | value must be a 32 bit integer
**ready** | bool,  | BoolClass,  | Specifies whether the container has passed its readiness probe. | 
**name** | str,  | str,  | This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated. | 
**containerID** | str,  | str,  | Container&#x27;s ID in the format &#x27;&lt;type&gt;://&lt;container_id&gt;&#x27;. | [optional] 
**lastState** | [**V1ContainerState**](V1ContainerState.md) | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 
**started** | bool,  | BoolClass,  | Specifies whether the container has passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. Is always true when no startupProbe is defined. | [optional] 
**state** | [**V1ContainerState**](V1ContainerState.md) | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

