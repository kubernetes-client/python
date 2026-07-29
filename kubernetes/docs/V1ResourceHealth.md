# V1ResourceHealth

ResourceHealth represents the health of a resource. It has the latest device health information. This is a part of KEP https://kep.k8s.io/4680.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health** | **str** | Health of the resource. can be one of:  - Healthy: operates as normal  - Unhealthy: reported unhealthy. We consider this a temporary health issue               since we do not have a mechanism today to distinguish               temporary and permanent issues.  - Unknown: The status cannot be determined.             For example, Device Plugin got unregistered and hasn&#39;t been re-registered since.  In future we may want to introduce the PermanentlyUnhealthy Status. | [optional]
**message** | **str** | Message provides human-readable context for Health (e.g. \&quot;ECC error count exceeded threshold\&quot;). This field is populated by the kubelet when ResourceHealthStatusMessage is enabled if the DRA plugin returns a message, and is null otherwise. | [optional]
**resource_id** | **str** | ResourceID is the unique identifier of the resource. See the ResourceID type for more information. |

## Example

```python
from kubernetes.client.models.v1_resource_health import V1ResourceHealth

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceHealth from a JSON string
v1_resource_health_instance = V1ResourceHealth.from_json(json)
# print the JSON string representation of the object
print(V1ResourceHealth.to_json())

# convert the object into a dict
v1_resource_health_dict = v1_resource_health_instance.to_dict()
# create an instance of V1ResourceHealth from a dict
v1_resource_health_from_dict = V1ResourceHealth.from_dict(v1_resource_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
