# V1ScopeSelector

A scope selector represents the AND of the selectors represented by the scoped-resource selector requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[V1ScopedResourceSelectorRequirement]**](V1ScopedResourceSelectorRequirement.md) | A list of scope selector requirements by scope of the resources. | [optional] 

## Example

```python
from kubernetes.client.models.v1_scope_selector import V1ScopeSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1ScopeSelector from a JSON string
v1_scope_selector_instance = V1ScopeSelector.from_json(json)
# print the JSON string representation of the object
print V1ScopeSelector.to_json()

# convert the object into a dict
v1_scope_selector_dict = v1_scope_selector_instance.to_dict()
# create an instance of V1ScopeSelector from a dict
v1_scope_selector_form_dict = v1_scope_selector.from_dict(v1_scope_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


