# flake8: noqa

__all__ = [
    "WellKnownApi",
    "AdmissionregistrationApi",
    "AdmissionregistrationV1Api",
    "AdmissionregistrationV1alpha1Api",
    "AdmissionregistrationV1beta1Api",
    "ApiextensionsApi",
    "ApiextensionsV1Api",
    "ApiregistrationApi",
    "ApiregistrationV1Api",
    "ApisApi",
    "AppsApi",
    "AppsV1Api",
    "AuthenticationApi",
    "AuthenticationV1Api",
    "AuthorizationApi",
    "AuthorizationV1Api",
    "AutoscalingApi",
    "AutoscalingV1Api",
    "AutoscalingV2Api",
    "BatchApi",
    "BatchV1Api",
    "CertificatesApi",
    "CertificatesV1Api",
    "CertificatesV1alpha1Api",
    "CertificatesV1beta1Api",
    "CoordinationApi",
    "CoordinationV1Api",
    "CoordinationV1alpha2Api",
    "CoordinationV1beta1Api",
    "CoreApi",
    "CoreV1Api",
    "CustomObjectsApi",
    "DiscoveryApi",
    "DiscoveryV1Api",
    "EventsApi",
    "EventsV1Api",
    "FlowcontrolApiserverApi",
    "FlowcontrolApiserverV1Api",
    "InternalApiserverApi",
    "InternalApiserverV1alpha1Api",
    "LogsApi",
    "NetworkingApi",
    "NetworkingV1Api",
    "NetworkingV1beta1Api",
    "NodeApi",
    "NodeV1Api",
    "OpenidApi",
    "PolicyApi",
    "PolicyV1Api",
    "RbacAuthorizationApi",
    "RbacAuthorizationV1Api",
    "ResourceApi",
    "ResourceV1Api",
    "ResourceV1alpha3Api",
    "ResourceV1beta1Api",
    "ResourceV1beta2Api",
    "SchedulingApi",
    "SchedulingV1Api",
    "SchedulingV1alpha2Api",
    "StorageApi",
    "StorageV1Api",
    "StorageV1beta1Api",
    "StoragemigrationApi",
    "StoragemigrationV1beta1Api",
    "VersionApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from kubernetes.aio.client.api.well_known_api import WellKnownApi
    from kubernetes.aio.client.api.admissionregistration_api import AdmissionregistrationApi
    from kubernetes.aio.client.api.admissionregistration_v1_api import AdmissionregistrationV1Api
    from kubernetes.aio.client.api.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api
    from kubernetes.aio.client.api.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api
    from kubernetes.aio.client.api.apiextensions_api import ApiextensionsApi
    from kubernetes.aio.client.api.apiextensions_v1_api import ApiextensionsV1Api
    from kubernetes.aio.client.api.apiregistration_api import ApiregistrationApi
    from kubernetes.aio.client.api.apiregistration_v1_api import ApiregistrationV1Api
    from kubernetes.aio.client.api.apis_api import ApisApi
    from kubernetes.aio.client.api.apps_api import AppsApi
    from kubernetes.aio.client.api.apps_v1_api import AppsV1Api
    from kubernetes.aio.client.api.authentication_api import AuthenticationApi
    from kubernetes.aio.client.api.authentication_v1_api import AuthenticationV1Api
    from kubernetes.aio.client.api.authorization_api import AuthorizationApi
    from kubernetes.aio.client.api.authorization_v1_api import AuthorizationV1Api
    from kubernetes.aio.client.api.autoscaling_api import AutoscalingApi
    from kubernetes.aio.client.api.autoscaling_v1_api import AutoscalingV1Api
    from kubernetes.aio.client.api.autoscaling_v2_api import AutoscalingV2Api
    from kubernetes.aio.client.api.batch_api import BatchApi
    from kubernetes.aio.client.api.batch_v1_api import BatchV1Api
    from kubernetes.aio.client.api.certificates_api import CertificatesApi
    from kubernetes.aio.client.api.certificates_v1_api import CertificatesV1Api
    from kubernetes.aio.client.api.certificates_v1alpha1_api import CertificatesV1alpha1Api
    from kubernetes.aio.client.api.certificates_v1beta1_api import CertificatesV1beta1Api
    from kubernetes.aio.client.api.coordination_api import CoordinationApi
    from kubernetes.aio.client.api.coordination_v1_api import CoordinationV1Api
    from kubernetes.aio.client.api.coordination_v1alpha2_api import CoordinationV1alpha2Api
    from kubernetes.aio.client.api.coordination_v1beta1_api import CoordinationV1beta1Api
    from kubernetes.aio.client.api.core_api import CoreApi
    from kubernetes.aio.client.api.core_v1_api import CoreV1Api
    from kubernetes.aio.client.api.custom_objects_api import CustomObjectsApi
    from kubernetes.aio.client.api.discovery_api import DiscoveryApi
    from kubernetes.aio.client.api.discovery_v1_api import DiscoveryV1Api
    from kubernetes.aio.client.api.events_api import EventsApi
    from kubernetes.aio.client.api.events_v1_api import EventsV1Api
    from kubernetes.aio.client.api.flowcontrol_apiserver_api import FlowcontrolApiserverApi
    from kubernetes.aio.client.api.flowcontrol_apiserver_v1_api import FlowcontrolApiserverV1Api
    from kubernetes.aio.client.api.internal_apiserver_api import InternalApiserverApi
    from kubernetes.aio.client.api.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api
    from kubernetes.aio.client.api.logs_api import LogsApi
    from kubernetes.aio.client.api.networking_api import NetworkingApi
    from kubernetes.aio.client.api.networking_v1_api import NetworkingV1Api
    from kubernetes.aio.client.api.networking_v1beta1_api import NetworkingV1beta1Api
    from kubernetes.aio.client.api.node_api import NodeApi
    from kubernetes.aio.client.api.node_v1_api import NodeV1Api
    from kubernetes.aio.client.api.openid_api import OpenidApi
    from kubernetes.aio.client.api.policy_api import PolicyApi
    from kubernetes.aio.client.api.policy_v1_api import PolicyV1Api
    from kubernetes.aio.client.api.rbac_authorization_api import RbacAuthorizationApi
    from kubernetes.aio.client.api.rbac_authorization_v1_api import RbacAuthorizationV1Api
    from kubernetes.aio.client.api.resource_api import ResourceApi
    from kubernetes.aio.client.api.resource_v1_api import ResourceV1Api
    from kubernetes.aio.client.api.resource_v1alpha3_api import ResourceV1alpha3Api
    from kubernetes.aio.client.api.resource_v1beta1_api import ResourceV1beta1Api
    from kubernetes.aio.client.api.resource_v1beta2_api import ResourceV1beta2Api
    from kubernetes.aio.client.api.scheduling_api import SchedulingApi
    from kubernetes.aio.client.api.scheduling_v1_api import SchedulingV1Api
    from kubernetes.aio.client.api.scheduling_v1alpha2_api import SchedulingV1alpha2Api
    from kubernetes.aio.client.api.storage_api import StorageApi
    from kubernetes.aio.client.api.storage_v1_api import StorageV1Api
    from kubernetes.aio.client.api.storage_v1beta1_api import StorageV1beta1Api
    from kubernetes.aio.client.api.storagemigration_api import StoragemigrationApi
    from kubernetes.aio.client.api.storagemigration_v1beta1_api import StoragemigrationV1beta1Api
    from kubernetes.aio.client.api.version_api import VersionApi

else:
    from importlib import import_module

    _exports = {
        "WellKnownApi": ".well_known_api",
        "AdmissionregistrationApi": ".admissionregistration_api",
        "AdmissionregistrationV1Api": ".admissionregistration_v1_api",
        "AdmissionregistrationV1alpha1Api": ".admissionregistration_v1alpha1_api",
        "AdmissionregistrationV1beta1Api": ".admissionregistration_v1beta1_api",
        "ApiextensionsApi": ".apiextensions_api",
        "ApiextensionsV1Api": ".apiextensions_v1_api",
        "ApiregistrationApi": ".apiregistration_api",
        "ApiregistrationV1Api": ".apiregistration_v1_api",
        "ApisApi": ".apis_api",
        "AppsApi": ".apps_api",
        "AppsV1Api": ".apps_v1_api",
        "AuthenticationApi": ".authentication_api",
        "AuthenticationV1Api": ".authentication_v1_api",
        "AuthorizationApi": ".authorization_api",
        "AuthorizationV1Api": ".authorization_v1_api",
        "AutoscalingApi": ".autoscaling_api",
        "AutoscalingV1Api": ".autoscaling_v1_api",
        "AutoscalingV2Api": ".autoscaling_v2_api",
        "BatchApi": ".batch_api",
        "BatchV1Api": ".batch_v1_api",
        "CertificatesApi": ".certificates_api",
        "CertificatesV1Api": ".certificates_v1_api",
        "CertificatesV1alpha1Api": ".certificates_v1alpha1_api",
        "CertificatesV1beta1Api": ".certificates_v1beta1_api",
        "CoordinationApi": ".coordination_api",
        "CoordinationV1Api": ".coordination_v1_api",
        "CoordinationV1alpha2Api": ".coordination_v1alpha2_api",
        "CoordinationV1beta1Api": ".coordination_v1beta1_api",
        "CoreApi": ".core_api",
        "CoreV1Api": ".core_v1_api",
        "CustomObjectsApi": ".custom_objects_api",
        "DiscoveryApi": ".discovery_api",
        "DiscoveryV1Api": ".discovery_v1_api",
        "EventsApi": ".events_api",
        "EventsV1Api": ".events_v1_api",
        "FlowcontrolApiserverApi": ".flowcontrol_apiserver_api",
        "FlowcontrolApiserverV1Api": ".flowcontrol_apiserver_v1_api",
        "InternalApiserverApi": ".internal_apiserver_api",
        "InternalApiserverV1alpha1Api": ".internal_apiserver_v1alpha1_api",
        "LogsApi": ".logs_api",
        "NetworkingApi": ".networking_api",
        "NetworkingV1Api": ".networking_v1_api",
        "NetworkingV1beta1Api": ".networking_v1beta1_api",
        "NodeApi": ".node_api",
        "NodeV1Api": ".node_v1_api",
        "OpenidApi": ".openid_api",
        "PolicyApi": ".policy_api",
        "PolicyV1Api": ".policy_v1_api",
        "RbacAuthorizationApi": ".rbac_authorization_api",
        "RbacAuthorizationV1Api": ".rbac_authorization_v1_api",
        "ResourceApi": ".resource_api",
        "ResourceV1Api": ".resource_v1_api",
        "ResourceV1alpha3Api": ".resource_v1alpha3_api",
        "ResourceV1beta1Api": ".resource_v1beta1_api",
        "ResourceV1beta2Api": ".resource_v1beta2_api",
        "SchedulingApi": ".scheduling_api",
        "SchedulingV1Api": ".scheduling_v1_api",
        "SchedulingV1alpha2Api": ".scheduling_v1alpha2_api",
        "StorageApi": ".storage_api",
        "StorageV1Api": ".storage_v1_api",
        "StorageV1beta1Api": ".storage_v1beta1_api",
        "StoragemigrationApi": ".storagemigration_api",
        "StoragemigrationV1beta1Api": ".storagemigration_v1beta1_api",
        "VersionApi": ".version_api",
    }

    def __getattr__(name: str) -> object:
        if (module_name := _exports.get(name)) is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(import_module(module_name, __name__), name)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(globals().keys() | _exports.keys())
