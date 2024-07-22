# V1NodeStatus

NodeStatus is information about the current status of a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[V1NodeAddress]**](V1NodeAddress.md) | List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See https://pr.k8s.io/79391 for an example. Consumers should assume that addresses can change during the lifetime of a Node. However, there are some exceptions where this may not be possible, such as Pods that inherit a Node&#39;s address in its own status or consumers of the downward API (status.hostIP). | [optional] 
**allocatable** | **Dict[str, str]** | Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. | [optional] 
**capacity** | **Dict[str, str]** | Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity | [optional] 
**conditions** | [**List[V1NodeCondition]**](V1NodeCondition.md) | Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition | [optional] 
**config** | [**V1NodeConfigStatus**](V1NodeConfigStatus.md) |  | [optional] 
**daemon_endpoints** | [**V1NodeDaemonEndpoints**](V1NodeDaemonEndpoints.md) |  | [optional] 
**images** | [**List[V1ContainerImage]**](V1ContainerImage.md) | List of container images on this node | [optional] 
**node_info** | [**V1NodeSystemInfo**](V1NodeSystemInfo.md) |  | [optional] 
**phase** | **str** | NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated. | [optional] 
**runtime_handlers** | [**List[V1NodeRuntimeHandler]**](V1NodeRuntimeHandler.md) | The available runtime handlers. | [optional] 
**volumes_attached** | [**List[V1AttachedVolume]**](V1AttachedVolume.md) | List of volumes that are attached to the node. | [optional] 
**volumes_in_use** | **List[str]** | List of attachable volumes in use (mounted) by the node. | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_status import V1NodeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeStatus from a JSON string
v1_node_status_instance = V1NodeStatus.from_json(json)
# print the JSON string representation of the object
print V1NodeStatus.to_json()

# convert the object into a dict
v1_node_status_dict = v1_node_status_instance.to_dict()
# create an instance of V1NodeStatus from a dict
v1_node_status_form_dict = v1_node_status.from_dict(v1_node_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


