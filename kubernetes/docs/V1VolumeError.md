# V1VolumeError

VolumeError captures an error encountered during a volume operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information. | [optional] 
**time** | **datetime** | time represents the time the error was encountered. | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_error import V1VolumeError

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeError from a JSON string
v1_volume_error_instance = V1VolumeError.from_json(json)
# print the JSON string representation of the object
print V1VolumeError.to_json()

# convert the object into a dict
v1_volume_error_dict = v1_volume_error_instance.to_dict()
# create an instance of V1VolumeError from a dict
v1_volume_error_form_dict = v1_volume_error.from_dict(v1_volume_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


