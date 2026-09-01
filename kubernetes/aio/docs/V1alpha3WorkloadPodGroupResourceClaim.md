# V1alpha3WorkloadPodGroupResourceClaim

WorkloadPodGroupResourceClaim references a dynamic resource claim that is shared across pods in the group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name uniquely identifies this resource claim inside the group. This field is required. It must be a DNS_LABEL. |
**resource_claim_name** | **str** | resourceClaimName is the name of a ResourceClaim object in the same namespace. This field is optional. If it is not specified, no resource claim is used. If set, it must be a DNS subdomain. | [optional]
**resource_claim_template_name** | **str** | resourceClaimTemplateName is the name of a ResourceClaimTemplate object in the same namespace. This field is optional. If it is not specified, no resource claim template is used. If set, it must be a DNS subdomain. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha3_workload_pod_group_resource_claim import V1alpha3WorkloadPodGroupResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3WorkloadPodGroupResourceClaim from a JSON string
v1alpha3_workload_pod_group_resource_claim_instance = V1alpha3WorkloadPodGroupResourceClaim.from_json(json)
# print the JSON string representation of the object
print(V1alpha3WorkloadPodGroupResourceClaim.to_json())

# convert the object into a dict
v1alpha3_workload_pod_group_resource_claim_dict = v1alpha3_workload_pod_group_resource_claim_instance.to_dict()
# create an instance of V1alpha3WorkloadPodGroupResourceClaim from a dict
v1alpha3_workload_pod_group_resource_claim_from_dict = V1alpha3WorkloadPodGroupResourceClaim.from_dict(v1alpha3_workload_pod_group_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
