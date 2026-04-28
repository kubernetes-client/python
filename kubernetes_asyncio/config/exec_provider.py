# Copyright 2018 The Kubernetes Authors.
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
import asyncio.subprocess
import json
import os
import sys

from .config_exception import ConfigException


class ExecProvider(object):
    """
    Implementation of the proposal for out-of-tree client authentication providers
    as described here --
    https://github.com/kubernetes/community/blob/master/contributors/design-proposals/auth/kubectl-exec-plugins.md

    Missing from implementation:

    * TLS cert support
    * caching
    """

    def __init__(self, exec_config):
        for key in ['command', 'apiVersion']:
            if key not in exec_config:
                raise ConfigException(
                    'exec: malformed request. missing key \'%s\'' % key)
        self.api_version = exec_config['apiVersion']
        self.args = [exec_config['command']]
        if exec_config.safe_get('args'):
            self.args.extend(exec_config['args'])
        self.env = os.environ.copy()
        if exec_config.safe_get('env'):
            additional_vars = {}
            for item in exec_config['env']:
                name = item['name']
                value = item['value']
                additional_vars[name] = value
            self.env.update(additional_vars)

    async def run(self, previous_response=None):
        # Validate the run can be executed on Windows
        if type(asyncio.get_event_loop()).__name__ == '_WindowsSelectorEventLoop':
            raise ConfigException(
                'exec: _WindowsSelectorEventLoop does NOT support subprocesses, see README.md'
            )

        kubernetes_exec_info = {
            'apiVersion': self.api_version,
            'kind': 'ExecCredential',
            'spec': {
                'interactive': sys.stdout.isatty()
            }
        }
        if previous_response:
            kubernetes_exec_info['spec']['response'] = previous_response
        self.env['KUBERNETES_EXEC_INFO'] = json.dumps(kubernetes_exec_info)

        cmd_exec = asyncio.create_subprocess_exec(*self.args,
                                                  env=self.env,
                                                  stdin=None,
                                                  stdout=asyncio.subprocess.PIPE,
                                                  stderr=asyncio.subprocess.PIPE)
        proc = await cmd_exec

        stdout = await proc.stdout.read()
        stderr = await proc.stderr.read()
        exit_code = await proc.wait()

        if exit_code != 0:
            msg = 'exec: process returned %d' % exit_code
            stderr = stderr.strip()
            if stderr:
                msg += '. %s' % stderr
            raise ConfigException(msg)
        try:
            data = json.loads(stdout)
        except ValueError as de:
            raise ConfigException(
                'exec: failed to decode process output: %s' % de)
        for key in ('apiVersion', 'kind', 'status'):
            if key not in data:
                raise ConfigException(
                    'exec: malformed response. missing key \'%s\'' % key)
        if data['apiVersion'] != self.api_version:
            raise ConfigException(
                'exec: plugin api version %s does not match %s' %
                (data['apiVersion'], self.api_version))
        return data['status']
