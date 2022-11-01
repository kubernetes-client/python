# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas import Api

from kubernetes.client.paths import PathValues

path = PathValues.API_V1_NAMESPACES_NAMESPACE_RESOURCEQUOTAS