# V1CephFSVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitors** | **list[str]** | Required: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it | 
**path** | **str** | Optional: Used as the mounted root, rather than the full Ceph tree, default is / | [optional] 
**read_only** | **bool** | Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_file** | **str** | Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it | [optional] 
**secret_ref** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it | [optional] 
**user** | **str** | Optional: User is the rados user name, default is admin More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


