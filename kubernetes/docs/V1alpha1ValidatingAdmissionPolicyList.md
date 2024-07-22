# V1alpha1ValidatingAdmissionPolicyList

ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1alpha1ValidatingAdmissionPolicy]**](V1alpha1ValidatingAdmissionPolicy.md) | List of ValidatingAdmissionPolicy. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy_list import V1alpha1ValidatingAdmissionPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicyList from a JSON string
v1alpha1_validating_admission_policy_list_instance = V1alpha1ValidatingAdmissionPolicyList.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicyList.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_list_dict = v1alpha1_validating_admission_policy_list_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicyList from a dict
v1alpha1_validating_admission_policy_list_form_dict = v1alpha1_validating_admission_policy_list.from_dict(v1alpha1_validating_admission_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


