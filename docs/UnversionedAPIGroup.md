# UnversionedAPIGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the group. | 
**preferred_version** | [**UnversionedGroupVersionForDiscovery**](UnversionedGroupVersionForDiscovery.md) | preferredVersion is the version preferred by the API server, which probably is the storage version. | [optional] 
**server_address_by_client_cid_rs** | [**list[UnversionedServerAddressByClientCIDR]**](UnversionedServerAddressByClientCIDR.md) | a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP. | 
**versions** | [**list[UnversionedGroupVersionForDiscovery]**](UnversionedGroupVersionForDiscovery.md) | versions are the versions supported in this group. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


