# V1ResourcePolicyRule

ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==\"\"`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **List[str]** | &#x60;apiGroups&#x60; is a list of matching API groups and may not be empty. \&quot;*\&quot; matches all API groups and, if present, must be the only entry. Required. | 
**cluster_scope** | **bool** | &#x60;clusterScope&#x60; indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the &#x60;namespaces&#x60; field must contain a non-empty list. | [optional] 
**namespaces** | **List[str]** | &#x60;namespaces&#x60; is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains \&quot;*\&quot;.  Note that \&quot;*\&quot; matches any specified namespace but does not match a request that _does not specify_ a namespace (see the &#x60;clusterScope&#x60; field for that). This list may be empty, but only if &#x60;clusterScope&#x60; is true. | [optional] 
**resources** | **List[str]** | &#x60;resources&#x60; is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ \&quot;services\&quot;, \&quot;nodes/status\&quot; ].  This list may not be empty. \&quot;*\&quot; matches all resources and, if present, must be the only entry. Required. | 
**verbs** | **List[str]** | &#x60;verbs&#x60; is a list of matching verbs and may not be empty. \&quot;*\&quot; matches all verbs and, if present, must be the only entry. Required. | 

## Example

```python
from kubernetes.client.models.v1_resource_policy_rule import V1ResourcePolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourcePolicyRule from a JSON string
v1_resource_policy_rule_instance = V1ResourcePolicyRule.from_json(json)
# print the JSON string representation of the object
print V1ResourcePolicyRule.to_json()

# convert the object into a dict
v1_resource_policy_rule_dict = v1_resource_policy_rule_instance.to_dict()
# create an instance of V1ResourcePolicyRule from a dict
v1_resource_policy_rule_form_dict = v1_resource_policy_rule.from_dict(v1_resource_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


