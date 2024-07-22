# V1NodeRuntimeHandler

NodeRuntimeHandler is a set of runtime handler information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**V1NodeRuntimeHandlerFeatures**](V1NodeRuntimeHandlerFeatures.md) |  | [optional] 
**name** | **str** | Runtime handler name. Empty for the default runtime handler. | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_runtime_handler import V1NodeRuntimeHandler

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeRuntimeHandler from a JSON string
v1_node_runtime_handler_instance = V1NodeRuntimeHandler.from_json(json)
# print the JSON string representation of the object
print V1NodeRuntimeHandler.to_json()

# convert the object into a dict
v1_node_runtime_handler_dict = v1_node_runtime_handler_instance.to_dict()
# create an instance of V1NodeRuntimeHandler from a dict
v1_node_runtime_handler_form_dict = v1_node_runtime_handler.from_dict(v1_node_runtime_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


