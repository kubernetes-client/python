# V1ResourceClaim

ResourceClaim references one entry in PodSpec.ResourceClaims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. | 

## Example

```python
from kubernetes.client.models.v1_resource_claim import V1ResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceClaim from a JSON string
v1_resource_claim_instance = V1ResourceClaim.from_json(json)
# print the JSON string representation of the object
print V1ResourceClaim.to_json()

# convert the object into a dict
v1_resource_claim_dict = v1_resource_claim_instance.to_dict()
# create an instance of V1ResourceClaim from a dict
v1_resource_claim_form_dict = v1_resource_claim.from_dict(v1_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


