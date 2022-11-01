# kubernetes.client.model.v1_load_balancer_status.V1LoadBalancerStatus

LoadBalancerStatus represents the status of a load-balancer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LoadBalancerStatus represents the status of a load-balancer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[ingress](#ingress)** | list, tuple,  | tuple,  | Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ingress

Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1LoadBalancerIngress**](V1LoadBalancerIngress.md) | [**V1LoadBalancerIngress**](V1LoadBalancerIngress.md) | [**V1LoadBalancerIngress**](V1LoadBalancerIngress.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

