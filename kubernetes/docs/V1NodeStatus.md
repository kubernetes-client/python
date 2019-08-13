# V1NodeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[V1NodeAddress]**](V1NodeAddress.md) | List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses | [optional] 
**allocatable** | **dict(str, str)** | Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. | [optional] 
**capacity** | **dict(str, str)** | Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**conditions** | [**list[V1NodeCondition]**](V1NodeCondition.md) | Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition | [optional] 
**config** | [**V1NodeConfigStatus**](V1NodeConfigStatus.md) |  | [optional] 
**daemon_endpoints** | [**V1NodeDaemonEndpoints**](V1NodeDaemonEndpoints.md) |  | [optional] 
**images** | [**list[V1ContainerImage]**](V1ContainerImage.md) | List of container images on this node | [optional] 
**node_info** | [**V1NodeSystemInfo**](V1NodeSystemInfo.md) |  | [optional] 
**phase** | **str** | NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. | [optional] 
**volumes_attached** | [**list[V1AttachedVolume]**](V1AttachedVolume.md) | List of volumes that are attached to the node. | [optional] 
**volumes_in_use** | **list[str]** | List of attachable volumes in use (mounted) by the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


