# V1HostAlias

HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod's hosts file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostnames** | **List[str]** | Hostnames for the above IP address. | [optional] 
**ip** | **str** | IP address of the host file entry. | 

## Example

```python
from kubernetes.client.models.v1_host_alias import V1HostAlias

# TODO update the JSON string below
json = "{}"
# create an instance of V1HostAlias from a JSON string
v1_host_alias_instance = V1HostAlias.from_json(json)
# print the JSON string representation of the object
print V1HostAlias.to_json()

# convert the object into a dict
v1_host_alias_dict = v1_host_alias_instance.to_dict()
# create an instance of V1HostAlias from a dict
v1_host_alias_form_dict = v1_host_alias.from_dict(v1_host_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


