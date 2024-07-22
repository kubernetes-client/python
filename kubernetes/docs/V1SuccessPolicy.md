# V1SuccessPolicy

SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[V1SuccessPolicyRule]**](V1SuccessPolicyRule.md) | rules represents the list of alternative rules for the declaring the Jobs as successful before &#x60;.status.succeeded &gt;&#x3D; .spec.completions&#x60;. Once any of the rules are met, the \&quot;SucceededCriteriaMet\&quot; condition is added, and the lingering pods are removed. The terminal state for such a Job has the \&quot;Complete\&quot; condition. Additionally, these rules are evaluated in order; Once the Job meets one of the rules, other rules are ignored. At most 20 elements are allowed. | 

## Example

```python
from kubernetes.client.models.v1_success_policy import V1SuccessPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1SuccessPolicy from a JSON string
v1_success_policy_instance = V1SuccessPolicy.from_json(json)
# print the JSON string representation of the object
print V1SuccessPolicy.to_json()

# convert the object into a dict
v1_success_policy_dict = v1_success_policy_instance.to_dict()
# create an instance of V1SuccessPolicy from a dict
v1_success_policy_form_dict = v1_success_policy.from_dict(v1_success_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


