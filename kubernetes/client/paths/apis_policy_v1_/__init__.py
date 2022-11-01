# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.apis_policy_v1_ import Api

from kubernetes.client.paths import PathValues

path = PathValues.APIS_POLICY_V1_