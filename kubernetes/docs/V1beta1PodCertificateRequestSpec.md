# V1beta1PodCertificateRequestSpec

PodCertificateRequestSpec describes the certificate request.  All fields are immutable after creation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_expiration_seconds** | **int** | maxExpirationSeconds is the maximum lifetime permitted for the certificate.  If omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter than 3600 (1 hour).  The maximum allowable value is 7862400 (91 days).  The signer implementation is then free to issue a certificate with any lifetime *shorter* than MaxExpirationSeconds, but no shorter than 3600 seconds (1 hour).  This constraint is enforced by kube-apiserver. &#x60;kubernetes.io&#x60; signers will never issue certificates with a lifetime longer than 24 hours. | [optional] 
**node_name** | **str** | nodeName is the name of the node the pod is assigned to. | 
**node_uid** | **str** | nodeUID is the UID of the node the pod is assigned to. | 
**pkix_public_key** | **str** | pkixPublicKey is the PKIX-serialized public key the signer will issue the certificate to.  The key must be one of RSA3072, RSA4096, ECDSAP256, ECDSAP384, ECDSAP521, or ED25519. Note that this list may be expanded in the future.  Signer implementations do not need to support all key types supported by kube-apiserver and kubelet.  If a signer does not support the key type used for a given PodCertificateRequest, it must deny the request by setting a status.conditions entry with a type of \&quot;Denied\&quot; and a reason of \&quot;UnsupportedKeyType\&quot;. It may also suggest a key type that it does support in the message field. | 
**pod_name** | **str** | podName is the name of the pod into which the certificate will be mounted. | 
**pod_uid** | **str** | podUID is the UID of the pod into which the certificate will be mounted. | 
**proof_of_possession** | **str** | proofOfPossession proves that the requesting kubelet holds the private key corresponding to pkixPublicKey.  It is contructed by signing the ASCII bytes of the pod&#39;s UID using &#x60;pkixPublicKey&#x60;.  kube-apiserver validates the proof of possession during creation of the PodCertificateRequest.  If the key is an RSA key, then the signature is over the ASCII bytes of the pod UID, using RSASSA-PSS from RFC 8017 (as implemented by the golang function crypto/rsa.SignPSS with nil options).  If the key is an ECDSA key, then the signature is as described by [SEC 1, Version 2.0](https://www.secg.org/sec1-v2.pdf) (as implemented by the golang library function crypto/ecdsa.SignASN1)  If the key is an ED25519 key, the the signature is as described by the [ED25519 Specification](https://ed25519.cr.yp.to/) (as implemented by the golang library crypto/ed25519.Sign). | 
**service_account_name** | **str** | serviceAccountName is the name of the service account the pod is running as. | 
**service_account_uid** | **str** | serviceAccountUID is the UID of the service account the pod is running as. | 
**signer_name** | **str** | signerName indicates the requested signer.  All signer names beginning with &#x60;kubernetes.io&#x60; are reserved for use by the Kubernetes project.  There is currently one well-known signer documented by the Kubernetes project, &#x60;kubernetes.io/kube-apiserver-kubernetes.client-pod&#x60;, which will issue kubernetes.client certificates understood by kube-apiserver.  It is currently unimplemented. | 
**unverified_user_annotations** | **dict[str, str]** | unverifiedUserAnnotations allow pod authors to pass additional information to the signer implementation.  Kubernetes does not restrict or validate this metadata in any way.  Entries are subject to the same validation as object metadata annotations, with the addition that all keys must be domain-prefixed. No restrictions are placed on values, except an overall size limitation on the entire field.  Signers should document the keys and values they support.  Signers should deny requests that contain keys they do not recognize. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


