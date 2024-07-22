# V1NetworkPolicyEgressRule

NetworkPolicyEgressRule describes a particular set of traffic that is allowed out of pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and to. This type is beta-level in 1.8

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | [**List[V1NetworkPolicyPort]**](V1NetworkPolicyPort.md) | ports is a list of destination ports for outgoing traffic. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. | [optional] 
**to** | [**List[V1NetworkPolicyPeer]**](V1NetworkPolicyPeer.md) | to is a list of destinations for outgoing traffic of pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all destinations (traffic not restricted by destination). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the to list. | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_egress_rule import V1NetworkPolicyEgressRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyEgressRule from a JSON string
v1_network_policy_egress_rule_instance = V1NetworkPolicyEgressRule.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicyEgressRule.to_json()

# convert the object into a dict
v1_network_policy_egress_rule_dict = v1_network_policy_egress_rule_instance.to_dict()
# create an instance of V1NetworkPolicyEgressRule from a dict
v1_network_policy_egress_rule_form_dict = v1_network_policy_egress_rule.from_dict(v1_network_policy_egress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


