# coding: utf-8


import unittest
from unittest import mock
import weakref

import kubernetes
from kubernetes.aio.client.configuration import Configuration as AsyncConfiguration
from kubernetes.client.configuration import Configuration
import urllib3


class TestApiClient(unittest.TestCase):
    def test_context_manager_closes_threadpool(self):
        with kubernetes.client.ApiClient() as client:
            pool = weakref.ref(client.pool)

        self.assertIsNone(client._pool)
        self.assertIsNone(pool())

    @mock.patch('kubernetes.client.api_client.atexit.register')
    def test_atexit_closes_threadpool(self, register):
        client = kubernetes.client.ApiClient()
        client.pool

        register.assert_called_once_with(client.close)
        register.call_args.args[0]()

        self.assertIsNone(client._pool)

    def test_deserialize_dict_syntax_compatibility(self):
        client = kubernetes.client.ApiClient()

        for response_type, expected in (
            ('Dict[str, str]', {'key': 'value'}),
            ('Dict[str, Dict[str, str]]', {'outer': {'key': 'value'}}),
        ):
            with self.subTest(response_type=response_type):
                self.assertEqual(
                    client._ApiClient__deserialize(expected, response_type),
                    expected,
                )

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
            config = Configuration(proxy='', no_proxy='')
            setattr(config, 'host', dst)
            if proxy is not None:
                setattr(config, 'proxy', proxy)
            if no_proxy is not None:
                setattr(config, 'no_proxy', no_proxy)
            # setup done

            # test
            client = kubernetes.client.ApiClient(configuration=config)
            self.assertEqual( expected_pool, type(client.rest_client.pool_manager) )


class TestConfigurationAuthSettings(unittest.TestCase):
    """Regression tests for Configuration.auth_settings() bearer-token lookup.

    Prior to v36.0.0 the generated client stored the bearer token under
    ``api_key['authorization']`` (e.g. set by ``load_kube_config`` or by
    user code directly). v36.0.0 switched the lookup to
    ``api_key['BearerToken']`` without a fallback, which silently dropped
    the Authorization header from every outgoing request and caused 401
    Unauthorized against any cluster relying on bearer tokens.
    See: https://github.com/kubernetes-client/python/issues/2595
    """

    def _bearer_value(self, config):
        settings = config.auth_settings()
        self.assertIn('BearerToken', settings)
        return settings['BearerToken']['value']

    def test_auth_settings_with_bearer_token_key(self):
        """The new key 'BearerToken' continues to work."""
        config = Configuration()
        config.api_key['BearerToken'] = 'Bearer abc123'
        self.assertEqual(self._bearer_value(config), 'Bearer abc123')

    def test_auth_settings_with_authorization_key(self):
        """Legacy key 'authorization' is honored as a fallback."""
        config = Configuration()
        config.api_key['authorization'] = 'Bearer abc123'
        self.assertEqual(self._bearer_value(config), 'Bearer abc123')

    def test_auth_settings_bearer_token_takes_precedence(self):
        """When both keys are set, 'BearerToken' wins."""
        config = Configuration()
        config.api_key['BearerToken'] = 'Bearer new'
        config.api_key['authorization'] = 'Bearer old'
        self.assertEqual(self._bearer_value(config), 'Bearer new')

    def test_auth_settings_with_no_token(self):
        """No api_key entry yields an empty auth dict."""
        config = Configuration()
        self.assertEqual(config.auth_settings(), {})

    def test_auth_settings_with_authorization_key_and_prefix(self):
        """Legacy callers that split the token and prefix across
        api_key['authorization'] and api_key_prefix['authorization'] (rather
        than embedding "Bearer " in the token itself) must still get the
        prefix applied. https://github.com/kubernetes-client/python/issues/2592
        """
        config = Configuration()
        config.api_key['authorization'] = 'abc123'
        config.api_key_prefix['authorization'] = 'Bearer'
        self.assertEqual(self._bearer_value(config), 'Bearer abc123')


class TestAsyncConfigurationAuthSettings(unittest.IsolatedAsyncioTestCase):
    async def test_auth_settings_with_authorization_key_and_prefix(self):
        config = AsyncConfiguration()
        config.api_key['authorization'] = 'abc123'
        config.api_key_prefix['authorization'] = 'Bearer'

        self.assertEqual(
            (await config.auth_settings())['BearerToken']['value'],
            'Bearer abc123',
        )

    async def test_auth_settings_bearer_token_takes_precedence(self):
        config = AsyncConfiguration()
        config.api_key['BearerToken'] = 'Bearer new'
        config.api_key['authorization'] = 'Bearer old'

        self.assertEqual(
            (await config.auth_settings())['BearerToken']['value'],
            'Bearer new',
        )
