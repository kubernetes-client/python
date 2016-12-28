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

import base64
import os
import shutil
import tempfile
import unittest
import yaml
from six import PY3

from .config_exception import ConfigException
from .kube_config import (ConfigNode, FileOrData, KubeConfigLoader,
                          _cleanup_temp_files, _create_temp_file_with_content,
                          load_kube_config, list_kube_config_contexts,
                          new_client_from_config)

BEARER_TOKEN_FORMAT = "Bearer %s"

NON_EXISTING_FILE = "zz_non_existing_file_472398324"


def _base64(string):
    return base64.encodestring(string.encode()).decode()


TEST_FILE_KEY = "file"
TEST_DATA_KEY = "data"
TEST_FILENAME = "test-filename"

TEST_DATA = "test-data"
TEST_DATA_BASE64 = _base64(TEST_DATA)

TEST_ANOTHER_DATA = "another-test-data"
TEST_ANOTHER_DATA_BASE64 = _base64(TEST_ANOTHER_DATA)

TEST_HOST = "test-host"
TEST_USERNAME = "me"
TEST_PASSWORD = "pass"
# token for me:pass
TEST_BASIC_TOKEN = "Basic bWU6cGFzcw=="

TEST_SSL_HOST = "https://test-host"
TEST_CERTIFICATE_AUTH = "cert-auth"
TEST_CERTIFICATE_AUTH_BASE64 = _base64(TEST_CERTIFICATE_AUTH)
TEST_CLIENT_KEY = "client-key"
TEST_CLIENT_KEY_BASE64 = _base64(TEST_CLIENT_KEY)
TEST_CLIENT_CERT = "client-cert"
TEST_CLIENT_CERT_BASE64 = _base64(TEST_CLIENT_CERT)


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self._temp_files = []

    def tearDown(self):
        for f in self._temp_files:
            os.remove(f)

    def _create_temp_file(self, content=""):
        handler, name = tempfile.mkstemp()
        self._temp_files.append(name)
        os.write(handler, str.encode(content))
        os.close(handler)
        return name

    def expect_exception(self, func, message_part):
        with self.assertRaises(ConfigException) as context:
            func()
        self.assertIn(message_part, str(context.exception))


