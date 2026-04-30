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
from unittest.mock import MagicMock, patch
from kubernetes import client, utils


class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.mock_api_client = MagicMock(spec=client.ApiClient)

    @patch('kubernetes.utils.metrics.CustomObjectsApi')
    def test_get_nodes_metrics_success(self, mock_custom_api_class):
        """Test successful retrieval of node metrics"""
        mock_api_instance = MagicMock()
        mock_custom_api_class.return_value = mock_api_instance
        
        expected_response = {
            'kind': 'NodeMetricsList',
            'apiVersion': 'metrics.k8s.io/v1beta1',
            'items': [
                {
                    'metadata': {'name': 'node1'},
                    'timestamp': '2024-01-01T00:00:00Z',
                    'window': '30s',
                    'usage': {'cpu': '100m', 'memory': '1Gi'}
                }
            ]
        }
        mock_api_instance.list_cluster_custom_object.return_value = expected_response
        
        result = utils.get_nodes_metrics(self.mock_api_client)
        
        mock_custom_api_class.assert_called_once_with(self.mock_api_client)
        mock_api_instance.list_cluster_custom_object.assert_called_once_with(
            group='metrics.k8s.io',
            version='v1beta1',
            plural='nodes'
        )
        self.assertEqual(result, expected_response)
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['items'][0]['metadata']['name'], 'node1')

    @patch('kubernetes.utils.metrics.CustomObjectsApi')
    def test_get_pods_metrics_success(self, mock_custom_api_class):
        """Test successful retrieval of pod metrics"""
        mock_api_instance = MagicMock()
        mock_custom_api_class.return_value = mock_api_instance
        
        expected_response = {
            'kind': 'PodMetricsList',
            'apiVersion': 'metrics.k8s.io/v1beta1',
            'items': [
                {
                    'metadata': {'name': 'pod1', 'namespace': 'default'},
                    'timestamp': '2024-01-01T00:00:00Z',
                    'window': '30s',
                    'containers': [
                        {
                            'name': 'container1',
                            'usage': {'cpu': '50m', 'memory': '512Mi'}
                        }
                    ]
                }
            ]
        }
        mock_api_instance.list_namespaced_custom_object.return_value = expected_response
        
        result = utils.get_pods_metrics(self.mock_api_client, 'default')
        
        mock_custom_api_class.assert_called_once_with(self.mock_api_client)
        mock_api_instance.list_namespaced_custom_object.assert_called_once_with(
            group='metrics.k8s.io',
            version='v1beta1',
            namespace='default',
            plural='pods'
        )
        self.assertEqual(result, expected_response)
        self.assertEqual(len(result['items']), 1)

    @patch('kubernetes.utils.metrics.CustomObjectsApi')
    def test_get_pods_metrics_with_label_selector(self, mock_custom_api_class):
        """Test pod metrics retrieval with label selector"""
        mock_api_instance = MagicMock()
        mock_custom_api_class.return_value = mock_api_instance
        
        expected_response = {'kind': 'PodMetricsList', 'items': []}
        mock_api_instance.list_namespaced_custom_object.return_value = expected_response
        
        utils.get_pods_metrics(self.mock_api_client, 'production', 'app=web')
        
        mock_api_instance.list_namespaced_custom_object.assert_called_once_with(
            group='metrics.k8s.io',
            version='v1beta1',
            namespace='production',
            plural='pods',
            label_selector='app=web'
        )

    def test_get_pods_metrics_empty_namespace_raises_error(self):
        """Test that empty namespace raises ValueError"""
        with self.assertRaises(ValueError) as context:
            utils.get_pods_metrics(self.mock_api_client, '')
        
        self.assertIn('namespace parameter is required', str(context.exception))

    def test_get_pods_metrics_none_namespace_raises_error(self):
        """Test that None namespace raises ValueError"""
        with self.assertRaises(ValueError) as context:
            utils.get_pods_metrics(self.mock_api_client, None)
        
        self.assertIn('namespace parameter is required', str(context.exception))

    @patch('kubernetes.utils.metrics.get_pods_metrics')
    def test_get_pods_metrics_in_all_namespaces_success(self, mock_get_pods):
        """Test fetching metrics across multiple namespaces"""
        mock_get_pods.side_effect = [
            {'kind': 'PodMetricsList', 'items': [{'metadata': {'name': 'pod1'}}]},
            {'kind': 'PodMetricsList', 'items': [{'metadata': {'name': 'pod2'}}]}
        ]
        
        result = utils.get_pods_metrics_in_all_namespaces(
            self.mock_api_client, 
            ['default', 'kube-system']
        )
        
        self.assertEqual(len(result), 2)
        self.assertIn('default', result)
        self.assertIn('kube-system', result)
        self.assertEqual(len(result['default']['items']), 1)
        self.assertEqual(len(result['kube-system']['items']), 1)

    @patch('kubernetes.utils.metrics.get_pods_metrics')
    def test_get_pods_metrics_in_all_namespaces_with_errors(self, mock_get_pods):
        """Test multi-namespace query with partial failures"""
        mock_get_pods.side_effect = [
            {'kind': 'PodMetricsList', 'items': []},
            Exception('Namespace not found')
        ]
        
        result = utils.get_pods_metrics_in_all_namespaces(
            self.mock_api_client,
            ['default', 'invalid-ns']
        )
        
        self.assertEqual(len(result), 2)
        self.assertIn('default', result)
        self.assertIn('invalid-ns', result)
        self.assertEqual(result['default']['kind'], 'PodMetricsList')
        self.assertEqual(result['invalid-ns']['kind'], 'Error')
        self.assertIn('error', result['invalid-ns'])

    @patch('kubernetes.utils.metrics.get_pods_metrics')
    def test_get_pods_metrics_in_all_namespaces_with_label_selector(self, mock_get_pods):
        """Test multi-namespace query with label selector"""
        mock_get_pods.return_value = {'kind': 'PodMetricsList', 'items': []}
        
        utils.get_pods_metrics_in_all_namespaces(
            self.mock_api_client,
            ['ns1', 'ns2'],
            'tier=frontend'
        )
        
        self.assertEqual(mock_get_pods.call_count, 2)
        mock_get_pods.assert_any_call(self.mock_api_client, 'ns1', 'tier=frontend')
        mock_get_pods.assert_any_call(self.mock_api_client, 'ns2', 'tier=frontend')


if __name__ == '__main__':
    unittest.main()
