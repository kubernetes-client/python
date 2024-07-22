# V1KeyToPath

Maps a string key to a path within a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is the key to project. | 
**mode** | **int** | mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**path** | **str** | path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element &#39;..&#39;. May not start with the string &#39;..&#39;. | 

## Example

```python
from kubernetes.client.models.v1_key_to_path import V1KeyToPath

# TODO update the JSON string below
json = "{}"
# create an instance of V1KeyToPath from a JSON string
v1_key_to_path_instance = V1KeyToPath.from_json(json)
# print the JSON string representation of the object
print V1KeyToPath.to_json()

# convert the object into a dict
v1_key_to_path_dict = v1_key_to_path_instance.to_dict()
# create an instance of V1KeyToPath from a dict
v1_key_to_path_form_dict = v1_key_to_path.from_dict(v1_key_to_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


