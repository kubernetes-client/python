# V1NodeConfigSource

NodeConfigSource specifies a source of node configuration. Exactly one subfield (excluding metadata) must be non-nil. This API is deprecated since 1.22

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map** | [**V1ConfigMapNodeConfigSource**](V1ConfigMapNodeConfigSource.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_config_source import V1NodeConfigSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeConfigSource from a JSON string
v1_node_config_source_instance = V1NodeConfigSource.from_json(json)
# print the JSON string representation of the object
print V1NodeConfigSource.to_json()

# convert the object into a dict
v1_node_config_source_dict = v1_node_config_source_instance.to_dict()
# create an instance of V1NodeConfigSource from a dict
v1_node_config_source_form_dict = v1_node_config_source.from_dict(v1_node_config_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


