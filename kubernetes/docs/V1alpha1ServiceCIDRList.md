# V1alpha1ServiceCIDRList

ServiceCIDRList contains a list of ServiceCIDR objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1alpha1ServiceCIDR]**](V1alpha1ServiceCIDR.md) | items is the list of ServiceCIDRs. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_service_cidr_list import V1alpha1ServiceCIDRList

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ServiceCIDRList from a JSON string
v1alpha1_service_cidr_list_instance = V1alpha1ServiceCIDRList.from_json(json)
# print the JSON string representation of the object
print V1alpha1ServiceCIDRList.to_json()

# convert the object into a dict
v1alpha1_service_cidr_list_dict = v1alpha1_service_cidr_list_instance.to_dict()
# create an instance of V1alpha1ServiceCIDRList from a dict
v1alpha1_service_cidr_list_form_dict = v1alpha1_service_cidr_list.from_dict(v1alpha1_service_cidr_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


