# V1NamespaceStatus

NamespaceStatus is information about the current status of a Namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1NamespaceCondition]**](V1NamespaceCondition.md) | Represents the latest available observations of a namespace&#39;s current state. | [optional] 
**phase** | **str** | Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ | [optional] 

## Example

```python
from kubernetes.client.models.v1_namespace_status import V1NamespaceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NamespaceStatus from a JSON string
v1_namespace_status_instance = V1NamespaceStatus.from_json(json)
# print the JSON string representation of the object
print V1NamespaceStatus.to_json()

# convert the object into a dict
v1_namespace_status_dict = v1_namespace_status_instance.to_dict()
# create an instance of V1NamespaceStatus from a dict
v1_namespace_status_form_dict = v1_namespace_status.from_dict(v1_namespace_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


