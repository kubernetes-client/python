# Copyright 2016 The Kubernetes Authors.
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

import asyncio
import atexit
import base64
import copy
import datetime
import json
import logging
import os
import pathlib
import platform
import tempfile

import yaml

from kubernetes_asyncio.client import ApiClient, Configuration

from .config_exception import ConfigException
from .dateutil import UTC, parse_rfc3339
from .exec_provider import ExecProvider
from .google_auth import google_auth_credentials
from .openid import OpenIDRequestor

EXPIRY_SKEW_PREVENTION_DELAY = datetime.timedelta(minutes=5)
KUBE_CONFIG_DEFAULT_LOCATION = os.environ.get('KUBECONFIG', (pathlib.Path.home() / '.kube/config').as_posix())
ENV_KUBECONFIG_PATH_SEPARATOR = ';' if platform.system() == 'Windows' else ':'
PROVIDER_TYPE_OIDC = 'oidc'
_temp_files = {}
logger = logging.getLogger(__name__)


def _cleanup_temp_files():
    global _temp_files
    for temp_file in _temp_files.values():
        try:
            os.remove(temp_file)
        except OSError:
            pass
    _temp_files = {}


def _is_expired(expiry):
    return ((parse_rfc3339(expiry) - EXPIRY_SKEW_PREVENTION_DELAY)
            <= datetime.datetime.utcnow().replace(tzinfo=UTC))


class FileOrData(object):
    """Utility class to read content of obj[%data_key_name] or file's
     content of obj[%file_key_name] and represent it as file or data.
     Note that the data is preferred. The obj[%file_key_name] will be used iff
     obj['%data_key_name'] is not set or empty. Assumption is file content is
     raw data and data field is base64 string. The assumption can be changed
     with base64_file_content flag. If set to False, the content of the file
     will assumed to be base64 and read as is. The default True value will
     result in base64 encode of the file content after read."""

    def __init__(self, obj, file_key_name, data_key_name=None,
                 file_base_path="", base64_file_content=True,
                 temp_file_path=None):
        if not data_key_name:
            data_key_name = file_key_name + "-data"
        self._file = None
        self._data = None
        self._base64_file_content = base64_file_content
        self._temp_file_path = temp_file_path
        if temp_file_path:
            os.makedirs(name=temp_file_path, exist_ok=True)
        if data_key_name in obj:
            self._data = obj[data_key_name]
        elif file_key_name in obj:
            self._file = os.path.normpath(
                os.path.join(file_base_path, obj[file_key_name]))

    def _create_temp_file_with_content(self, content):
        if len(_temp_files) == 0:
            atexit.register(_cleanup_temp_files)
        # Because we may change context several times, try to remember files we
        # created and reuse them at a small memory cost.
        content_key = str(content)
        if content_key in _temp_files:
            return _temp_files[content_key]
        _, name = tempfile.mkstemp(dir=self._temp_file_path)
        _temp_files[content_key] = name
        with open(name, 'wb') as fd:
            fd.write(content.encode() if isinstance(content, str) else content)
        return name

    def as_file(self):
        """If obj[%data_key_name] exists, return name of a file with base64
        decoded obj[%data_key_name] content otherwise obj[%file_key_name]."""
        use_data_if_no_file = not self._file and self._data
        if use_data_if_no_file:
            if self._base64_file_content:
                if isinstance(self._data, str):
                    content = self._data.encode()
                else:
                    content = self._data
                self._file = self._create_temp_file_with_content(
                    base64.standard_b64decode(content))
            else:
                self._file = self._create_temp_file_with_content(self._data)
        if self._file and not os.path.isfile(self._file):
            raise ConfigException("File does not exists: %s" % self._file)
        return self._file

    def as_data(self):
        """If obj[%data_key_name] exists, Return obj[%data_key_name] otherwise
        base64 encoded string of obj[%file_key_name] file content."""
        use_file_if_no_data = not self._data and self._file
        if use_file_if_no_data:
            with open(self._file) as f:
                if self._base64_file_content:
                    self._data = bytes.decode(
                        base64.standard_b64encode(str.encode(f.read())))
                else:
                    self._data = f.read()
        return self._data


