# V1alpha1EvictionRequest

EvictionRequest defines a request that should ideally result in a graceful eviction of a .spec.target (e.g. termination of a pod).  The evictionrequest-controller observes intents of all EvictionRequests and transforms them into Evictions.   - .spec.requester is set as a label on the Eviction for easier lookup.   - Each target can have a set of responders assigned to it. Eviction objects are observed by     these responders, who implement the eviction logic and update the Eviction's status with     progress.  There is many-to-many relationship between EvictionRequests and Evictions in general. And many-to-one if the target is a  pod.  If all requesters withdraw their eviction intent for a common target, the eviction will be canceled. Deleting an EvictionRequest also counts as a withdrawal. Once all EvictionRequest of a target are removed, the corresponding Evictions are eventually garbage collected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1alpha1EvictionRequestSpec**](V1alpha1EvictionRequestSpec.md) |  |
**status** | [**V1alpha1EvictionRequestStatus**](V1alpha1EvictionRequestStatus.md) |  | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha1_eviction_request import V1alpha1EvictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionRequest from a JSON string
v1alpha1_eviction_request_instance = V1alpha1EvictionRequest.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionRequest.to_json())

# convert the object into a dict
v1alpha1_eviction_request_dict = v1alpha1_eviction_request_instance.to_dict()
# create an instance of V1alpha1EvictionRequest from a dict
v1alpha1_eviction_request_from_dict = V1alpha1EvictionRequest.from_dict(v1alpha1_eviction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
