# V1ContainerStateWaiting

ContainerStateWaiting is a waiting state of a container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message regarding why the container is not yet running. | [optional] 
**reason** | **str** | (brief) reason the container is not yet running. | [optional] 

## Example

```python
from kubernetes.client.models.v1_container_state_waiting import V1ContainerStateWaiting

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerStateWaiting from a JSON string
v1_container_state_waiting_instance = V1ContainerStateWaiting.from_json(json)
# print the JSON string representation of the object
print V1ContainerStateWaiting.to_json()

# convert the object into a dict
v1_container_state_waiting_dict = v1_container_state_waiting_instance.to_dict()
# create an instance of V1ContainerStateWaiting from a dict
v1_container_state_waiting_form_dict = v1_container_state_waiting.from_dict(v1_container_state_waiting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


