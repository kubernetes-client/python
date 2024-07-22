# V1AppArmorProfile

AppArmorProfile defines a pod or container's AppArmor settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localhost_profile** | **str** | localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is \&quot;Localhost\&quot;. | [optional] 
**type** | **str** | type indicates which kind of AppArmor profile will be applied. Valid options are:   Localhost - a profile pre-loaded on the node.   RuntimeDefault - the container runtime&#39;s default profile.   Unconfined - no AppArmor enforcement. | 

## Example

```python
from kubernetes.client.models.v1_app_armor_profile import V1AppArmorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of V1AppArmorProfile from a JSON string
v1_app_armor_profile_instance = V1AppArmorProfile.from_json(json)
# print the JSON string representation of the object
print V1AppArmorProfile.to_json()

# convert the object into a dict
v1_app_armor_profile_dict = v1_app_armor_profile_instance.to_dict()
# create an instance of V1AppArmorProfile from a dict
v1_app_armor_profile_form_dict = v1_app_armor_profile.from_dict(v1_app_armor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


