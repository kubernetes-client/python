# V1RBDVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd | [optional] 
**image** | **str** | The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | 
**keyring** | **str** | Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | [optional] 
**monitors** | **list[str]** | A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | 
**pool** | **str** | The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. | [optional] 
**read_only** | **bool** | ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | [optional] 
**user** | **str** | The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


