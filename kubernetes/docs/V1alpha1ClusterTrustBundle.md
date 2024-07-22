# V1alpha1ClusterTrustBundle

ClusterTrustBundle is a cluster-scoped container for X.509 trust anchors (root certificates).  ClusterTrustBundle objects are considered to be readable by any authenticated user in the cluster, because they can be mounted by pods using the `clusterTrustBundle` projection.  All service accounts have read access to ClusterTrustBundles by default.  Users who only have namespace-level access to a cluster can read ClusterTrustBundles by impersonating a serviceaccount that they have access to.  It can be optionally associated with a particular assigner, in which case it contains one valid set of trust anchors for that signer. Signers may have multiple associated ClusterTrustBundles; each is an independent set of trust anchors for that signer. Admission control is used to enforce that only users with permissions on the signer can create or modify the corresponding bundle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1ClusterTrustBundleSpec**](V1alpha1ClusterTrustBundleSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha1_cluster_trust_bundle import V1alpha1ClusterTrustBundle

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ClusterTrustBundle from a JSON string
v1alpha1_cluster_trust_bundle_instance = V1alpha1ClusterTrustBundle.from_json(json)
# print the JSON string representation of the object
print V1alpha1ClusterTrustBundle.to_json()

# convert the object into a dict
v1alpha1_cluster_trust_bundle_dict = v1alpha1_cluster_trust_bundle_instance.to_dict()
# create an instance of V1alpha1ClusterTrustBundle from a dict
v1alpha1_cluster_trust_bundle_form_dict = v1alpha1_cluster_trust_bundle.from_dict(v1alpha1_cluster_trust_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


