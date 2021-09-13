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
**usages** | **list[str]** | allowedUsages specifies a set of usage contexts the key will be valid for. See: https://tools.ietf.org/html/rfc5280#section-4.2.1.3      https://tools.ietf.org/html/rfc5280#section-4.2.1.12 Valid values are:  \&quot;signing\&quot;,  \&quot;digital signature\&quot;,  \&quot;content commitment\&quot;,  \&quot;key encipherment\&quot;,  \&quot;key agreement\&quot;,  \&quot;data encipherment\&quot;,  \&quot;cert sign\&quot;,  \&quot;crl sign\&quot;,  \&quot;encipher only\&quot;,  \&quot;decipher only\&quot;,  \&quot;any\&quot;,  \&quot;server auth\&quot;,  \&quot;kubernetes.client auth\&quot;,  \&quot;code signing\&quot;,  \&quot;email protection\&quot;,  \&quot;s/mime\&quot;,  \&quot;ipsec end system\&quot;,  \&quot;ipsec tunnel\&quot;,  \&quot;ipsec user\&quot;,  \&quot;timestamping\&quot;,  \&quot;ocsp signing\&quot;,  \&quot;microsoft sgc\&quot;,  \&quot;netscape sgc\&quot; | [optional] 
**username** | **str** | Information about the requesting user. See user.Info interface for details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


