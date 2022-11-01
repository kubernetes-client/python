# kubernetes.client.model.v1_api_versions.V1APIVersions

APIVersions lists the versions that are available, to allow kubernetes.clients to discover the API at /api, which is the root path of the legacy v1 API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | APIVersions lists the versions that are available, to allow kubernetes.clients to discover the API at /api, which is the root path of the legacy v1 API. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[versions](#versions)** | list, tuple,  | tuple,  | versions are the api versions that are available. | 
**[serverAddressByClientCIDRs](#serverAddressByClientCIDRs)** | list, tuple,  | tuple,  | a map of kubernetes.client CIDR to server address that is serving this group. This is to help kubernetes.clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, kubernetes.clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the kubernetes.client can match. For example: the master will return an internal IP CIDR only, if the kubernetes.client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the kubernetes.client IP. | 
**apiVersion** | str,  | str,  | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | str,  | str,  | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# serverAddressByClientCIDRs

a map of kubernetes.client CIDR to server address that is serving this group. This is to help kubernetes.clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, kubernetes.clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the kubernetes.client can match. For example: the master will return an internal IP CIDR only, if the kubernetes.client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the kubernetes.client IP.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | a map of kubernetes.client CIDR to server address that is serving this group. This is to help kubernetes.clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, kubernetes.clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the kubernetes.client can match. For example: the master will return an internal IP CIDR only, if the kubernetes.client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the kubernetes.client IP. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ServerAddressByClientCIDR**](V1ServerAddressByClientCIDR.md) | [**V1ServerAddressByClientCIDR**](V1ServerAddressByClientCIDR.md) | [**V1ServerAddressByClientCIDR**](V1ServerAddressByClientCIDR.md) |  | 

# versions

versions are the api versions that are available.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | versions are the api versions that are available. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

