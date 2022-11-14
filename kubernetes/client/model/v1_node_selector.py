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


class V1NodeSelector(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.
    """


    class MetaOapg:
        required = {
            "nodeSelectorTerms",
        }
        
        class properties:
            
            
            class nodeSelectorTerms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['V1NodeSelectorTerm']:
                        return V1NodeSelectorTerm
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['V1NodeSelectorTerm'], typing.List['V1NodeSelectorTerm']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nodeSelectorTerms':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'V1NodeSelectorTerm':
                    return super().__getitem__(i)
            __annotations__ = {
                "nodeSelectorTerms": nodeSelectorTerms,
            }
    
    nodeSelectorTerms: MetaOapg.properties.nodeSelectorTerms
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeSelectorTerms"]) -> MetaOapg.properties.nodeSelectorTerms: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nodeSelectorTerms", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeSelectorTerms"]) -> MetaOapg.properties.nodeSelectorTerms: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nodeSelectorTerms", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        nodeSelectorTerms: typing.Union[MetaOapg.properties.nodeSelectorTerms, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'V1NodeSelector':
        return super().__new__(
            cls,
            *args,
            nodeSelectorTerms=nodeSelectorTerms,
            _configuration=_configuration,
            **kwargs,
        )

from kubernetes.client.model.v1_node_selector_term import V1NodeSelectorTerm