# V1alpha1ExpressionWarning

ExpressionWarning is a warning information that targets a specific expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ref** | **str** | The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is \&quot;spec.validations[0].expression\&quot; | 
**warning** | **str** | The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler. | 

## Example

```python
from kubernetes.client.models.v1alpha1_expression_warning import V1alpha1ExpressionWarning

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ExpressionWarning from a JSON string
v1alpha1_expression_warning_instance = V1alpha1ExpressionWarning.from_json(json)
# print the JSON string representation of the object
print V1alpha1ExpressionWarning.to_json()

# convert the object into a dict
v1alpha1_expression_warning_dict = v1alpha1_expression_warning_instance.to_dict()
# create an instance of V1alpha1ExpressionWarning from a dict
v1alpha1_expression_warning_form_dict = v1alpha1_expression_warning.from_dict(v1alpha1_expression_warning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


