# kubernetes.client.model.v1alpha1_cluster_cidr_spec.V1alpha1ClusterCIDRSpec

ClusterCIDRSpec defines the desired state of ClusterCIDR.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ClusterCIDRSpec defines the desired state of ClusterCIDR. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**perNodeHostBits** | decimal.Decimal, int,  | decimal.Decimal,  | PerNodeHostBits defines the number of host bits to be configured per node. A subnet mask determines how much of the address is used for network bits and host bits. For example an IPv4 address of 192.168.0.0/24, splits the address into 24 bits for the network portion and 8 bits for the host portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4 (16 IPs). This field is immutable. | value must be a 32 bit integer
**ipv4** | str,  | str,  | IPv4 defines an IPv4 IP block in CIDR notation(e.g. \&quot;10.0.0.0/8\&quot;). At least one of IPv4 and IPv6 must be specified. This field is immutable. | [optional] 
**ipv6** | str,  | str,  | IPv6 defines an IPv6 IP block in CIDR notation(e.g. \&quot;fd12:3456:789a:1::/64\&quot;). At least one of IPv4 and IPv6 must be specified. This field is immutable. | [optional] 
**nodeSelector** | [**V1NodeSelector**](V1NodeSelector.md) | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

