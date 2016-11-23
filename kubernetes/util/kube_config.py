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

import atexit
import base64
import os
import tempfile

import urllib3
import yaml
from kubernetes.client import configuration
from oauth2client.client import GoogleCredentials

_temp_files = []


def _cleanup_temp_files():
    for f in _temp_files:
        os.remove(f)


def _create_temp_file_with_content(content):
    if len(_temp_files) == 0:
        atexit.register(_cleanup_temp_files)
    _, name = tempfile.mkstemp()
    _temp_files.append(name)
    if isinstance(content, str):
        content = content.encode('utf8')
    with open(name, 'wb') as fd:
        fd.write(base64.decodestring(content))
    return name


def _file_from_file_or_data(o, file_key_name, data_key_name=None):
    if not data_key_name:
        data_key_name = file_key_name + "-data"
    if data_key_name in o:
        return _create_temp_file_with_content(o[data_key_name])
    if file_key_name in o:
        return o[file_key_name]


def _data_from_file_or_data(o, file_key_name, data_key_name=None):
    if not data_key_name:
        data_key_name = file_key_name + "_data"
    if data_key_name in o:
        return o[data_key_name]
    if file_key_name in o:
        with open(o[file_key_name], 'r') as f:
            data = f.read()
        return data


def _load_gcp_token(user):
    if 'auth-provider' not in user:
        return
    if 'name' not in user['auth-provider']:
        return
    if user['auth-provider']['name'] != 'gcp':
        return
    # Ignore configs in auth-provider and rely on GoogleCredentials
    # caching and refresh mechanism.
    # TODO: support gcp command based token ("cmd-path" config).
    return (GoogleCredentials
            .get_application_default()
            .get_access_token()
            .access_token)


def _load_authentication(user):
    """Read authentication from kube-config user section.

    This function goes through various authetication methods in user section of
    kubeconfig and stops if it founds a valid authentication method. The order
    of authentication methods is:

        1. GCP auth-provider
        2. token_data
        3. token field (point to a token file)
        4. username/password
    """
    # Read authentication
    token = _load_gcp_token(user)
    if not token:
        token = _data_from_file_or_data(user, 'tokenFile', 'token')
    if token:
        configuration.api_key['authorization'] = "bearer " + token
    else:
        if 'username' in user and 'password' in user:
            configuration.api_key['authorization'] = urllib3.util.make_headers(
                basic_auth=user['username'] + ':' +
                user['password']).get('authorization')


def _load_cluster_info(cluster, user):
    """Loads cluster information from kubeconfig such as host and SSL certs."""
    if 'server' in cluster:
        configuration.host = cluster['server']
        if configuration.host.startswith("https"):
            configuration.ssl_ca_cert = _file_from_file_or_data(
                cluster, 'certificate-authority')
            configuration.cert_file = _file_from_file_or_data(
                user, 'client-certificate')
            configuration.key_file = _file_from_file_or_data(
                user, 'client-key')


class _node:
    """Remembers each key's path and construct a relevant exception message
    in case of missing keys."""

    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __contains__(self, key):
        return key in self._value

    def __getitem__(self, key):
        if key in self._value:
            v = self._value[key]
            if isinstance(v, dict) or isinstance(v, list):
                return _node('%s/%s' % (self._name, key), v)
            else:
                return v
        raise Exception(
            'Invalid kube-config file. Expected key %s in %s'
            % (key, self._name))

    def get_with_name(self, name):
        if not isinstance(self._value, list):
            raise Exception(
                'Invalid kube-config file. Expected %s to be a list'
                % self._name)
        for v in self._value:
            if 'name' not in v:
                raise Exception(
                    'Invalid kube-config file. '
                    'Expected all values in %s list to have \'name\' key'
                    % self._name)
            if v['name'] == name:
                return _node('%s[name=%s]' % (self._name, name), v)
        raise Exception(
            "Cannot find object with name %s in %s list" % (name, self._name))


def load_kube_config(config_file):
    """Loads authentication and cluster information from kube-config file
    and store them in kubernetes.client.configuration."""

    with open(config_file) as f:
        config = _node('kube-config', yaml.load(f))

        current_context = config['contexts'].get_with_name(
            config['current-context'])['context']
        user = config['users'].get_with_name(current_context['user'])['user']
        cluster = config['clusters'].get_with_name(
            current_context['cluster'])['cluster']

        _load_cluster_info(cluster, user)
        _load_authentication(user)
