# V1IngressSpec

IngressSpec describes the Ingress the user wishes to exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_backend** | [**V1IngressBackend**](V1IngressBackend.md) |  | [optional] 
**ingress_class_name** | **str** | ingressClassName is the name of an IngressClass cluster resource. Ingress controller implementations use this field to know whether they should be serving this Ingress resource, by a transitive connection (controller -&gt; IngressClass -&gt; Ingress resource). Although the &#x60;kubernetes.io/ingress.class&#x60; annotation (simple constant name) was never formally defined, it was widely supported by Ingress controllers to create a direct binding between Ingress controller and Ingress resources. Newly created Ingress resources should prefer using the field. However, even though the annotation is officially deprecated, for backwards compatibility reasons, ingress controllers should still honor that annotation if present. | [optional] 
**rules** | [**List[V1IngressRule]**](V1IngressRule.md) | rules is a list of host rules used to configure the Ingress. If unspecified, or no rule matches, all traffic is sent to the default backend. | [optional] 
**tls** | [**List[V1IngressTLS]**](V1IngressTLS.md) | tls represents the TLS configuration. Currently the Ingress only supports a single TLS port, 443. If multiple members of this list specify different hosts, they will be multiplexed on the same port according to the hostname specified through the SNI TLS extension, if the ingress controller fulfilling the ingress supports SNI. | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_spec import V1IngressSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressSpec from a JSON string
v1_ingress_spec_instance = V1IngressSpec.from_json(json)
# print the JSON string representation of the object
print V1IngressSpec.to_json()

# convert the object into a dict
v1_ingress_spec_dict = v1_ingress_spec_instance.to_dict()
# create an instance of V1IngressSpec from a dict
v1_ingress_spec_form_dict = v1_ingress_spec.from_dict(v1_ingress_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


