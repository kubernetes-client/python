# V1beta1TypeChecking

TypeChecking contains results of type checking the expressions in the ValidatingAdmissionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_warnings** | [**List[V1beta1ExpressionWarning]**](V1beta1ExpressionWarning.md) | The type checking warnings for each expression. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_type_checking import V1beta1TypeChecking

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1TypeChecking from a JSON string
v1beta1_type_checking_instance = V1beta1TypeChecking.from_json(json)
# print the JSON string representation of the object
print V1beta1TypeChecking.to_json()

# convert the object into a dict
v1beta1_type_checking_dict = v1beta1_type_checking_instance.to_dict()
# create an instance of V1beta1TypeChecking from a dict
v1beta1_type_checking_form_dict = v1beta1_type_checking.from_dict(v1beta1_type_checking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


