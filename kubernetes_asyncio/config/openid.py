import aiohttp

from .config_exception import ConfigException

GRANT_TYPE_REFRESH_TOKEN = 'refresh_token'


class OpenIDRequestor:

    def __init__(self, client_id, client_secret, issuer_url, ssl_ca_cert=None):
        """OpenIDRequestor implements a very limited subset of the oauth2 APIs that we
        require in order to refresh access tokens"""

        self._client_id = client_id
        self._client_secret = client_secret
        self._issuer_url = issuer_url
        self._ssl_ca_cert = ssl_ca_cert
        self._well_known = None

    def _get_connector(self):
        return aiohttp.TCPConnector(
            verify_ssl=self._ssl_ca_cert is not None,
            ssl_context=self._ssl_ca_cert
        )

    def _client_session(self):
        return aiohttp.ClientSession(
            headers=self._default_headers,
            connector=self._get_connector(),
            auth=aiohttp.BasicAuth(self._client_id, self._client_secret),
            raise_for_status=True,
            trust_env=True
        )

    async def refresh_token(self, refresh_token):
        """
        :param refresh_token: an openid refresh-token from a previous token request
        """
        async with self._client_session() as client:
            well_known = await self._get_well_known(client)

            try:
                return await self._post(
                    client,
                    well_known['token_endpoint'],
                    data={
                        'grant_type': GRANT_TYPE_REFRESH_TOKEN,
                        'refresh_token': refresh_token,
                    }
                )
            except aiohttp.ClientResponseError:
                raise ConfigException('oidc: failed to refresh access token')

    async def _get(self, client, *args, **kwargs):
        async with client.get(*args, **kwargs) as resp:
            return await resp.json()

    async def _post(self, client, *args, **kwargs):
        async with client.post(*args, **kwargs) as resp:
            return await resp.json()

    async def _get_well_known(self, client):
        if self._well_known is None:
            try:
                self._well_known = await self._get(
                    client,
                    '{}/.well-known/openid-configuration'.format(self._issuer_url.rstrip('/'))
                )
            except aiohttp.ClientResponseError:
                raise ConfigException('oidc: failed to query well-known metadata endpoint')

        return self._well_known

    @property
    def _default_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        }
