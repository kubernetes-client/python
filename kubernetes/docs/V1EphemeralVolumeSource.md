# V1EphemeralVolumeSource

Represents an ephemeral volume that is handled by a normal storage driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_claim_template** | [**V1PersistentVolumeClaimTemplate**](V1PersistentVolumeClaimTemplate.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ephemeral_volume_source import V1EphemeralVolumeSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EphemeralVolumeSource from a JSON string
v1_ephemeral_volume_source_instance = V1EphemeralVolumeSource.from_json(json)
# print the JSON string representation of the object
print V1EphemeralVolumeSource.to_json()

# convert the object into a dict
v1_ephemeral_volume_source_dict = v1_ephemeral_volume_source_instance.to_dict()
# create an instance of V1EphemeralVolumeSource from a dict
v1_ephemeral_volume_source_form_dict = v1_ephemeral_volume_source.from_dict(v1_ephemeral_volume_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


