# V1CSIDriver

CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1CSIDriverSpec**](V1CSIDriverSpec.md) |  | 

## Example

```python
from kubernetes.client.models.v1_csi_driver import V1CSIDriver

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSIDriver from a JSON string
v1_csi_driver_instance = V1CSIDriver.from_json(json)
# print the JSON string representation of the object
print V1CSIDriver.to_json()

# convert the object into a dict
v1_csi_driver_dict = v1_csi_driver_instance.to_dict()
# create an instance of V1CSIDriver from a dict
v1_csi_driver_form_dict = v1_csi_driver.from_dict(v1_csi_driver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


