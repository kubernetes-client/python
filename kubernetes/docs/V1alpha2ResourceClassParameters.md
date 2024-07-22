# V1alpha2ResourceClassParameters

ResourceClassParameters defines resource requests for a ResourceClass in an in-tree format understood by Kubernetes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**filters** | [**List[V1alpha2ResourceFilter]**](V1alpha2ResourceFilter.md) | Filters describes additional contraints that must be met when using the class. | [optional] 
**generated_from** | [**V1alpha2ResourceClassParametersReference**](V1alpha2ResourceClassParametersReference.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**vendor_parameters** | [**List[V1alpha2VendorParameters]**](V1alpha2VendorParameters.md) | VendorParameters are arbitrary setup parameters for all claims using this class. They are ignored while allocating the claim. There must not be more than one entry per driver. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_class_parameters import V1alpha2ResourceClassParameters

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClassParameters from a JSON string
v1alpha2_resource_class_parameters_instance = V1alpha2ResourceClassParameters.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClassParameters.to_json()

# convert the object into a dict
v1alpha2_resource_class_parameters_dict = v1alpha2_resource_class_parameters_instance.to_dict()
# create an instance of V1alpha2ResourceClassParameters from a dict
v1alpha2_resource_class_parameters_form_dict = v1alpha2_resource_class_parameters.from_dict(v1alpha2_resource_class_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


