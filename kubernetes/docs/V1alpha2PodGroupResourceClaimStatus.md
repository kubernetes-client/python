# V1alpha2PodGroupResourceClaimStatus

PodGroupResourceClaimStatus is stored in the PodGroupStatus for each PodGroupResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name uniquely identifies this resource claim inside the PodGroup. This must match the name of an entry in podgroup.spec.resourceClaims, which implies that the string must be a DNS_LABEL. |
**resource_claim_name** | **str** | ResourceClaimName is the name of the ResourceClaim that was generated for the PodGroup in the namespace of the PodGroup. If this is unset, then generating a ResourceClaim was not necessary. The podgroup.spec.resourceClaims entry can be ignored in this case. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group_resource_claim_status import V1alpha2PodGroupResourceClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroupResourceClaimStatus from a JSON string
v1alpha2_pod_group_resource_claim_status_instance = V1alpha2PodGroupResourceClaimStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroupResourceClaimStatus.to_json())

# convert the object into a dict
v1alpha2_pod_group_resource_claim_status_dict = v1alpha2_pod_group_resource_claim_status_instance.to_dict()
# create an instance of V1alpha2PodGroupResourceClaimStatus from a dict
v1alpha2_pod_group_resource_claim_status_from_dict = V1alpha2PodGroupResourceClaimStatus.from_dict(v1alpha2_pod_group_resource_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
