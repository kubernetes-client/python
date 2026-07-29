# V2APIGroupDiscovery

APIGroupDiscovery holds information about which resources are being served for all version of the API Group. It contains a list of APIVersionDiscovery that holds a list of APIResourceDiscovery types served for a version. Versions are in descending order of preference, with the first version being the preferred entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional]
**kind** | **str** |  | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**versions** | [**List[V2APIVersionDiscovery]**](V2APIVersionDiscovery.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v2_api_group_discovery import V2APIGroupDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of V2APIGroupDiscovery from a JSON string
v2_api_group_discovery_instance = V2APIGroupDiscovery.from_json(json)
# print the JSON string representation of the object
print(V2APIGroupDiscovery.to_json())

# convert the object into a dict
v2_api_group_discovery_dict = v2_api_group_discovery_instance.to_dict()
# create an instance of V2APIGroupDiscovery from a dict
v2_api_group_discovery_from_dict = V2APIGroupDiscovery.from_dict(v2_api_group_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
