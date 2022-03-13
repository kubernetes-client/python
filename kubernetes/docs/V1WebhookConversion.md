# V1WebhookConversion

WebhookConversion describes how to call a conversion webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_review_versions** | **[str]** | conversionReviewVersions is an ordered list of preferred &#x60;ConversionReview&#x60; versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. | 
**kubernetes.client_config** | [**ApiextensionsV1WebhookClientConfig**](ApiextensionsV1WebhookClientConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


