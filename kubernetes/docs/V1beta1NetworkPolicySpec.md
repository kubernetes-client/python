# V1beta1NetworkPolicySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress** | [**list[V1beta1NetworkPolicyEgressRule]**](V1beta1NetworkPolicyEgressRule.md) | List of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no NetworkPolicies selecting the pod (and cluster policy otherwise allows the traffic), OR if the traffic matches at least one egress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy limits all outgoing traffic (and serves solely to ensure that the pods it selects are isolated by default). This field is beta-level in 1.8 | [optional] 
**ingress** | [**list[V1beta1NetworkPolicyIngressRule]**](V1beta1NetworkPolicyIngressRule.md) | List of ingress rules to be applied to the selected pods. Traffic is allowed to a pod if there are no NetworkPolicies selecting the pod OR if the traffic source is the pod&#39;s local node, OR if the traffic matches at least one ingress rule across all of the NetworkPolicy objects whose podSelector matches the pod. If this field is empty then this NetworkPolicy does not allow any traffic (and serves solely to ensure that the pods it selects are isolated by default). | [optional] 
**pod_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**policy_types** | **list[str]** | List of rule types that the NetworkPolicy relates to. Valid options are \&quot;Ingress\&quot;, \&quot;Egress\&quot;, or \&quot;Ingress,Egress\&quot;. If this field is not specified, it will default based on the existence of Ingress or Egress rules; policies that contain an Egress section are assumed to affect Egress, and all policies (whether or not they contain an Ingress section) are assumed to affect Ingress. If you want to write an egress-only policy, you must explicitly specify policyTypes [ \&quot;Egress\&quot; ]. Likewise, if you want to write a policy that specifies that no egress is allowed, you must specify a policyTypes value that include \&quot;Egress\&quot; (since such a policy would not include an Egress section and would otherwise default to just [ \&quot;Ingress\&quot; ]). This field is beta-level in 1.8 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


