# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from kubernetes.client.paths.well_known_openid_configuration_ import Api

from kubernetes.client.paths import PathValues

path = PathValues._WELLKNOWN_OPENIDCONFIGURATION_