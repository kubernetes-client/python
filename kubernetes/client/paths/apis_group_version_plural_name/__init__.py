# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.apis_group_version_plural_name import Api

from kubernetes.client.paths import PathValues

path = PathValues.APIS_GROUP_VERSION_PLURAL_NAME