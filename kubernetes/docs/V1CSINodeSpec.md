# V1CSINodeSpec

CSINodeSpec holds information about the specification of all CSI drivers installed on a node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drivers** | [**List[V1CSINodeDriver]**](V1CSINodeDriver.md) | drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty. | 

## Example

```python
from kubernetes.client.models.v1_csi_node_spec import V1CSINodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1CSINodeSpec from a JSON string
v1_csi_node_spec_instance = V1CSINodeSpec.from_json(json)
# print the JSON string representation of the object
print V1CSINodeSpec.to_json()

# convert the object into a dict
v1_csi_node_spec_dict = v1_csi_node_spec_instance.to_dict()
# create an instance of V1CSINodeSpec from a dict
v1_csi_node_spec_form_dict = v1_csi_node_spec.from_dict(v1_csi_node_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


