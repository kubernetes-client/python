# V1alpha1ClusterTrustBundleSpec

ClusterTrustBundleSpec contains the signer and trust anchors.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_name** | **str** | signerName indicates the associated signer, if any.  In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group&#x3D;certificates.k8s.io resource&#x3D;signers resourceName&#x3D;&lt;the signer name&gt; verb&#x3D;attest.  If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name &#x60;example.com/foo&#x60;, valid ClusterTrustBundle object names include &#x60;example.com:foo:abc&#x60; and &#x60;example.com:foo:v1&#x60;.  If signerName is empty, then the ClusterTrustBundle object&#39;s name must not have such a prefix.  List/watch requests for ClusterTrustBundles can filter on this field using a &#x60;spec.signerName&#x3D;NAME&#x60; field selector. | [optional] 
**trust_bundle** | **str** | trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.  The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.  Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


