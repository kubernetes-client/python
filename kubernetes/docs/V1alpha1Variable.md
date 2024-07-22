# V1alpha1Variable

Variable is the definition of a variable that is used for composition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. | 
**name** | **str** | Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through &#x60;variables&#x60; For example, if name is \&quot;foo\&quot;, the variable will be available as &#x60;variables.foo&#x60; | 

## Example

```python
from kubernetes.client.models.v1alpha1_variable import V1alpha1Variable

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1Variable from a JSON string
v1alpha1_variable_instance = V1alpha1Variable.from_json(json)
# print the JSON string representation of the object
print V1alpha1Variable.to_json()

# convert the object into a dict
v1alpha1_variable_dict = v1alpha1_variable_instance.to_dict()
# create an instance of V1alpha1Variable from a dict
v1alpha1_variable_form_dict = v1alpha1_variable.from_dict(v1alpha1_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


