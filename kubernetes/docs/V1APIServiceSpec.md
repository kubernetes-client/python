# V1APIServiceSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_bundle** | **str** | CABundle is a PEM encoded CA bundle which will be used to validate an API server&#39;s serving certificate. | 
**group** | **str** | Group is the API group name this server hosts | [optional] 
**group_priority_minimum** | **int** | GroupPriorityMininum is the priority this group should have at least. Higher priority means that the group is preferred by kubernetes.clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMininum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We&#39;d recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s | 
**insecure_skip_tls_verify** | **bool** | InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead. | [optional] 
**service** | [**V1ServiceReference**](V1ServiceReference.md) | Service is a reference to the service for this API server.  It must communicate on port 443 If the Service is nil, that means the handling for the API groupversion is handled locally on this server. The call will simply delegate to the normal handler chain to be fulfilled. | 
**version** | **str** | Version is the API version this server hosts.  For example, \&quot;v1\&quot; | [optional] 
**version_priority** | **int** | VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) Since it&#39;s inside of a group, the number can be small, probably in the 10s. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


