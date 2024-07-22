# V1PersistentVolumeClaimTemplate

PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1PersistentVolumeClaimSpec**](V1PersistentVolumeClaimSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimTemplate from a JSON string
v1_persistent_volume_claim_template_instance = V1PersistentVolumeClaimTemplate.from_json(json)
# print the JSON string representation of the object
print V1PersistentVolumeClaimTemplate.to_json()

# convert the object into a dict
v1_persistent_volume_claim_template_dict = v1_persistent_volume_claim_template_instance.to_dict()
# create an instance of V1PersistentVolumeClaimTemplate from a dict
v1_persistent_volume_claim_template_form_dict = v1_persistent_volume_claim_template.from_dict(v1_persistent_volume_claim_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


