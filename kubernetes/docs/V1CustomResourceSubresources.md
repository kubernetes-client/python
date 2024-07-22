# V1CustomResourceSubresources

CustomResourceSubresources defines the status and scale subresources for CustomResources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | [**V1CustomResourceSubresourceScale**](V1CustomResourceSubresourceScale.md) |  | [optional] 
**status** | **object** | status indicates the custom resource should serve a &#x60;/status&#x60; subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the &#x60;status&#x60; stanza of the object. 2. requests to the custom resource &#x60;/status&#x60; subresource ignore changes to anything other than the &#x60;status&#x60; stanza of the object. | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_subresources import V1CustomResourceSubresources

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceSubresources from a JSON string
v1_custom_resource_subresources_instance = V1CustomResourceSubresources.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceSubresources.to_json()

# convert the object into a dict
v1_custom_resource_subresources_dict = v1_custom_resource_subresources_instance.to_dict()
# create an instance of V1CustomResourceSubresources from a dict
v1_custom_resource_subresources_form_dict = v1_custom_resource_subresources.from_dict(v1_custom_resource_subresources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


