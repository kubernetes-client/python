# V1alpha3ResourcePoolStatusRequest

ResourcePoolStatusRequest triggers a one-time calculation of resource pool status based on the provided filters. Once status is set, the request is considered complete and will not be reprocessed. Users should delete and recreate requests to get updated information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  |
**spec** | [**V1alpha3ResourcePoolStatusRequestSpec**](V1alpha3ResourcePoolStatusRequestSpec.md) |  |
**status** | [**V1alpha3ResourcePoolStatusRequestStatus**](V1alpha3ResourcePoolStatusRequestStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_resource_pool_status_request import V1alpha3ResourcePoolStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourcePoolStatusRequest from a JSON string
v1alpha3_resource_pool_status_request_instance = V1alpha3ResourcePoolStatusRequest.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourcePoolStatusRequest.to_json())

# convert the object into a dict
v1alpha3_resource_pool_status_request_dict = v1alpha3_resource_pool_status_request_instance.to_dict()
# create an instance of V1alpha3ResourcePoolStatusRequest from a dict
v1alpha3_resource_pool_status_request_from_dict = V1alpha3ResourcePoolStatusRequest.from_dict(v1alpha3_resource_pool_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
