# V1VolumeNodeResources

VolumeNodeResources is a set of resource limits for scheduling of volumes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded. | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_node_resources import V1VolumeNodeResources

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeNodeResources from a JSON string
v1_volume_node_resources_instance = V1VolumeNodeResources.from_json(json)
# print the JSON string representation of the object
print V1VolumeNodeResources.to_json()

# convert the object into a dict
v1_volume_node_resources_dict = v1_volume_node_resources_instance.to_dict()
# create an instance of V1VolumeNodeResources from a dict
v1_volume_node_resources_form_dict = v1_volume_node_resources.from_dict(v1_volume_node_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