class KubeConfigLoader(object):

    def __init__(self, config_dict, active_context=None,
                 get_google_credentials=None,
                 config_base_path="",
                 config_persister=None,
                 temp_file_path=None):

        if isinstance(config_dict, ConfigNode):
            self._config = config_dict
        else:
            self._config = ConfigNode('kube-config', config_dict)

        self._current_context = None
        self._user = None
        self._cluster = None
        self.provider = None
        self.set_active_context(active_context)
        self._config_base_path = config_base_path
        self._config_persister = config_persister
        self._temp_file_path = temp_file_path
        if get_google_credentials:
            self._get_google_credentials = get_google_credentials
        else:
            self._get_google_credentials = None

    def set_active_context(self, context_name=None):
        if context_name is None:
            context_name = self._config['current-context']
        self._current_context = self._config['contexts'].get_with_name(
            context_name)
        if (self._current_context['context'].safe_get('user') and
                self._config.safe_get('users')):
            user = self._config['users'].get_with_name(
                self._current_context['context']['user'], safe=True)
            if user:
                self._user = user['user']
            else:
                self._user = None
        else:
            self._user = None
        self._cluster = self._config['clusters'].get_with_name(
            self._current_context['context']['cluster'])['cluster']
        if self._user is not None and 'auth-provider' in self._user and 'name' in self._user['auth-provider']:
            self.provider = self._user['auth-provider']['name']

        logger.debug('kubeconfig loader - current-context %s, cluster %s, user %s, provider %s',
                     context_name,
                     self._current_context['context']['cluster'],
                     self._current_context['context'].safe_get('user'),
                     self.provider)

    async def _load_authentication(self):
        """Read authentication from kube-config user section if exists.

        This function goes through various authentication methods in user
        section of kube-config and stops if it finds a valid authentication
        method. The order of authentication methods is:

            1. GCP auth-provider
            2. token field (point to a token file)
            3. oidc auth-provider
            4. exec provided plugin
            5. username/password
        """

        if not self._user:
            logger.debug('No user section in current context.')
            return

        if self.provider == 'gcp':
            await self.load_gcp_token()
            return

        if self.provider == PROVIDER_TYPE_OIDC:
            await self._load_oid_token()
            return

        if 'exec' in self._user:
            logger.debug('Try to use exec provider')
            res_exec_plugin = await self.load_from_exec_plugin()
            if res_exec_plugin:
                return

        logger.debug('Try to load user token')
        if self._load_user_token():
            return

        logger.debug('Try to use username and password')
        self._load_user_pass_token()

    async def load_gcp_token(self):

        if 'config' not in self._user['auth-provider']:
            self._user['auth-provider'].value['config'] = {}

        config = self._user['auth-provider']['config']

        if (('access-token' not in config) or
                ('expiry' in config and _is_expired(config['expiry']))):

            if self._get_google_credentials is not None:
                if asyncio.iscoroutinefunction(self._get_google_credentials):
                    credentials = await self._get_google_credentials()
                else:
                    credentials = self._get_google_credentials()
            else:
                credentials = await google_auth_credentials(config)
            config.value['access-token'] = credentials.token
            config.value['expiry'] = credentials.expiry
            if self._config_persister:
                self._config_persister(self._config.value)

        self.token = "Bearer %s" % config['access-token']
        return self.token

    async def _load_oid_token(self):
        provider = self._user['auth-provider']

        if 'config' not in provider:
            raise ValueError('oidc: missing configuration')

        if 'id-token' not in provider['config']:
            await self._refresh_oidc(provider)

            self.token = 'Bearer {}'.format(provider['config']['id-token'])
            return self.token

        parts = provider['config']['id-token'].split('.')

        if len(parts) != 3:
            raise ValueError('oidc: JWT tokens should contain 3 period-delimited parts')

        id_token = parts[1]
        # Re-pad the unpadded JWT token
        id_token += (4 - len(id_token) % 4) * '='
        jwt_attributes = json.loads(base64.b64decode(id_token).decode('utf8'))
        expires = jwt_attributes.get('exp')

        if (
            expires is not None and
            _is_expired(datetime.datetime.utcfromtimestamp(expires))
        ):
            await self._refresh_oidc(provider)

        self.token = 'Bearer {}'.format(provider['config']['id-token'])
        return self.token

    async def _refresh_oidc(self, provider):
        if 'refresh-token' not in provider['config']:
            raise ConfigException('oidc: No valid id-token, and cannot refresh without refresh-token')

        with tempfile.NamedTemporaryFile(delete=True) as certfile:
            ssl_ca_cert = None
            cert_auth_data = self._retrieve_oidc_cacert(provider)
            if cert_auth_data is not None:
                certfile.write(cert_auth_data)
                certfile.flush()
                ssl_ca_cert = certfile.name

            requestor = OpenIDRequestor(
                provider['config']['client-id'],
                provider['config']['client-secret'],
                provider['config']['idp-issuer-url'],
                ssl_ca_cert,
            )

            resp = await requestor.refresh_token(provider['config']['refresh-token'])

            provider['config'].value['id-token'] = resp['id_token']
            provider['config'].value['refresh-token'] = resp['refresh_token']

            if self._config_persister:
                self._config_persister(self._config.value)

    def _retrieve_oidc_cacert(self, provider):
        if 'idp-certificate-authority-data' in provider['config']:
            return base64.b64decode(provider['config']['idp-certificate-authority-data'])

        return None

    async def load_from_exec_plugin(self):
        try:
            if hasattr(self, 'exec_plugin_expiry') and not _is_expired(self.exec_plugin_expiry):
                return True
            base_path = self._get_base_path(self._cluster.path)
            status = await ExecProvider(self._user['exec']).run()
            if 'token' in status:
                self.token = "Bearer %s" % status['token']
                if 'expirationTimestamp' in status:
                    self.exec_plugin_expiry = parse_rfc3339(status['expirationTimestamp'])
            elif 'clientCertificateData' in status:
                # https://kubernetes.io/docs/reference/access-authn-authz/authentication/#input-and-output-formats
                # Plugin has provided certificates instead of a token.
                if 'clientKeyData' not in status:
                    logger.error('exec: missing clientKeyData field in '
                                 'plugin output')
                    return None
                self.cert_file = FileOrData(
                    status, None,
                    data_key_name='clientCertificateData',
                    file_base_path=base_path,
                    base64_file_content=False,
                    temp_file_path=self._temp_file_path).as_file()
                self.key_file = FileOrData(
                    status, None,
                    data_key_name='clientKeyData',
                    file_base_path=base_path,
                    base64_file_content=False,
                    temp_file_path=self._temp_file_path).as_file()
            else:
                logger.error('exec: missing token or clientCertificateData '
                             'field in plugin output')
            return True
        except Exception as e:
            logger.error(str(e))

    def _load_user_token(self):
        base_path = self._get_base_path(self._user.path)
        token = FileOrData(
            self._user, 'tokenFile', 'token',
            file_base_path=base_path,
            base64_file_content=False).as_data()
        if token:
            self.token = "Bearer %s" % token
            return True

    def _load_user_pass_token(self):
        if 'username' in self._user and 'password' in self._user:
            basic_auth = self._user['username'] + ':' + self._user['password']
            self.token = 'Basic ' + base64.b64encode(
                basic_auth.encode()).decode('utf-8')
            return True

    def _get_base_path(self, config_path):
        if self._config_base_path is not None:
            return self._config_base_path
        if config_path is not None:
            return os.path.abspath(os.path.dirname(config_path))
        return ""

    def _load_cluster_info(self):
        if 'server' in self._cluster:
            self.host = self._cluster['server'].rstrip('/')
            if self.host.startswith("https"):
                base_path = self._get_base_path(self._cluster.path)
                self.ssl_ca_cert = FileOrData(
                    self._cluster, 'certificate-authority',
                    file_base_path=base_path,
                    temp_file_path=self._temp_file_path).as_file()
                if 'cert_file' not in self.__dict__:
                    # cert_file could have been provided by
                    # _load_from_exec_plugin; only load from the _user
                    # section if we need it.
                    self.cert_file = FileOrData(
                        self._user, 'client-certificate',
                        file_base_path=base_path,
                        temp_file_path=self._temp_file_path).as_file()
                    self.key_file = FileOrData(
                        self._user, 'client-key',
                        file_base_path=base_path,
                        temp_file_path=self._temp_file_path).as_file()
        if 'insecure-skip-tls-verify' in self._cluster:
            self.verify_ssl = not self._cluster['insecure-skip-tls-verify']
        if 'tls-server-name' in self._cluster:
            self.tls_server_name = self._cluster['tls-server-name']
        if 'proxy-url' in self._cluster:
            self.proxy = self._cluster['proxy-url']

    def _set_config(self, client_configuration):

        if 'token' in self.__dict__:
            client_configuration.api_key['BearerToken'] = self.token

        # copy these keys directly from self to configuration object
        keys = ['host', 'ssl_ca_cert', 'cert_file', 'key_file',
                'verify_ssl', 'tls_server_name', 'proxy']
        for key in keys:
            if key in self.__dict__:
                setattr(client_configuration, key, getattr(self, key))

    async def load_and_set(self, client_configuration):
        await self._load_authentication()
        self._load_cluster_info()
        self._set_config(client_configuration)

    def list_contexts(self):
        return [context.value for context in self._config['contexts']]

    @property
    def current_context(self):
        return self._current_context.value


