# V1beta1MutatingAdmissionPolicy

MutatingAdmissionPolicy describes the definition of an admission mutation policy that mutates the object coming into admission chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1beta1MutatingAdmissionPolicySpec**](V1beta1MutatingAdmissionPolicySpec.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_mutating_admission_policy import V1beta1MutatingAdmissionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1MutatingAdmissionPolicy from a JSON string
v1beta1_mutating_admission_policy_instance = V1beta1MutatingAdmissionPolicy.from_json(json)
# print the JSON string representation of the object
print(V1beta1MutatingAdmissionPolicy.to_json())

# convert the object into a dict
v1beta1_mutating_admission_policy_dict = v1beta1_mutating_admission_policy_instance.to_dict()
# create an instance of V1beta1MutatingAdmissionPolicy from a dict
v1beta1_mutating_admission_policy_from_dict = V1beta1MutatingAdmissionPolicy.from_dict(v1beta1_mutating_admission_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
