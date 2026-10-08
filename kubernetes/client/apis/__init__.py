from __future__ import absolute_import
from importlib import import_module as _import_module
from types import ModuleType as _ModuleType
import warnings

# flake8: noqa

# alias kubernetes.client.api package and print deprecation warning
from kubernetes.client.api import *

warnings.filterwarnings('default', module='kubernetes.client.apis')
warnings.warn(
    "The package kubernetes.client.apis is renamed and deprecated, use kubernetes.client.api instead (please note that the trailing s was removed).",
    DeprecationWarning
)


def __getattr__(name: str) -> _ModuleType:
    # kubernetes.client.api imports its submodules lazily, so the star import
    # above no longer brings in module names such as core_v1_api.
    if name.startswith('_') or not name.isidentifier():
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name = f"kubernetes.client.api.{name}"
    try:
        return _import_module(module_name)
    except ModuleNotFoundError as e:
        if e.name != module_name:
            raise
        raise AttributeError(
            f"module {__name__!r} has no attribute {name!r}") from None
