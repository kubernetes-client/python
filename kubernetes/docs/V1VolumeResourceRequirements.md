# V1VolumeResourceRequirements

VolumeResourceRequirements describes the storage resource requirements for a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **Dict[str, str]** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **Dict[str, str]** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

## Example

```python
from kubernetes.client.models.v1_volume_resource_requirements import V1VolumeResourceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeResourceRequirements from a JSON string
v1_volume_resource_requirements_instance = V1VolumeResourceRequirements.from_json(json)
# print the JSON string representation of the object
print V1VolumeResourceRequirements.to_json()

# convert the object into a dict
v1_volume_resource_requirements_dict = v1_volume_resource_requirements_instance.to_dict()
# create an instance of V1VolumeResourceRequirements from a dict
v1_volume_resource_requirements_form_dict = v1_volume_resource_requirements.from_dict(v1_volume_resource_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


