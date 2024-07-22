# V1RuleWithOperations

RuleWithOperations is a tuple of Operations and Resources. It is recommended to make sure that all the tuple expansions are valid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_groups** | **List[str]** | APIGroups is the API groups the resources belong to. &#39;*&#39; is all groups. If &#39;*&#39; is present, the length of the slice must be one. Required. | [optional] 
**api_versions** | **List[str]** | APIVersions is the API versions the resources belong to. &#39;*&#39; is all versions. If &#39;*&#39; is present, the length of the slice must be one. Required. | [optional] 
**operations** | **List[str]** | Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If &#39;*&#39; is present, the length of the slice must be one. Required. | [optional] 
**resources** | **List[str]** | Resources is a list of resources this rule applies to.  For example: &#39;pods&#39; means pods. &#39;pods/log&#39; means the log subresource of pods. &#39;*&#39; means all resources, but not subresources. &#39;pods/*&#39; means all subresources of pods. &#39;*/scale&#39; means all scale subresources. &#39;*/*&#39; means all resources and their subresources.  If wildcard is present, the validation rule will ensure resources do not overlap with each other.  Depending on the enclosing object, subresources might not be allowed. Required. | [optional] 
**scope** | **str** | scope specifies the scope of this rule. Valid values are \&quot;Cluster\&quot;, \&quot;Namespaced\&quot;, and \&quot;*\&quot; \&quot;Cluster\&quot; means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. \&quot;Namespaced\&quot; means that only namespaced resources will match this rule. \&quot;*\&quot; means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is \&quot;*\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_rule_with_operations import V1RuleWithOperations

# TODO update the JSON string below
json = "{}"
# create an instance of V1RuleWithOperations from a JSON string
v1_rule_with_operations_instance = V1RuleWithOperations.from_json(json)
# print the JSON string representation of the object
print V1RuleWithOperations.to_json()

# convert the object into a dict
v1_rule_with_operations_dict = v1_rule_with_operations_instance.to_dict()
# create an instance of V1RuleWithOperations from a dict
v1_rule_with_operations_form_dict = v1_rule_with_operations.from_dict(v1_rule_with_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


