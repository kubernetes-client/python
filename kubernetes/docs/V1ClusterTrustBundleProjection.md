# V1ClusterTrustBundleProjection

ClusterTrustBundleProjection describes how to select a set of ClusterTrustBundle objects and project their contents into the pod filesystem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**name** | **str** | Select a single ClusterTrustBundle by object name.  Mutually-exclusive with signerName and labelSelector. | [optional] 
**optional** | **bool** | If true, don&#39;t block pod startup if the referenced ClusterTrustBundle(s) aren&#39;t available.  If using name, then the named ClusterTrustBundle is allowed not to exist.  If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles. | [optional] 
**path** | **str** | Relative path from the volume root to write the bundle. | 
**signer_name** | **str** | Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name.  The contents of all selected ClusterTrustBundles will be unified and deduplicated. | [optional] 

## Example

```python
from kubernetes.client.models.v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterTrustBundleProjection from a JSON string
v1_cluster_trust_bundle_projection_instance = V1ClusterTrustBundleProjection.from_json(json)
# print the JSON string representation of the object
print V1ClusterTrustBundleProjection.to_json()

# convert the object into a dict
v1_cluster_trust_bundle_projection_dict = v1_cluster_trust_bundle_projection_instance.to_dict()
# create an instance of V1ClusterTrustBundleProjection from a dict
v1_cluster_trust_bundle_projection_form_dict = v1_cluster_trust_bundle_projection.from_dict(v1_cluster_trust_bundle_projection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


