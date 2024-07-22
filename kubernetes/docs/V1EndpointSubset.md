# V1EndpointSubset

EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:   {    Addresses: [{\"ip\": \"10.10.1.1\"}, {\"ip\": \"10.10.2.2\"}],    Ports:     [{\"name\": \"a\", \"port\": 8675}, {\"name\": \"b\", \"port\": 309}]  }  The resulting set of endpoints can be viewed as:   a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],  b: [ 10.10.1.1:309, 10.10.2.2:309 ]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[V1EndpointAddress]**](V1EndpointAddress.md) | IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and kubernetes.clients to utilize. | [optional] 
**not_ready_addresses** | [**List[V1EndpointAddress]**](V1EndpointAddress.md) | IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. | [optional] 
**ports** | [**List[CoreV1EndpointPort]**](CoreV1EndpointPort.md) | Port numbers available on the related IP addresses. | [optional] 

## Example

```python
from kubernetes.client.models.v1_endpoint_subset import V1EndpointSubset

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointSubset from a JSON string
v1_endpoint_subset_instance = V1EndpointSubset.from_json(json)
# print the JSON string representation of the object
print V1EndpointSubset.to_json()

# convert the object into a dict
v1_endpoint_subset_dict = v1_endpoint_subset_instance.to_dict()
# create an instance of V1EndpointSubset from a dict
v1_endpoint_subset_form_dict = v1_endpoint_subset.from_dict(v1_endpoint_subset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


