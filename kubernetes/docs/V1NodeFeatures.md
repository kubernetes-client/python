# V1NodeFeatures

NodeFeatures describes the set of features implemented by the CRI implementation. The features contained in the NodeFeatures should depend only on the cri implementation independent of runtime handlers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplemental_groups_policy** | **bool** | SupplementalGroupsPolicy is set to true if the runtime supports SupplementalGroupsPolicy and ContainerUser. | [optional]

## Example

```python
from kubernetes.client.models.v1_node_features import V1NodeFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeFeatures from a JSON string
v1_node_features_instance = V1NodeFeatures.from_json(json)
# print the JSON string representation of the object
print(V1NodeFeatures.to_json())

# convert the object into a dict
v1_node_features_dict = v1_node_features_instance.to_dict()
# create an instance of V1NodeFeatures from a dict
v1_node_features_from_dict = V1NodeFeatures.from_dict(v1_node_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
