# coding: utf-8


import atexit
import weakref
import unittest

import kubernetes
from kubernetes.client.configuration import Configuration
import urllib3
import datetime
from kubernetes.config import dateutil as kube_dateutil

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
    
    def test_1_parse_rfc3339(self):
        dt = datetime.datetime(2023, 1, 1, 12, 0, 0)
        result = kube_dateutil.parse_rfc3339(dt)
        self.assertIsNotNone(result.tzinfo)
    
    def test_2_parse_rfc3339(self):
        """Test that invalid RFC3339 strings raise ValueError with descriptive message"""
        invalid_inputs = [
            "invalid-datetime-string",
            "",
            "not-a-date",
            "2023",  # incomplete
            "random text",
            "2023-13-01T12:00:00Z",  # invalid month
            "not-rfc3339-format"
        ]
        
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError) as context:
                    kube_dateutil.parse_rfc3339(invalid_input)
                
                # Check that the error message includes the invalid input
                error_message = str(context.exception)
                self.assertIn("Error in RFC339 Date Formatting", error_message)
                self.assertIn(invalid_input, error_message)