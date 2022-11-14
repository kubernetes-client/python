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

from kubernetes.client import schemas  # noqa: F401


class StorageV1TokenRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    TokenRequest contains parameters of a service account token.
    """


    class MetaOapg:
        required = {
            "audience",
        }
        
        class properties:
            audience = schemas.StrSchema
            expirationSeconds = schemas.Int64Schema
            __annotations__ = {
                "audience": audience,
                "expirationSeconds": expirationSeconds,
            }
    
    audience: MetaOapg.properties.audience
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience"]) -> MetaOapg.properties.audience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationSeconds"]) -> MetaOapg.properties.expirationSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["audience", "expirationSeconds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience"]) -> MetaOapg.properties.audience: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationSeconds"]) -> typing.Union[MetaOapg.properties.expirationSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["audience", "expirationSeconds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        audience: typing.Union[MetaOapg.properties.audience, str, ],
        expirationSeconds: typing.Union[MetaOapg.properties.expirationSeconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StorageV1TokenRequest':
        return super().__new__(
            cls,
            *args,
            audience=audience,
            expirationSeconds=expirationSeconds,
            _configuration=_configuration,
            **kwargs,
        )