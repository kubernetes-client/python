# V1alpha2ResourceClaimList

ResourceClaimList is a collection of claims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1alpha2ResourceClaim]**](V1alpha2ResourceClaim.md) | Items is the list of resource claims. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim_list import V1alpha2ResourceClaimList

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaimList from a JSON string
v1alpha2_resource_claim_list_instance = V1alpha2ResourceClaimList.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaimList.to_json()

# convert the object into a dict
v1alpha2_resource_claim_list_dict = v1alpha2_resource_claim_list_instance.to_dict()
# create an instance of V1alpha2ResourceClaimList from a dict
v1alpha2_resource_claim_list_form_dict = v1alpha2_resource_claim_list.from_dict(v1alpha2_resource_claim_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


