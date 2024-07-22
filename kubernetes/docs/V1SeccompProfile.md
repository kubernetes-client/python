# V1SeccompProfile

SeccompProfile defines a pod/container's seccomp profile settings. Only one profile source may be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**localhost_profile** | **str** | localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet&#39;s configured seccomp profile location. Must be set if type is \&quot;Localhost\&quot;. Must NOT be set for any other type. | [optional] 
**type** | **str** | type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied. | 

## Example

```python
from kubernetes.client.models.v1_seccomp_profile import V1SeccompProfile

# TODO update the JSON string below
json = "{}"
# create an instance of V1SeccompProfile from a JSON string
v1_seccomp_profile_instance = V1SeccompProfile.from_json(json)
# print the JSON string representation of the object
print V1SeccompProfile.to_json()

# convert the object into a dict
v1_seccomp_profile_dict = v1_seccomp_profile_instance.to_dict()
# create an instance of V1SeccompProfile from a dict
v1_seccomp_profile_form_dict = v1_seccomp_profile.from_dict(v1_seccomp_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


