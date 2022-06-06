# V1AzureFilePersistentVolumeSource

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_name** | **str** | secretName is the name of secret that contains Azure Storage Account Name and Key | 
**secret_namespace** | **str** | secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod | [optional] 
**share_name** | **str** | shareName is the azure Share Name | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


