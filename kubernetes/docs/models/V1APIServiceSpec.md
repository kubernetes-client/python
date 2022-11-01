# kubernetes.client.model.v1_api_service_spec.V1APIServiceSpec

APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**groupPriorityMinimum** | decimal.Decimal, int,  | decimal.Decimal,  | GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by kubernetes.clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We&#x27;d recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s | value must be a 32 bit integer
**versionPriority** | decimal.Decimal, int,  | decimal.Decimal,  | VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it&#x27;s inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is \&quot;kube-like\&quot;, it will sort above non \&quot;kube-like\&quot; version strings, which are ordered lexicographically. \&quot;Kube-like\&quot; versions start with a \&quot;v\&quot;, then are followed by a number (the major version), then optionally the string \&quot;alpha\&quot; or \&quot;beta\&quot; and another number (the minor version). These are sorted first by GA &gt; beta &gt; alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. | value must be a 32 bit integer
**caBundle** | str,  | str,  | CABundle is a PEM encoded CA bundle which will be used to validate an API server&#x27;s serving certificate. If unspecified, system trust roots on the apiserver are used. | [optional] 
**group** | str,  | str,  | Group is the API group name this server hosts | [optional] 
**insecureSkipTLSVerify** | bool,  | BoolClass,  | InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead. | [optional] 
**service** | [**ApiregistrationV1ServiceReference**](ApiregistrationV1ServiceReference.md) | [**ApiregistrationV1ServiceReference**](ApiregistrationV1ServiceReference.md) |  | [optional] 
**version** | str,  | str,  | Version is the API version this server hosts.  For example, \&quot;v1\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

