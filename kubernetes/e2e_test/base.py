# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import copy
import os
import unittest
import urllib3

from kubernetes.client.configuration import configuration
from kubernetes.config import kube_config

DEFAULT_E2E_HOST = '127.0.0.1'


def get_e2e_configuration():
    config = copy.copy(configuration)
    config.host = None
    default_config_path = os.path.expanduser(kube_config.KUBE_CONFIG_DEFAULT_LOCATION)
    if os.path.exists(default_config_path):
        print("Loaded config from %s" % default_config_path)
        kube_config.load_kube_config(client_configuration=config)
        kube_config.load_kube_config()
    else:
        print('Unable to load config from %s' % default_config_path)
        for url in ['https://%s:8443' % DEFAULT_E2E_HOST,
                    'http://%s:8080' % DEFAULT_E2E_HOST]:
            try:
                urllib3.PoolManager().request('GET', url)
                config.host = url
                config.verify_ssl = False
                urllib3.disable_warnings()
                break
            except urllib3.exceptions.HTTPError:
                pass
        config.assert_hostname = False
    if config.host is None:
        raise unittest.SkipTest('Unable to find a running Kubernetes instance')
    print('Running test against : %s' % config.host)
    return config
