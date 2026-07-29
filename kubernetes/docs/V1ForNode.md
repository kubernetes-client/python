# V1ForNode

ForNode provides information about which nodes should consume this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name represents the name of the node. |

## Example

```python
from kubernetes.client.models.v1_for_node import V1ForNode

# TODO update the JSON string below
json = "{}"
# create an instance of V1ForNode from a JSON string
v1_for_node_instance = V1ForNode.from_json(json)
# print the JSON string representation of the object
print(V1ForNode.to_json())

# convert the object into a dict
v1_for_node_dict = v1_for_node_instance.to_dict()
# create an instance of V1ForNode from a dict
v1_for_node_from_dict = V1ForNode.from_dict(v1_for_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
