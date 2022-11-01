# kubernetes.client.model.v1_iscsi_volume_source.V1ISCSIVolumeSource

Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Represents an ISCSI disk. ISCSI volumes can only be mounted as read/write once. ISCSI volumes support ownership management and SELinux relabeling. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lun** | decimal.Decimal, int,  | decimal.Decimal,  | lun represents iSCSI Target Lun number. | value must be a 32 bit integer
**iqn** | str,  | str,  | iqn is the target iSCSI Qualified Name. | 
**targetPortal** | str,  | str,  | targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | 
**chapAuthDiscovery** | bool,  | BoolClass,  | chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication | [optional] 
**chapAuthSession** | bool,  | BoolClass,  | chapAuthSession defines whether support iSCSI Session CHAP authentication | [optional] 
**fsType** | str,  | str,  | fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi | [optional] 
**initiatorName** | str,  | str,  | initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface &lt;target portal&gt;:&lt;volume name&gt; will be created for the connection. | [optional] 
**iscsiInterface** | str,  | str,  | iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to &#x27;default&#x27; (tcp). | [optional] 
**[portals](#portals)** | list, tuple,  | tuple,  | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | [optional] 
**readOnly** | bool,  | BoolClass,  | readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. | [optional] 
**secretRef** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | [**V1LocalObjectReference**](V1LocalObjectReference.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# portals

portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

