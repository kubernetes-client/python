# V1NodeSwapStatus

NodeSwapStatus represents swap memory information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Total amount of swap memory in bytes. | [optional]

## Example

```python
from kubernetes.client.models.v1_node_swap_status import V1NodeSwapStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeSwapStatus from a JSON string
v1_node_swap_status_instance = V1NodeSwapStatus.from_json(json)
# print the JSON string representation of the object
print(V1NodeSwapStatus.to_json())

# convert the object into a dict
v1_node_swap_status_dict = v1_node_swap_status_instance.to_dict()
# create an instance of V1NodeSwapStatus from a dict
v1_node_swap_status_from_dict = V1NodeSwapStatus.from_dict(v1_node_swap_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
