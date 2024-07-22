# V1APIGroupList

APIGroupList is a list of APIGroup, to allow kubernetes.clients to discover the API at /apis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**groups** | [**List[V1APIGroup]**](V1APIGroup.md) | groups is a list of APIGroup. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 

## Example

```python
from kubernetes.client.models.v1_api_group_list import V1APIGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIGroupList from a JSON string
v1_api_group_list_instance = V1APIGroupList.from_json(json)
# print the JSON string representation of the object
print V1APIGroupList.to_json()

# convert the object into a dict
v1_api_group_list_dict = v1_api_group_list_instance.to_dict()
# create an instance of V1APIGroupList from a dict
v1_api_group_list_form_dict = v1_api_group_list.from_dict(v1_api_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


