# Copyright 2017 The Kubernetes Authors.
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
import unittest
import urllib3

from mock import patch

from kubernetes.client import Configuration
from kubernetes.client.rest import RESTClientObject


class RestTest(unittest.TestCase):

    def test_poolmanager(self):
        'Test that a poolmanager is created for rest client'
        with patch.object(urllib3, 'PoolManager') as pool:
            RESTClientObject(config=Configuration())
            pool.assert_called_once()

    def test_proxy(self):
        'Test that proxy is created when the config especifies it'
        config = Configuration()
        config.http_proxy_url = 'http://proxy.example.com'

        with patch.object(urllib3, 'proxy_from_url') as proxy:
            RESTClientObject(config=config)
            proxy.assert_called_once()


if __name__ == '__main__':
    unittest.main()
