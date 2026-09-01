# V1alpha3PartitionTypeStatus

PartitionTypeStatus reports allocatability for a single partition type, identified by the value of a grouping attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatable** | **int** | Allocatable is the number of additional devices of this partition type that could still be allocated given current shared-counter consumption. |
**attribute** | **str** | Attribute is the fully qualified name of the device attribute whose value groups this entry. It is the PartitionTypeAttribute declared by the devices&#39; own slice, or the default named in the request when their slice declares none. |
**total** | **int** | Total is the number of devices of this partition type in the pool. |
**type** | **str** | Type is the partition type value (e.g. \&quot;Full\&quot; or \&quot;Half\&quot;). |

## Example

```python
from kubernetes.aio.client.models.v1alpha3_partition_type_status import V1alpha3PartitionTypeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3PartitionTypeStatus from a JSON string
v1alpha3_partition_type_status_instance = V1alpha3PartitionTypeStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3PartitionTypeStatus.to_json())

# convert the object into a dict
v1alpha3_partition_type_status_dict = v1alpha3_partition_type_status_instance.to_dict()
# create an instance of V1alpha3PartitionTypeStatus from a dict
v1alpha3_partition_type_status_from_dict = V1alpha3PartitionTypeStatus.from_dict(v1alpha3_partition_type_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
