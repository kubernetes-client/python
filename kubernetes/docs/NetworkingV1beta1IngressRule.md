# NetworkingV1beta1IngressRule

IngressRule represents the rules mapping the paths under a specified host to the related backend services. Incoming requests are first evaluated for a host match, then routed to the backend associated with the matching IngressRuleValue.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host is the fully qualified domain name of a network host, as defined by RFC 3986. Note the following deviations from the \&quot;host\&quot; part of the URI as defined in RFC 3986: 1. IPs are not allowed. Currently an IngressRuleValue can only apply to    the IP in the Spec of the parent Ingress. 2. The &#x60;:&#x60; delimiter is not respected because ports are not allowed.    Currently the port of an Ingress is implicitly :80 for http and    :443 for https. Both these may change in the future. Incoming requests are matched against the host before the IngressRuleValue. If the host is unspecified, the Ingress routes all traffic based on the specified IngressRuleValue.  Host can be \&quot;precise\&quot; which is a domain name without the terminating dot of a network host (e.g. \&quot;foo.bar.com\&quot;) or \&quot;wildcard\&quot;, which is a domain name prefixed with a single wildcard label (e.g. \&quot;*.foo.com\&quot;). The wildcard character &#39;*&#39; must appear by itself as the first DNS label and matches only a single label. You cannot have a wildcard label by itself (e.g. Host &#x3D;&#x3D; \&quot;*\&quot;). Requests will be matched against the Host field in the following way: 1. If Host is precise, the request matches this rule if the http host header is equal to Host. 2. If Host is a wildcard, then the request matches this rule if the http host header is to equal to the suffix (removing the first label) of the wildcard rule. | [optional] 
**http** | [**NetworkingV1beta1HTTPIngressRuleValue**](NetworkingV1beta1HTTPIngressRuleValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


