# V1SELinuxOptions

SELinuxOptions are the labels to be applied to the container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | Level is SELinux level label that applies to the container. | [optional] 
**role** | **str** | Role is a SELinux role label that applies to the container. | [optional] 
**type** | **str** | Type is a SELinux type label that applies to the container. | [optional] 
**user** | **str** | User is a SELinux user label that applies to the container. | [optional] 

## Example

```python
from kubernetes.client.models.v1_se_linux_options import V1SELinuxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of V1SELinuxOptions from a JSON string
v1_se_linux_options_instance = V1SELinuxOptions.from_json(json)
# print the JSON string representation of the object
print V1SELinuxOptions.to_json()

# convert the object into a dict
v1_se_linux_options_dict = v1_se_linux_options_instance.to_dict()
# create an instance of V1SELinuxOptions from a dict
v1_se_linux_options_form_dict = v1_se_linux_options.from_dict(v1_se_linux_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


