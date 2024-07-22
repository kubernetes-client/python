# V1NetworkPolicySpec

NetworkPolicySpec provides the specification of a NetworkPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress** | [**List[V1NetworkPolicyEgressRule]**](V1NetworkPolicyEgressRule.md) | egress is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8 | [optional] 
**ingress** | [**List[V1NetworkPolicyIngressRule]**](V1NetworkPolicyIngressRule.md) | ingress is a list of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic source is the pod&#39;s local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default) | [optional] 
**pod_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**policy_types** | **List[str]** | policyTypes is a list of rule types that the NetworkPolicy relates to. Valid options are [\&quot;Ingress\&quot;], [\&quot;Egress\&quot;], or [\&quot;Ingress\&quot;, \&quot;Egress\&quot;]. If this field is not specified, it will default based on the existence of ingress or egress rules; policies that contain an egress section are assumed to affect egress, and all policies (whether or not they contain an ingress section) are assumed to affect ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ \&quot;Egress\&quot; ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include \&quot;Egress\&quot; (since such a policy would not include an egress section and would otherwise default to just [ \&quot;Ingress\&quot; ]). This field is beta-level in 1.8 | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_spec import V1NetworkPolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicySpec from a JSON string
v1_network_policy_spec_instance = V1NetworkPolicySpec.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicySpec.to_json()

# convert the object into a dict
v1_network_policy_spec_dict = v1_network_policy_spec_instance.to_dict()
# create an instance of V1NetworkPolicySpec from a dict
v1_network_policy_spec_form_dict = v1_network_policy_spec.from_dict(v1_network_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


