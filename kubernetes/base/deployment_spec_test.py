# Copyright 2026 The Kubernetes Authors.
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

import unittest

from kubernetes.client import ApiClient
from kubernetes.client.models import V1DeploymentSpec


class DeploymentSpecTest(unittest.TestCase):

    def test_round_trip_preserves_nested_fields(self):
        spec_dict = {
            'selector': {'matchLabels': {'name': 'my-operator'}},
            'template': {'spec': {
                'affinity': {'nodeAffinity': {
                    'requiredDuringSchedulingIgnoredDuringExecution': {
                        'nodeSelectorTerms': [{'matchExpressions': [{
                            'key': 'kubernetes.io/arch',
                            'operator': 'In',
                            'values': ['s390x', 'amd64'],
                        }]}],
                    },
                }},
                'containers': [{
                    'name': 'op',
                    'image': 'img:1',
                    'imagePullPolicy': 'Always',
                    'env': [{
                        'name': 'WATCH_NAMESPACE',
                        'valueFrom': {
                            'fieldRef': {
                                'fieldPath': "metadata.annotations['olm.targetNamespaces']",
                            },
                        },
                    }],
                    'livenessProbe': {
                        'httpGet': {'path': '/healthz', 'port': 8081},
                        'initialDelaySeconds': 15,
                        'failureThreshold': 4,
                    },
                }],
            }},
        }
        expected = {
            **spec_dict,
            'template': {
                **spec_dict['template'],
                'spec': {
                    **spec_dict['template']['spec'],
                    'containers': [{
                        **spec_dict['template']['spec']['containers'][0],
                        'image': 'img:2',
                    }],
                },
            },
        }

        model = V1DeploymentSpec.from_dict(spec_dict)
        model.template.spec.containers[0].image = 'img:2'
        model = V1DeploymentSpec.from_dict(model.to_dict())

        self.assertEqual(
            ApiClient().sanitize_for_serialization(model),
            expected,
        )
