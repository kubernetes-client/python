# V1alpha2ResourceRequest

ResourceRequest is a request for resources from one particular driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**named_resources** | [**V1alpha2NamedResourcesRequest**](V1alpha2NamedResourcesRequest.md) |  | [optional] 
**vendor_parameters** | **object** | VendorParameters are arbitrary setup parameters for the requested resource. They are ignored while allocating a claim. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_request import V1alpha2ResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceRequest from a JSON string
v1alpha2_resource_request_instance = V1alpha2ResourceRequest.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceRequest.to_json()

# convert the object into a dict
v1alpha2_resource_request_dict = v1alpha2_resource_request_instance.to_dict()
# create an instance of V1alpha2ResourceRequest from a dict
v1alpha2_resource_request_form_dict = v1alpha2_resource_request.from_dict(v1alpha2_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


