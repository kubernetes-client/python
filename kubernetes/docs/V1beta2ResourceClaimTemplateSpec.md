# V1beta2ResourceClaimTemplateSpec

ResourceClaimTemplateSpec contains the metadata and fields for a ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1beta2ResourceClaimSpec**](V1beta2ResourceClaimSpec.md) |  |

## Example

```python
from kubernetes.client.models.v1beta2_resource_claim_template_spec import V1beta2ResourceClaimTemplateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2ResourceClaimTemplateSpec from a JSON string
v1beta2_resource_claim_template_spec_instance = V1beta2ResourceClaimTemplateSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta2ResourceClaimTemplateSpec.to_json())

# convert the object into a dict
v1beta2_resource_claim_template_spec_dict = v1beta2_resource_claim_template_spec_instance.to_dict()
# create an instance of V1beta2ResourceClaimTemplateSpec from a dict
v1beta2_resource_claim_template_spec_from_dict = V1beta2ResourceClaimTemplateSpec.from_dict(v1beta2_resource_claim_template_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
