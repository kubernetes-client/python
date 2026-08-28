# V1alpha3ShareableSummaryStatus

ShareableSummaryStatus reports aggregate capacity for a pool that contains devices with AllowMultipleAllocations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**List[V1alpha3ShareableCapacityStatus]**](V1alpha3ShareableCapacityStatus.md) | Capacity reports aggregate total, consumed, and available amounts per shareable capacity key across the pool. | [optional]
**fully_available_devices** | **int** | FullyAvailableDevices is the number of shareable devices with no capacity consumed. |
**partially_available_devices** | **int** | PartiallyAvailableDevices is the number of shareable devices with some but not all capacity consumed. |

## Example

```python
from kubernetes.aio.client.models.v1alpha3_shareable_summary_status import V1alpha3ShareableSummaryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ShareableSummaryStatus from a JSON string
v1alpha3_shareable_summary_status_instance = V1alpha3ShareableSummaryStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ShareableSummaryStatus.to_json())

# convert the object into a dict
v1alpha3_shareable_summary_status_dict = v1alpha3_shareable_summary_status_instance.to_dict()
# create an instance of V1alpha3ShareableSummaryStatus from a dict
v1alpha3_shareable_summary_status_from_dict = V1alpha3ShareableSummaryStatus.from_dict(v1alpha3_shareable_summary_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
