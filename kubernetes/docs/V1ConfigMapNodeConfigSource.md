# V1ConfigMapNodeConfigSource

ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubelet_config_key** | **str** | KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases. | 
**name** | **str** | Name is the metadata.name of the referenced ConfigMap. This field is required in all cases. | 
**namespace** | **str** | Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases. | 
**resource_version** | **str** | ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. | [optional] 
**uid** | **str** | UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status. | [optional] 

## Example

```python
from kubernetes.client.models.v1_config_map_node_config_source import V1ConfigMapNodeConfigSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1ConfigMapNodeConfigSource from a JSON string
v1_config_map_node_config_source_instance = V1ConfigMapNodeConfigSource.from_json(json)
# print the JSON string representation of the object
print V1ConfigMapNodeConfigSource.to_json()

# convert the object into a dict
v1_config_map_node_config_source_dict = v1_config_map_node_config_source_instance.to_dict()
# create an instance of V1ConfigMapNodeConfigSource from a dict
v1_config_map_node_config_source_form_dict = v1_config_map_node_config_source.from_dict(v1_config_map_node_config_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


