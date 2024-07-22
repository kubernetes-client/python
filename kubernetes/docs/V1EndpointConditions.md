# V1EndpointConditions

EndpointConditions represents the current condition of an endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** | ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be \&quot;true\&quot; for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag. | [optional] 
**serving** | **bool** | serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. | [optional] 
**terminating** | **bool** | terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. | [optional] 

## Example

```python
from kubernetes.client.models.v1_endpoint_conditions import V1EndpointConditions

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointConditions from a JSON string
v1_endpoint_conditions_instance = V1EndpointConditions.from_json(json)
# print the JSON string representation of the object
print V1EndpointConditions.to_json()

# convert the object into a dict
v1_endpoint_conditions_dict = v1_endpoint_conditions_instance.to_dict()
# create an instance of V1EndpointConditions from a dict
v1_endpoint_conditions_form_dict = v1_endpoint_conditions.from_dict(v1_endpoint_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


