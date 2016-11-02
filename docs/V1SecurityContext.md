# V1SecurityContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**V1Capabilities**](V1Capabilities.md) | The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. | [optional] 
**privileged** | **bool** | Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. | [optional] 
**read_only_root_filesystem** | **bool** | Whether this container has a read-only root filesystem. Default is false. | [optional] 
**run_as_non_root** | **bool** | Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 
**run_as_user** | **int** | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 
**se_linux_options** | [**V1SELinuxOptions**](V1SELinuxOptions.md) | The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container.  May also be set in PodSecurityContext.  If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


