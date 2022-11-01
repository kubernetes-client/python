from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers_name.get import ApiForget
from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers_name.put import ApiForput
from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers_name.delete import ApiFordelete
from kubernetes.client.paths.apis_autoscaling_v1_namespaces_namespace_horizontalpodautoscalers_name.patch import ApiForpatch


class ApisAutoscalingV1NamespacesNamespaceHorizontalpodautoscalersName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
