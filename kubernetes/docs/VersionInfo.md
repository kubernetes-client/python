# VersionInfo

Info contains versioning information. how we'll want to distribute that information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **str** |  | 
**compiler** | **str** |  | 
**git_commit** | **str** |  | 
**git_tree_state** | **str** |  | 
**git_version** | **str** |  | 
**go_version** | **str** |  | 
**major** | **str** |  | 
**minor** | **str** |  | 
**platform** | **str** |  | 

## Example

```python
from kubernetes.client.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print VersionInfo.to_json()

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_form_dict = version_info.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


