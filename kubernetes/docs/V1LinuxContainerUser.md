# V1LinuxContainerUser

LinuxContainerUser represents user identity information in Linux containers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** | GID is the primary gid initially attached to the first process in the container |
**supplemental_groups** | **List[int]** | SupplementalGroups are the supplemental groups initially attached to the first process in the container | [optional]
**uid** | **int** | UID is the primary uid initially attached to the first process in the container |

## Example

```python
from kubernetes.client.models.v1_linux_container_user import V1LinuxContainerUser

# TODO update the JSON string below
json = "{}"
# create an instance of V1LinuxContainerUser from a JSON string
v1_linux_container_user_instance = V1LinuxContainerUser.from_json(json)
# print the JSON string representation of the object
print(V1LinuxContainerUser.to_json())

# convert the object into a dict
v1_linux_container_user_dict = v1_linux_container_user_instance.to_dict()
# create an instance of V1LinuxContainerUser from a dict
v1_linux_container_user_from_dict = V1LinuxContainerUser.from_dict(v1_linux_container_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
