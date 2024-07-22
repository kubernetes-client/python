# V1StatefulSetPersistentVolumeClaimRetentionPolicy

StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_deleted** | **str** | WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of &#x60;Retain&#x60; causes PVCs to not be affected by StatefulSet deletion. The &#x60;Delete&#x60; policy causes those PVCs to be deleted. | [optional] 
**when_scaled** | **str** | WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of &#x60;Retain&#x60; causes PVCs to not be affected by a scaledown. The &#x60;Delete&#x60; policy causes the associated PVCs for any excess pods above the replica count to be deleted. | [optional] 

## Example

```python
from kubernetes.client.models.v1_stateful_set_persistent_volume_claim_retention_policy import V1StatefulSetPersistentVolumeClaimRetentionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of V1StatefulSetPersistentVolumeClaimRetentionPolicy from a JSON string
v1_stateful_set_persistent_volume_claim_retention_policy_instance = V1StatefulSetPersistentVolumeClaimRetentionPolicy.from_json(json)
# print the JSON string representation of the object
print V1StatefulSetPersistentVolumeClaimRetentionPolicy.to_json()

# convert the object into a dict
v1_stateful_set_persistent_volume_claim_retention_policy_dict = v1_stateful_set_persistent_volume_claim_retention_policy_instance.to_dict()
# create an instance of V1StatefulSetPersistentVolumeClaimRetentionPolicy from a dict
v1_stateful_set_persistent_volume_claim_retention_policy_form_dict = v1_stateful_set_persistent_volume_claim_retention_policy.from_dict(v1_stateful_set_persistent_volume_claim_retention_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


