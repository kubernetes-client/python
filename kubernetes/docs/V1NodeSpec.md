# V1NodeSpec

NodeSpec describes the attributes that a node is created with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_source** | [**V1NodeConfigSource**](V1NodeConfigSource.md) |  | [optional] 
**external_id** | **str** | Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 | [optional] 
**pod_cidr** | **str** | PodCIDR represents the pod IP range assigned to the node. | [optional] 
**pod_cidrs** | **List[str]** | podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6. | [optional] 
**provider_id** | **str** | ID of the node assigned by the cloud provider in the format: &lt;ProviderName&gt;://&lt;ProviderSpecificNodeID&gt; | [optional] 
**taints** | [**List[V1Taint]**](V1Taint.md) | If specified, the node&#39;s taints. | [optional] 
**unschedulable** | **bool** | Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_spec import V1NodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeSpec from a JSON string
v1_node_spec_instance = V1NodeSpec.from_json(json)
# print the JSON string representation of the object
print V1NodeSpec.to_json()

# convert the object into a dict
v1_node_spec_dict = v1_node_spec_instance.to_dict()
# create an instance of V1NodeSpec from a dict
v1_node_spec_form_dict = v1_node_spec.from_dict(v1_node_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


