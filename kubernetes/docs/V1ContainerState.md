# V1ContainerState

ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**running** | [**V1ContainerStateRunning**](V1ContainerStateRunning.md) |  | [optional] 
**terminated** | [**V1ContainerStateTerminated**](V1ContainerStateTerminated.md) |  | [optional] 
**waiting** | [**V1ContainerStateWaiting**](V1ContainerStateWaiting.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_container_state import V1ContainerState

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerState from a JSON string
v1_container_state_instance = V1ContainerState.from_json(json)
# print the JSON string representation of the object
print V1ContainerState.to_json()

# convert the object into a dict
v1_container_state_dict = v1_container_state_instance.to_dict()
# create an instance of V1ContainerState from a dict
v1_container_state_form_dict = v1_container_state.from_dict(v1_container_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


