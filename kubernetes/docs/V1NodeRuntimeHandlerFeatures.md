# V1NodeRuntimeHandlerFeatures

NodeRuntimeHandlerFeatures is a set of runtime features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recursive_read_only_mounts** | **bool** | RecursiveReadOnlyMounts is set to true if the runtime handler supports RecursiveReadOnlyMounts. | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeRuntimeHandlerFeatures from a JSON string
v1_node_runtime_handler_features_instance = V1NodeRuntimeHandlerFeatures.from_json(json)
# print the JSON string representation of the object
print V1NodeRuntimeHandlerFeatures.to_json()

# convert the object into a dict
v1_node_runtime_handler_features_dict = v1_node_runtime_handler_features_instance.to_dict()
# create an instance of V1NodeRuntimeHandlerFeatures from a dict
v1_node_runtime_handler_features_form_dict = v1_node_runtime_handler_features.from_dict(v1_node_runtime_handler_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


