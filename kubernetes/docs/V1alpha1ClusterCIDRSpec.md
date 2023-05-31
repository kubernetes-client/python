# V1alpha1ClusterCIDRSpec

ClusterCIDRSpec defines the desired state of ClusterCIDR.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | ipv4 defines an IPv4 IP block in CIDR notation(e.g. \&quot;10.0.0.0/8\&quot;). At least one of ipv4 and ipv6 must be specified. This field is immutable. | [optional] 
**ipv6** | **str** | ipv6 defines an IPv6 IP block in CIDR notation(e.g. \&quot;2001:db8::/64\&quot;). At least one of ipv4 and ipv6 must be specified. This field is immutable. | [optional] 
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 
**per_node_host_bits** | **int** | perNodeHostBits defines the number of host bits to be configured per node. A subnet mask determines how much of the address is used for network bits and host bits. For example an IPv4 address of 192.168.0.0/24, splits the address into 24 bits for the network portion and 8 bits for the host portion. To allocate 256 IPs, set this field to 8 (a /24 mask for IPv4 or a /120 for IPv6). Minimum value is 4 (16 IPs). This field is immutable. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


