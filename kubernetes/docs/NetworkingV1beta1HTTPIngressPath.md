# NetworkingV1beta1HTTPIngressPath

HTTPIngressPath associates a path regex with a backend. Incoming urls matching the path are forwarded to the backend.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend** | [**NetworkingV1beta1IngressBackend**](NetworkingV1beta1IngressBackend.md) |  | 
**path** | **str** | Path is an extended POSIX regex as defined by IEEE Std 1003.1, (i.e this follows the egrep/unix syntax, not the perl syntax) matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional \&quot;path\&quot; part of a URL as defined by RFC 3986. Paths must begin with a &#39;/&#39;. If unspecified, the path defaults to a catch all sending traffic to the backend. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


