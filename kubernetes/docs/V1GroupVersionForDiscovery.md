# V1GroupVersionForDiscovery

GroupVersion contains the \"group/version\" and \"version\" string of a version. It is made a struct to keep extensibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_version** | **str** | groupVersion specifies the API group and version in the form \&quot;group/version\&quot; | 
**version** | **str** | version specifies the version in the form of \&quot;version\&quot;. This is to save the kubernetes.clients the trouble of splitting the GroupVersion. | 

## Example

```python
from kubernetes.client.models.v1_group_version_for_discovery import V1GroupVersionForDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupVersionForDiscovery from a JSON string
v1_group_version_for_discovery_instance = V1GroupVersionForDiscovery.from_json(json)
# print the JSON string representation of the object
print V1GroupVersionForDiscovery.to_json()

# convert the object into a dict
v1_group_version_for_discovery_dict = v1_group_version_for_discovery_instance.to_dict()
# create an instance of V1GroupVersionForDiscovery from a dict
v1_group_version_for_discovery_form_dict = v1_group_version_for_discovery.from_dict(v1_group_version_for_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


