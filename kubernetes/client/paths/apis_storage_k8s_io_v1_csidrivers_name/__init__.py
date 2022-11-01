# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers_name import Api

from kubernetes.client.paths import PathValues

path = PathValues.APIS_STORAGE_K8S_IO_V1_CSIDRIVERS_NAME