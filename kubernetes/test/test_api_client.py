# coding: utf-8


import atexit
import weakref
import unittest

import kubernetes
from kubernetes.client.configuration import Configuration
import urllib3

class TestApiClient(unittest.TestCase):

    def test_context_manager_closes_threadpool(self):
        with kubernetes.client.ApiClient() as client:
            self.assertIsNotNone(client.pool)
            pool_ref = weakref.ref(client._pool)
            self.assertIsNotNone(pool_ref())
        self.assertIsNone(pool_ref())

    def test_atexit_closes_threadpool(self):
        client = kubernetes.client.ApiClient()
        self.assertIsNotNone(client.pool)
        self.assertIsNotNone(client._pool)
        atexit._run_exitfuncs()
        self.assertIsNone(client._pool)

    def test_deserialize_dict_syntax_compatibility(self):
        """Test ApiClient.__deserialize supports both dict(str, str) and dict[str, str] syntax"""
        client = kubernetes.client.ApiClient()
        
        # Test data
        test_data = {
            'key1': 'value1',
            'key2': 'value2'
        }
        
        # Test legacy syntax: dict(str, str)
        result_legacy = client._ApiClient__deserialize(test_data, 'dict(str, str)')
        self.assertEqual(result_legacy, test_data)
        
        # Test modern syntax: dict[str, str]
        result_modern = client._ApiClient__deserialize(test_data, 'dict[str, str]')
        self.assertEqual(result_modern, test_data)
        
        # Test nested dict: dict[str, dict[str, str]]
        nested_data = {
            'outer1': {'inner1': 'value1', 'inner2': 'value2'},
            'outer2': {'inner3': 'value3'}
        }
        result_nested = client._ApiClient__deserialize(nested_data, 'dict[str, dict[str, str]]')
        self.assertEqual(result_nested, nested_data)

    def test_rest_proxycare(self):

        pool = { 'proxy': urllib3.ProxyManager, 'direct': urllib3.PoolManager }

        for dst, proxy, no_proxy, expected_pool in [
             ( 'http://kube.local/',           None,                       None,                           pool['direct']),
             ( 'http://kube.local/',          'http://proxy.local:8080/',  None,                           pool['proxy']),
             ( 'http://127.0.0.1:8080/',      'http://proxy.local:8080/',  'localhost,127.0.0.0/8,.local', pool['direct']),
             ( 'http://kube.local/',          'http://proxy.local:8080/',  'localhost,127.0.0.0/8,.local', pool['direct']),
             ( 'http://kube.others.com:1234/','http://proxy.local:8080/',  'localhost,127.0.0.0/8,.local', pool['proxy']),
             ( 'http://kube.others.com:1234/','http://proxy.local:8080/',  '*',                            pool['direct']),
        ]:
            # setup input
            config = Configuration()
            setattr(config, 'host', dst)
            if proxy is not None:
                setattr(config, 'proxy', proxy)
            if no_proxy is not None:
                setattr(config, 'no_proxy', no_proxy)
            # setup done

            # test
            client = kubernetes.client.ApiClient(configuration=config)
            self.assertEqual( expected_pool, type(client.rest_client.pool_manager) )
