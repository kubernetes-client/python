# kubernetes.client.model.v1_container_port.V1ContainerPort

ContainerPort represents a network port in a single container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ContainerPort represents a network port in a single container. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**containerPort** | decimal.Decimal, int,  | decimal.Decimal,  | Number of port to expose on the pod&#x27;s IP address. This must be a valid port number, 0 &lt; x &lt; 65536. | value must be a 32 bit integer
**hostIP** | str,  | str,  | What host IP to bind the external port to. | [optional] 
**hostPort** | decimal.Decimal, int,  | decimal.Decimal,  | Number of port to expose on the host. If specified, this must be a valid port number, 0 &lt; x &lt; 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this. | [optional] value must be a 32 bit integer
**name** | str,  | str,  | If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services. | [optional] 
**protocol** | str,  | str,  | Protocol for port. Must be UDP, TCP, or SCTP. Defaults to \&quot;TCP\&quot;.   | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

