# V1ComponentCondition

Information about the condition of a component.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Condition error code for a component. For example, a health check error code. | [optional] 
**message** | **str** | Message about the condition for a component. For example, information about a health check. | [optional] 
**status** | **str** | Status of the condition for a component. Valid values for \&quot;Healthy\&quot;: \&quot;True\&quot;, \&quot;False\&quot;, or \&quot;Unknown\&quot;. | 
**type** | **str** | Type of condition for a component. Valid value: \&quot;Healthy\&quot; | 

## Example

```python
from kubernetes.client.models.v1_component_condition import V1ComponentCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1ComponentCondition from a JSON string
v1_component_condition_instance = V1ComponentCondition.from_json(json)
# print the JSON string representation of the object
print V1ComponentCondition.to_json()

# convert the object into a dict
v1_component_condition_dict = v1_component_condition_instance.to_dict()
# create an instance of V1ComponentCondition from a dict
v1_component_condition_form_dict = v1_component_condition.from_dict(v1_component_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


