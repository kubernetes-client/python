# V1IPBlock

IPBlock describes a particular CIDR (Ex. \"192.168.1.0/24\",\"2001:db8::/64\") that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The except entry describes CIDRs that should not be included within this rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | cidr is a string representing the IPBlock Valid examples are \&quot;192.168.1.0/24\&quot; or \&quot;2001:db8::/64\&quot; | 
**var_except** | **List[str]** | except is a slice of CIDRs that should not be included within an IPBlock Valid examples are \&quot;192.168.1.0/24\&quot; or \&quot;2001:db8::/64\&quot; Except values will be rejected if they are outside the cidr range | [optional] 

## Example

```python
from kubernetes.client.models.v1_ip_block import V1IPBlock

# TODO update the JSON string below
json = "{}"
# create an instance of V1IPBlock from a JSON string
v1_ip_block_instance = V1IPBlock.from_json(json)
# print the JSON string representation of the object
print V1IPBlock.to_json()

# convert the object into a dict
v1_ip_block_dict = v1_ip_block_instance.to_dict()
# create an instance of V1IPBlock from a dict
v1_ip_block_form_dict = v1_ip_block.from_dict(v1_ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


