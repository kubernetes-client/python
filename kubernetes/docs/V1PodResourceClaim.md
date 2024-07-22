# V1PodResourceClaim

PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL. | 
**source** | [**V1ClaimSource**](V1ClaimSource.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_resource_claim import V1PodResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodResourceClaim from a JSON string
v1_pod_resource_claim_instance = V1PodResourceClaim.from_json(json)
# print the JSON string representation of the object
print V1PodResourceClaim.to_json()

# convert the object into a dict
v1_pod_resource_claim_dict = v1_pod_resource_claim_instance.to_dict()
# create an instance of V1PodResourceClaim from a dict
v1_pod_resource_claim_form_dict = v1_pod_resource_claim.from_dict(v1_pod_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


