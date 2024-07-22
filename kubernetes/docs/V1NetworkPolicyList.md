# V1NetworkPolicyList

NetworkPolicyList is a list of NetworkPolicy objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1NetworkPolicy]**](V1NetworkPolicy.md) | items is a list of schema objects. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_network_policy_list import V1NetworkPolicyList

# TODO update the JSON string below
json = "{}"
# create an instance of V1NetworkPolicyList from a JSON string
v1_network_policy_list_instance = V1NetworkPolicyList.from_json(json)
# print the JSON string representation of the object
print V1NetworkPolicyList.to_json()

# convert the object into a dict
v1_network_policy_list_dict = v1_network_policy_list_instance.to_dict()
# create an instance of V1NetworkPolicyList from a dict
v1_network_policy_list_form_dict = v1_network_policy_list.from_dict(v1_network_policy_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


