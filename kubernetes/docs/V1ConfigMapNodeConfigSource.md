# V1ConfigMapNodeConfigSource

ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubelet_config_key** | **str** | KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. | 
**name** | **str** | Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. | 
**namespace** | **str** | Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. | 
**resource_version** | **str** | ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. | [optional] 
**uid** | **str** | UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


