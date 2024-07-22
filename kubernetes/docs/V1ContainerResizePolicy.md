# V1ContainerResizePolicy

ContainerResizePolicy represents resource resize policy for the container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_name** | **str** | Name of the resource to which this resource resize policy applies. Supported values: cpu, memory. | 
**restart_policy** | **str** | Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired. | 

## Example

```python
from kubernetes.client.models.v1_container_resize_policy import V1ContainerResizePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerResizePolicy from a JSON string
v1_container_resize_policy_instance = V1ContainerResizePolicy.from_json(json)
# print the JSON string representation of the object
print V1ContainerResizePolicy.to_json()

# convert the object into a dict
v1_container_resize_policy_dict = v1_container_resize_policy_instance.to_dict()
# create an instance of V1ContainerResizePolicy from a dict
v1_container_resize_policy_form_dict = v1_container_resize_policy.from_dict(v1_container_resize_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


