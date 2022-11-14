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


class V1CSIStorageCapacity(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment.  This can be used when considering where to instantiate new PersistentVolumes.

For example this can express things like: - StorageClass "standard" has "1234 GiB" available in "topology.kubernetes.io/zone=us-east1" - StorageClass "localssd" has "10 GiB" available in "kubernetes.io/hostname=knode-abc123"

The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero

The producer of these objects can decide which approach is more suitable.

They are consumed by the kube-scheduler when a CSI driver opts into capacity-aware scheduling with CSIDriverSpec.StorageCapacity. The scheduler compares the MaximumVolumeSize against the requested size of pending volumes to filter out unsuitable nodes. If MaximumVolumeSize is unset, it falls back to a comparison against the less precise Capacity. If that is also unset, the scheduler assumes that capacity is insufficient and tries some other node.
    """


    class MetaOapg:
        required = {
            "storageClassName",
        }
        
        class properties:
            storageClassName = schemas.StrSchema
            apiVersion = schemas.StrSchema
            capacity = schemas.StrSchema
            kind = schemas.StrSchema
            maximumVolumeSize = schemas.StrSchema
        
            @staticmethod
            def metadata() -> typing.Type['V1ObjectMeta']:
                return V1ObjectMeta
        
            @staticmethod
            def nodeTopology() -> typing.Type['V1LabelSelector']:
                return V1LabelSelector
            __annotations__ = {
                "storageClassName": storageClassName,
                "apiVersion": apiVersion,
                "capacity": capacity,
                "kind": kind,
                "maximumVolumeSize": maximumVolumeSize,
                "metadata": metadata,
                "nodeTopology": nodeTopology,
            }
    
    storageClassName: MetaOapg.properties.storageClassName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageClassName"]) -> MetaOapg.properties.storageClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiVersion"]) -> MetaOapg.properties.apiVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kind"]) -> MetaOapg.properties.kind: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumVolumeSize"]) -> MetaOapg.properties.maximumVolumeSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'V1ObjectMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeTopology"]) -> 'V1LabelSelector': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["storageClassName", "apiVersion", "capacity", "kind", "maximumVolumeSize", "metadata", "nodeTopology", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageClassName"]) -> MetaOapg.properties.storageClassName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiVersion"]) -> typing.Union[MetaOapg.properties.apiVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> typing.Union[MetaOapg.properties.capacity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kind"]) -> typing.Union[MetaOapg.properties.kind, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumVolumeSize"]) -> typing.Union[MetaOapg.properties.maximumVolumeSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['V1ObjectMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeTopology"]) -> typing.Union['V1LabelSelector', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["storageClassName", "apiVersion", "capacity", "kind", "maximumVolumeSize", "metadata", "nodeTopology", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        storageClassName: typing.Union[MetaOapg.properties.storageClassName, str, ],
        apiVersion: typing.Union[MetaOapg.properties.apiVersion, str, schemas.Unset] = schemas.unset,
        capacity: typing.Union[MetaOapg.properties.capacity, str, schemas.Unset] = schemas.unset,
        kind: typing.Union[MetaOapg.properties.kind, str, schemas.Unset] = schemas.unset,
        maximumVolumeSize: typing.Union[MetaOapg.properties.maximumVolumeSize, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['V1ObjectMeta', schemas.Unset] = schemas.unset,
        nodeTopology: typing.Union['V1LabelSelector', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1CSIStorageCapacity':
        return super().__new__(
            cls,
            *args,
            storageClassName=storageClassName,
            apiVersion=apiVersion,
            capacity=capacity,
            kind=kind,
            maximumVolumeSize=maximumVolumeSize,
            metadata=metadata,
            nodeTopology=nodeTopology,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_label_selector import V1LabelSelector
from client.model.v1_object_meta import V1ObjectMeta