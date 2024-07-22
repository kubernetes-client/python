# V1alpha2ResourceClaimParametersReference

ResourceClaimParametersReference contains enough information to let you locate the parameters for a ResourceClaim. The object must be in the same namespace as the ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced. This is the same value as in the parameter object&#39;s metadata, for example \&quot;ConfigMap\&quot;. | 
**name** | **str** | Name is the name of resource being referenced. | 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim_parameters_reference import V1alpha2ResourceClaimParametersReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaimParametersReference from a JSON string
v1alpha2_resource_claim_parameters_reference_instance = V1alpha2ResourceClaimParametersReference.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaimParametersReference.to_json()

# convert the object into a dict
v1alpha2_resource_claim_parameters_reference_dict = v1alpha2_resource_claim_parameters_reference_instance.to_dict()
# create an instance of V1alpha2ResourceClaimParametersReference from a dict
v1alpha2_resource_claim_parameters_reference_form_dict = v1alpha2_resource_claim_parameters_reference.from_dict(v1alpha2_resource_claim_parameters_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


