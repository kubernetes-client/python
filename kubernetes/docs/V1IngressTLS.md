# V1IngressTLS

IngressTLS describes the transport layer security associated with an ingress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** | hosts is a list of hosts included in the TLS certificate. The values in this list must match the name/s used in the tlsSecret. Defaults to the wildcard host setting for the loadbalancer controller fulfilling this Ingress, if left unspecified. | [optional] 
**secret_name** | **str** | secretName is the name of the secret used to terminate TLS traffic on port 443. Field is left optional to allow TLS routing based on SNI hostname alone. If the SNI host in a listener conflicts with the \&quot;Host\&quot; header field used by an IngressRule, the SNI host is used for termination and value of the \&quot;Host\&quot; header is used for routing. | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_tls import V1IngressTLS

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressTLS from a JSON string
v1_ingress_tls_instance = V1IngressTLS.from_json(json)
# print the JSON string representation of the object
print V1IngressTLS.to_json()

# convert the object into a dict
v1_ingress_tls_dict = v1_ingress_tls_instance.to_dict()
# create an instance of V1IngressTLS from a dict
v1_ingress_tls_form_dict = v1_ingress_tls.from_dict(v1_ingress_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


