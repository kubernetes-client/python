# V1ResourceRule

ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **List[str]** | APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \&quot;*\&quot; means all. | [optional] 
**resource_names** | **List[str]** | ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \&quot;*\&quot; means all. | [optional] 
**resources** | **List[str]** | Resources is a list of resources this rule applies to.  \&quot;*\&quot; means all in the specified apiGroups.  \&quot;*/foo\&quot; represents the subresource &#39;foo&#39; for all resources in the specified apiGroups. | [optional] 
**verbs** | **List[str]** | Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \&quot;*\&quot; means all. | 

## Example

```python
from kubernetes.client.models.v1_resource_rule import V1ResourceRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceRule from a JSON string
v1_resource_rule_instance = V1ResourceRule.from_json(json)
# print the JSON string representation of the object
print V1ResourceRule.to_json()

# convert the object into a dict
v1_resource_rule_dict = v1_resource_rule_instance.to_dict()
# create an instance of V1ResourceRule from a dict
v1_resource_rule_form_dict = v1_resource_rule.from_dict(v1_resource_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


