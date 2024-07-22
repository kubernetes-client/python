# V1ClusterRole

ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_rule** | [**V1AggregationRule**](V1AggregationRule.md) |  | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**rules** | [**List[V1PolicyRule]**](V1PolicyRule.md) | Rules holds all the PolicyRules for this ClusterRole | [optional] 

## Example

```python
from kubernetes.client.models.v1_cluster_role import V1ClusterRole

# TODO update the JSON string below
json = "{}"
# create an instance of V1ClusterRole from a JSON string
v1_cluster_role_instance = V1ClusterRole.from_json(json)
# print the JSON string representation of the object
print V1ClusterRole.to_json()

# convert the object into a dict
v1_cluster_role_dict = v1_cluster_role_instance.to_dict()
# create an instance of V1ClusterRole from a dict
v1_cluster_role_form_dict = v1_cluster_role.from_dict(v1_cluster_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


