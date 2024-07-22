# V1alpha2DriverRequests

DriverRequests describes all resources that are needed from one particular driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_name** | **str** | DriverName is the name used by the DRA driver kubelet plugin. | [optional] 
**requests** | [**List[V1alpha2ResourceRequest]**](V1alpha2ResourceRequest.md) | Requests describes all resources that are needed from the driver. | [optional] 
**vendor_parameters** | **object** | VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_driver_requests import V1alpha2DriverRequests

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2DriverRequests from a JSON string
v1alpha2_driver_requests_instance = V1alpha2DriverRequests.from_json(json)
# print the JSON string representation of the object
print V1alpha2DriverRequests.to_json()

# convert the object into a dict
v1alpha2_driver_requests_dict = v1alpha2_driver_requests_instance.to_dict()
# create an instance of V1alpha2DriverRequests from a dict
v1alpha2_driver_requests_form_dict = v1alpha2_driver_requests.from_dict(v1alpha2_driver_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


