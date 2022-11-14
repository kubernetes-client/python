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


class V1SubjectRulesReviewStatus(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.
    """


    class MetaOapg:
        required = {
            "incomplete",
            "nonResourceRules",
            "resourceRules",
        }
        
        class properties:
            incomplete = schemas.BoolSchema
            
            
            class nonResourceRules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NonResourceRule']:
                        return V1NonResourceRule
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NonResourceRule'], typing.List['V1NonResourceRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nonResourceRules':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NonResourceRule':
                    return super().__getitem__(i)
            
            
            class resourceRules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1ResourceRule']:
                        return V1ResourceRule
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1ResourceRule'], typing.List['V1ResourceRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'resourceRules':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1ResourceRule':
                    return super().__getitem__(i)
            evaluationError = schemas.StrSchema
            __annotations__ = {
                "incomplete": incomplete,
                "nonResourceRules": nonResourceRules,
                "resourceRules": resourceRules,
                "evaluationError": evaluationError,
            }
    
    incomplete: MetaOapg.properties.incomplete
    nonResourceRules: MetaOapg.properties.nonResourceRules
    resourceRules: MetaOapg.properties.resourceRules
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["incomplete"]) -> MetaOapg.properties.incomplete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonResourceRules"]) -> MetaOapg.properties.nonResourceRules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceRules"]) -> MetaOapg.properties.resourceRules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluationError"]) -> MetaOapg.properties.evaluationError: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["incomplete", "nonResourceRules", "resourceRules", "evaluationError", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["incomplete"]) -> MetaOapg.properties.incomplete: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonResourceRules"]) -> MetaOapg.properties.nonResourceRules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceRules"]) -> MetaOapg.properties.resourceRules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluationError"]) -> typing.Union[MetaOapg.properties.evaluationError, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["incomplete", "nonResourceRules", "resourceRules", "evaluationError", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        incomplete: typing.Union[MetaOapg.properties.incomplete, bool, ],
        nonResourceRules: typing.Union[MetaOapg.properties.nonResourceRules, list, tuple, ],
        resourceRules: typing.Union[MetaOapg.properties.resourceRules, list, tuple, ],
        evaluationError: typing.Union[MetaOapg.properties.evaluationError, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1SubjectRulesReviewStatus':
        return super().__new__(
            cls,
            *args,
            incomplete=incomplete,
            nonResourceRules=nonResourceRules,
            resourceRules=resourceRules,
            evaluationError=evaluationError,
            _configuration=_configuration,
            **kwargs,
        )

from client.model.v1_non_resource_rule import V1NonResourceRule
from client.model.v1_resource_rule import V1ResourceRule