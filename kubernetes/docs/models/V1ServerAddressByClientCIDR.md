# kubernetes.client.model.v1_server_address_by_client_cidr.V1ServerAddressByClientCIDR

ServerAddressByClientCIDR helps the kubernetes.client to determine the server address that they should use, depending on the kubernetes.clientCIDR that they match.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ServerAddressByClientCIDR helps the kubernetes.client to determine the server address that they should use, depending on the kubernetes.clientCIDR that they match. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kubernetes.clientCIDR** | str,  | str,  | The CIDR with which kubernetes.clients can match their IP to figure out the server address that they should use. | 
**serverAddress** | str,  | str,  | Address of this server, suitable for a kubernetes.client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

