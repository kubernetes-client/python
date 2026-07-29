# V1ServiceCIDRStatus

ServiceCIDRStatus describes the current state of the ServiceCIDR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state | [optional]

## Example

```python
from kubernetes.client.models.v1_service_cidr_status import V1ServiceCIDRStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServiceCIDRStatus from a JSON string
v1_service_cidr_status_instance = V1ServiceCIDRStatus.from_json(json)
# print the JSON string representation of the object
print(V1ServiceCIDRStatus.to_json())

# convert the object into a dict
v1_service_cidr_status_dict = v1_service_cidr_status_instance.to_dict()
# create an instance of V1ServiceCIDRStatus from a dict
v1_service_cidr_status_from_dict = V1ServiceCIDRStatus.from_dict(v1_service_cidr_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
