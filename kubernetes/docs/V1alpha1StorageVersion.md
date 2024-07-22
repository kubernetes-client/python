# V1alpha1StorageVersion

Storage version of a specific resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | **object** | Spec is an empty spec. It is here to comply with Kubernetes API style. | 
**status** | [**V1alpha1StorageVersionStatus**](V1alpha1StorageVersionStatus.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version import V1alpha1StorageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersion from a JSON string
v1alpha1_storage_version_instance = V1alpha1StorageVersion.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersion.to_json()

# convert the object into a dict
v1alpha1_storage_version_dict = v1alpha1_storage_version_instance.to_dict()
# create an instance of V1alpha1StorageVersion from a dict
v1alpha1_storage_version_form_dict = v1alpha1_storage_version.from_dict(v1alpha1_storage_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


