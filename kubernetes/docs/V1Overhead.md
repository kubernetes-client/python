# V1Overhead

Overhead structure represents the resource overhead associated with running a pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_fixed** | **Dict[str, str]** | podFixed represents the fixed resource overhead associated with running a pod. | [optional] 

## Example

```python
from kubernetes.client.models.v1_overhead import V1Overhead

# TODO update the JSON string below
json = "{}"
# create an instance of V1Overhead from a JSON string
v1_overhead_instance = V1Overhead.from_json(json)
# print the JSON string representation of the object
print V1Overhead.to_json()

# convert the object into a dict
v1_overhead_dict = v1_overhead_instance.to_dict()
# create an instance of V1Overhead from a dict
v1_overhead_form_dict = v1_overhead.from_dict(v1_overhead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


