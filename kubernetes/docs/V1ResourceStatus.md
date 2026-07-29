# V1ResourceStatus

ResourceStatus represents the status of a single resource allocated to a Pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the resource. Must be unique within the pod and in case of non-DRA resource, match one of the resources from the pod spec. For DRA resources, the value must be \&quot;claim:&lt;claim_name&gt;/&lt;request&gt;\&quot;. When this status is reported about a container, the \&quot;claim_name\&quot; and \&quot;request\&quot; must match one of the claims of this container. |
**resources** | [**List[V1ResourceHealth]**](V1ResourceHealth.md) | List of unique resources health. Each element in the list contains an unique resource ID and its health. At a minimum, for the lifetime of a Pod, resource ID must uniquely identify the resource allocated to the Pod on the Node. If other Pod on the same Node reports the status with the same resource ID, it must be the same resource they share. See ResourceID type definition for a specific format it has in various use cases. | [optional]

## Example

```python
from kubernetes.client.models.v1_resource_status import V1ResourceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceStatus from a JSON string
v1_resource_status_instance = V1ResourceStatus.from_json(json)
# print the JSON string representation of the object
print(V1ResourceStatus.to_json())

# convert the object into a dict
v1_resource_status_dict = v1_resource_status_instance.to_dict()
# create an instance of V1ResourceStatus from a dict
v1_resource_status_from_dict = V1ResourceStatus.from_dict(v1_resource_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
