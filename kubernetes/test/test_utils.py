# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest
from os import path

import yaml

from kubernetes import utils, client
from kubernetes.client import V1Deployment
from kubernetes.client.rest import ApiException
from kubernetes.e2e_test import base


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.path_prefix = "kubernetes/e2e_test/test_yaml/"

    def test_deserialize_from_data(self):
        deployment_file = self.path_prefix + "apps-deployment.yaml"
        with open(path.abspath(deployment_file)) as f:
            deployment_data = yaml.safe_load(f)

        k8s_client = client.api_client.ApiClient()
        v1depl = k8s_client.deserialize_data(deployment_data, "V1Deployment")

        assert isinstance(v1depl, V1Deployment)
        assert v1depl.metadata.name == "nginx-app"
