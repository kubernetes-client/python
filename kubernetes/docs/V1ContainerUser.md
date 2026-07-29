# V1ContainerUser

ContainerUser represents user identity information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linux** | [**V1LinuxContainerUser**](V1LinuxContainerUser.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1_container_user import V1ContainerUser

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerUser from a JSON string
v1_container_user_instance = V1ContainerUser.from_json(json)
# print the JSON string representation of the object
print(V1ContainerUser.to_json())

# convert the object into a dict
v1_container_user_dict = v1_container_user_instance.to_dict()
# create an instance of V1ContainerUser from a dict
v1_container_user_from_dict = V1ContainerUser.from_dict(v1_container_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
