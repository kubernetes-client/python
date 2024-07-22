# V1alpha2VendorParameters

VendorParameters are opaque parameters for one particular driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_name** | **str** | DriverName is the name used by the DRA driver kubelet plugin. | [optional] 
**parameters** | **object** | Parameters can be arbitrary setup parameters. They are ignored while allocating a claim. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_vendor_parameters import V1alpha2VendorParameters

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2VendorParameters from a JSON string
v1alpha2_vendor_parameters_instance = V1alpha2VendorParameters.from_json(json)
# print the JSON string representation of the object
print V1alpha2VendorParameters.to_json()

# convert the object into a dict
v1alpha2_vendor_parameters_dict = v1alpha2_vendor_parameters_instance.to_dict()
# create an instance of V1alpha2VendorParameters from a dict
v1alpha2_vendor_parameters_form_dict = v1alpha2_vendor_parameters.from_dict(v1alpha2_vendor_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


