# V1VolumeNodeAffinity

VolumeNodeAffinity defines constraints that limit what nodes this volume can be accessed from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_node_affinity import V1VolumeNodeAffinity

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeNodeAffinity from a JSON string
v1_volume_node_affinity_instance = V1VolumeNodeAffinity.from_json(json)
# print the JSON string representation of the object
print V1VolumeNodeAffinity.to_json()

# convert the object into a dict
v1_volume_node_affinity_dict = v1_volume_node_affinity_instance.to_dict()
# create an instance of V1VolumeNodeAffinity from a dict
v1_volume_node_affinity_form_dict = v1_volume_node_affinity.from_dict(v1_volume_node_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


