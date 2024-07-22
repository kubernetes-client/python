# V1alpha1ValidatingAdmissionPolicyStatus

ValidatingAdmissionPolicyStatus represents the status of a ValidatingAdmissionPolicy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | The conditions represent the latest available observations of a policy&#39;s current state. | [optional] 
**observed_generation** | **int** | The generation observed by the controller. | [optional] 
**type_checking** | [**V1alpha1TypeChecking**](V1alpha1TypeChecking.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_validating_admission_policy_status import V1alpha1ValidatingAdmissionPolicyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ValidatingAdmissionPolicyStatus from a JSON string
v1alpha1_validating_admission_policy_status_instance = V1alpha1ValidatingAdmissionPolicyStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1ValidatingAdmissionPolicyStatus.to_json()

# convert the object into a dict
v1alpha1_validating_admission_policy_status_dict = v1alpha1_validating_admission_policy_status_instance.to_dict()
# create an instance of V1alpha1ValidatingAdmissionPolicyStatus from a dict
v1alpha1_validating_admission_policy_status_form_dict = v1alpha1_validating_admission_policy_status.from_dict(v1alpha1_validating_admission_policy_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


