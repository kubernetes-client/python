# V1ServerAddressByClientCIDR

ServerAddressByClientCIDR helps the kubernetes.client to determine the server address that they should use, depending on the kubernetes.clientCIDR that they match.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_cidr** | **str** | The CIDR with which kubernetes.clients can match their IP to figure out the server address that they should use. | 
**server_address** | **str** | Address of this server, suitable for a kubernetes.client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


