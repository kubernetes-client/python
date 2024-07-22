# V1alpha1ValidatingAdmissionPolicyBinding

ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.  For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.  The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1ValidatingAdmissionPolicyBindingSpec**](V1alpha1ValidatingAdmissionPolicyBindingSpec.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy_binding import V1alpha1ValidatingAdmissionPolicyBinding

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicyBinding from a JSON string
v1alpha1_validating_admission_policy_binding_instance = V1alpha1ValidatingAdmissionPolicyBinding.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicyBinding.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_binding_dict = v1alpha1_validating_admission_policy_binding_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicyBinding from a dict
v1alpha1_validating_admission_policy_binding_form_dict = v1alpha1_validating_admission_policy_binding.from_dict(v1alpha1_validating_admission_policy_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


