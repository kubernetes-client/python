# V1alpha2NamedResourcesInstance

NamedResourcesInstance represents one individual hardware instance that can be selected based on its attributes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[V1alpha2NamedResourcesAttribute]**](V1alpha2NamedResourcesAttribute.md) | Attributes defines the attributes of this resource instance. The name of each attribute must be unique. | [optional] 
**name** | **str** | Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain. | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_instance import V1alpha2NamedResourcesInstance

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesInstance from a JSON string
v1alpha2_named_resources_instance_instance = V1alpha2NamedResourcesInstance.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesInstance.to_json()

# convert the object into a dict
v1alpha2_named_resources_instance_dict = v1alpha2_named_resources_instance_instance.to_dict()
# create an instance of V1alpha2NamedResourcesInstance from a dict
v1alpha2_named_resources_instance_form_dict = v1alpha2_named_resources_instance.from_dict(v1alpha2_named_resources_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


