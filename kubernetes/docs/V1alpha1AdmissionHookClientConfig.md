# V1alpha1AdmissionHookClientConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_bundle** | **str** | CABundle is a PEM encoded CA bundle which will be used to validate webhook&#39;s server certificate. Required | 
**service** | [**V1alpha1ServiceReference**](V1alpha1ServiceReference.md) | Service is a reference to the service for this webhook. If there is only one port open for the service, that port will be used. If there are multiple ports open, port 443 will be used if it is open, otherwise it is an error. Required | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


