import asyncio
import json
from contextlib import contextmanager
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch

from aiohttp import web
from aiohttp.test_utils import (
    TestClient as _TestClient, TestServer as _TestServer,
)

from .config_exception import ConfigException
from .openid import OpenIDRequestor


def make_responder(response):

    async def responder(request):
        return response

    return responder


def respond_json(data):
    return make_responder(
        web.Response(
            text=json.dumps(data),
            content_type='application/json',
        )
    )


@contextmanager
def working_client():
    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/.well-known/openid-configuration', respond_json({'token_endpoint': '/token'}))
    app.router.add_post('/token', respond_json({'id-token': 'id-token-data', 'refresh-token': 'refresh-token-data'}))

    with patch('kubernetes_asyncio.config.openid.aiohttp.ClientSession') as _client_session:
        client = _TestClient(_TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client

        yield client


@contextmanager
def fail_well_known_client():
    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/.well-known/openid-configuration', make_responder(web.Response(status=500)))

    with patch('kubernetes_asyncio.config.openid.aiohttp.ClientSession') as _client_session:
        client = _TestClient(_TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client
        yield client


@contextmanager
def fail_token_request_client():
    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/.well-known/openid-configuration', respond_json({'token_endpoint': '/token'}))
    app.router.add_post('/token', make_responder(web.Response(status=500)))

    with patch('kubernetes_asyncio.config.openid.aiohttp.ClientSession') as _client_session:
        client = _TestClient(_TestServer(app, loop=loop), loop=loop)
        _client_session.return_value = client

        yield client


class OpenIDRequestorTest(IsolatedAsyncioTestCase):

    def setUp(self):
        self.requestor = OpenIDRequestor(
            'client-id',
            'client-secret',
            '',
        )

    async def test_refresh_token_success(self):
        with working_client():
            resp = await self.requestor.refresh_token('my-refresh-token')

            assert resp['id-token'] == 'id-token-data'
            assert resp['refresh-token'] == 'refresh-token-data'

    async def test_failed_well_known(self):
        with fail_well_known_client():
            with self.assertRaises(ConfigException):
                await self.requestor.refresh_token('my-refresh-token')

    async def test_failed_refresh_token(self):
        with fail_token_request_client():
            with self.assertRaises(ConfigException):
                await self.requestor.refresh_token('my-refresh-token')
