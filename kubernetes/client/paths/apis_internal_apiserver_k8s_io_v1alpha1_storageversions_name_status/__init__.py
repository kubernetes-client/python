# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.apis_internal_apiserver_k8s_io_v1alpha1_storageversions_name_status import Api

from kubernetes.client.paths import PathValues

path = PathValues.APIS_INTERNAL_APISERVER_K8S_IO_V1ALPHA1_STORAGEVERSIONS_NAME_STATUS