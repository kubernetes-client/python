# V1GroupResource

GroupResource specifies a Group and a Resource, but does not force a version.  This is useful for identifying concepts during lookup stages without having partially valid types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  |
**resource** | **str** |  |

## Example

```python
from kubernetes.client.models.v1_group_resource import V1GroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupResource from a JSON string
v1_group_resource_instance = V1GroupResource.from_json(json)
# print the JSON string representation of the object
print(V1GroupResource.to_json())

# convert the object into a dict
v1_group_resource_dict = v1_group_resource_instance.to_dict()
# create an instance of V1GroupResource from a dict
v1_group_resource_from_dict = V1GroupResource.from_dict(v1_group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
