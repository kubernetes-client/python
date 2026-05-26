# V1ExpressionWarning

ExpressionWarning is a warning information that targets a specific expression.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_ref** | **str** | fieldRef is the path to the field that refers to the expression. For example, the reference to the expression of the first item of validations is \&quot;spec.validations[0].expression\&quot; | 
**warning** | **str** | warning contains the content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


