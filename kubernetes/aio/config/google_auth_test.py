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

from unittest import IsolatedAsyncioTestCase

from .google_auth import google_auth_credentials


class TestGoogleAuth(IsolatedAsyncioTestCase):

    async def test_google_auth_credentials(self):

        provider = {
            'cmd-path': '/bin/echo',
            'cmd-args': '{\\"credential\\": {\\"access_token\\": \\"token\\", '
                        '\\"token_expiry\\": \\"2001.01.01T00:00:00Z\\"}}'
        }

        ret = await google_auth_credentials(provider)

        self.assertEqual(ret.token, 'token')
        self.assertEqual(ret.expiry, '2001.01.01T00:00:00Z')

    async def test_google_auth_credentials_exception(self):

        with self.assertRaisesRegex(ValueError, "cmd-path, cmd-args are required."):
            await google_auth_credentials({})
