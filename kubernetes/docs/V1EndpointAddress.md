# V1EndpointAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The Hostname of this endpoint | [optional] 
**ip** | **str** | The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready. | 
**node_name** | **str** | Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node. | [optional] 
**target_ref** | [**V1ObjectReference**](V1ObjectReference.md) | Reference to object providing the endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


