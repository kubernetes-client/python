# V1NodeAllocatableMappedResources

NodeAllocatableMappedResources describes mapped node allocatable resource allocations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the resource (e.g., cpu, memory). |
**quantity** | **str** | Quantity is the total node allocatable resource capacity allocated for the claim. This claim&#39;s allocated devices is shared by all the containers referencing the claim. Kubelet adds this value to both requests and limits at the pod-level cgroup, and to limits at the container-level cgroup for each container referencing the claim. |

## Example

```python
from kubernetes.aio.client.models.v1_node_allocatable_mapped_resources import V1NodeAllocatableMappedResources

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAllocatableMappedResources from a JSON string
v1_node_allocatable_mapped_resources_instance = V1NodeAllocatableMappedResources.from_json(json)
# print the JSON string representation of the object
print(V1NodeAllocatableMappedResources.to_json())

# convert the object into a dict
v1_node_allocatable_mapped_resources_dict = v1_node_allocatable_mapped_resources_instance.to_dict()
# create an instance of V1NodeAllocatableMappedResources from a dict
v1_node_allocatable_mapped_resources_from_dict = V1NodeAllocatableMappedResources.from_dict(v1_node_allocatable_mapped_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
