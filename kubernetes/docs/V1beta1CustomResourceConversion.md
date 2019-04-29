# V1beta1CustomResourceConversion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_review_versions** | **list[str]** | ConversionReviewVersions is an ordered list of preferred &#x60;ConversionReview&#x60; versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, conversion will fail for this object. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. Default to &#x60;[&#39;v1beta1&#39;]&#x60;. | [optional] 
**strategy** | **str** | &#x60;strategy&#x60; specifies the conversion strategy. Allowed values are: - &#x60;None&#x60;: The converter only change the apiVersion and would not touch any other field in the CR. - &#x60;Webhook&#x60;: API Server will call to an external webhook to do the conversion. Additional information is needed for this option. | 
**webhook_client_config** | [**ApiextensionsV1beta1WebhookClientConfig**](ApiextensionsV1beta1WebhookClientConfig.md) | &#x60;webhookClientConfig&#x60; is the instructions for how to call the webhook if strategy is &#x60;Webhook&#x60;. This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


