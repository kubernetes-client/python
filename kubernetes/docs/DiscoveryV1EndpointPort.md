# DiscoveryV1EndpointPort

EndpointPort represents a Port used by an EndpointSlice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_protocol** | **str** | The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).  * Kubernetes-defined prefixed names:   * &#39;kubernetes.io/h2c&#39; - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-   * &#39;kubernetes.io/ws&#39;  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455   * &#39;kubernetes.io/wss&#39; - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455  * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol. | [optional] 
**name** | **str** | name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or &#39;-&#39;. * must start and end with an alphanumeric character. Default is empty string. | [optional] 
**port** | **int** | port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer. | [optional] 
**protocol** | **str** | protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP. | [optional] 

## Example

```python
from kubernetes.client.models.discovery_v1_endpoint_port import DiscoveryV1EndpointPort

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryV1EndpointPort from a JSON string
discovery_v1_endpoint_port_instance = DiscoveryV1EndpointPort.from_json(json)
# print the JSON string representation of the object
print DiscoveryV1EndpointPort.to_json()

# convert the object into a dict
discovery_v1_endpoint_port_dict = discovery_v1_endpoint_port_instance.to_dict()
# create an instance of DiscoveryV1EndpointPort from a dict
discovery_v1_endpoint_port_form_dict = discovery_v1_endpoint_port.from_dict(discovery_v1_endpoint_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


