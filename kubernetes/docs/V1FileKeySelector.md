# V1FileKeySelector

FileKeySelector selects a key of the env file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except &#39;&#x3D;&#39;. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters. |
**optional** | **bool** | Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod&#39;s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation. | [optional]
**path** | **str** | The path within the volume from which to select the file. Must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. |
**volume_name** | **str** | The name of the volume mount containing the env file. |

## Example

```python
from kubernetes.client.models.v1_file_key_selector import V1FileKeySelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1FileKeySelector from a JSON string
v1_file_key_selector_instance = V1FileKeySelector.from_json(json)
# print the JSON string representation of the object
print(V1FileKeySelector.to_json())

# convert the object into a dict
v1_file_key_selector_dict = v1_file_key_selector_instance.to_dict()
# create an instance of V1FileKeySelector from a dict
v1_file_key_selector_from_dict = V1FileKeySelector.from_dict(v1_file_key_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
