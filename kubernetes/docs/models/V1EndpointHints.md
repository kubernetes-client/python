# kubernetes.client.model.v1_endpoint_hints.V1EndpointHints

EndpointHints provides hints describing how an endpoint should be consumed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EndpointHints provides hints describing how an endpoint should be consumed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[forZones](#forZones)** | list, tuple,  | tuple,  | forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# forZones

forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ForZone**](V1ForZone.md) | [**V1ForZone**](V1ForZone.md) | [**V1ForZone**](V1ForZone.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

