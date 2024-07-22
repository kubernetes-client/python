# V1APIResourceList

APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in a specific group and version, and if the resource is namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**group_version** | **str** | groupVersion is the group and version this APIResourceList is for. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**resources** | [**List[V1APIResource]**](V1APIResource.md) | resources contains the name of the resources and if they are namespaced. | 

## Example

```python
from kubernetes.client.models.v1_api_resource_list import V1APIResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIResourceList from a JSON string
v1_api_resource_list_instance = V1APIResourceList.from_json(json)
# print the JSON string representation of the object
print V1APIResourceList.to_json()

# convert the object into a dict
v1_api_resource_list_dict = v1_api_resource_list_instance.to_dict()
# create an instance of V1APIResourceList from a dict
v1_api_resource_list_form_dict = v1_api_resource_list.from_dict(v1_api_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


