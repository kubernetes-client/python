# kubernetes.client.model.v1_stateful_set_spec.V1StatefulSetSpec

A StatefulSetSpec is the specification of a StatefulSet.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A StatefulSetSpec is the specification of a StatefulSet. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**serviceName** | str,  | str,  | serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \&quot;pod-specific-string\&quot; is managed by the StatefulSet controller. | 
**minReadySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] value must be a 32 bit integer
**persistentVolumeClaimRetentionPolicy** | [**V1StatefulSetPersistentVolumeClaimRetentionPolicy**](V1StatefulSetPersistentVolumeClaimRetentionPolicy.md) | [**V1StatefulSetPersistentVolumeClaimRetentionPolicy**](V1StatefulSetPersistentVolumeClaimRetentionPolicy.md) |  | [optional] 
**podManagementPolicy** | str,  | str,  | podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is &#x60;OrderedReady&#x60;, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is &#x60;Parallel&#x60; which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.   | [optional] 
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1. | [optional] value must be a 32 bit integer
**revisionHistoryLimit** | decimal.Decimal, int,  | decimal.Decimal,  | revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet&#x27;s revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10. | [optional] value must be a 32 bit integer
**updateStrategy** | [**V1StatefulSetUpdateStrategy**](V1StatefulSetUpdateStrategy.md) | [**V1StatefulSetUpdateStrategy**](V1StatefulSetUpdateStrategy.md) |  | [optional] 
**[volumeClaimTemplates](#volumeClaimTemplates)** | list, tuple,  | tuple,  | volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# volumeClaimTemplates

volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md) | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md) | [**V1PersistentVolumeClaim**](V1PersistentVolumeClaim.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

