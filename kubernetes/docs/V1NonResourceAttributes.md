# V1NonResourceAttributes

NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path is the URL path of the request | [optional] 
**verb** | **str** | Verb is the standard HTTP verb | [optional] 

## Example

```python
from kubernetes.client.models.v1_non_resource_attributes import V1NonResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of V1NonResourceAttributes from a JSON string
v1_non_resource_attributes_instance = V1NonResourceAttributes.from_json(json)
# print the JSON string representation of the object
print V1NonResourceAttributes.to_json()

# convert the object into a dict
v1_non_resource_attributes_dict = v1_non_resource_attributes_instance.to_dict()
# create an instance of V1NonResourceAttributes from a dict
v1_non_resource_attributes_form_dict = v1_non_resource_attributes.from_dict(v1_non_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


