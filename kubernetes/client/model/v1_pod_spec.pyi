# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.25
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from client import schemas  # noqa: F401


class V1PodSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    PodSpec is a description of a pod.
    """


    class MetaOapg:
        required = {
            "containers",
        }
        
        class properties:
            
            
            class containers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Container']:
                        return V1Container
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Container'], typing.List['V1Container']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'containers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Container':
                    return super().__getitem__(i)
            activeDeadlineSeconds = schemas.Int64Schema
        
            @staticmethod
            def affinity() -> typing.Type['V1Affinity']:
                return V1Affinity
            automountServiceAccountToken = schemas.BoolSchema
        
            @staticmethod
            def dnsConfig() -> typing.Type['V1PodDNSConfig']:
                return V1PodDNSConfig
            dnsPolicy = schemas.StrSchema
            enableServiceLinks = schemas.BoolSchema
            
            
            class ephemeralContainers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1EphemeralContainer']:
                        return V1EphemeralContainer
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1EphemeralContainer'], typing.List['V1EphemeralContainer']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ephemeralContainers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1EphemeralContainer':
                    return super().__getitem__(i)
            
            
            class hostAliases(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1HostAlias']:
                        return V1HostAlias
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1HostAlias'], typing.List['V1HostAlias']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hostAliases':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1HostAlias':
                    return super().__getitem__(i)
            hostIPC = schemas.BoolSchema
            hostNetwork = schemas.BoolSchema
            hostPID = schemas.BoolSchema
            hostUsers = schemas.BoolSchema
            hostname = schemas.StrSchema
            
            
            class imagePullSecrets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1LocalObjectReference']:
                        return V1LocalObjectReference
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1LocalObjectReference'], typing.List['V1LocalObjectReference']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'imagePullSecrets':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1LocalObjectReference':
                    return super().__getitem__(i)
            
            
            class initContainers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Container']:
                        return V1Container
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Container'], typing.List['V1Container']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'initContainers':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Container':
                    return super().__getitem__(i)
            nodeName = schemas.StrSchema
            
            
            class nodeSelector(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'nodeSelector':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def os() -> typing.Type['V1PodOS']:
                return V1PodOS
            
            
            class overhead(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'overhead':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            preemptionPolicy = schemas.StrSchema
            priority = schemas.Int32Schema
            priorityClassName = schemas.StrSchema
            
            
            class readinessGates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1PodReadinessGate']:
                        return V1PodReadinessGate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1PodReadinessGate'], typing.List['V1PodReadinessGate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'readinessGates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1PodReadinessGate':
                    return super().__getitem__(i)
            restartPolicy = schemas.StrSchema
            runtimeClassName = schemas.StrSchema
            schedulerName = schemas.StrSchema
        
            @staticmethod
            def securityContext() -> typing.Type['V1PodSecurityContext']:
                return V1PodSecurityContext
            serviceAccount = schemas.StrSchema
            serviceAccountName = schemas.StrSchema
            setHostnameAsFQDN = schemas.BoolSchema
            shareProcessNamespace = schemas.BoolSchema
            subdomain = schemas.StrSchema
            terminationGracePeriodSeconds = schemas.Int64Schema
            
            
            class tolerations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Toleration']:
                        return V1Toleration
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Toleration'], typing.List['V1Toleration']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tolerations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Toleration':
                    return super().__getitem__(i)
            
            
            class topologySpreadConstraints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1TopologySpreadConstraint']:
                        return V1TopologySpreadConstraint
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1TopologySpreadConstraint'], typing.List['V1TopologySpreadConstraint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'topologySpreadConstraints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1TopologySpreadConstraint':
                    return super().__getitem__(i)
            
            
            class volumes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1Volume']:
                        return V1Volume
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1Volume'], typing.List['V1Volume']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'volumes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1Volume':
                    return super().__getitem__(i)
            __annotations__ = {
                "containers": containers,
                "activeDeadlineSeconds": activeDeadlineSeconds,
                "affinity": affinity,
                "automountServiceAccountToken": automountServiceAccountToken,
                "dnsConfig": dnsConfig,
                "dnsPolicy": dnsPolicy,
                "enableServiceLinks": enableServiceLinks,
                "ephemeralContainers": ephemeralContainers,
                "hostAliases": hostAliases,
                "hostIPC": hostIPC,
                "hostNetwork": hostNetwork,
                "hostPID": hostPID,
                "hostUsers": hostUsers,
                "hostname": hostname,
                "imagePullSecrets": imagePullSecrets,
                "initContainers": initContainers,
                "nodeName": nodeName,
                "nodeSelector": nodeSelector,
                "os": os,
                "overhead": overhead,
                "preemptionPolicy": preemptionPolicy,
                "priority": priority,
                "priorityClassName": priorityClassName,
                "readinessGates": readinessGates,
                "restartPolicy": restartPolicy,
                "runtimeClassName": runtimeClassName,
                "schedulerName": schedulerName,
                "securityContext": securityContext,
                "serviceAccount": serviceAccount,
                "serviceAccountName": serviceAccountName,
                "setHostnameAsFQDN": setHostnameAsFQDN,
                "shareProcessNamespace": shareProcessNamespace,
                "subdomain": subdomain,
                "terminationGracePeriodSeconds": terminationGracePeriodSeconds,
                "tolerations": tolerations,
                "topologySpreadConstraints": topologySpreadConstraints,
                "volumes": volumes,
            }
    
    containers: MetaOapg.properties.containers
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containers"]) -> MetaOapg.properties.containers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeDeadlineSeconds"]) -> MetaOapg.properties.activeDeadlineSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["affinity"]) -> 'V1Affinity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["automountServiceAccountToken"]) -> MetaOapg.properties.automountServiceAccountToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dnsConfig"]) -> 'V1PodDNSConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dnsPolicy"]) -> MetaOapg.properties.dnsPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableServiceLinks"]) -> MetaOapg.properties.enableServiceLinks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ephemeralContainers"]) -> MetaOapg.properties.ephemeralContainers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostAliases"]) -> MetaOapg.properties.hostAliases: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostIPC"]) -> MetaOapg.properties.hostIPC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostNetwork"]) -> MetaOapg.properties.hostNetwork: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostPID"]) -> MetaOapg.properties.hostPID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostUsers"]) -> MetaOapg.properties.hostUsers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imagePullSecrets"]) -> MetaOapg.properties.imagePullSecrets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initContainers"]) -> MetaOapg.properties.initContainers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeName"]) -> MetaOapg.properties.nodeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeSelector"]) -> MetaOapg.properties.nodeSelector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os"]) -> 'V1PodOS': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overhead"]) -> MetaOapg.properties.overhead: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preemptionPolicy"]) -> MetaOapg.properties.preemptionPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priorityClassName"]) -> MetaOapg.properties.priorityClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readinessGates"]) -> MetaOapg.properties.readinessGates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restartPolicy"]) -> MetaOapg.properties.restartPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runtimeClassName"]) -> MetaOapg.properties.runtimeClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedulerName"]) -> MetaOapg.properties.schedulerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securityContext"]) -> 'V1PodSecurityContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceAccount"]) -> MetaOapg.properties.serviceAccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceAccountName"]) -> MetaOapg.properties.serviceAccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setHostnameAsFQDN"]) -> MetaOapg.properties.setHostnameAsFQDN: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shareProcessNamespace"]) -> MetaOapg.properties.shareProcessNamespace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subdomain"]) -> MetaOapg.properties.subdomain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminationGracePeriodSeconds"]) -> MetaOapg.properties.terminationGracePeriodSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tolerations"]) -> MetaOapg.properties.tolerations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topologySpreadConstraints"]) -> MetaOapg.properties.topologySpreadConstraints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["volumes"]) -> MetaOapg.properties.volumes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["containers", "activeDeadlineSeconds", "affinity", "automountServiceAccountToken", "dnsConfig", "dnsPolicy", "enableServiceLinks", "ephemeralContainers", "hostAliases", "hostIPC", "hostNetwork", "hostPID", "hostUsers", "hostname", "imagePullSecrets", "initContainers", "nodeName", "nodeSelector", "os", "overhead", "preemptionPolicy", "priority", "priorityClassName", "readinessGates", "restartPolicy", "runtimeClassName", "schedulerName", "securityContext", "serviceAccount", "serviceAccountName", "setHostnameAsFQDN", "shareProcessNamespace", "subdomain", "terminationGracePeriodSeconds", "tolerations", "topologySpreadConstraints", "volumes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containers"]) -> MetaOapg.properties.containers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeDeadlineSeconds"]) -> typing.Union[MetaOapg.properties.activeDeadlineSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["affinity"]) -> typing.Union['V1Affinity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["automountServiceAccountToken"]) -> typing.Union[MetaOapg.properties.automountServiceAccountToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dnsConfig"]) -> typing.Union['V1PodDNSConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dnsPolicy"]) -> typing.Union[MetaOapg.properties.dnsPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableServiceLinks"]) -> typing.Union[MetaOapg.properties.enableServiceLinks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ephemeralContainers"]) -> typing.Union[MetaOapg.properties.ephemeralContainers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostAliases"]) -> typing.Union[MetaOapg.properties.hostAliases, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostIPC"]) -> typing.Union[MetaOapg.properties.hostIPC, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostNetwork"]) -> typing.Union[MetaOapg.properties.hostNetwork, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostPID"]) -> typing.Union[MetaOapg.properties.hostPID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostUsers"]) -> typing.Union[MetaOapg.properties.hostUsers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imagePullSecrets"]) -> typing.Union[MetaOapg.properties.imagePullSecrets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initContainers"]) -> typing.Union[MetaOapg.properties.initContainers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeName"]) -> typing.Union[MetaOapg.properties.nodeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeSelector"]) -> typing.Union[MetaOapg.properties.nodeSelector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> typing.Union['V1PodOS', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overhead"]) -> typing.Union[MetaOapg.properties.overhead, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preemptionPolicy"]) -> typing.Union[MetaOapg.properties.preemptionPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priorityClassName"]) -> typing.Union[MetaOapg.properties.priorityClassName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readinessGates"]) -> typing.Union[MetaOapg.properties.readinessGates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restartPolicy"]) -> typing.Union[MetaOapg.properties.restartPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runtimeClassName"]) -> typing.Union[MetaOapg.properties.runtimeClassName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedulerName"]) -> typing.Union[MetaOapg.properties.schedulerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securityContext"]) -> typing.Union['V1PodSecurityContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceAccount"]) -> typing.Union[MetaOapg.properties.serviceAccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceAccountName"]) -> typing.Union[MetaOapg.properties.serviceAccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setHostnameAsFQDN"]) -> typing.Union[MetaOapg.properties.setHostnameAsFQDN, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shareProcessNamespace"]) -> typing.Union[MetaOapg.properties.shareProcessNamespace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subdomain"]) -> typing.Union[MetaOapg.properties.subdomain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminationGracePeriodSeconds"]) -> typing.Union[MetaOapg.properties.terminationGracePeriodSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tolerations"]) -> typing.Union[MetaOapg.properties.tolerations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topologySpreadConstraints"]) -> typing.Union[MetaOapg.properties.topologySpreadConstraints, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["volumes"]) -> typing.Union[MetaOapg.properties.volumes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["containers", "activeDeadlineSeconds", "affinity", "automountServiceAccountToken", "dnsConfig", "dnsPolicy", "enableServiceLinks", "ephemeralContainers", "hostAliases", "hostIPC", "hostNetwork", "hostPID", "hostUsers", "hostname", "imagePullSecrets", "initContainers", "nodeName", "nodeSelector", "os", "overhead", "preemptionPolicy", "priority", "priorityClassName", "readinessGates", "restartPolicy", "runtimeClassName", "schedulerName", "securityContext", "serviceAccount", "serviceAccountName", "setHostnameAsFQDN", "shareProcessNamespace", "subdomain", "terminationGracePeriodSeconds", "tolerations", "topologySpreadConstraints", "volumes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        containers: typing.Union[MetaOapg.properties.containers, list, tuple, ],
        activeDeadlineSeconds: typing.Union[MetaOapg.properties.activeDeadlineSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        affinity: typing.Union['V1Affinity', schemas.Unset] = schemas.unset,
        automountServiceAccountToken: typing.Union[MetaOapg.properties.automountServiceAccountToken, bool, schemas.Unset] = schemas.unset,
        dnsConfig: typing.Union['V1PodDNSConfig', schemas.Unset] = schemas.unset,
        dnsPolicy: typing.Union[MetaOapg.properties.dnsPolicy, str, schemas.Unset] = schemas.unset,
        enableServiceLinks: typing.Union[MetaOapg.properties.enableServiceLinks, bool, schemas.Unset] = schemas.unset,
        ephemeralContainers: typing.Union[MetaOapg.properties.ephemeralContainers, list, tuple, schemas.Unset] = schemas.unset,
        hostAliases: typing.Union[MetaOapg.properties.hostAliases, list, tuple, schemas.Unset] = schemas.unset,
        hostIPC: typing.Union[MetaOapg.properties.hostIPC, bool, schemas.Unset] = schemas.unset,
        hostNetwork: typing.Union[MetaOapg.properties.hostNetwork, bool, schemas.Unset] = schemas.unset,
        hostPID: typing.Union[MetaOapg.properties.hostPID, bool, schemas.Unset] = schemas.unset,
        hostUsers: typing.Union[MetaOapg.properties.hostUsers, bool, schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
        imagePullSecrets: typing.Union[MetaOapg.properties.imagePullSecrets, list, tuple, schemas.Unset] = schemas.unset,
        initContainers: typing.Union[MetaOapg.properties.initContainers, list, tuple, schemas.Unset] = schemas.unset,
        nodeName: typing.Union[MetaOapg.properties.nodeName, str, schemas.Unset] = schemas.unset,
        nodeSelector: typing.Union[MetaOapg.properties.nodeSelector, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        os: typing.Union['V1PodOS', schemas.Unset] = schemas.unset,
        overhead: typing.Union[MetaOapg.properties.overhead, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        preemptionPolicy: typing.Union[MetaOapg.properties.preemptionPolicy, str, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        priorityClassName: typing.Union[MetaOapg.properties.priorityClassName, str, schemas.Unset] = schemas.unset,
        readinessGates: typing.Union[MetaOapg.properties.readinessGates, list, tuple, schemas.Unset] = schemas.unset,
        restartPolicy: typing.Union[MetaOapg.properties.restartPolicy, str, schemas.Unset] = schemas.unset,
        runtimeClassName: typing.Union[MetaOapg.properties.runtimeClassName, str, schemas.Unset] = schemas.unset,
        schedulerName: typing.Union[MetaOapg.properties.schedulerName, str, schemas.Unset] = schemas.unset,
        securityContext: typing.Union['V1PodSecurityContext', schemas.Unset] = schemas.unset,
        serviceAccount: typing.Union[MetaOapg.properties.serviceAccount, str, schemas.Unset] = schemas.unset,
        serviceAccountName: typing.Union[MetaOapg.properties.serviceAccountName, str, schemas.Unset] = schemas.unset,
        setHostnameAsFQDN: typing.Union[MetaOapg.properties.setHostnameAsFQDN, bool, schemas.Unset] = schemas.unset,
        shareProcessNamespace: typing.Union[MetaOapg.properties.shareProcessNamespace, bool, schemas.Unset] = schemas.unset,
        subdomain: typing.Union[MetaOapg.properties.subdomain, str, schemas.Unset] = schemas.unset,
        terminationGracePeriodSeconds: typing.Union[MetaOapg.properties.terminationGracePeriodSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tolerations: typing.Union[MetaOapg.properties.tolerations, list, tuple, schemas.Unset] = schemas.unset,
        topologySpreadConstraints: typing.Union[MetaOapg.properties.topologySpreadConstraints, list, tuple, schemas.Unset] = schemas.unset,
        volumes: typing.Union[MetaOapg.properties.volumes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1PodSpec':
        return super().__new__(
            cls,
            *args,
            containers=containers,
            activeDeadlineSeconds=activeDeadlineSeconds,
            affinity=affinity,
            automountServiceAccountToken=automountServiceAccountToken,
            dnsConfig=dnsConfig,
            dnsPolicy=dnsPolicy,
            enableServiceLinks=enableServiceLinks,
            ephemeralContainers=ephemeralContainers,
            hostAliases=hostAliases,
            hostIPC=hostIPC,
            hostNetwork=hostNetwork,
            hostPID=hostPID,
            hostUsers=hostUsers,
            hostname=hostname,
            imagePullSecrets=imagePullSecrets,
            initContainers=initContainers,
            nodeName=nodeName,
            nodeSelector=nodeSelector,
            os=os,
            overhead=overhead,
            preemptionPolicy=preemptionPolicy,
            priority=priority,
            priorityClassName=priorityClassName,
            readinessGates=readinessGates,
            restartPolicy=restartPolicy,
            runtimeClassName=runtimeClassName,
            schedulerName=schedulerName,
            securityContext=securityContext,
            serviceAccount=serviceAccount,
            serviceAccountName=serviceAccountName,
            setHostnameAsFQDN=setHostnameAsFQDN,
            shareProcessNamespace=shareProcessNamespace,
            subdomain=subdomain,
            terminationGracePeriodSeconds=terminationGracePeriodSeconds,
            tolerations=tolerations,
            topologySpreadConstraints=topologySpreadConstraints,
            volumes=volumes,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_affinity import V1Affinity
from client.model.v1_container import V1Container
from client.model.v1_ephemeral_container import V1EphemeralContainer
from client.model.v1_host_alias import V1HostAlias
from client.model.v1_local_object_reference import V1LocalObjectReference
from client.model.v1_pod_dns_config import V1PodDNSConfig
from client.model.v1_pod_os import V1PodOS
from client.model.v1_pod_readiness_gate import V1PodReadinessGate
from client.model.v1_pod_security_context import V1PodSecurityContext
from client.model.v1_toleration import V1Toleration
from client.model.v1_topology_spread_constraint import V1TopologySpreadConstraint
from client.model.v1_volume import V1Volume