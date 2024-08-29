# V1NodeStatus

NodeStatus is information about the current status of a node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[V1NodeAddress]**](V1NodeAddress.md) | List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node&#39;s address in its own status or consumers of the downward API (status.hostIP). | [optional] 
**allocatable** | **dict(str, str)** | Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. | [optional] 
**capacity** | **dict(str, str)** | Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**conditions** | [**list[V1NodeCondition]**](V1NodeCondition.md) | Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition | [optional] 
**config** | [**V1NodeConfigStatus**](V1NodeConfigStatus.md) |  | [optional] 
**daemon_endpoints** | [**V1NodeDaemonEndpoints**](V1NodeDaemonEndpoints.md) |  | [optional] 
**images** | [**list[V1ContainerImage]**](V1ContainerImage.md) | List of container images on this node | [optional] 
**node_info** | [**V1NodeSystemInfo**](V1NodeSystemInfo.md) |  | [optional] 
**phase** | **str** | NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. | [optional] 
**runtime_handlers** | [**list[V1NodeRuntimeHandler]**](V1NodeRuntimeHandler.md) | The available runtime handlers. | [optional] 
**volumes_attached** | [**list[V1AttachedVolume]**](V1AttachedVolume.md) | List of volumes that are attached to the node. | [optional] 
**volumes_in_use** | **list[str]** | List of attachable volumes in use (mounted) by the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


