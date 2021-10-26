# Copyright 2016 The Kubernetes Authors.
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
__version__ = "20.11.0a1"

import kubernetes.client
import kubernetes.config
import kubernetes.dynamic
import kubernetes.watch
import kubernetes.stream
import kubernetes.utils
import kubernetes.leaderelection
