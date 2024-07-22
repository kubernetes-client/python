# V1PodResourceClaimStatus

PodResourceClaimStatus is stored in the PodStatus for each PodResourceClaim which references a ResourceClaimTemplate. It stores the generated name for the corresponding ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name uniquely identifies this resource claim inside the pod. This must match the name of an entry in pod.spec.resourceClaims, which implies that the string must be a DNS_LABEL. | 
**resource_claim_name** | **str** | ResourceClaimName is the name of the ResourceClaim that was generated for the Pod in the namespace of the Pod. It this is unset, then generating a ResourceClaim was not necessary. The pod.spec.resourceClaims entry can be ignored in this case. | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_resource_claim_status import V1PodResourceClaimStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodResourceClaimStatus from a JSON string
v1_pod_resource_claim_status_instance = V1PodResourceClaimStatus.from_json(json)
# print the JSON string representation of the object
print V1PodResourceClaimStatus.to_json()

# convert the object into a dict
v1_pod_resource_claim_status_dict = v1_pod_resource_claim_status_instance.to_dict()
# create an instance of V1PodResourceClaimStatus from a dict
v1_pod_resource_claim_status_form_dict = v1_pod_resource_claim_status.from_dict(v1_pod_resource_claim_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