class TestFileOrData(BaseTestCase):

    @staticmethod
    def get_file_content(filename):
        with open(filename) as f:
            return f.read()

    def test_file_given_file(self):
        temp_filename = _create_temp_file_with_content(TEST_DATA)
        obj = {TEST_FILE_KEY: temp_filename}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_given_non_existing_file(self):
        temp_filename = NON_EXISTING_FILE
        obj = {TEST_FILE_KEY: temp_filename}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.expect_exception(t.as_file, "does not exists")

    def test_file_given_data(self):
        obj = {TEST_DATA_KEY: TEST_DATA_BASE64}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_data_given_data(self):
        obj = {TEST_DATA_KEY: TEST_DATA_BASE64}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_data_given_file(self):
        obj = {
            TEST_FILE_KEY: self._create_temp_file(content=TEST_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_data_given_file_and_data(self):
        obj = {
            TEST_DATA_KEY: TEST_DATA_BASE64,
            TEST_FILE_KEY: self._create_temp_file(
                content=TEST_ANOTHER_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA_BASE64, t.as_data())

    def test_file_given_file_and_data(self):
        obj = {
            TEST_DATA_KEY: TEST_DATA_BASE64,
            TEST_FILE_KEY: self._create_temp_file(
                content=TEST_ANOTHER_DATA)}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       data_key_name=TEST_DATA_KEY)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_file_with_custom_dirname(self):
        tempfile = self._create_temp_file(content=TEST_DATA)
        tempfile_dir = os.path.dirname(tempfile)
        tempfile_basename = os.path.basename(tempfile)
        obj = {TEST_FILE_KEY: tempfile_basename}
        t = FileOrData(obj=obj, file_key_name=TEST_FILE_KEY,
                       file_base_path=tempfile_dir)
        self.assertEqual(TEST_DATA, self.get_file_content(t.as_file()))

    def test_create_temp_file_with_content(self):
        self.assertEqual(TEST_DATA,
                         self.get_file_content(
                             _create_temp_file_with_content(TEST_DATA)))
        _cleanup_temp_files()


class TestConfigNode(BaseTestCase):

    test_obj = {"key1": "test", "key2": ["a", "b", "c"],
                "key3": {"inner_key": "inner_value"},
                "with_names": [{"name": "test_name", "value": "test_value"},
                               {"name": "test_name2",
                                "value": {"key1", "test"}},
                               {"name": "test_name3", "value": [1, 2, 3]}]}

    def setUp(self):
        super(TestConfigNode, self).setUp()
        self.node = ConfigNode("test_obj", self.test_obj)

    def test_normal_map_array_operations(self):
        self.assertEqual("test", self.node['key1'])
        self.assertEqual(4, len(self.node))

        self.assertEqual("test_obj/key2", self.node['key2'].name)
        self.assertEqual(["a", "b", "c"], self.node['key2'].value)
        self.assertEqual("b", self.node['key2'][1])
        self.assertEqual(3, len(self.node['key2']))

        self.assertEqual("test_obj/key3", self.node['key3'].name)
        self.assertEqual({"inner_key": "inner_value"}, self.node['key3'].value)
        self.assertEqual("inner_value", self.node['key3']["inner_key"])
        self.assertEqual(1, len(self.node['key3']))

    def test_get_with_name(self):
        node = self.node["with_names"]
        self.assertEqual(
            "test_value",
            node.get_with_name("test_name")["value"])
        self.assertTrue(
            isinstance(node.get_with_name("test_name2"), ConfigNode))
        self.assertTrue(
            isinstance(node.get_with_name("test_name3"), ConfigNode))
        self.assertEqual("test_obj/with_names[name=test_name2]",
                         node.get_with_name("test_name2").name)
        self.assertEqual("test_obj/with_names[name=test_name3]",
                         node.get_with_name("test_name3").name)

    def test_key_does_not_exists(self):
        self.expect_exception(lambda: self.node['not-exists-key'],
                              "Expected key not-exists-key in test_obj")
        self.expect_exception(lambda: self.node['key3']['not-exists-key'],
                              "Expected key not-exists-key in test_obj/key3")

    def test_get_with_name_on_invalid_object(self):
        self.expect_exception(
            lambda: self.node['key2'].get_with_name('no-name'),
            "Expected all values in test_obj/key2 list to have \'name\' key")

    def test_get_with_name_on_non_list_object(self):
        self.expect_exception(
            lambda: self.node['key3'].get_with_name('no-name'),
            "Expected test_obj/key3 to be a list")

    def test_get_with_name_on_name_does_not_exists(self):
        self.expect_exception(
            lambda: self.node['with_names'].get_with_name('no-name'),
            "Expected object with name no-name in test_obj/with_names list")


class FakeConfig:

    FILE_KEYS = ["ssl_ca_cert", "key_file", "cert_file"]

    def __init__(self, token=None, **kwargs):
        self.api_key = {}
        if token:
            self.api_key['authorization'] = token

        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if len(self.__dict__) != len(other.__dict__):
            return
        for k, v in self.__dict__.items():
            if k not in other.__dict__:
                return
            if k in self.FILE_KEYS:
                try:
                    with open(v) as f1, open(other.__dict__[k]) as f2:
                        if f1.read() != f2.read():
                            return
                except IOError:
                    # fall back to only compare filenames in case we are
                    # testing the passing of filenames to the config
                    if other.__dict__[k] != v:
                        return
            else:
                if other.__dict__[k] != v:
                    return
        return True

    def __repr__(self):
        rep = "\n"
        for k, v in self.__dict__.items():
            val = v
            if k in self.FILE_KEYS:
                try:
                    with open(v) as f:
                        val = "FILE: %s" % str.decode(f.read())
                except IOError as e:
                    val = "ERROR: %s" % str(e)
            rep += "\t%s: %s\n" % (k, val)
        return "Config(%s\n)" % rep


class TestKubeConfigLoader(BaseTestCase):
    TEST_KUBE_CONFIG = {
        "current-context": "no_user",
        "contexts": [
            {
                "name": "no_user",
                "context": {
                    "cluster": "default"
                }
            },
            {
                "name": "simple_token",
                "context": {
                    "cluster": "default",
                    "user": "simple_token"
                }
            },
            {
                "name": "gcp",
                "context": {
                    "cluster": "default",
                    "user": "gcp"
                }
            },
            {
                "name": "user_pass",
                "context": {
                    "cluster": "default",
                    "user": "user_pass"
                }
            },
            {
                "name": "ssl",
                "context": {
                    "cluster": "ssl",
                    "user": "ssl"
                }
            },
            {
                "name": "ssl-no_file",
                "context": {
                    "cluster": "ssl-no_file",
                    "user": "ssl-no_file"
                }
            },
            {
                "name": "ssl-local-file",
                "context": {
                    "cluster": "ssl-local-file",
                    "user": "ssl-local-file"
                }
            },
        ],
        "clusters": [
            {
                "name": "default",
                "cluster": {
                    "server": TEST_HOST
                }
            },
            {
                "name": "ssl-no_file",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority": TEST_CERTIFICATE_AUTH,
                }
            },
            {
                "name": "ssl-local-file",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority": "cert_test",
                }
            },
            {
                "name": "ssl",
                "cluster": {
                    "server": TEST_SSL_HOST,
                    "certificate-authority-data": TEST_CERTIFICATE_AUTH_BASE64,
                }
            },
        ],
        "users": [
            {
                "name": "simple_token",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "gcp",
                "user": {
                    "auth-provider": {
                        "name": "gcp",
                        "access_token": "not_used",
                    },
                    "token": TEST_DATA_BASE64,  # should be ignored
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "user_pass",
                "user": {
                    "username": TEST_USERNAME,  # should be ignored
                    "password": TEST_PASSWORD,  # should be ignored
                }
            },
            {
                "name": "ssl-no_file",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "client-certificate": TEST_CLIENT_CERT,
                    "client-key": TEST_CLIENT_KEY,
                }
            },
            {
                "name": "ssl-local-file",
                "user": {
                    "tokenFile": "token_file",
                    "client-certificate": "client_cert",
                    "client-key": "client_key",
                }
            },
            {
                "name": "ssl",
                "user": {
                    "token": TEST_DATA_BASE64,
                    "client-certificate-data": TEST_CLIENT_CERT_BASE64,
                    "client-key-data": TEST_CLIENT_KEY_BASE64,
                }
            },
        ]
    }

    def test_no_user_context(self):
        expected = FakeConfig(host=TEST_HOST)
        actual = FakeConfig()
        KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="no_user",
            client_configuration=actual).load_and_set()
        self.assertEqual(expected, actual)

    def test_simple_token(self):
        expected = FakeConfig(host=TEST_HOST,
                              token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        actual = FakeConfig()
        KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="simple_token",
            client_configuration=actual).load_and_set()
        self.assertEqual(expected, actual)

    def test_load_user_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="simple_token")
        self.assertTrue(loader._load_user_token())
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64, loader.token)

    def test_gcp(self):
        expected = FakeConfig(
            host=TEST_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_ANOTHER_DATA_BASE64)
        actual = FakeConfig()
        KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="gcp",
            client_configuration=actual,
            get_google_credentials=lambda: TEST_ANOTHER_DATA_BASE64) \
            .load_and_set()
        self.assertEqual(expected, actual)

    def test_load_gcp_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="gcp",
            get_google_credentials=lambda: TEST_ANOTHER_DATA_BASE64)
        self.assertTrue(loader._load_gcp_token())
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_ANOTHER_DATA_BASE64,
                         loader.token)

    def test_user_pass(self):
        expected = FakeConfig(host=TEST_HOST, token=TEST_BASIC_TOKEN)
        actual = FakeConfig()
        KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="user_pass",
            client_configuration=actual).load_and_set()
        self.assertEqual(expected, actual)

    def test_load_user_pass_token(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="user_pass")
        self.assertTrue(loader._load_user_pass_token())
        self.assertEqual(TEST_BASIC_TOKEN, loader.token)

    def test_ssl_no_cert_files(self):
        actual = FakeConfig()
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="ssl-no_file",
            client_configuration=actual)
        self.expect_exception(loader.load_and_set, "does not exists")

    def test_ssl(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            ssl_ca_cert=self._create_temp_file(TEST_CERTIFICATE_AUTH)
        )
        actual = FakeConfig()
        KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="ssl",
            client_configuration=actual).load_and_set()
        self.assertEqual(expected, actual)

    def test_list_contexts(self):
        loader = KubeConfigLoader(
            config_dict=self.TEST_KUBE_CONFIG,
            active_context="no_user")
        actual_contexts = loader.list_contexts()
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        for actual in actual_contexts:
            expected = expected_contexts.get_with_name(actual['name'])
            self.assertEqual(expected.value, actual)

    def test_current_context(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        self.assertEqual(expected_contexts.get_with_name("no_user").value,
                         loader.current_context)

    def test_set_active_context(self):
        loader = KubeConfigLoader(config_dict=self.TEST_KUBE_CONFIG)
        loader.set_active_context("ssl")
        expected_contexts = ConfigNode("", self.TEST_KUBE_CONFIG)['contexts']
        self.assertEqual(expected_contexts.get_with_name("ssl").value,
                         loader.current_context)

    def test_ssl_with_relative_ssl_files(self):
        expected = FakeConfig(
            host=TEST_SSL_HOST,
            token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
            cert_file=self._create_temp_file(TEST_CLIENT_CERT),
            key_file=self._create_temp_file(TEST_CLIENT_KEY),
            ssl_ca_cert=self._create_temp_file(TEST_CERTIFICATE_AUTH)
        )
        try:
            temp_dir = tempfile.mkdtemp()
            actual = FakeConfig()
            with open(os.path.join(temp_dir, "cert_test"), "wb") as fd:
                fd.write(TEST_CERTIFICATE_AUTH.encode())
            with open(os.path.join(temp_dir, "client_cert"), "wb") as fd:
                fd.write(TEST_CLIENT_CERT.encode())
            with open(os.path.join(temp_dir, "client_key"), "wb") as fd:
                fd.write(TEST_CLIENT_KEY.encode())
            with open(os.path.join(temp_dir, "token_file"), "wb") as fd:
                fd.write(TEST_DATA.encode())
            KubeConfigLoader(
                config_dict=self.TEST_KUBE_CONFIG,
                active_context="ssl-local-file",
                config_base_path=temp_dir,
                client_configuration=actual).load_and_set()
            self.assertEqual(expected, actual)
        finally:
            shutil.rmtree(temp_dir)

    def test_load_kube_config(self):
        expected = FakeConfig(host=TEST_HOST,
                              token=BEARER_TOKEN_FORMAT % TEST_DATA_BASE64)
        config_file = self._create_temp_file(yaml.dump(self.TEST_KUBE_CONFIG))
        actual = FakeConfig()
        load_kube_config(config_file=config_file,context="simple_token",
                         client_configuration=actual)
        self.assertEqual(expected, actual)

    def test_list_kube_config_contexts(self):
        config_file = self._create_temp_file(yaml.dump(self.TEST_KUBE_CONFIG))
        contexts, active_context = list_kube_config_contexts(
            config_file=config_file)
        self.assertDictEqual(self.TEST_KUBE_CONFIG['contexts'][0],
                             active_context)
        if PY3:
            self.assertCountEqual(self.TEST_KUBE_CONFIG['contexts'],
                                  contexts)
        else:
            self.assertItemsEqual(self.TEST_KUBE_CONFIG['contexts'],
                                  contexts)

    def test_new_client_from_config(self):
        config_file = self._create_temp_file(yaml.dump(self.TEST_KUBE_CONFIG))
        client = new_client_from_config(
            config_file=config_file, context="simple_token")
        self.assertEqual(TEST_HOST, client.config.host)
        self.assertEqual(BEARER_TOKEN_FORMAT % TEST_DATA_BASE64,
                         client.config.api_key['authorization'])


if __name__ == '__main__':
    unittest.main()
