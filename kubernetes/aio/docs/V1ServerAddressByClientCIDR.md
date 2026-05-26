# V1ServerAddressByClientCIDR

ServerAddressByClientCIDR helps the kubernetes.aio.client to determine the server address that they should use, depending on the kubernetes.aio.clientCIDR that they match.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.aio.client_cidr** | **str** | The CIDR with which kubernetes.aio.clients can match their IP to figure out the server address that they should use. | 
**server_address** | **str** | Address of this server, suitable for a kubernetes.aio.client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


