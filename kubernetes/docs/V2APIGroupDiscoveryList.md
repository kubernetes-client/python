# V2APIGroupDiscoveryList

APIGroupDiscoveryList is a resource containing a list of APIGroupDiscovery. This is one of the types able to be returned from the /api and /apis endpoint and contains an aggregated list of API resources (built-ins, Custom Resource Definitions, resources from aggregated servers) that a cluster supports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional]
**kind** | **str** |  | [optional]
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional]
**items** | [**List[V2APIGroupDiscovery]**](V2APIGroupDiscovery.md) |  |

## Example

```python
from kubernetes.client.models.v2_api_group_discovery_list import V2APIGroupDiscoveryList

# TODO update the JSON string below
json = "{}"
# create an instance of V2APIGroupDiscoveryList from a JSON string
v2_api_group_discovery_list_instance = V2APIGroupDiscoveryList.from_json(json)
# print the JSON string representation of the object
print(V2APIGroupDiscoveryList.to_json())

# convert the object into a dict
v2_api_group_discovery_list_dict = v2_api_group_discovery_list_instance.to_dict()
# create an instance of V2APIGroupDiscoveryList from a dict
v2_api_group_discovery_list_from_dict = V2APIGroupDiscoveryList.from_dict(v2_api_group_discovery_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
