# V1AzureFilePersistentVolumeSource

AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_name** | **str** | secretName is the name of secret that contains Azure Storage Account Name and Key | 
**secret_namespace** | **str** | secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod | [optional] 
**share_name** | **str** | shareName is the azure Share Name | 

## Example

```python
from kubernetes.client.models.v1_azure_file_persistent_volume_source import V1AzureFilePersistentVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1AzureFilePersistentVolumeSource from a JSON string
v1_azure_file_persistent_volume_source_instance = V1AzureFilePersistentVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1AzureFilePersistentVolumeSource.to_json()

# convert the object into a dict
v1_azure_file_persistent_volume_source_dict = v1_azure_file_persistent_volume_source_instance.to_dict()
# create an instance of V1AzureFilePersistentVolumeSource from a dict
v1_azure_file_persistent_volume_source_form_dict = v1_azure_file_persistent_volume_source.from_dict(v1_azure_file_persistent_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


