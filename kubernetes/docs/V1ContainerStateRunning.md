# V1ContainerStateRunning

ContainerStateRunning is a running state of a container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **datetime** | Time at which the container was last (re-)started | [optional] 

## Example

```python
from kubernetes.client.models.v1_container_state_running import V1ContainerStateRunning

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerStateRunning from a JSON string
v1_container_state_running_instance = V1ContainerStateRunning.from_json(json)
# print the JSON string representation of the object
print V1ContainerStateRunning.to_json()

# convert the object into a dict
v1_container_state_running_dict = v1_container_state_running_instance.to_dict()
# create an instance of V1ContainerStateRunning from a dict
v1_container_state_running_form_dict = v1_container_state_running.from_dict(v1_container_state_running_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


