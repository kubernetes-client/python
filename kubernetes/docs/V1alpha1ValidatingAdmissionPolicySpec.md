# V1alpha1ValidatingAdmissionPolicySpec

ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_policy** | **str** | FailurePolicy defines how to handle failures for the admission policy. Failures can occur from invalid or mis-configured policy definitions or bindings. A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource. Allowed values are Ignore or Fail. Defaults to Fail. | [optional] 
**match_constraints** | [**V1alpha1MatchResources**](V1alpha1MatchResources.md) |  | [optional] 
**param_kind** | [**V1alpha1ParamKind**](V1alpha1ParamKind.md) |  | [optional] 
**validations** | [**list[V1alpha1Validation]**](V1alpha1Validation.md) | Validations contain CEL expressions which is used to apply the validation. A minimum of one validation is required for a policy definition. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


