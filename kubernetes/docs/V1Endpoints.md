# V1Endpoints

Endpoints is a collection of endpoints that implement the actual service. Example:    Name: \"mysvc\",   Subsets: [     {       Addresses: [{\"ip\": \"10.10.1.1\"}, {\"ip\": \"10.10.2.2\"}],       Ports: [{\"name\": \"a\", \"port\": 8675}, {\"name\": \"b\", \"port\": 309}]     },     {       Addresses: [{\"ip\": \"10.10.3.3\"}],       Ports: [{\"name\": \"a\", \"port\": 93}, {\"name\": \"b\", \"port\": 76}]     },  ]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**subsets** | [**List[V1EndpointSubset]**](V1EndpointSubset.md) | The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. | [optional] 

## Example

```python
from kubernetes.client.models.v1_endpoints import V1Endpoints

# TODO update the JSON string below
json = "{}"
# create an instance of V1Endpoints from a JSON string
v1_endpoints_instance = V1Endpoints.from_json(json)
# print the JSON string representation of the object
print V1Endpoints.to_json()

# convert the object into a dict
v1_endpoints_dict = v1_endpoints_instance.to_dict()
# create an instance of V1Endpoints from a dict
v1_endpoints_form_dict = v1_endpoints.from_dict(v1_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


