# kubernetes.client.model.v1_azure_file_persistent_volume_source.V1AzureFilePersistentVolumeSource

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**secretName** | str,  | str,  | secretName is the name of secret that contains Azure Storage Account Name and Key | 
**shareName** | str,  | str,  | shareName is the azure Share Name | 
**readOnly** | bool,  | BoolClass,  | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secretNamespace** | str,  | str,  | secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