class ConfigNode(object):
    """Remembers each config key's path and construct a relevant exception
    message in case of missing keys. The assumption is all access keys are
    present in a well-formed kube-config."""

    def __init__(self, name, value, path=None):
        self.name = name
        self.value = value
        self.path = path

    def __contains__(self, key):
        return key in self.value

    def __len__(self):
        return len(self.value)

    def safe_get(self, key):
        if (isinstance(self.value, list) and isinstance(key, int) or
                (self.value and key in self.value)):
            return self.value[key]

    def __getitem__(self, key):
        v = self.safe_get(key)
        if v is None:
            raise ConfigException(
                'Invalid kube-config file. Expected key %s in %s'
                % (key, self.name))
        if isinstance(v, dict) or isinstance(v, list):
            return ConfigNode('%s/%s' % (self.name, key), v, self.path)
        else:
            return v

    def get_with_name(self, name, safe=False):
        if not isinstance(self.value, list):
            raise ConfigException(
                'Invalid kube-config file. Expected %s to be a list'
                % self.name)
        result = None
        for v in self.value:
            if 'name' not in v:
                raise ConfigException(
                    'Invalid kube-config file. '
                    'Expected all values in %s list to have \'name\' key'
                    % self.name)
            if v['name'] == name:
                if result is None:
                    result = v
                else:
                    raise ConfigException(
                        'Invalid kube-config file. '
                        'Expected only one object with name %s in %s list'
                        % (name, self.name))
        if result is not None:
            if isinstance(result, ConfigNode):
                return result
            else:
                return ConfigNode(
                    '%s[name=%s]' %
                    (self.name, name), result, self.path)
        if safe:
            return None
        raise ConfigException(
            'Invalid kube-config file. '
            'Expected object with name %s in %s list' % (name, self.name))


