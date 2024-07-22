# V1alpha2NamedResourcesRequest

NamedResourcesRequest is used in ResourceRequestModel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** | Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/  In addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:     attributes.quantity[\&quot;a\&quot;].isGreaterThan(quantity(\&quot;0\&quot;)) &amp;&amp;    attributes.stringslice[\&quot;b\&quot;].isSorted() | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_request import V1alpha2NamedResourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesRequest from a JSON string
v1alpha2_named_resources_request_instance = V1alpha2NamedResourcesRequest.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesRequest.to_json()

# convert the object into a dict
v1alpha2_named_resources_request_dict = v1alpha2_named_resources_request_instance.to_dict()
# create an instance of V1alpha2NamedResourcesRequest from a dict
v1alpha2_named_resources_request_form_dict = v1alpha2_named_resources_request.from_dict(v1alpha2_named_resources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


