# V1GRPCAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port number of the gRPC service. Number must be in the range 1 to 65535. | 
**service** | **str** | Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md).  If this is not specified, the default behavior is defined by gRPC. | [optional] 

## Example

```python
from kubernetes.client.models.v1_grpc_action import V1GRPCAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1GRPCAction from a JSON string
v1_grpc_action_instance = V1GRPCAction.from_json(json)
# print the JSON string representation of the object
print V1GRPCAction.to_json()

# convert the object into a dict
v1_grpc_action_dict = v1_grpc_action_instance.to_dict()
# create an instance of V1GRPCAction from a dict
v1_grpc_action_form_dict = v1_grpc_action.from_dict(v1_grpc_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


