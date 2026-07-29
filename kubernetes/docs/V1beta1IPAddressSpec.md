# V1beta1IPAddressSpec

IPAddressSpec describe the attributes in an IP Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ref** | [**V1beta1ParentReference**](V1beta1ParentReference.md) |  |

## Example

```python
from kubernetes.client.models.v1beta1_ip_address_spec import V1beta1IPAddressSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1IPAddressSpec from a JSON string
v1beta1_ip_address_spec_instance = V1beta1IPAddressSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1IPAddressSpec.to_json())

# convert the object into a dict
v1beta1_ip_address_spec_dict = v1beta1_ip_address_spec_instance.to_dict()
# create an instance of V1beta1IPAddressSpec from a dict
v1beta1_ip_address_spec_from_dict = V1beta1IPAddressSpec.from_dict(v1beta1_ip_address_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
