# V1beta1MutatingAdmissionPolicyBindingSpec

MutatingAdmissionPolicyBindingSpec is the specification of the MutatingAdmissionPolicyBinding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1beta1MatchResources**](V1beta1MatchResources.md) |  | [optional] 
**param_ref** | [**V1beta1ParamRef**](V1beta1ParamRef.md) |  | [optional] 
**policy_name** | **str** | policyName references a MutatingAdmissionPolicy name which the MutatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


