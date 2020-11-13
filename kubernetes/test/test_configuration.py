# coding: utf-8

import unittest

from kubernetes.client import Configuration

class TestConfiguration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        # reset Configuration
        Configuration.set_default(None)

    def testConfiguration(self):
        # check that different instances use different dictionaries
        c1 = Configuration()
        c2 = Configuration()
        self.assertNotEqual(id(c1.api_key), id(c2.api_key))
        self.assertNotEqual(id(c1.api_key_prefix), id(c2.api_key_prefix))

    def testDefaultConfiguration(self):
        # prepare default configuration
        c1 = Configuration(host="example.com")
        c1.debug = True
        Configuration.set_default(c1)

        # get default configuration
        c2 = Configuration.get_default_copy()
        self.assertEqual(c2.host, "example.com")
        self.assertTrue(c2.debug)

        self.assertNotEqual(id(c1.api_key), id(c2.api_key))
        self.assertNotEqual(id(c1.api_key_prefix), id(c2.api_key_prefix))


if __name__ == '__main__':
    unittest.main()
