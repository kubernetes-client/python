# kubernetes.client.model.v1_azure_file_volume_source.V1AzureFileVolumeSource

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**secretName** | str,  | str,  | secretName is the  name of secret that contains Azure Storage Account Name and Key | 
**shareName** | str,  | str,  | shareName is the azure share Name | 
**readOnly** | bool,  | BoolClass,  | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

