# V1PodExtendedResourceClaimStatus

PodExtendedResourceClaimStatus is stored in the PodStatus for the extended resource requests backed by DRA. It stores the generated name for the corresponding special ResourceClaim created by the scheduler.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_mappings** | [**List[V1ContainerExtendedResourceRequest]**](V1ContainerExtendedResourceRequest.md) | RequestMappings identifies the mapping of &lt;container, extended resource backed by DRA&gt; to  device request in the generated ResourceClaim. |
**resource_claim_name** | **str** | ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. |

## Example

```python
from kubernetes.client.models.v1_pod_extended_resource_claim_status import V1PodExtendedResourceClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodExtendedResourceClaimStatus from a JSON string
v1_pod_extended_resource_claim_status_instance = V1PodExtendedResourceClaimStatus.from_json(json)
# print the JSON string representation of the object
print(V1PodExtendedResourceClaimStatus.to_json())

# convert the object into a dict
v1_pod_extended_resource_claim_status_dict = v1_pod_extended_resource_claim_status_instance.to_dict()
# create an instance of V1PodExtendedResourceClaimStatus from a dict
v1_pod_extended_resource_claim_status_from_dict = V1PodExtendedResourceClaimStatus.from_dict(v1_pod_extended_resource_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
