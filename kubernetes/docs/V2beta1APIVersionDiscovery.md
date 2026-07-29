# V2beta1APIVersionDiscovery

APIVersionDiscovery holds a list of APIResourceDiscovery types that are served for a particular version within an API Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | version is the name of the version within a group version. |
**resources** | [**List[V2beta1APIResourceDiscovery]**](V2beta1APIResourceDiscovery.md) |  | [optional]
**freshness** | **str** | freshness marks whether a group version&#39;s discovery document is up to date. | [optional]

## Example

```python
from kubernetes.client.models.v2beta1_api_version_discovery import V2beta1APIVersionDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of V2beta1APIVersionDiscovery from a JSON string
v2beta1_api_version_discovery_instance = V2beta1APIVersionDiscovery.from_json(json)
# print the JSON string representation of the object
print(V2beta1APIVersionDiscovery.to_json())

# convert the object into a dict
v2beta1_api_version_discovery_dict = v2beta1_api_version_discovery_instance.to_dict()
# create an instance of V2beta1APIVersionDiscovery from a dict
v2beta1_api_version_discovery_from_dict = V2beta1APIVersionDiscovery.from_dict(v2beta1_api_version_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
