# V1alpha1VolumeAttributesClass

VolumeAttributesClass represents a specification of mutable volume attributes defined by the CSI driver. The class can be specified during dynamic provisioning of PersistentVolumeClaims, and changed in the PersistentVolumeClaim spec after provisioning.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_name** | **str** | Name of the CSI driver This field is immutable. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**parameters** | **Dict[str, str]** | parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.  This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an \&quot;Infeasible\&quot; state in the modifyVolumeStatus field. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_volume_attributes_class import V1alpha1VolumeAttributesClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1VolumeAttributesClass from a JSON string
v1alpha1_volume_attributes_class_instance = V1alpha1VolumeAttributesClass.from_json(json)
# print the JSON string representation of the object
print V1alpha1VolumeAttributesClass.to_json()

# convert the object into a dict
v1alpha1_volume_attributes_class_dict = v1alpha1_volume_attributes_class_instance.to_dict()
# create an instance of V1alpha1VolumeAttributesClass from a dict
v1alpha1_volume_attributes_class_form_dict = v1alpha1_volume_attributes_class.from_dict(v1alpha1_volume_attributes_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


