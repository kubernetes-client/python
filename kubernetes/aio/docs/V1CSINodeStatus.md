# V1CSINodeStatus

CSINodeStatus contains health and status information for storage on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_health** | [**List[V1StorageHealth]**](V1StorageHealth.md) | storageHealth contains backend health reports for CSI drivers registered on the node. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_csi_node_status import V1CSINodeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSINodeStatus from a JSON string
v1_csi_node_status_instance = V1CSINodeStatus.from_json(json)
# print the JSON string representation of the object
print(V1CSINodeStatus.to_json())

# convert the object into a dict
v1_csi_node_status_dict = v1_csi_node_status_instance.to_dict()
# create an instance of V1CSINodeStatus from a dict
v1_csi_node_status_from_dict = V1CSINodeStatus.from_dict(v1_csi_node_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
