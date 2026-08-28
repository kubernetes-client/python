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
    "LifecycleApi",
    "LifecycleV1alpha1Api",
    "LogsApi",
    "NetworkingApi",
    "NetworkingV1Api",
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
    "SchedulingV1alpha3Api",
    "SchedulingV1beta1Api",
    "StorageApi",
    "StorageV1Api",
    "StoragemigrationApi",
    "StoragemigrationV1Api",
    "StoragemigrationV1beta1Api",
    "VersionApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from kubernetes.client.api.well_known_api import WellKnownApi
    from kubernetes.client.api.admissionregistration_api import AdmissionregistrationApi
    from kubernetes.client.api.admissionregistration_v1_api import AdmissionregistrationV1Api
    from kubernetes.client.api.admissionregistration_v1alpha1_api import AdmissionregistrationV1alpha1Api
    from kubernetes.client.api.admissionregistration_v1beta1_api import AdmissionregistrationV1beta1Api
    from kubernetes.client.api.apiextensions_api import ApiextensionsApi
    from kubernetes.client.api.apiextensions_v1_api import ApiextensionsV1Api
    from kubernetes.client.api.apiregistration_api import ApiregistrationApi
    from kubernetes.client.api.apiregistration_v1_api import ApiregistrationV1Api
    from kubernetes.client.api.apis_api import ApisApi
    from kubernetes.client.api.apps_api import AppsApi
    from kubernetes.client.api.apps_v1_api import AppsV1Api
    from kubernetes.client.api.authentication_api import AuthenticationApi
    from kubernetes.client.api.authentication_v1_api import AuthenticationV1Api
    from kubernetes.client.api.authorization_api import AuthorizationApi
    from kubernetes.client.api.authorization_v1_api import AuthorizationV1Api
    from kubernetes.client.api.autoscaling_api import AutoscalingApi
    from kubernetes.client.api.autoscaling_v1_api import AutoscalingV1Api
    from kubernetes.client.api.autoscaling_v2_api import AutoscalingV2Api
    from kubernetes.client.api.batch_api import BatchApi
    from kubernetes.client.api.batch_v1_api import BatchV1Api
    from kubernetes.client.api.certificates_api import CertificatesApi
    from kubernetes.client.api.certificates_v1_api import CertificatesV1Api
    from kubernetes.client.api.certificates_v1beta1_api import CertificatesV1beta1Api
    from kubernetes.client.api.coordination_api import CoordinationApi
    from kubernetes.client.api.coordination_v1_api import CoordinationV1Api
    from kubernetes.client.api.coordination_v1alpha2_api import CoordinationV1alpha2Api
    from kubernetes.client.api.coordination_v1beta1_api import CoordinationV1beta1Api
    from kubernetes.client.api.core_api import CoreApi
    from kubernetes.client.api.core_v1_api import CoreV1Api
    from kubernetes.client.api.custom_objects_api import CustomObjectsApi
    from kubernetes.client.api.discovery_api import DiscoveryApi
    from kubernetes.client.api.discovery_v1_api import DiscoveryV1Api
    from kubernetes.client.api.events_api import EventsApi
    from kubernetes.client.api.events_v1_api import EventsV1Api
    from kubernetes.client.api.flowcontrol_apiserver_api import FlowcontrolApiserverApi
    from kubernetes.client.api.flowcontrol_apiserver_v1_api import FlowcontrolApiserverV1Api
    from kubernetes.client.api.internal_apiserver_api import InternalApiserverApi
    from kubernetes.client.api.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api
    from kubernetes.client.api.lifecycle_api import LifecycleApi
    from kubernetes.client.api.lifecycle_v1alpha1_api import LifecycleV1alpha1Api
    from kubernetes.client.api.logs_api import LogsApi
    from kubernetes.client.api.networking_api import NetworkingApi
    from kubernetes.client.api.networking_v1_api import NetworkingV1Api
    from kubernetes.client.api.node_api import NodeApi
    from kubernetes.client.api.node_v1_api import NodeV1Api
    from kubernetes.client.api.openid_api import OpenidApi
    from kubernetes.client.api.policy_api import PolicyApi
    from kubernetes.client.api.policy_v1_api import PolicyV1Api
    from kubernetes.client.api.rbac_authorization_api import RbacAuthorizationApi
    from kubernetes.client.api.rbac_authorization_v1_api import RbacAuthorizationV1Api
    from kubernetes.client.api.resource_api import ResourceApi
    from kubernetes.client.api.resource_v1_api import ResourceV1Api
    from kubernetes.client.api.resource_v1alpha3_api import ResourceV1alpha3Api
    from kubernetes.client.api.resource_v1beta1_api import ResourceV1beta1Api
    from kubernetes.client.api.resource_v1beta2_api import ResourceV1beta2Api
    from kubernetes.client.api.scheduling_api import SchedulingApi
    from kubernetes.client.api.scheduling_v1_api import SchedulingV1Api
    from kubernetes.client.api.scheduling_v1alpha3_api import SchedulingV1alpha3Api
    from kubernetes.client.api.scheduling_v1beta1_api import SchedulingV1beta1Api
    from kubernetes.client.api.storage_api import StorageApi
    from kubernetes.client.api.storage_v1_api import StorageV1Api
    from kubernetes.client.api.storagemigration_api import StoragemigrationApi
    from kubernetes.client.api.storagemigration_v1_api import StoragemigrationV1Api
    from kubernetes.client.api.storagemigration_v1beta1_api import StoragemigrationV1beta1Api
    from kubernetes.client.api.version_api import VersionApi

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
        "LifecycleApi": ".lifecycle_api",
        "LifecycleV1alpha1Api": ".lifecycle_v1alpha1_api",
        "LogsApi": ".logs_api",
        "NetworkingApi": ".networking_api",
        "NetworkingV1Api": ".networking_v1_api",
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
        "SchedulingV1alpha3Api": ".scheduling_v1alpha3_api",
        "SchedulingV1beta1Api": ".scheduling_v1beta1_api",
        "StorageApi": ".storage_api",
        "StorageV1Api": ".storage_v1_api",
        "StoragemigrationApi": ".storagemigration_api",
        "StoragemigrationV1Api": ".storagemigration_v1_api",
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
