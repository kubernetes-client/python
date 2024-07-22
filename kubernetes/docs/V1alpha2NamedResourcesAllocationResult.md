# V1alpha2NamedResourcesAllocationResult

NamedResourcesAllocationResult is used in AllocationResultModel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the selected resource instance. | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_allocation_result import V1alpha2NamedResourcesAllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesAllocationResult from a JSON string
v1alpha2_named_resources_allocation_result_instance = V1alpha2NamedResourcesAllocationResult.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesAllocationResult.to_json()

# convert the object into a dict
v1alpha2_named_resources_allocation_result_dict = v1alpha2_named_resources_allocation_result_instance.to_dict()
# create an instance of V1alpha2NamedResourcesAllocationResult from a dict
v1alpha2_named_resources_allocation_result_form_dict = v1alpha2_named_resources_allocation_result.from_dict(v1alpha2_named_resources_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


