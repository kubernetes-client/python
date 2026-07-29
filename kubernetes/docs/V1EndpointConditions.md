# V1EndpointConditions

EndpointConditions represents the current condition of an endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **bool** | ready indicates that this endpoint is ready to receive traffic, according to whatever system is managing the endpoint. A nil value should be interpreted as \&quot;true\&quot;. In general, an endpoint should be marked ready if it is serving and not terminating, though this can be overridden in some cases, such as when the associated Service has set the publishNotReadyAddresses flag. | [optional]
**serving** | **bool** | serving indicates that this endpoint is able to receive traffic, according to whatever system is managing the endpoint. For endpoints backed by pods, the EndpointSlice controller will mark the endpoint as serving if the pod&#39;s Ready condition is True. A nil value should be interpreted as \&quot;true\&quot;. | [optional]
**terminating** | **bool** | terminating indicates that this endpoint is terminating. A nil value should be interpreted as \&quot;false\&quot;. | [optional]

## Example

```python
from kubernetes.client.models.v1_endpoint_conditions import V1EndpointConditions

# TODO update the JSON string below
json = "{}"
# create an instance of V1EndpointConditions from a JSON string
v1_endpoint_conditions_instance = V1EndpointConditions.from_json(json)
# print the JSON string representation of the object
print(V1EndpointConditions.to_json())

# convert the object into a dict
v1_endpoint_conditions_dict = v1_endpoint_conditions_instance.to_dict()
# create an instance of V1EndpointConditions from a dict
v1_endpoint_conditions_from_dict = V1EndpointConditions.from_dict(v1_endpoint_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
