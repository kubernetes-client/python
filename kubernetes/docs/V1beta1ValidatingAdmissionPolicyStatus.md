# V1beta1ValidatingAdmissionPolicyStatus

ValidatingAdmissionPolicyStatus represents the status of an admission validation policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | The conditions represent the latest available observations of a policy&#39;s current state. | [optional] 
**observed_generation** | **int** | The generation observed by the controller. | [optional] 
**type_checking** | [**V1beta1TypeChecking**](V1beta1TypeChecking.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_validating_admission_policy_status import V1beta1ValidatingAdmissionPolicyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ValidatingAdmissionPolicyStatus from a JSON string
v1beta1_validating_admission_policy_status_instance = V1beta1ValidatingAdmissionPolicyStatus.from_json(json)
# print the JSON string representation of the object
print V1beta1ValidatingAdmissionPolicyStatus.to_json()

# convert the object into a dict
v1beta1_validating_admission_policy_status_dict = v1beta1_validating_admission_policy_status_instance.to_dict()
# create an instance of V1beta1ValidatingAdmissionPolicyStatus from a dict
v1beta1_validating_admission_policy_status_form_dict = v1beta1_validating_admission_policy_status.from_dict(v1beta1_validating_admission_policy_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


