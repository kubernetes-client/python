# V1NetworkPolicyIngressRule

NetworkPolicyIngressRule describes a particular set of traffic that is allowed to the pods matched by a NetworkPolicySpec's podSelector. The traffic must match both ports and from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**List[V1NetworkPolicyPeer]**](V1NetworkPolicyPeer.md) | from is a list of sources which should be able to access the pods selected for this rule. Items in this list are combined using a logical OR operation. If this field is empty or missing, this rule matches all sources (traffic not restricted by source). If this field is present and contains at least one item, this rule allows traffic only if the traffic matches at least one item in the from list. | [optional] 
**ports** | [**List[V1NetworkPolicyPort]**](V1NetworkPolicyPort.md) | ports is a list of ports which should be made accessible on the pods selected for this rule. Each item in this list is combined using a logical OR. If this field is empty or missing, this rule matches all ports (traffic not restricted by port). If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list. | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyIngressRule from a JSON string
v1_network_policy_ingress_rule_instance = V1NetworkPolicyIngressRule.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicyIngressRule.to_json()

# convert the object into a dict
v1_network_policy_ingress_rule_dict = v1_network_policy_ingress_rule_instance.to_dict()
# create an instance of V1NetworkPolicyIngressRule from a dict
v1_network_policy_ingress_rule_form_dict = v1_network_policy_ingress_rule.from_dict(v1_network_policy_ingress_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


