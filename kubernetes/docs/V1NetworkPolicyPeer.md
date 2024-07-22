# V1NetworkPolicyPeer

NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_block** | [**V1IPBlock**](V1IPBlock.md) |  | [optional] 
**namespace_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**pod_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_peer import V1NetworkPolicyPeer

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyPeer from a JSON string
v1_network_policy_peer_instance = V1NetworkPolicyPeer.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicyPeer.to_json()

# convert the object into a dict
v1_network_policy_peer_dict = v1_network_policy_peer_instance.to_dict()
# create an instance of V1NetworkPolicyPeer from a dict
v1_network_policy_peer_form_dict = v1_network_policy_peer.from_dict(v1_network_policy_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


