# V1WebhookConversion

WebhookConversion describes how to call a conversion webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_config** | [**ApiextensionsV1WebhookClientConfig**](ApiextensionsV1WebhookClientConfig.md) |  | [optional] 
**conversion_review_versions** | **List[str]** | conversionReviewVersions is an ordered list of preferred &#x60;ConversionReview&#x60; versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. | 

## Example

```python
from kubernetes.client.models.v1_webhook_conversion import V1WebhookConversion

# TODO update the JSON string below
json = "{}"
# create an instance of V1WebhookConversion from a JSON string
v1_webhook_conversion_instance = V1WebhookConversion.from_json(json)
# print the JSON string representation of the object
print V1WebhookConversion.to_json()

# convert the object into a dict
v1_webhook_conversion_dict = v1_webhook_conversion_instance.to_dict()
# create an instance of V1WebhookConversion from a dict
v1_webhook_conversion_form_dict = v1_webhook_conversion.from_dict(v1_webhook_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


