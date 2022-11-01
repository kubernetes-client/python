# kubernetes.client.model.v1_pod_failure_policy_on_pod_conditions_pattern.V1PodFailurePolicyOnPodConditionsPattern

PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PodFailurePolicyOnPodConditionsPattern describes a pattern for matching an actual pod condition type. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Specifies the required Pod condition type. To match a pod condition it is required that specified type equals the pod condition type. | 
**status** | str,  | str,  | Specifies the required Pod condition status. To match a pod condition it is required that the specified status equals the pod condition status. Defaults to True. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

