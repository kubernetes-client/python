# V1alpha1IPAddressSpec

IPAddressSpec describe the attributes in an IP Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_ref** | [**V1alpha1ParentReference**](V1alpha1ParentReference.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha1_ip_address_spec import V1alpha1IPAddressSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1IPAddressSpec from a JSON string
v1alpha1_ip_address_spec_instance = V1alpha1IPAddressSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1IPAddressSpec.to_json()

# convert the object into a dict
v1alpha1_ip_address_spec_dict = v1alpha1_ip_address_spec_instance.to_dict()
# create an instance of V1alpha1IPAddressSpec from a dict
v1alpha1_ip_address_spec_form_dict = v1alpha1_ip_address_spec.from_dict(v1alpha1_ip_address_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


