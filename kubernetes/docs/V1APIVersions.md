# V1APIVersions

APIVersions lists the versions that are available, to allow kubernetes.clients to discover the API at /api, which is the root path of the legacy v1 API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**server_address_by_client_cidrs** | [**List[V1ServerAddressByClientCIDR]**](V1ServerAddressByClientCIDR.md) | a map of kubernetes.client CIDR to server address that is serving this group. This is to help kubernetes.clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, kubernetes.clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the kubernetes.client can match. For example: the master will return an internal IP CIDR only, if the kubernetes.client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the kubernetes.client IP. | 
**versions** | **List[str]** | versions are the api versions that are available. | 

## Example

```python
from kubernetes.client.models.v1_api_versions import V1APIVersions

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIVersions from a JSON string
v1_api_versions_instance = V1APIVersions.from_json(json)
# print the JSON string representation of the object
print V1APIVersions.to_json()

# convert the object into a dict
v1_api_versions_dict = v1_api_versions_instance.to_dict()
# create an instance of V1APIVersions from a dict
v1_api_versions_form_dict = v1_api_versions.from_dict(v1_api_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


