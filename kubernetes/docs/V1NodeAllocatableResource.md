# V1NodeAllocatableResource

NodeAllocatableResource defines the translation between the DRA device/capacity units requested to the corresponding quantity of the node allocatable resource. At least one of Mapping or Overhead must be specified. Not specifying either is an invalid configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**V1NodeAllocatableMapping**](V1NodeAllocatableMapping.md) |  | [optional]
**overhead** | [**V1NodeAllocatableOverhead**](V1NodeAllocatableOverhead.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1_node_allocatable_resource import V1NodeAllocatableResource

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAllocatableResource from a JSON string
v1_node_allocatable_resource_instance = V1NodeAllocatableResource.from_json(json)
# print the JSON string representation of the object
print(V1NodeAllocatableResource.to_json())

# convert the object into a dict
v1_node_allocatable_resource_dict = v1_node_allocatable_resource_instance.to_dict()
# create an instance of V1NodeAllocatableResource from a dict
v1_node_allocatable_resource_from_dict = V1NodeAllocatableResource.from_dict(v1_node_allocatable_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
