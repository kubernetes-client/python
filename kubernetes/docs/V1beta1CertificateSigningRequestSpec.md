# V1beta1CertificateSigningRequestSpec

This information is immutable after the request is created. Only the Request and Usages fields can be set on creation, other fields are derived by Kubernetes and cannot be modified by users.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **dict(str, list[str])** | Extra information about the requesting user. See user.Info interface for details. | [optional] 
**groups** | **list[str]** | Group information about the requesting user. See user.Info interface for details. | [optional] 
**request** | **str** | Base64-encoded PKCS#10 CSR data | 
**signer_name** | **str** | Requested signer for the request. It is a qualified name in the form: &#x60;scope-hostname.io/name&#x60;. If empty, it will be defaulted:  1. If it&#39;s a kubelet kubernetes.client certificate, it is assigned     \&quot;kubernetes.io/kube-apiserver-kubernetes.client-kubelet\&quot;.  2. If it&#39;s a kubelet serving certificate, it is assigned     \&quot;kubernetes.io/kubelet-serving\&quot;.  3. Otherwise, it is assigned \&quot;kubernetes.io/legacy-unknown\&quot;. Distribution of trust for signers happens out of band. You can select on this field using &#x60;spec.signerName&#x60;. | [optional] 
**uid** | **str** | UID information about the requesting user. See user.Info interface for details. | [optional] 
**usages** | **list[str]** | allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3      https://tools.ietf.org/html/rfc5280#section-4.2.1.12 | [optional] 
**username** | **str** | Information about the requesting user. See user.Info interface for details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


