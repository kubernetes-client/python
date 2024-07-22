# V1LeaseSpec

LeaseSpec is a specification of a Lease.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquire_time** | **datetime** | acquireTime is a time when the current lease was acquired. | [optional] 
**holder_identity** | **str** | holderIdentity contains the identity of the holder of a current lease. | [optional] 
**lease_duration_seconds** | **int** | leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime. | [optional] 
**lease_transitions** | **int** | leaseTransitions is the number of transitions of a lease between holders. | [optional] 
**renew_time** | **datetime** | renewTime is a time when the current holder of a lease has last updated the lease. | [optional] 

## Example

```python
from kubernetes.client.models.v1_lease_spec import V1LeaseSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1LeaseSpec from a JSON string
v1_lease_spec_instance = V1LeaseSpec.from_json(json)
# print the JSON string representation of the object
print V1LeaseSpec.to_json()

# convert the object into a dict
v1_lease_spec_dict = v1_lease_spec_instance.to_dict()
# create an instance of V1LeaseSpec from a dict
v1_lease_spec_form_dict = v1_lease_spec.from_dict(v1_lease_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