class KubeConfigMerger:

    """Reads and merges configuration from one or more kube-config's.
    The propery `config` can be passed to the KubeConfigLoader as config_dict.
    It uses a path attribute from ConfigNode to store the path to kubeconfig.
    This path is required to load certs from relative paths.
    A method `save_changes` updates changed kubeconfig's (it compares current
    state of dicts with).
    """

    def __init__(self, paths):
        self.paths = []
        self.config_files = {}
        self.config_merged = None

        file_loaded = False
        for path in paths.split(ENV_KUBECONFIG_PATH_SEPARATOR):
            if path:
                path = os.path.expanduser(path)
                if os.path.exists(path):
                    self.paths.append(path)
                    self.load_config(path)
                    file_loaded = True
        self.config_saved = copy.deepcopy(self.config_files)
        if not file_loaded:
            logger.warning('Config not found: %s', paths)

    @property
    def config(self):
        return self.config_merged

    def load_config(self, path):
        with open(path) as f:
            config = yaml.safe_load(f)

        if self.config_merged is None:
            config_merged = copy.deepcopy(config)
            for item in ('clusters', 'contexts', 'users'):
                config_merged[item] = []
            self.config_merged = ConfigNode(path, config_merged, path)

        for item in ('clusters', 'contexts', 'users'):
            self._merge(item, config.get(item, []) or [], path)

        if 'current-context' in config:
            self.config_merged.value['current-context'] = config['current-context']

        self.config_files[path] = config

    def _merge(self, item, add_cfg, path):
        for new_item in add_cfg:
            for exists in self.config_merged.value[item]:
                if exists['name'] == new_item['name']:
                    break
            else:
                self.config_merged.value[item].append(ConfigNode(
                    '{}/{}'.format(path, new_item), new_item, path))

    def save_changes(self):
        for path in self.paths:
            if self.config_saved[path] != self.config_files[path]:
                self.save_config(path)
        self.config_saved = copy.deepcopy(self.config_files)

    def save_config(self, path):
        with open(path, 'w') as f:
            yaml.safe_dump(self.config_files[path], f,
                           default_flow_style=False)


