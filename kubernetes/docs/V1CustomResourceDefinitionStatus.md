# V1CustomResourceDefinitionStatus

CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_names** | [**V1CustomResourceDefinitionNames**](V1CustomResourceDefinitionNames.md) |  | [optional] 
**conditions** | [**List[V1CustomResourceDefinitionCondition]**](V1CustomResourceDefinitionCondition.md) | conditions indicate state for particular aspects of a CustomResourceDefinition | [optional] 
**stored_versions** | **List[str]** | storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from &#x60;spec.versions&#x60; while they exist in this list. | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_definition_status import V1CustomResourceDefinitionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceDefinitionStatus from a JSON string
v1_custom_resource_definition_status_instance = V1CustomResourceDefinitionStatus.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceDefinitionStatus.to_json()

# convert the object into a dict
v1_custom_resource_definition_status_dict = v1_custom_resource_definition_status_instance.to_dict()
# create an instance of V1CustomResourceDefinitionStatus from a dict
v1_custom_resource_definition_status_form_dict = v1_custom_resource_definition_status.from_dict(v1_custom_resource_definition_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


