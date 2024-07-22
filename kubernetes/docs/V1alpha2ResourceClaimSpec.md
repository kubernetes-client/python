# V1alpha2ResourceClaimSpec

ResourceClaimSpec defines how a resource is to be allocated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_mode** | **str** | Allocation can start immediately or when a Pod wants to use the resource. \&quot;WaitForFirstConsumer\&quot; is the default. | [optional] 
**parameters_ref** | [**V1alpha2ResourceClaimParametersReference**](V1alpha2ResourceClaimParametersReference.md) |  | [optional] 
**resource_class_name** | **str** | ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. | 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim_spec import V1alpha2ResourceClaimSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaimSpec from a JSON string
v1alpha2_resource_claim_spec_instance = V1alpha2ResourceClaimSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaimSpec.to_json()

# convert the object into a dict
v1alpha2_resource_claim_spec_dict = v1alpha2_resource_claim_spec_instance.to_dict()
# create an instance of V1alpha2ResourceClaimSpec from a dict
v1alpha2_resource_claim_spec_form_dict = v1alpha2_resource_claim_spec.from_dict(v1alpha2_resource_claim_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


