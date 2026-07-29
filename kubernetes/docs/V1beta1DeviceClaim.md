# V1beta1DeviceClaim

DeviceClaim defines how to request devices with a ResourceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1beta1DeviceClaimConfiguration]**](V1beta1DeviceClaimConfiguration.md) | This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim. | [optional]
**constraints** | [**List[V1beta1DeviceConstraint]**](V1beta1DeviceConstraint.md) | These constraints must be satisfied by the set of devices that get allocated for the claim. | [optional]
**requests** | [**List[V1beta1DeviceRequest]**](V1beta1DeviceRequest.md) | Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_device_claim import V1beta1DeviceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceClaim from a JSON string
v1beta1_device_claim_instance = V1beta1DeviceClaim.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceClaim.to_json())

# convert the object into a dict
v1beta1_device_claim_dict = v1beta1_device_claim_instance.to_dict()
# create an instance of V1beta1DeviceClaim from a dict
v1beta1_device_claim_from_dict = V1beta1DeviceClaim.from_dict(v1beta1_device_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
