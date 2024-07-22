# V1alpha2DriverAllocationResult

DriverAllocationResult contains vendor parameters and the allocation result for one request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**named_resources** | [**V1alpha2NamedResourcesAllocationResult**](V1alpha2NamedResourcesAllocationResult.md) |  | [optional] 
**vendor_request_parameters** | **object** | VendorRequestParameters are the per-request configuration parameters from the time that the claim was allocated. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_driver_allocation_result import V1alpha2DriverAllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2DriverAllocationResult from a JSON string
v1alpha2_driver_allocation_result_instance = V1alpha2DriverAllocationResult.from_json(json)
# print the JSON string representation of the object
print V1alpha2DriverAllocationResult.to_json()

# convert the object into a dict
v1alpha2_driver_allocation_result_dict = v1alpha2_driver_allocation_result_instance.to_dict()
# create an instance of V1alpha2DriverAllocationResult from a dict
v1alpha2_driver_allocation_result_form_dict = v1alpha2_driver_allocation_result.from_dict(v1alpha2_driver_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


