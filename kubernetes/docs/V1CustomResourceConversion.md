# V1CustomResourceConversion

CustomResourceConversion describes how to convert different versions of a CR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | strategy specifies how custom resources are converted between versions. Allowed values are: - &#x60;\&quot;None\&quot;&#x60;: The converter only change the apiVersion and would not touch any other field in the custom resource. - &#x60;\&quot;Webhook\&quot;&#x60;: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set. | 
**webhook** | [**V1WebhookConversion**](V1WebhookConversion.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_conversion import V1CustomResourceConversion

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceConversion from a JSON string
v1_custom_resource_conversion_instance = V1CustomResourceConversion.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceConversion.to_json()

# convert the object into a dict
v1_custom_resource_conversion_dict = v1_custom_resource_conversion_instance.to_dict()
# create an instance of V1CustomResourceConversion from a dict
v1_custom_resource_conversion_form_dict = v1_custom_resource_conversion.from_dict(v1_custom_resource_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


