# V1beta1CustomResourceConversion

CustomResourceConversion describes how to convert different versions of a CR.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_review_versions** | **list[str]** | conversionReviewVersions is an ordered list of preferred &#x60;ConversionReview&#x60; versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. Defaults to &#x60;[\&quot;v1beta1\&quot;]&#x60;. | [optional] 
**strategy** | **str** | strategy specifies how custom resources are converted between versions. Allowed values are: - &#x60;None&#x60;: The converter only change the apiVersion and would not touch any other field in the custom resource. - &#x60;Webhook&#x60;: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhookClientConfig to be set. | 
**webhook_client_config** | [**ApiextensionsV1beta1WebhookClientConfig**](ApiextensionsV1beta1WebhookClientConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


