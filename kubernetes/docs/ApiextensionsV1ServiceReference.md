# ApiextensionsV1ServiceReference

ServiceReference holds a reference to Service.legacy.k8s.io
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the service. Required | 
**namespace** | **str** | namespace is the namespace of the service. Required | 
**path** | **str** | path is an optional URL path at which the webhook will be contacted. | [optional] 
**port** | **int** | port is an optional service port at which the webhook will be contacted. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


