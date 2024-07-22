# V1FlockerVolumeSource

Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_name** | **str** | datasetName is Name of the dataset stored as metadata -&gt; name on the dataset for Flocker should be considered as deprecated | [optional] 
**dataset_uuid** | **str** | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset | [optional] 

## Example

```python
from kubernetes.client.models.v1_flocker_volume_source import V1FlockerVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlockerVolumeSource from a JSON string
v1_flocker_volume_source_instance = V1FlockerVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1FlockerVolumeSource.to_json()

# convert the object into a dict
v1_flocker_volume_source_dict = v1_flocker_volume_source_instance.to_dict()
# create an instance of V1FlockerVolumeSource from a dict
v1_flocker_volume_source_form_dict = v1_flocker_volume_source.from_dict(v1_flocker_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


