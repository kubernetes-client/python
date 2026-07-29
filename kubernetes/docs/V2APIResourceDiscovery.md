# V2APIResourceDiscovery

APIResourceDiscovery provides information about an API resource for discovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | resource is the plural name of the resource. |
**response_kind** | [**V1GroupVersionKind**](V1GroupVersionKind.md) |  | [optional]
**scope** | **str** | scope indicates the scope of a resource, either Cluster or Namespaced |
**singular_resource** | **str** | singularResource is the singular name of the resource. |
**verbs** | **List[str]** | verbs is a list of supported API operation types |
**short_names** | **List[str]** | shortNames is a list of suggested short names of the resource. | [optional]
**categories** | **List[str]** | categories is a list of the grouped resources this resource belongs to. | [optional]
**subresources** | [**List[V2APISubresourceDiscovery]**](V2APISubresourceDiscovery.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v2_api_resource_discovery import V2APIResourceDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of V2APIResourceDiscovery from a JSON string
v2_api_resource_discovery_instance = V2APIResourceDiscovery.from_json(json)
# print the JSON string representation of the object
print(V2APIResourceDiscovery.to_json())

# convert the object into a dict
v2_api_resource_discovery_dict = v2_api_resource_discovery_instance.to_dict()
# create an instance of V2APIResourceDiscovery from a dict
v2_api_resource_discovery_from_dict = V2APIResourceDiscovery.from_dict(v2_api_resource_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
