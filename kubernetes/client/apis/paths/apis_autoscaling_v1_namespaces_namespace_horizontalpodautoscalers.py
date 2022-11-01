from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers.get import ApiForget
from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers.post import ApiForpost
from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers.delete import ApiFordelete


class ApisAutoscalingV1NamespacesNamespaceHorizontalpodautoscalers(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
