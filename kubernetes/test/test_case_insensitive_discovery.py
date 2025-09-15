# Copyright 2023 The Kubernetes Authors.
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

"""
Test for case insensitive resource lookup in the Dynamic Client.
This test addresses issue #2402: Resource lookup is case-sensitive while it shouldn't
"""

import unittest
import kubernetes.config as config
from kubernetes import client, dynamic
from kubernetes.dynamic.exceptions import ResourceNotFoundError
import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestCaseInsensitiveDiscovery(unittest.TestCase):
    """
    Test case for case-insensitive resource lookup in the Dynamic Client.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test class - load kubernetes configuration
        """
        try:
            config.load_kube_config()
            cls.api_client = client.ApiClient()
            cls.dynamic_client = dynamic.DynamicClient(cls.api_client)
        except Exception as e:
            logger.warning(f"Could not load kubernetes configuration: {e}")
            cls.skipTest(cls, f"Failed to load kubernetes configuration: {e}")

    def test_case_sensitivity_service(self):
        """
        Test that Service resource can be found regardless of case
        """
        # 1. Test with exact case
        try:
            resource = self.dynamic_client.resources.get(kind='Service')
            self.assertEqual(resource.kind, 'Service')
            logger.info("Successfully found resource with correct case: Service")
        except Exception as e:
            self.fail(f"Failed to get resource with correct case 'Service': {e}")

        # 2. Test with lowercase
        try:
            resource = self.dynamic_client.resources.get(kind='service')
            self.assertEqual(resource.kind, 'Service')
            logger.info("Successfully found resource with lowercase: service")
        except Exception as e:
            self.fail(f"Failed to get resource with lowercase 'service': {e}")

        # 3. Test with mixed case
        try:
            resource = self.dynamic_client.resources.get(kind='SerVicE')
            self.assertEqual(resource.kind, 'Service')
            logger.info("Successfully found resource with mixed case: SerVicE")
        except Exception as e:
            self.fail(f"Failed to get resource with mixed case 'SerVicE': {e}")

    def test_case_sensitivity_deployment(self):
        """
        Test that Deployment resource can be found regardless of case
        """
        # 1. Test with exact case
        try:
            resource = self.dynamic_client.resources.get(kind='Deployment')
            self.assertEqual(resource.kind, 'Deployment')
            logger.info("Successfully found resource with correct case: Deployment")
        except Exception as e:
            self.fail(f"Failed to get resource with correct case 'Deployment': {e}")

        # 2. Test with lowercase
        try:
            resource = self.dynamic_client.resources.get(kind='deployment')
            self.assertEqual(resource.kind, 'Deployment')
            logger.info("Successfully found resource with lowercase: deployment")
        except Exception as e:
            self.fail(f"Failed to get resource with lowercase 'deployment': {e}")
    
    def test_nonexistent_resource(self):
        """
        Test that looking up a non-existent resource still returns the appropriate error
        """
        with self.assertRaises(ResourceNotFoundError):
            self.dynamic_client.resources.get(kind='NonExistentResource')
            logger.info("Correctly raised ResourceNotFoundError for non-existent resource")
    
    def test_with_api_version(self):
        """
        Test case insensitive lookup with api_version specified
        """
        try:
            resource = self.dynamic_client.resources.get(
                api_version='apps/v1', kind='deployment')
            self.assertEqual(resource.kind, 'Deployment')
            self.assertEqual(resource.group, 'apps')
            self.assertEqual(resource.api_version, 'v1')
            logger.info("Successfully found resource with api_version and lowercase kind")
        except Exception as e:
            self.fail(f"Failed to get resource with api_version and lowercase kind: {e}")


if __name__ == '__main__':
    unittest.main()
