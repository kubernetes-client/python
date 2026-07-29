# V1ContainerExtendedResourceRequest

ContainerExtendedResourceRequest has the mapping of container name, extended resource name to the device request name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** | The name of the container requesting resources. |
**request_name** | **str** | The name of the request in the special ResourceClaim which corresponds to the extended resource. |
**resource_name** | **str** | The name of the extended resource in that container which gets backed by DRA. |

## Example

```python
from kubernetes.client.models.v1_container_extended_resource_request import V1ContainerExtendedResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerExtendedResourceRequest from a JSON string
v1_container_extended_resource_request_instance = V1ContainerExtendedResourceRequest.from_json(json)
# print the JSON string representation of the object
print(V1ContainerExtendedResourceRequest.to_json())

# convert the object into a dict
v1_container_extended_resource_request_dict = v1_container_extended_resource_request_instance.to_dict()
# create an instance of V1ContainerExtendedResourceRequest from a dict
v1_container_extended_resource_request_from_dict = V1ContainerExtendedResourceRequest.from_dict(v1_container_extended_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
