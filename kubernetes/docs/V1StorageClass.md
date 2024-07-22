# V1StorageClass

StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.  StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_volume_expansion** | **bool** | allowVolumeExpansion shows whether the storage class allow volume expand. | [optional] 
**allowed_topologies** | [**List[V1TopologySelectorTerm]**](V1TopologySelectorTerm.md) | allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature. | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**mount_options** | **List[str]** | mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. [\&quot;ro\&quot;, \&quot;soft\&quot;]. Not validated - mount of the PVs will simply fail if one is invalid. | [optional] 
**parameters** | **Dict[str, str]** | parameters holds the parameters for the provisioner that should create volumes of this storage class. | [optional] 
**provisioner** | **str** | provisioner indicates the type of the provisioner. | 
**reclaim_policy** | **str** | reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete. | [optional] 
**volume_binding_mode** | **str** | volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature. | [optional] 

## Example

```python
from kubernetes.client.models.v1_storage_class import V1StorageClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1StorageClass from a JSON string
v1_storage_class_instance = V1StorageClass.from_json(json)
# print the JSON string representation of the object
print V1StorageClass.to_json()

# convert the object into a dict
v1_storage_class_dict = v1_storage_class_instance.to_dict()
# create an instance of V1StorageClass from a dict
v1_storage_class_form_dict = v1_storage_class.from_dict(v1_storage_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


