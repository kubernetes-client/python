# kubernetes.client.model.v1_volume.V1Volume

Volume represents a named volume in a pod that may be accessed by any container in the pod.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Volume represents a named volume in a pod that may be accessed by any container in the pod. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**awsElasticBlockStore** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) |  | [optional] 
**azureDisk** | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) |  | [optional] 
**azureFile** | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) |  | [optional] 
**cephfs** | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) |  | [optional] 
**cinder** | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) |  | [optional] 
**configMap** | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) |  | [optional] 
**csi** | [**V1CSIVolumeSource**](V1CSIVolumeSource.md) | [**V1CSIVolumeSource**](V1CSIVolumeSource.md) |  | [optional] 
**downwardAPI** | [**V1DownwardAPIVolumeSource**](V1DownwardAPIVolumeSource.md) | [**V1DownwardAPIVolumeSource**](V1DownwardAPIVolumeSource.md) |  | [optional] 
**emptyDir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) |  | [optional] 
**ephemeral** | [**V1EphemeralVolumeSource**](V1EphemeralVolumeSource.md) | [**V1EphemeralVolumeSource**](V1EphemeralVolumeSource.md) |  | [optional] 
**fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) | [**V1FCVolumeSource**](V1FCVolumeSource.md) |  | [optional] 
**flexVolume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) |  | [optional] 
**flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) |  | [optional] 
**gcePersistentDisk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) |  | [optional] 
**gitRepo** | [**V1GitRepoVolumeSource**](V1GitRepoVolumeSource.md) | [**V1GitRepoVolumeSource**](V1GitRepoVolumeSource.md) |  | [optional] 
**glusterfs** | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) |  | [optional] 
**hostPath** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) |  | [optional] 
**iscsi** | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) |  | [optional] 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) |  | [optional] 
**persistentVolumeClaim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) |  | [optional] 
**photonPersistentDisk** | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) |  | [optional] 
**portworxVolume** | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) |  | [optional] 
**projected** | [**V1ProjectedVolumeSource**](V1ProjectedVolumeSource.md) | [**V1ProjectedVolumeSource**](V1ProjectedVolumeSource.md) |  | [optional] 
**quobyte** | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) |  | [optional] 
**rbd** | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) |  | [optional] 
**scaleIO** | [**V1ScaleIOVolumeSource**](V1ScaleIOVolumeSource.md) | [**V1ScaleIOVolumeSource**](V1ScaleIOVolumeSource.md) |  | [optional] 
**secret** | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) |  | [optional] 
**storageos** | [**V1StorageOSVolumeSource**](V1StorageOSVolumeSource.md) | [**V1StorageOSVolumeSource**](V1StorageOSVolumeSource.md) |  | [optional] 
**vsphereVolume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

