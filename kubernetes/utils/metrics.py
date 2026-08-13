# Copyright 2024 The Kubernetes Authors.
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
Metrics utilities for Kubernetes resource monitoring.

Provides helpers for fetching and processing resource usage data from the
metrics.k8s.io API endpoint, enabling monitoring and autoscaling workflows.
"""

METRICS_API_GROUP = "metrics.k8s.io"
METRICS_API_VERSION = "v1beta1"


def _custom_objects_api(api_client):
    from kubernetes.client.api.custom_objects_api import CustomObjectsApi

    return CustomObjectsApi(api_client)


def get_nodes_metrics(api_client):
    """
    Fetch current resource usage for all cluster nodes.
    
    Retrieves CPU and memory consumption metrics from the metrics-server
    for every node in the cluster.
    
    Parameters:
        api_client: An initialized kubernetes.client.ApiClient instance
        
    Returns:
        A dictionary containing the metrics response with structure:
        {
            'kind': 'NodeMetricsList',
            'apiVersion': 'metrics.k8s.io/v1beta1',
            'metadata': {...},
            'items': [
                {
                    'metadata': {'name': 'node-1', ...},
                    'timestamp': '2024-01-01T00:00:00Z',
                    'window': '30s',
                    'usage': {'cpu': '100m', 'memory': '1024Mi'}
                },
                ...
            ]
        }
        
    Raises:
        ApiException: If the metrics server is not available or request fails
        
    Example:
        >>> from kubernetes import client, config
        >>> config.load_kube_config()
        >>> api_client = client.ApiClient()
        >>> metrics = get_nodes_metrics(api_client)
        >>> for node in metrics['items']:
        ...     name = node['metadata']['name']
        ...     cpu = node['usage']['cpu']
        ...     mem = node['usage']['memory']
        ...     print(f"Node {name}: CPU={cpu}, Memory={mem}")
    """
    api = _custom_objects_api(api_client)
    return api.list_cluster_custom_object(
        group=METRICS_API_GROUP,
        version=METRICS_API_VERSION,
        plural="nodes"
    )


def get_pods_metrics(api_client, namespace, label_selector=None):
    """
    Fetch current resource usage for pods in a namespace.
    
    Retrieves CPU and memory consumption metrics from the metrics-server
    for pods in the specified namespace, with optional label filtering.
    
    Parameters:
        api_client: An initialized kubernetes.client.ApiClient instance
        namespace: The namespace name to query (required)
        label_selector: Optional label query to filter pods (e.g., 'app=web,env=prod')
        
    Returns:
        A dictionary containing the metrics response with structure:
        {
            'kind': 'PodMetricsList',
            'apiVersion': 'metrics.k8s.io/v1beta1',
            'metadata': {...},
            'items': [
                {
                    'metadata': {'name': 'pod-1', 'namespace': 'default', ...},
                    'timestamp': '2024-01-01T00:00:00Z',
                    'window': '30s',
                    'containers': [
                        {
                            'name': 'container-1',
                            'usage': {'cpu': '50m', 'memory': '512Mi'}
                        },
                        ...
                    ]
                },
                ...
            ]
        }
        
    Raises:
        ValueError: If namespace is None or empty
        ApiException: If the metrics server is not available or request fails
        
    Example:
        >>> from kubernetes import client, config
        >>> config.load_kube_config()
        >>> api_client = client.ApiClient()
        >>> 
        >>> # Get all pods in namespace
        >>> metrics = get_pods_metrics(api_client, 'default')
        >>> 
        >>> # Get pods with specific labels
        >>> metrics = get_pods_metrics(api_client, 'default', 'app=nginx')
        >>> 
        >>> for pod in metrics['items']:
        ...     pod_name = pod['metadata']['name']
        ...     print(f"Pod: {pod_name}")
        ...     for container in pod['containers']:
        ...         cname = container['name']
        ...         cpu = container['usage']['cpu']
        ...         mem = container['usage']['memory']
        ...         print(f"  Container {cname}: CPU={cpu}, Memory={mem}")
    """
    if not namespace:
        raise ValueError("namespace parameter is required and cannot be empty")
    
    api = _custom_objects_api(api_client)
    
    kwargs = {
        "group": METRICS_API_GROUP,
        "version": METRICS_API_VERSION,
        "namespace": namespace,
        "plural": "pods"
    }
    
    if label_selector:
        kwargs["label_selector"] = label_selector
    
    return api.list_namespaced_custom_object(**kwargs)


def get_pods_metrics_in_all_namespaces(api_client, namespaces, label_selector=None):
    """
    Fetch pod metrics across multiple namespaces.
    
    Queries pod metrics in each specified namespace and returns an aggregated
    result. If a namespace query fails, the error is captured in the result
    rather than raising an exception.
    
    Parameters:
        api_client: An initialized kubernetes.client.ApiClient instance
        namespaces: A list of namespace names to query
        label_selector: Optional label query applied to all namespaces
        
    Returns:
        A dictionary mapping namespace names to their metrics or error info:
        {
            'namespace-1': {
                'items': [...],
                'kind': 'PodMetricsList',
                ...
            },
            'namespace-2': {
                'error': 'error message',
                'kind': 'Error'
            },
            ...
        }
        
    Example:
        >>> from kubernetes import client, config
        >>> config.load_kube_config()
        >>> api_client = client.ApiClient()
        >>> 
        >>> namespaces = ['default', 'kube-system', 'monitoring']
        >>> all_metrics = get_pods_metrics_in_all_namespaces(api_client, namespaces)
        >>> 
        >>> for ns, result in all_metrics.items():
        ...     if 'error' in result:
        ...         print(f"{ns}: ERROR - {result['error']}")
        ...     else:
        ...         pod_count = len(result.get('items', []))
        ...         print(f"{ns}: {pod_count} pods")
    """
    results = {}
    
    for ns in namespaces:
        try:
            results[ns] = get_pods_metrics(api_client, ns, label_selector)
        except Exception as e:
            results[ns] = {
                'kind': 'Error',
                'error': str(e)
            }
    
    return results
