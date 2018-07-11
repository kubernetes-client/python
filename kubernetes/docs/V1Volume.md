# V1Volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_elastic_block_store** | [**V1AWSElasticBlockStoreVolumeSource**](V1AWSElasticBlockStoreVolumeSource.md) | AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore | [optional] 
**azure_disk** | [**V1AzureDiskVolumeSource**](V1AzureDiskVolumeSource.md) | AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. | [optional] 
**azure_file** | [**V1AzureFileVolumeSource**](V1AzureFileVolumeSource.md) | AzureFile represents an Azure File Service mount on the host and bind mount to the pod. | [optional] 
**cephfs** | [**V1CephFSVolumeSource**](V1CephFSVolumeSource.md) | CephFS represents a Ceph FS mount on the host that shares a pod&#39;s lifetime | [optional] 
**cinder** | [**V1CinderVolumeSource**](V1CinderVolumeSource.md) | Cinder represents a cinder volume attached and mounted on kubelets host machine More info: https://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md | [optional] 
**config_map** | [**V1ConfigMapVolumeSource**](V1ConfigMapVolumeSource.md) | ConfigMap represents a configMap that should populate this volume | [optional] 
**downward_api** | [**V1DownwardAPIVolumeSource**](V1DownwardAPIVolumeSource.md) | DownwardAPI represents downward API about the pod that should populate this volume | [optional] 
**empty_dir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) | EmptyDir represents a temporary directory that shares a pod&#39;s lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir | [optional] 
**fc** | [**V1FCVolumeSource**](V1FCVolumeSource.md) | FC represents a Fibre Channel resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. | [optional] 
**flex_volume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) | FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. | [optional] 
**flocker** | [**V1FlockerVolumeSource**](V1FlockerVolumeSource.md) | Flocker represents a Flocker volume attached to a kubelet&#39;s host machine. This depends on the Flocker control service being running | [optional] 
**gce_persistent_disk** | [**V1GCEPersistentDiskVolumeSource**](V1GCEPersistentDiskVolumeSource.md) | GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk | [optional] 
**git_repo** | [**V1GitRepoVolumeSource**](V1GitRepoVolumeSource.md) | GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod&#39;s container. | [optional] 
**glusterfs** | [**V1GlusterfsVolumeSource**](V1GlusterfsVolumeSource.md) | Glusterfs represents a Glusterfs mount on the host that shares a pod&#39;s lifetime. More info: https://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) | HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath | [optional] 
**iscsi** | [**V1ISCSIVolumeSource**](V1ISCSIVolumeSource.md) | ISCSI represents an ISCSI Disk resource that is attached to a kubelet&#39;s host machine and then exposed to the pod. More info: https://releases.k8s.io/HEAD/examples/volumes/iscsi/README.md | [optional] 
**name** | **str** | Volume&#39;s name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) | NFS represents an NFS mount on the host that shares a pod&#39;s lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs | [optional] 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) | PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims | [optional] 
**photon_persistent_disk** | [**V1PhotonPersistentDiskVolumeSource**](V1PhotonPersistentDiskVolumeSource.md) | PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine | [optional] 
**portworx_volume** | [**V1PortworxVolumeSource**](V1PortworxVolumeSource.md) | PortworxVolume represents a portworx volume attached and mounted on kubelets host machine | [optional] 
**projected** | [**V1ProjectedVolumeSource**](V1ProjectedVolumeSource.md) | Items for all in one resources secrets, configmaps, and downward API | [optional] 
**quobyte** | [**V1QuobyteVolumeSource**](V1QuobyteVolumeSource.md) | Quobyte represents a Quobyte mount on the host that shares a pod&#39;s lifetime | [optional] 
**rbd** | [**V1RBDVolumeSource**](V1RBDVolumeSource.md) | RBD represents a Rados Block Device mount on the host that shares a pod&#39;s lifetime. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md | [optional] 
**scale_io** | [**V1ScaleIOVolumeSource**](V1ScaleIOVolumeSource.md) | ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. | [optional] 
**secret** | [**V1SecretVolumeSource**](V1SecretVolumeSource.md) | Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret | [optional] 
**storageos** | [**V1StorageOSVolumeSource**](V1StorageOSVolumeSource.md) | StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. | [optional] 
**vsphere_volume** | [**V1VsphereVirtualDiskVolumeSource**](V1VsphereVirtualDiskVolumeSource.md) | VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


