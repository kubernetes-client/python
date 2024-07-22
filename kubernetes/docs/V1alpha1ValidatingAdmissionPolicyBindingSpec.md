# V1alpha1ValidatingAdmissionPolicyBindingSpec

ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1alpha1MatchResources**](V1alpha1MatchResources.md) |  | [optional] 
**param_ref** | [**V1alpha1ParamRef**](V1alpha1ParamRef.md) |  | [optional] 
**policy_name** | **str** | PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional] 
**validation_actions** | **List[str]** | validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy&#39;s FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  \&quot;Deny\&quot; specifies that a validation failure results in a denied request.  \&quot;Warn\&quot; specifies that a validation failure is reported to the request kubernetes.client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  \&quot;Audit\&quot; specifies that a validation failure is included in the published audit event for the request. The audit event will contain a &#x60;validation.policy.admission.k8s.io/validation_failure&#x60; audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: &#x60;\&quot;validation.policy.admission.k8s.io/validation_failure\&quot;: \&quot;[{\&quot;message\&quot;: \&quot;Invalid value\&quot;, {\&quot;policy\&quot;: \&quot;policy.example.com\&quot;, {\&quot;binding\&quot;: \&quot;policybinding.example.com\&quot;, {\&quot;expressionIndex\&quot;: \&quot;1\&quot;, {\&quot;validationActions\&quot;: [\&quot;Audit\&quot;]}]\&quot;&#x60;  Clients should expect to handle additional values by ignoring any values not recognized.  \&quot;Deny\&quot; and \&quot;Warn\&quot; may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy_binding_spec import V1alpha1ValidatingAdmissionPolicyBindingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicyBindingSpec from a JSON string
v1alpha1_validating_admission_policy_binding_spec_instance = V1alpha1ValidatingAdmissionPolicyBindingSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicyBindingSpec.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_binding_spec_dict = v1alpha1_validating_admission_policy_binding_spec_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicyBindingSpec from a dict
v1alpha1_validating_admission_policy_binding_spec_form_dict = v1alpha1_validating_admission_policy_binding_spec.from_dict(v1alpha1_validating_admission_policy_binding_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


