# V1ContainerStateTerminated

ContainerStateTerminated is a terminated state of a container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** | Container&#39;s ID in the format &#39;&lt;type&gt;://&lt;container_id&gt;&#39; | [optional] 
**exit_code** | **int** | Exit status from the last termination of the container | 
**finished_at** | **datetime** | Time at which the container last terminated | [optional] 
**message** | **str** | Message regarding the last termination of the container | [optional] 
**reason** | **str** | (brief) reason from the last termination of the container | [optional] 
**signal** | **int** | Signal from the last termination of the container | [optional] 
**started_at** | **datetime** | Time at which previous execution of the container started | [optional] 

## Example

```python
from kubernetes.client.models.v1_container_state_terminated import V1ContainerStateTerminated

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerStateTerminated from a JSON string
v1_container_state_terminated_instance = V1ContainerStateTerminated.from_json(json)
# print the JSON string representation of the object
print V1ContainerStateTerminated.to_json()

# convert the object into a dict
v1_container_state_terminated_dict = v1_container_state_terminated_instance.to_dict()
# create an instance of V1ContainerStateTerminated from a dict
v1_container_state_terminated_form_dict = v1_container_state_terminated.from_dict(v1_container_state_terminated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


