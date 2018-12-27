# V1beta1CustomResourceConversion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | &#x60;strategy&#x60; specifies the conversion strategy. Allowed values are: - &#x60;None&#x60;: The converter only change the apiVersion and would not touch any other field in the CR. - &#x60;Webhook&#x60;: API Server will call to an external webhook to do the conversion. Additional information is needed for this option. | 
**webhook_client_config** | [**ApiextensionsV1beta1WebhookClientConfig**](ApiextensionsV1beta1WebhookClientConfig.md) | &#x60;webhookClientConfig&#x60; is the instructions for how to call the webhook if strategy is &#x60;Webhook&#x60;. This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