def _get_kube_config_loader_for_yaml_file(
        filename, persist_config=False, **kwargs):

    kcfg = KubeConfigMerger(filename)
    if persist_config and 'config_persister' not in kwargs:
        kwargs['config_persister'] = kcfg.save_changes()

    return KubeConfigLoader(
        config_dict=kcfg.config,
        config_base_path=None,
        **kwargs)


def list_kube_config_contexts(config_file=None):

    if config_file is None:
        config_file = os.path.expanduser(KUBE_CONFIG_DEFAULT_LOCATION)

    loader = _get_kube_config_loader_for_yaml_file(config_file)
    return loader.list_contexts(), loader.current_context


async def load_kube_config(config_file=None, context=None,
                           client_configuration=None,
                           persist_config=True,
                           temp_file_path=None):
    """Loads authentication and cluster information from kube-config file
    and stores them in kubernetes.client.configuration.

    :param config_file: Name of the kube-config file.
    :param context: set the active context. If is set to None, current_context
        from config file will be used.
    :param client_configuration: The kubernetes.client.Configuration to
        set configs to.
    :param persist_config: If True, config file will be updated when changed
        (e.g GCP token refresh).
    :param temp_file_path: directory where temp files are stored
        (default - system temp dir).
    """

    if config_file is None:
        config_file = KUBE_CONFIG_DEFAULT_LOCATION

    loader = _get_kube_config_loader_for_yaml_file(
        config_file, active_context=context,
        persist_config=persist_config,
        temp_file_path=temp_file_path)
    if client_configuration is None:
        config = type.__call__(Configuration)
        await loader.load_and_set(config)
        Configuration.set_default(config)
    else:
        await loader.load_and_set(client_configuration)

    return loader


async def load_kube_config_from_dict(config_dict, context=None,
                                     client_configuration=None,
                                     temp_file_path=None):
    """Loads authentication and cluster information from config_dict
    and stores them in kubernetes.client.configuration.

    :param config_dict: Takes the config file as a dict.
    :param context: set the active context. If is set to None, current_context
        from config file will be used.
    :param client_configuration: The kubernetes_asyncio.client.Configuration to
        set configs to.
    :param temp_file_path: directory where temp files are stored
        (default - system temp dir).
    """

    loader = KubeConfigLoader(
        config_dict=config_dict,
        config_base_path=None,
        active_context=context,
        temp_file_path=temp_file_path)

    if client_configuration is None:
        config = type.__call__(Configuration)
        await loader.load_and_set(config)
        Configuration.set_default(config)
    else:
        await loader.load_and_set(client_configuration)

    return loader


async def refresh_token(loader, client_configuration=None, interval=60):
    """Refresh token if necessary, updates the token in client configurarion

    :param loader: KubeConfigLoader returned by load_kube_config
    :param client_configuration: The kubernetes.client.Configuration to
            set configs to.
    :param interval: how often check if token is up-to-date

    """

    if client_configuration is None:
        raise NotImplementedError

    if loader.provider == 'gcp':
        while 1:
            await asyncio.sleep(interval)
            await loader.load_gcp_token()
            client_configuration.api_key['BearerToken'] = loader.token
    elif 'exec' in loader._user:
        while 1:
            await asyncio.sleep(interval)
            await loader.load_from_exec_plugin()
            client_configuration.api_key['BearerToken'] = loader.token


async def new_client_from_config(config_file=None, context=None, persist_config=True,
                                 temp_file_path=None):
    """Loads configuration the same as load_kube_config but returns an ApiClient
    to be used with any API object. This will allow the caller to concurrently
    talk with multiple clusters."""
    client_config = type.__call__(Configuration)

    await load_kube_config(config_file=config_file, context=context,
                           client_configuration=client_config,
                           persist_config=persist_config,
                           temp_file_path=temp_file_path)

    return ApiClient(configuration=client_config)


async def new_client_from_config_dict(config_dict=None, context=None,
                                      temp_file_path=None):
    """Loads configuration the same as load_kube_config_dict but returns an ApiClient
    to be used with any API object. This will allow the caller to concurrently
    talk with multiple clusters."""
    client_config = type.__call__(Configuration)

    await load_kube_config_from_dict(config_dict=config_dict, context=context,
                                     client_configuration=client_config,
                                     temp_file_path=temp_file_path)

    return ApiClient(configuration=client_config)
