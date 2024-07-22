# V1alpha2StructuredResourceHandle

StructuredResourceHandle is the in-tree representation of the allocation result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_name** | **str** | NodeName is the name of the node providing the necessary resources if the resources are local to a node. | [optional] 
**results** | [**List[V1alpha2DriverAllocationResult]**](V1alpha2DriverAllocationResult.md) | Results lists all allocated driver resources. | 
**vendor_claim_parameters** | **object** | VendorClaimParameters are the per-claim configuration parameters from the resource claim parameters at the time that the claim was allocated. | [optional] 
**vendor_class_parameters** | **object** | VendorClassParameters are the per-claim configuration parameters from the resource class at the time that the claim was allocated. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_structured_resource_handle import V1alpha2StructuredResourceHandle

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2StructuredResourceHandle from a JSON string
v1alpha2_structured_resource_handle_instance = V1alpha2StructuredResourceHandle.from_json(json)
# print the JSON string representation of the object
print V1alpha2StructuredResourceHandle.to_json()

# convert the object into a dict
v1alpha2_structured_resource_handle_dict = v1alpha2_structured_resource_handle_instance.to_dict()
# create an instance of V1alpha2StructuredResourceHandle from a dict
v1alpha2_structured_resource_handle_form_dict = v1alpha2_structured_resource_handle.from_dict(v1alpha2_structured_resource_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


