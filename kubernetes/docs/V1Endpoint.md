# V1Endpoint

Endpoint represents a single logical \"backend\" implementing a service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **list[str]** | addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. | 
**conditions** | [**V1EndpointConditions**](V1EndpointConditions.md) |  | [optional] 
**deprecated_topology** | **dict(str, str)** | deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead. | [optional] 
**hints** | [**V1EndpointHints**](V1EndpointHints.md) |  | [optional] 
**hostname** | **str** | hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation. | [optional] 
**node_name** | **str** | nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate. | [optional] 
**target_ref** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**zone** | **str** | zone is the name of the Zone this endpoint exists in. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


