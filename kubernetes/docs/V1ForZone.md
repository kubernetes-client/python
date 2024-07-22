# V1ForZone

ForZone provides information about which zones should consume this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name represents the name of the zone. | 

## Example

```python
from kubernetes.client.models.v1_for_zone import V1ForZone

# TODO update the JSON string below
json = "{}"
# create an instance of V1ForZone from a JSON string
v1_for_zone_instance = V1ForZone.from_json(json)
# print the JSON string representation of the object
print V1ForZone.to_json()

# convert the object into a dict
v1_for_zone_dict = v1_for_zone_instance.to_dict()
# create an instance of V1ForZone from a dict
v1_for_zone_form_dict = v1_for_zone.from_dict(v1_for_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


