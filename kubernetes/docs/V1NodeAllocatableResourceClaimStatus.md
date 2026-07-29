# V1NodeAllocatableResourceClaimStatus

NodeAllocatableResourceClaimStatus describes the status of node allocatable resources allocated via DRA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | **List[str]** | Containers lists the names of all containers in this pod that reference the claim. | [optional]
**resource_claim_name** | **str** | ResourceClaimName is the resource claim referenced by the pod that resulted in this node allocatable resource allocation. |
**resources** | **Dict[str, str]** | Resources is a map of the node-allocatable resource name to the aggregate quantity allocated to the claim. |

## Example

```python
from kubernetes.client.models.v1_node_allocatable_resource_claim_status import V1NodeAllocatableResourceClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAllocatableResourceClaimStatus from a JSON string
v1_node_allocatable_resource_claim_status_instance = V1NodeAllocatableResourceClaimStatus.from_json(json)
# print the JSON string representation of the object
print(V1NodeAllocatableResourceClaimStatus.to_json())

# convert the object into a dict
v1_node_allocatable_resource_claim_status_dict = v1_node_allocatable_resource_claim_status_instance.to_dict()
# create an instance of V1NodeAllocatableResourceClaimStatus from a dict
v1_node_allocatable_resource_claim_status_from_dict = V1NodeAllocatableResourceClaimStatus.from_dict(v1_node_allocatable_resource_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
