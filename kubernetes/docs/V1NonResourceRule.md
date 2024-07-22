# V1NonResourceRule

NonResourceRule holds information that describes a rule for the non-resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_resource_urls** | **List[str]** | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  \&quot;*\&quot; means all. | [optional] 
**verbs** | **List[str]** | Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  \&quot;*\&quot; means all. | 

## Example

```python
from kubernetes.client.models.v1_non_resource_rule import V1NonResourceRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1NonResourceRule from a JSON string
v1_non_resource_rule_instance = V1NonResourceRule.from_json(json)
# print the JSON string representation of the object
print V1NonResourceRule.to_json()

# convert the object into a dict
v1_non_resource_rule_dict = v1_non_resource_rule_instance.to_dict()
# create an instance of V1NonResourceRule from a dict
v1_non_resource_rule_form_dict = v1_non_resource_rule.from_dict(v1_non_resource_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


