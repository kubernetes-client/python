# V1PodFailurePolicyOnPodConditionsPattern

PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. | 
**type** | **str** | Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. | 

## Example

```python
from kubernetes.client.models.v1_pod_failure_policy_on_pod_conditions_pattern import V1PodFailurePolicyOnPodConditionsPattern

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodFailurePolicyOnPodConditionsPattern from a JSON string
v1_pod_failure_policy_on_pod_conditions_pattern_instance = V1PodFailurePolicyOnPodConditionsPattern.from_json(json)
# print the JSON string representation of the object
print V1PodFailurePolicyOnPodConditionsPattern.to_json()

# convert the object into a dict
v1_pod_failure_policy_on_pod_conditions_pattern_dict = v1_pod_failure_policy_on_pod_conditions_pattern_instance.to_dict()
# create an instance of V1PodFailurePolicyOnPodConditionsPattern from a dict
v1_pod_failure_policy_on_pod_conditions_pattern_form_dict = v1_pod_failure_policy_on_pod_conditions_pattern.from_dict(v1_pod_failure_policy_on_pod_conditions_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


