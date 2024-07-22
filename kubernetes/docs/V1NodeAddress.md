# V1NodeAddress

NodeAddress contains information for the node's address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The node address. | 
**type** | **str** | Node address type, one of Hostname, ExternalIP or InternalIP. | 

## Example

```python
from kubernetes.client.models.v1_node_address import V1NodeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeAddress from a JSON string
v1_node_address_instance = V1NodeAddress.from_json(json)
# print the JSON string representation of the object
print V1NodeAddress.to_json()

# convert the object into a dict
v1_node_address_dict = v1_node_address_instance.to_dict()
# create an instance of V1NodeAddress from a dict
v1_node_address_form_dict = v1_node_address.from_dict(v1_node_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


