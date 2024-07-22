# V1alpha1ServiceCIDRSpec

ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidrs** | **List[str]** | CIDRs defines the IP blocks in CIDR notation (e.g. \&quot;192.168.0.0/24\&quot; or \&quot;2001:db8::/64\&quot;) from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_service_cidr_spec import V1alpha1ServiceCIDRSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ServiceCIDRSpec from a JSON string
v1alpha1_service_cidr_spec_instance = V1alpha1ServiceCIDRSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1ServiceCIDRSpec.to_json()

# convert the object into a dict
v1alpha1_service_cidr_spec_dict = v1alpha1_service_cidr_spec_instance.to_dict()
# create an instance of V1alpha1ServiceCIDRSpec from a dict
v1alpha1_service_cidr_spec_form_dict = v1alpha1_service_cidr_spec.from_dict(v1alpha1_service_cidr_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


