"""
    Test cases for multiple client configuration usage.
"""

import unittest
from kubernetes.client import Configuration


class TestMultipleClientConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthinfoNotShared(self):
        conf_a = Configuration()
        conf_a.api_key['authorization'] = "token a"
        conf_a.api_key_prefix['authorization'] = "Bearer"
        conf_b = Configuration()
        conf_b.api_key['authorization'] = "token b"
        conf_b.api_key_prefix['authorization'] = "Token"
        self.assertEqual(conf_a.api_key['authorization'], "token a")
        self.assertEqual(conf_a.api_key_prefix['authorization'], "Bearer")
        self.assertEqual(conf_b.api_key['authorization'], "token b")
        self.assertEqual(conf_b.api_key_prefix['authorization'], "Token")

