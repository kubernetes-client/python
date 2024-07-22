# V1APIService

APIService represents a server for a particular GroupVersion. Name must be \"version.group\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1APIServiceSpec**](V1APIServiceSpec.md) |  | [optional] 
**status** | [**V1APIServiceStatus**](V1APIServiceStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_api_service import V1APIService

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIService from a JSON string
v1_api_service_instance = V1APIService.from_json(json)
# print the JSON string representation of the object
print V1APIService.to_json()

# convert the object into a dict
v1_api_service_dict = v1_api_service_instance.to_dict()
# create an instance of V1APIService from a dict
v1_api_service_form_dict = v1_api_service.from_dict(v1_api_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


