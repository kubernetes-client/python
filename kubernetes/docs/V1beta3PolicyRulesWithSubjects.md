# V1beta3PolicyRulesWithSubjects

PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_resource_rules** | [**List[V1beta3NonResourcePolicyRule]**](V1beta3NonResourcePolicyRule.md) | &#x60;nonResourceRules&#x60; is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL. | [optional] 
**resource_rules** | [**List[V1beta3ResourcePolicyRule]**](V1beta3ResourcePolicyRule.md) | &#x60;resourceRules&#x60; is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of &#x60;resourceRules&#x60; and &#x60;nonResourceRules&#x60; has to be non-empty. | [optional] 
**subjects** | [**List[V1beta3Subject]**](V1beta3Subject.md) | subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_policy_rules_with_subjects import V1beta3PolicyRulesWithSubjects

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3PolicyRulesWithSubjects from a JSON string
v1beta3_policy_rules_with_subjects_instance = V1beta3PolicyRulesWithSubjects.from_json(json)
# print the JSON string representation of the object
print V1beta3PolicyRulesWithSubjects.to_json()

# convert the object into a dict
v1beta3_policy_rules_with_subjects_dict = v1beta3_policy_rules_with_subjects_instance.to_dict()
# create an instance of V1beta3PolicyRulesWithSubjects from a dict
v1beta3_policy_rules_with_subjects_form_dict = v1beta3_policy_rules_with_subjects.from_dict(v1beta3_policy_rules_with_subjects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


