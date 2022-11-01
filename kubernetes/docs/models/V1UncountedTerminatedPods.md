# kubernetes.client.model.v1_uncounted_terminated_pods.V1UncountedTerminatedPods

UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | UncountedTerminatedPods holds UIDs of Pods that have terminated but haven&#x27;t been accounted in Job status counters. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[failed](#failed)** | list, tuple,  | tuple,  | Failed holds UIDs of failed Pods. | [optional] 
**[succeeded](#succeeded)** | list, tuple,  | tuple,  | Succeeded holds UIDs of succeeded Pods. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# failed

Failed holds UIDs of failed Pods.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Failed holds UIDs of failed Pods. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# succeeded

Succeeded holds UIDs of succeeded Pods.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Succeeded holds UIDs of succeeded Pods. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

