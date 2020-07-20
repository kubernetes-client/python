# V1beta1CustomResourceSubresources

CustomResourceSubresources defines the status and scale subresources for CustomResources.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | [**V1beta1CustomResourceSubresourceScale**](V1beta1CustomResourceSubresourceScale.md) |  | [optional] 
**status** | [**object**](.md) | status indicates the custom resource should serve a &#x60;/status&#x60; subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the &#x60;status&#x60; stanza of the object. 2. requests to the custom resource &#x60;/status&#x60; subresource ignore changes to anything other than the &#x60;status&#x60; stanza of the object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


