# Copyright 2022 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__project__ = 'kubernetes'
# The version is auto-updated. Please do not edit.
__version__ = "35.0.0+snapshot"

from . import client  # keep direct import of generated client package

# Windows compatibility: historical layout used directory symlinks named
# config, dynamic, watch, stream, leaderelection pointing to base/*.
# In Windows dev environments those symlinks are replaced with plain files
# (without .py) which the import system cannot load as packages. To remain
# cross-platform, we import the canonical implementations from kubernetes.base
# and explicitly register them in sys.modules under the legacy public names.
import sys as _sys
from .base import config as _base_config
from .base import dynamic as _base_dynamic
from .base import watch as _base_watch
from .base import stream as _base_stream
from .base import leaderelection as _base_leaderelection

_sys.modules[__name__ + '.config'] = _base_config
_sys.modules[__name__ + '.dynamic'] = _base_dynamic
_sys.modules[__name__ + '.watch'] = _base_watch
_sys.modules[__name__ + '.stream'] = _base_stream
_sys.modules[__name__ + '.leaderelection'] = _base_leaderelection

# Expose attributes for "from kubernetes import config" style imports
config = _base_config
dynamic = _base_dynamic
watch = _base_watch
stream = _base_stream
leaderelection = _base_leaderelection

# Now that dynamic is registered, import utils which depends on dynamic
from . import utils as utils  # noqa: E402
