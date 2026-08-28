# V1StorageHealth

StorageHealth contains storage backend health reported by a CSI driver on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_conditions** | [**List[V1StorageHealthCondition]**](V1StorageHealthCondition.md) | healthConditions are the adverse storage backend conditions reported by the CSI driver. At most 16 conditions may be reported. | [optional]
**name** | **str** | name is the CSI driver name, matching CSINodeDriver.name. |

## Example

```python
from kubernetes.aio.client.models.v1_storage_health import V1StorageHealth

# TODO update the JSON string below
json = "{}"
# create an instance of V1StorageHealth from a JSON string
v1_storage_health_instance = V1StorageHealth.from_json(json)
# print the JSON string representation of the object
print(V1StorageHealth.to_json())

# convert the object into a dict
v1_storage_health_dict = v1_storage_health_instance.to_dict()
# create an instance of V1StorageHealth from a dict
v1_storage_health_from_dict = V1StorageHealth.from_dict(v1_storage_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
