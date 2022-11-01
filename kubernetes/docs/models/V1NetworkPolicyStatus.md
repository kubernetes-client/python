# kubernetes.client.model.v1_network_policy_status.V1NetworkPolicyStatus

NetworkPolicyStatus describe the current state of the NetworkPolicy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NetworkPolicyStatus describe the current state of the NetworkPolicy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[conditions](#conditions)** | list, tuple,  | tuple,  | Conditions holds an array of metav1.Condition that describe the state of the NetworkPolicy. Current service state | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Conditions holds an array of metav1.Condition that describe the state of the NetworkPolicy. Current service state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Conditions holds an array of metav1.Condition that describe the state of the NetworkPolicy. Current service state | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1Condition**](V1Condition.md) | [**V1Condition**](V1Condition.md) | [**V1Condition**](V1Condition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

