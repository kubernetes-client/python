# V1beta1MutatingAdmissionPolicyBindingSpec

MutatingAdmissionPolicyBindingSpec is the specification of the MutatingAdmissionPolicyBinding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_resources** | [**V1beta1MatchResources**](V1beta1MatchResources.md) |  | [optional]
**param_ref** | [**V1beta1ParamRef**](V1beta1ParamRef.md) |  | [optional]
**policy_name** | **str** | policyName references a MutatingAdmissionPolicy name which the MutatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_mutating_admission_policy_binding_spec import V1beta1MutatingAdmissionPolicyBindingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1MutatingAdmissionPolicyBindingSpec from a JSON string
v1beta1_mutating_admission_policy_binding_spec_instance = V1beta1MutatingAdmissionPolicyBindingSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1MutatingAdmissionPolicyBindingSpec.to_json())

# convert the object into a dict
v1beta1_mutating_admission_policy_binding_spec_dict = v1beta1_mutating_admission_policy_binding_spec_instance.to_dict()
# create an instance of V1beta1MutatingAdmissionPolicyBindingSpec from a dict
v1beta1_mutating_admission_policy_binding_spec_from_dict = V1beta1MutatingAdmissionPolicyBindingSpec.from_dict(v1beta1_mutating_admission_policy_binding_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
