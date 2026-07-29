# V2APISubresourceDiscovery

APISubresourceDiscovery provides information about an API subresource for discovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subresource** | **str** | subresource is the name of the subresource. |
**response_kind** | [**V1GroupVersionKind**](V1GroupVersionKind.md) |  | [optional]
**accepted_types** | [**List[V1GroupVersionKind]**](V1GroupVersionKind.md) |  | [optional]
**verbs** | **List[str]** | verbs is a list of supported API operation types |

## Example

```python
from kubernetes.client.models.v2_api_subresource_discovery import V2APISubresourceDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of V2APISubresourceDiscovery from a JSON string
v2_api_subresource_discovery_instance = V2APISubresourceDiscovery.from_json(json)
# print the JSON string representation of the object
print(V2APISubresourceDiscovery.to_json())

# convert the object into a dict
v2_api_subresource_discovery_dict = v2_api_subresource_discovery_instance.to_dict()
# create an instance of V2APISubresourceDiscovery from a dict
v2_api_subresource_discovery_from_dict = V2APISubresourceDiscovery.from_dict(v2_api_subresource_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
