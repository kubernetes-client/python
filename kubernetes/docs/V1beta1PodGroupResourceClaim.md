# V1beta1PodGroupResourceClaim

PodGroupResourceClaim references exactly one ResourceClaim, either directly or by naming a ResourceClaimTemplate which is then turned into a ResourceClaim for the PodGroup.  It adds a name to it that uniquely identifies the ResourceClaim inside the PodGroup. Pods that need access to the ResourceClaim define a matching reference in its own Spec.ResourceClaims. The Pod's claim must match all fields of the PodGroup's claim exactly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name uniquely identifies this resource claim inside the PodGroup. This must be a DNS_LABEL. |
**resource_claim_name** | **str** | resourceClaimName is the name of a ResourceClaim object in the same namespace as this PodGroup. The ResourceClaim will be reserved for the PodGroup instead of its individual pods.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional]
**resource_claim_template_name** | **str** | resourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace as this PodGroup.  The template will be used to create a new ResourceClaim, which will be bound to this PodGroup. When this PodGroup is deleted, the ResourceClaim will also be deleted. The PodGroup name and resource name, along with a generated component, will be used to form a unique name for the ResourceClaim, which will be recorded in podgroup.status.resourceClaimStatuses.  This field is immutable and no changes will be made to the corresponding ResourceClaim by the control plane after creating the ResourceClaim.  Exactly one of ResourceClaimName and ResourceClaimTemplateName must be set. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_pod_group_resource_claim import V1beta1PodGroupResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodGroupResourceClaim from a JSON string
v1beta1_pod_group_resource_claim_instance = V1beta1PodGroupResourceClaim.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodGroupResourceClaim.to_json())

# convert the object into a dict
v1beta1_pod_group_resource_claim_dict = v1beta1_pod_group_resource_claim_instance.to_dict()
# create an instance of V1beta1PodGroupResourceClaim from a dict
v1beta1_pod_group_resource_claim_from_dict = V1beta1PodGroupResourceClaim.from_dict(v1beta1_pod_group_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
