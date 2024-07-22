# V2HPAScalingPolicy

HPAScalingPolicy is a single policy which must hold true for a specified past interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_seconds** | **int** | periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). | 
**type** | **str** | type is used to specify the scaling policy. | 
**value** | **int** | value contains the amount of change which is permitted by the policy. It must be greater than zero | 

## Example

```python
from kubernetes.client.models.v2_hpa_scaling_policy import V2HPAScalingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V2HPAScalingPolicy from a JSON string
v2_hpa_scaling_policy_instance = V2HPAScalingPolicy.from_json(json)
# print the JSON string representation of the object
print V2HPAScalingPolicy.to_json()

# convert the object into a dict
v2_hpa_scaling_policy_dict = v2_hpa_scaling_policy_instance.to_dict()
# create an instance of V2HPAScalingPolicy from a dict
v2_hpa_scaling_policy_form_dict = v2_hpa_scaling_policy.from_dict(v2_hpa_scaling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


