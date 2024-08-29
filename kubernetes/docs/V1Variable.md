# V1Variable

Variable is the definition of a variable that is used for composition. A variable is defined as a named expression.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | Expression is the expression that will be evaluated as the value of the variable. The CEL expression has access to the same identifiers as the CEL expressions in Validation. | 
**name** | **str** | Name is the name of the variable. The name must be a valid CEL identifier and unique among all variables. The variable can be accessed in other expressions through &#x60;variables&#x60; For example, if name is \&quot;foo\&quot;, the variable will be available as &#x60;variables.foo&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


