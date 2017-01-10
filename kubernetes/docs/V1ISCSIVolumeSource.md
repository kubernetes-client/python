# V1ISCSIVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi | [optional] 
**iqn** | **str** | Target iSCSI Qualified Name. | 
**iscsi_interface** | **str** | Optional: Defaults to &#39;default&#39; (tcp). iSCSI interface name that uses an iSCSI transport. | [optional] 
**lun** | **int** | iSCSI target lun number. | 
**read_only** | **bool** | ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. | [optional] 
**target_portal** | **str** | iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


