# Copyright 2026 The Kubernetes Authors.
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

import importlib
import pkgutil
import unittest
from unittest import mock
import warnings

import kubernetes.client.api


def _import_alias():
    # The alias installs its own 'default' filter for its DeprecationWarning,
    # so record the warning instead of trying to filter it out.
    with warnings.catch_warnings(record=True):
        return importlib.import_module('kubernetes.client.apis')


class TestApisAlias(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.apis = _import_alias()

    def test_from_import_submodule(self):
        from kubernetes.client.apis import core_v1_api

        self.assertIs(
            core_v1_api,
            importlib.import_module('kubernetes.client.api.core_v1_api'))

    def test_every_api_submodule_is_reachable(self):
        names = [m.name for m in pkgutil.iter_modules(
            kubernetes.client.api.__path__)]
        self.assertIn('core_v1_api', names)
        for name in names:
            with self.subTest(name=name):
                self.assertIs(
                    getattr(self.apis, name),
                    importlib.import_module('kubernetes.client.api.' + name))

    def test_from_import_class(self):
        from kubernetes.client.apis import CoreV1Api

        self.assertIs(CoreV1Api, kubernetes.client.api.CoreV1Api)

    def test_unknown_name(self):
        with self.assertRaises(ImportError):
            from kubernetes.client.apis import no_such_api  # noqa: F401
        self.assertFalse(hasattr(self.apis, 'no_such_api'))

    def test_non_submodule_names_are_not_imported(self):
        with mock.patch('kubernetes.client.apis._import_module') as m:
            for name in ('__wrapped__', '_no_such_api', '.core_v1_api'):
                with self.subTest(name=name):
                    self.assertFalse(hasattr(self.apis, name))
        m.assert_not_called()

    def test_missing_dependency_propagates(self):
        error = ModuleNotFoundError("No module named 'missing_dep'",
                                    name='missing_dep')
        with mock.patch('kubernetes.client.apis._import_module',
                        side_effect=error):
            with self.assertRaises(ModuleNotFoundError) as cm:
                self.apis.core_v1_api
        self.assertIs(cm.exception, error)


if __name__ == '__main__':
    unittest.main()
