# V1ContainerStatus

ContainerStatus contains details for the current status of this container.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_resources** | **dict(str, str)** | AllocatedResources represents the compute resources allocated for this container by the node. Kubelet sets this value to Container.Resources.Requests upon successful pod admission and after successfully admitting desired pod resize. | [optional] 
**container_id** | **str** | ContainerID is the ID of the container in the format &#39;&lt;type&gt;://&lt;container_id&gt;&#39;. Where type is a container runtime identifier, returned from Version call of CRI API (for example \&quot;containerd\&quot;). | [optional] 
**image** | **str** | Image is the name of container image that the container is running. The container image may not match the image used in the PodSpec, as it may have been resolved by the runtime. More info: https://kubernetes.io/docs/concepts/containers/images. | 
**image_id** | **str** | ImageID is the image ID of the container&#39;s image. The image ID may not match the image ID of the image used in the PodSpec, as it may have been resolved by the runtime. | 
**last_state** | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 
**name** | **str** | Name is a DNS_LABEL representing the unique name of the container. Each container in a pod must have a unique name across all container types. Cannot be updated. | 
**ready** | **bool** | Ready specifies whether the container is currently passing its readiness check. The value will change as readiness probes keep executing. If no readiness probes are specified, this field defaults to true once the container is fully started (see Started field).  The value is typically used to determine whether a container is ready to accept traffic. | 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**restart_count** | **int** | RestartCount holds the number of times the container has been restarted. Kubelet makes an effort to always increment the value, but there are cases when the state may be lost due to node restarts and then the value may be reset to 0. The value is never negative. | 
**started** | **bool** | Started indicates whether the container has finished its postStart lifecycle hook and passed its startup probe. Initialized as false, becomes true after startupProbe is considered successful. Resets to false when the container is restarted, or if kubelet loses state temporarily. In both cases, startup probes will run again. Is always true when no startupProbe is defined and container is running and has passed the postStart lifecycle hook. The null value must be treated the same as false. | [optional] 
**state** | [**V1ContainerState**](V1ContainerState.md) |  | [optional] 
**volume_mounts** | [**list[V1VolumeMountStatus]**](V1VolumeMountStatus.md) | Status of volume mounts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


