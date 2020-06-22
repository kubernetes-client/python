# coding: utf-8


import atexit
import weakref
import unittest

import kubernetes


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
