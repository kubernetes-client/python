# V1PreferredSchedulingTerm

An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preference** | [**V1NodeSelectorTerm**](V1NodeSelectorTerm.md) |  | 
**weight** | **int** | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. | 

## Example

```python
from kubernetes.client.models.v1_preferred_scheduling_term import V1PreferredSchedulingTerm

# TODO update the JSON string below
json = "{}"
# create an instance of V1PreferredSchedulingTerm from a JSON string
v1_preferred_scheduling_term_instance = V1PreferredSchedulingTerm.from_json(json)
# print the JSON string representation of the object
print V1PreferredSchedulingTerm.to_json()

# convert the object into a dict
v1_preferred_scheduling_term_dict = v1_preferred_scheduling_term_instance.to_dict()
# create an instance of V1PreferredSchedulingTerm from a dict
v1_preferred_scheduling_term_form_dict = v1_preferred_scheduling_term.from_dict(v1_preferred_scheduling_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


