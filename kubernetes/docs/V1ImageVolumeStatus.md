# V1ImageVolumeStatus

ImageVolumeStatus represents the image-based volume status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_ref** | **str** | ImageRef is the digest of the image used for this volume. It should have a value that&#39;s similar to the pod&#39;s status.containerStatuses[i].imageID. The ImageRef length should not exceed 256 characters. |

## Example

```python
from kubernetes.client.models.v1_image_volume_status import V1ImageVolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ImageVolumeStatus from a JSON string
v1_image_volume_status_instance = V1ImageVolumeStatus.from_json(json)
# print the JSON string representation of the object
print(V1ImageVolumeStatus.to_json())

# convert the object into a dict
v1_image_volume_status_dict = v1_image_volume_status_instance.to_dict()
# create an instance of V1ImageVolumeStatus from a dict
v1_image_volume_status_from_dict = V1ImageVolumeStatus.from_dict(v1_image_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
