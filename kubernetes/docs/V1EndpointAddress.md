# V1EndpointAddress

EndpointAddress is a tuple that describes single IP address.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready. | 
**hostname** | **str** | The Hostname of this endpoint | [optional] 
**node_name** | **str** | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. | [optional] 
**target_ref** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


