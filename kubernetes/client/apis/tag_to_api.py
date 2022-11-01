import typing_extensions

from kubernetes.client.apis.tags import TagValues
from kubernetes.client.apis.tags.well_known_api import WellKnownApi
from kubernetes.client.apis.tags.admissionregistration_api import AdmissionregistrationApi
from kubernetes.client.apis.tags.admissionregistration_v1_api import AdmissionregistrationV1Api
from kubernetes.client.apis.tags.apiextensions_api import ApiextensionsApi
from kubernetes.client.apis.tags.apiextensions_v1_api import ApiextensionsV1Api
from kubernetes.client.apis.tags.apiregistration_api import ApiregistrationApi
from kubernetes.client.apis.tags.apiregistration_v1_api import ApiregistrationV1Api
from kubernetes.client.apis.tags.apis_api import ApisApi
from kubernetes.client.apis.tags.apps_api import AppsApi
from kubernetes.client.apis.tags.apps_v1_api import AppsV1Api
from kubernetes.client.apis.tags.authentication_api import AuthenticationApi
from kubernetes.client.apis.tags.authentication_v1_api import AuthenticationV1Api
from kubernetes.client.apis.tags.authorization_api import AuthorizationApi
from kubernetes.client.apis.tags.authorization_v1_api import AuthorizationV1Api
from kubernetes.client.apis.tags.autoscaling_api import AutoscalingApi
from kubernetes.client.apis.tags.autoscaling_v1_api import AutoscalingV1Api
from kubernetes.client.apis.tags.autoscaling_v2_api import AutoscalingV2Api
from kubernetes.client.apis.tags.autoscaling_v2beta2_api import AutoscalingV2beta2Api
from kubernetes.client.apis.tags.batch_api import BatchApi
from kubernetes.client.apis.tags.batch_v1_api import BatchV1Api
from kubernetes.client.apis.tags.certificates_api import CertificatesApi
from kubernetes.client.apis.tags.certificates_v1_api import CertificatesV1Api
from kubernetes.client.apis.tags.coordination_api import CoordinationApi
from kubernetes.client.apis.tags.coordination_v1_api import CoordinationV1Api
from kubernetes.client.apis.tags.core_api import CoreApi
from kubernetes.client.apis.tags.core_v1_api import CoreV1Api
from kubernetes.client.apis.tags.custom_objects_api import CustomObjectsApi
from kubernetes.client.apis.tags.discovery_api import DiscoveryApi
from kubernetes.client.apis.tags.discovery_v1_api import DiscoveryV1Api
from kubernetes.client.apis.tags.events_api import EventsApi
from kubernetes.client.apis.tags.events_v1_api import EventsV1Api
from kubernetes.client.apis.tags.flowcontrol_apiserver_api import FlowcontrolApiserverApi
from kubernetes.client.apis.tags.flowcontrol_apiserver_v1beta1_api import FlowcontrolApiserverV1beta1Api
from kubernetes.client.apis.tags.flowcontrol_apiserver_v1beta2_api import FlowcontrolApiserverV1beta2Api
from kubernetes.client.apis.tags.internal_apiserver_api import InternalApiserverApi
from kubernetes.client.apis.tags.internal_apiserver_v1alpha1_api import InternalApiserverV1alpha1Api
from kubernetes.client.apis.tags.logs_api import LogsApi
from kubernetes.client.apis.tags.networking_api import NetworkingApi
from kubernetes.client.apis.tags.networking_v1_api import NetworkingV1Api
from kubernetes.client.apis.tags.networking_v1alpha1_api import NetworkingV1alpha1Api
from kubernetes.client.apis.tags.node_api import NodeApi
from kubernetes.client.apis.tags.node_v1_api import NodeV1Api
from kubernetes.client.apis.tags.openid_api import OpenidApi
from kubernetes.client.apis.tags.policy_api import PolicyApi
from kubernetes.client.apis.tags.policy_v1_api import PolicyV1Api
from kubernetes.client.apis.tags.rbac_authorization_api import RbacAuthorizationApi
from kubernetes.client.apis.tags.rbac_authorization_v1_api import RbacAuthorizationV1Api
from kubernetes.client.apis.tags.scheduling_api import SchedulingApi
from kubernetes.client.apis.tags.scheduling_v1_api import SchedulingV1Api
from kubernetes.client.apis.tags.storage_api import StorageApi
from kubernetes.client.apis.tags.storage_v1_api import StorageV1Api
from kubernetes.client.apis.tags.storage_v1beta1_api import StorageV1beta1Api
from kubernetes.client.apis.tags.version_api import VersionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WELL_KNOWN: WellKnownApi,
        TagValues.ADMISSIONREGISTRATION: AdmissionregistrationApi,
        TagValues.ADMISSIONREGISTRATION_V1: AdmissionregistrationV1Api,
        TagValues.APIEXTENSIONS: ApiextensionsApi,
        TagValues.APIEXTENSIONS_V1: ApiextensionsV1Api,
        TagValues.APIREGISTRATION: ApiregistrationApi,
        TagValues.APIREGISTRATION_V1: ApiregistrationV1Api,
        TagValues.APIS: ApisApi,
        TagValues.APPS: AppsApi,
        TagValues.APPS_V1: AppsV1Api,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.AUTHENTICATION_V1: AuthenticationV1Api,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.AUTHORIZATION_V1: AuthorizationV1Api,
        TagValues.AUTOSCALING: AutoscalingApi,
        TagValues.AUTOSCALING_V1: AutoscalingV1Api,
        TagValues.AUTOSCALING_V2: AutoscalingV2Api,
        TagValues.AUTOSCALING_V2BETA2: AutoscalingV2beta2Api,
        TagValues.BATCH: BatchApi,
        TagValues.BATCH_V1: BatchV1Api,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.CERTIFICATES_V1: CertificatesV1Api,
        TagValues.COORDINATION: CoordinationApi,
        TagValues.COORDINATION_V1: CoordinationV1Api,
        TagValues.CORE: CoreApi,
        TagValues.CORE_V1: CoreV1Api,
        TagValues.CUSTOM_OBJECTS: CustomObjectsApi,
        TagValues.DISCOVERY: DiscoveryApi,
        TagValues.DISCOVERY_V1: DiscoveryV1Api,
        TagValues.EVENTS: EventsApi,
        TagValues.EVENTS_V1: EventsV1Api,
        TagValues.FLOWCONTROL_APISERVER: FlowcontrolApiserverApi,
        TagValues.FLOWCONTROL_APISERVER_V1BETA1: FlowcontrolApiserverV1beta1Api,
        TagValues.FLOWCONTROL_APISERVER_V1BETA2: FlowcontrolApiserverV1beta2Api,
        TagValues.INTERNAL_APISERVER: InternalApiserverApi,
        TagValues.INTERNAL_APISERVER_V1ALPHA1: InternalApiserverV1alpha1Api,
        TagValues.LOGS: LogsApi,
        TagValues.NETWORKING: NetworkingApi,
        TagValues.NETWORKING_V1: NetworkingV1Api,
        TagValues.NETWORKING_V1ALPHA1: NetworkingV1alpha1Api,
        TagValues.NODE: NodeApi,
        TagValues.NODE_V1: NodeV1Api,
        TagValues.OPENID: OpenidApi,
        TagValues.POLICY: PolicyApi,
        TagValues.POLICY_V1: PolicyV1Api,
        TagValues.RBAC_AUTHORIZATION: RbacAuthorizationApi,
        TagValues.RBAC_AUTHORIZATION_V1: RbacAuthorizationV1Api,
        TagValues.SCHEDULING: SchedulingApi,
        TagValues.SCHEDULING_V1: SchedulingV1Api,
        TagValues.STORAGE: StorageApi,
        TagValues.STORAGE_V1: StorageV1Api,
        TagValues.STORAGE_V1BETA1: StorageV1beta1Api,
        TagValues.VERSION: VersionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WELL_KNOWN: WellKnownApi,
        TagValues.ADMISSIONREGISTRATION: AdmissionregistrationApi,
        TagValues.ADMISSIONREGISTRATION_V1: AdmissionregistrationV1Api,
        TagValues.APIEXTENSIONS: ApiextensionsApi,
        TagValues.APIEXTENSIONS_V1: ApiextensionsV1Api,
        TagValues.APIREGISTRATION: ApiregistrationApi,
        TagValues.APIREGISTRATION_V1: ApiregistrationV1Api,
        TagValues.APIS: ApisApi,
        TagValues.APPS: AppsApi,
        TagValues.APPS_V1: AppsV1Api,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.AUTHENTICATION_V1: AuthenticationV1Api,
        TagValues.AUTHORIZATION: AuthorizationApi,
        TagValues.AUTHORIZATION_V1: AuthorizationV1Api,
        TagValues.AUTOSCALING: AutoscalingApi,
        TagValues.AUTOSCALING_V1: AutoscalingV1Api,
        TagValues.AUTOSCALING_V2: AutoscalingV2Api,
        TagValues.AUTOSCALING_V2BETA2: AutoscalingV2beta2Api,
        TagValues.BATCH: BatchApi,
        TagValues.BATCH_V1: BatchV1Api,
        TagValues.CERTIFICATES: CertificatesApi,
        TagValues.CERTIFICATES_V1: CertificatesV1Api,
        TagValues.COORDINATION: CoordinationApi,
        TagValues.COORDINATION_V1: CoordinationV1Api,
        TagValues.CORE: CoreApi,
        TagValues.CORE_V1: CoreV1Api,
        TagValues.CUSTOM_OBJECTS: CustomObjectsApi,
        TagValues.DISCOVERY: DiscoveryApi,
        TagValues.DISCOVERY_V1: DiscoveryV1Api,
        TagValues.EVENTS: EventsApi,
        TagValues.EVENTS_V1: EventsV1Api,
        TagValues.FLOWCONTROL_APISERVER: FlowcontrolApiserverApi,
        TagValues.FLOWCONTROL_APISERVER_V1BETA1: FlowcontrolApiserverV1beta1Api,
        TagValues.FLOWCONTROL_APISERVER_V1BETA2: FlowcontrolApiserverV1beta2Api,
        TagValues.INTERNAL_APISERVER: InternalApiserverApi,
        TagValues.INTERNAL_APISERVER_V1ALPHA1: InternalApiserverV1alpha1Api,
        TagValues.LOGS: LogsApi,
        TagValues.NETWORKING: NetworkingApi,
        TagValues.NETWORKING_V1: NetworkingV1Api,
        TagValues.NETWORKING_V1ALPHA1: NetworkingV1alpha1Api,
        TagValues.NODE: NodeApi,
        TagValues.NODE_V1: NodeV1Api,
        TagValues.OPENID: OpenidApi,
        TagValues.POLICY: PolicyApi,
        TagValues.POLICY_V1: PolicyV1Api,
        TagValues.RBAC_AUTHORIZATION: RbacAuthorizationApi,
        TagValues.RBAC_AUTHORIZATION_V1: RbacAuthorizationV1Api,
        TagValues.SCHEDULING: SchedulingApi,
        TagValues.SCHEDULING_V1: SchedulingV1Api,
        TagValues.STORAGE: StorageApi,
        TagValues.STORAGE_V1: StorageV1Api,
        TagValues.STORAGE_V1BETA1: StorageV1beta1Api,
        TagValues.VERSION: VersionApi,
    }
)
