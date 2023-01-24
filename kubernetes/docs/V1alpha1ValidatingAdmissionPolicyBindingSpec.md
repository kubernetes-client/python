# V1alpha1ValidatingAdmissionPolicyBindingSpec

ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1alpha1MatchResources**](V1alpha1MatchResources.md) |  | [optional] 
**param_ref** | [**V1alpha1ParamRef**](V1alpha1ParamRef.md) |  | [optional] 
**policy_name** | **str** | PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


