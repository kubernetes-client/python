# kubernetes.client.model.v1_lease_spec.V1LeaseSpec

LeaseSpec is a specification of a Lease.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LeaseSpec is a specification of a Lease. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**acquireTime** | str, datetime,  | str,  | acquireTime is a time when the current lease was acquired. | [optional] value must conform to RFC-3339 date-time
**holderIdentity** | str,  | str,  | holderIdentity contains the identity of the holder of a current lease. | [optional] 
**leaseDurationSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime. | [optional] value must be a 32 bit integer
**leaseTransitions** | decimal.Decimal, int,  | decimal.Decimal,  | leaseTransitions is the number of transitions of a lease between holders. | [optional] value must be a 32 bit integer
**renewTime** | str, datetime,  | str,  | renewTime is a time when the current holder of a lease has last updated the lease. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

