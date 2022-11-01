# kubernetes.client.model.v1_se_linux_options.V1SELinuxOptions

SELinuxOptions are the labels to be applied to the container

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SELinuxOptions are the labels to be applied to the container | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**level** | str,  | str,  | Level is SELinux level label that applies to the container. | [optional] 
**role** | str,  | str,  | Role is a SELinux role label that applies to the container. | [optional] 
**type** | str,  | str,  | Type is a SELinux type label that applies to the container. | [optional] 
**user** | str,  | str,  | User is a SELinux user label that applies to the container. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

