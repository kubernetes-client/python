# V1beta1StatefulSetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_management_policy** | **str** | podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is &#x60;OrderedReady&#x60;, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is &#x60;Parallel&#x60; which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once. | [optional] 
**replicas** | **int** | replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1. | [optional] 
**revision_history_limit** | **int** | revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet&#39;s revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10. | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | selector is a label query over pods that should match the replica count. If empty, defaulted to labels on the pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors | [optional] 
**service_name** | **str** | serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where \&quot;pod-specific-string\&quot; is managed by the StatefulSet controller. | 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. | 
**update_strategy** | [**V1beta1StatefulSetUpdateStrategy**](V1beta1StatefulSetUpdateStrategy.md) | updateStrategy indicates the StatefulSetUpdateStrategy that will be employed to update Pods in the StatefulSet when a revision is made to Template. | [optional] 
**volume_claim_templates** | [**list[V1PersistentVolumeClaim]**](V1PersistentVolumeClaim.md) | volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


