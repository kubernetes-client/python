# V1VolumeProjection

Projection that may be projected along with other supported volume types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_trust_bundle** | [**V1ClusterTrustBundleProjection**](V1ClusterTrustBundleProjection.md) |  | [optional] 
**config_map** | [**V1ConfigMapProjection**](V1ConfigMapProjection.md) |  | [optional] 
**downward_api** | [**V1DownwardAPIProjection**](V1DownwardAPIProjection.md) |  | [optional] 
**secret** | [**V1SecretProjection**](V1SecretProjection.md) |  | [optional] 
**service_account_token** | [**V1ServiceAccountTokenProjection**](V1ServiceAccountTokenProjection.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_projection import V1VolumeProjection

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeProjection from a JSON string
v1_volume_projection_instance = V1VolumeProjection.from_json(json)
# print the JSON string representation of the object
print V1VolumeProjection.to_json()

# convert the object into a dict
v1_volume_projection_dict = v1_volume_projection_instance.to_dict()
# create an instance of V1VolumeProjection from a dict
v1_volume_projection_form_dict = v1_volume_projection.from_dict(v1_volume_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


