# V1alpha2ResourceClaim

ResourceClaim describes which resources are needed by a resource consumer. Its status tracks whether the resource has been allocated and what the resulting attributes are.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha2ResourceClaimSpec**](V1alpha2ResourceClaimSpec.md) |  | 
**status** | [**V1alpha2ResourceClaimStatus**](V1alpha2ResourceClaimStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim import V1alpha2ResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaim from a JSON string
v1alpha2_resource_claim_instance = V1alpha2ResourceClaim.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaim.to_json()

# convert the object into a dict
v1alpha2_resource_claim_dict = v1alpha2_resource_claim_instance.to_dict()
# create an instance of V1alpha2ResourceClaim from a dict
v1alpha2_resource_claim_form_dict = v1alpha2_resource_claim.from_dict(v1alpha2_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


