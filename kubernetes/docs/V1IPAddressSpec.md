# V1IPAddressSpec

IPAddressSpec describe the attributes in an IP Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ref** | [**V1ParentReference**](V1ParentReference.md) |  |

## Example

```python
from kubernetes.client.models.v1_ip_address_spec import V1IPAddressSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1IPAddressSpec from a JSON string
v1_ip_address_spec_instance = V1IPAddressSpec.from_json(json)
# print the JSON string representation of the object
print(V1IPAddressSpec.to_json())

# convert the object into a dict
v1_ip_address_spec_dict = v1_ip_address_spec_instance.to_dict()
# create an instance of V1IPAddressSpec from a dict
v1_ip_address_spec_from_dict = V1IPAddressSpec.from_dict(v1_ip_address_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
