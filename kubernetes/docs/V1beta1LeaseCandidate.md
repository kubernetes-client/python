# V1beta1LeaseCandidate

LeaseCandidate defines a candidate for a Lease object. Candidates are created such that coordinated leader election will pick the best leader from the list of candidates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1beta1LeaseCandidateSpec**](V1beta1LeaseCandidateSpec.md) |  |

## Example

```python
from kubernetes.client.models.v1beta1_lease_candidate import V1beta1LeaseCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1LeaseCandidate from a JSON string
v1beta1_lease_candidate_instance = V1beta1LeaseCandidate.from_json(json)
# print the JSON string representation of the object
print(V1beta1LeaseCandidate.to_json())

# convert the object into a dict
v1beta1_lease_candidate_dict = v1beta1_lease_candidate_instance.to_dict()
# create an instance of V1beta1LeaseCandidate from a dict
v1beta1_lease_candidate_from_dict = V1beta1LeaseCandidate.from_dict(v1beta1_lease_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
