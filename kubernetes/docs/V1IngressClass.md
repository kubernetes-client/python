# V1IngressClass

IngressClass represents the class of the Ingress, referenced by the Ingress Spec. The `ingressclass.kubernetes.io/is-default-class` annotation can be used to indicate that an IngressClass should be considered default. When a single IngressClass resource has this annotation set to true, new Ingress resources without a class specified will be assigned this default class.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1IngressClassSpec**](V1IngressClassSpec.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_class import V1IngressClass

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressClass from a JSON string
v1_ingress_class_instance = V1IngressClass.from_json(json)
# print the JSON string representation of the object
print V1IngressClass.to_json()

# convert the object into a dict
v1_ingress_class_dict = v1_ingress_class_instance.to_dict()
# create an instance of V1IngressClass from a dict
v1_ingress_class_form_dict = v1_ingress_class.from_dict(v1_ingress_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


