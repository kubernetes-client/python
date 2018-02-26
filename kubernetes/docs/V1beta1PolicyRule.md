# V1beta1PolicyRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **list[str]** | APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. | [optional] 
**non_resource_ur_ls** | **list[str]** | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as \&quot;pods\&quot; or \&quot;secrets\&quot;) or non-resource URL paths (such as \&quot;/api\&quot;),  but not both. | [optional] 
**resource_names** | **list[str]** | ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed. | [optional] 
**resources** | **list[str]** | Resources is a list of resources this rule applies to.  &#39;*&#39; represents all resources in the specified apiGroups. &#39;*/foo&#39; represents the subresource &#39;foo&#39; for all resources in the specified apiGroups. | [optional] 
**verbs** | **list[str]** | Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


