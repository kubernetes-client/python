# V1EndpointHints

EndpointHints provides hints describing how an endpoint should be consumed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_nodes** | [**List[V1ForNode]**](V1ForNode.md) | forNodes indicates the node(s) this endpoint should be consumed by when using topology aware routing. May contain a maximum of 8 entries. | [optional]
**for_zones** | [**List[V1ForZone]**](V1ForZone.md) | forZones indicates the zone(s) this endpoint should be consumed by when using topology aware routing. May contain a maximum of 8 entries. | [optional]

## Example

```python
from kubernetes.client.models.v1_endpoint_hints import V1EndpointHints

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointHints from a JSON string
v1_endpoint_hints_instance = V1EndpointHints.from_json(json)
# print the JSON string representation of the object
print(V1EndpointHints.to_json())

# convert the object into a dict
v1_endpoint_hints_dict = v1_endpoint_hints_instance.to_dict()
# create an instance of V1EndpointHints from a dict
v1_endpoint_hints_from_dict = V1EndpointHints.from_dict(v1_endpoint_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
