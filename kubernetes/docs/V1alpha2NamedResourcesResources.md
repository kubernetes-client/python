# V1alpha2NamedResourcesResources

NamedResourcesResources is used in ResourceModel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[V1alpha2NamedResourcesInstance]**](V1alpha2NamedResourcesInstance.md) | The list of all individual resources instances currently available. | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_resources import V1alpha2NamedResourcesResources

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesResources from a JSON string
v1alpha2_named_resources_resources_instance = V1alpha2NamedResourcesResources.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesResources.to_json()

# convert the object into a dict
v1alpha2_named_resources_resources_dict = v1alpha2_named_resources_resources_instance.to_dict()
# create an instance of V1alpha2NamedResourcesResources from a dict
v1alpha2_named_resources_resources_form_dict = v1alpha2_named_resources_resources.from_dict(v1alpha2_named_resources_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


