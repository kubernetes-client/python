# V1CustomResourceConversion

CustomResourceConversion describes how to convert different versions of a CR.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | strategy specifies how custom resources are converted between versions. Allowed values are: - &#x60;None&#x60;: The converter only change the apiVersion and would not touch any other field in the custom resource. - &#x60;Webhook&#x60;: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. | 
**webhook** | [**V1WebhookConversion**](V1WebhookConversion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


