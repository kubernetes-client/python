# V1alpha3ShareableCapacityStatus

ShareableCapacityStatus reports aggregate amounts for a single shareable capacity key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** | Available is Total minus Consumed, never negative. |
**consumed** | **str** | Consumed is the amount drawn by current allocations. |
**name** | **str** | Name is the capacity name. |
**total** | **str** | Total is the sum of this capacity across shareable devices in the pool. |

## Example

```python
from kubernetes.client.models.v1alpha3_shareable_capacity_status import V1alpha3ShareableCapacityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ShareableCapacityStatus from a JSON string
v1alpha3_shareable_capacity_status_instance = V1alpha3ShareableCapacityStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ShareableCapacityStatus.to_json())

# convert the object into a dict
v1alpha3_shareable_capacity_status_dict = v1alpha3_shareable_capacity_status_instance.to_dict()
# create an instance of V1alpha3ShareableCapacityStatus from a dict
v1alpha3_shareable_capacity_status_from_dict = V1alpha3ShareableCapacityStatus.from_dict(v1alpha3_shareable_capacity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
