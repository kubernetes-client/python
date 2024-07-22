# V1PolicyRule

PolicyRule holds information that describes a policy rule, but does not contain information about who the rule applies to or which namespace the rule applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **List[str]** | APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. \&quot;\&quot; represents the core API group and \&quot;*\&quot; represents all API groups. | [optional] 
**non_resource_urls** | **List[str]** | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as \&quot;pods\&quot; or \&quot;secrets\&quot;) or non-resource URL paths (such as \&quot;/api\&quot;),  but not both. | [optional] 
**resource_names** | **List[str]** | ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. | [optional] 
**resources** | **List[str]** | Resources is a list of resources this rule applies to. &#39;*&#39; represents all resources. | [optional] 
**verbs** | **List[str]** | Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. &#39;*&#39; represents all verbs. | 

## Example

```python
from kubernetes.client.models.v1_policy_rule import V1PolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1PolicyRule from a JSON string
v1_policy_rule_instance = V1PolicyRule.from_json(json)
# print the JSON string representation of the object
print V1PolicyRule.to_json()

# convert the object into a dict
v1_policy_rule_dict = v1_policy_rule_instance.to_dict()
# create an instance of V1PolicyRule from a dict
v1_policy_rule_form_dict = v1_policy_rule.from_dict(v1_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


