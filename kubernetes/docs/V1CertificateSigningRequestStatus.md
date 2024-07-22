# V1CertificateSigningRequestStatus

CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **bytearray** | certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.  If the certificate signing request is denied, a condition of type \&quot;Denied\&quot; is added and this field remains empty. If the signer cannot issue the certificate, a condition of type \&quot;Failed\&quot; is added and this field remains empty.  Validation requirements:  1. certificate must contain one or more PEM blocks.  2. All PEM blocks must have the \&quot;CERTIFICATE\&quot; label, contain no headers, and the encoded data   must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.  3. Non-PEM content may appear before or after the \&quot;CERTIFICATE\&quot; PEM blocks and is unvalidated,   to allow for explanatory text as described in section 5.2 of RFC7468.  If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  The certificate is encoded in PEM format.  When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:      base64(     -----BEGIN CERTIFICATE-----     ...     -----END CERTIFICATE-----     ) | [optional] 
**conditions** | [**List[V1CertificateSigningRequestCondition]**](V1CertificateSigningRequestCondition.md) | conditions applied to the request. Known conditions are \&quot;Approved\&quot;, \&quot;Denied\&quot;, and \&quot;Failed\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_certificate_signing_request_status import V1CertificateSigningRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1CertificateSigningRequestStatus from a JSON string
v1_certificate_signing_request_status_instance = V1CertificateSigningRequestStatus.from_json(json)
# print the JSON string representation of the object
print V1CertificateSigningRequestStatus.to_json()

# convert the object into a dict
v1_certificate_signing_request_status_dict = v1_certificate_signing_request_status_instance.to_dict()
# create an instance of V1CertificateSigningRequestStatus from a dict
v1_certificate_signing_request_status_form_dict = v1_certificate_signing_request_status.from_dict(v1_certificate_signing_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


