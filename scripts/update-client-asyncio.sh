#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
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

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="$(dirname ${SCRIPT_ROOT})/kubernetes_asyncio"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)_asyncio
DEVELOPMENT_STATUS=$(python "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

source ${SCRIPT_ROOT}/util/common.sh
util::common::check_sed

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

TEMP_FOLDER=$(mktemp -d) 
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

SETTING_FILE="${TEMP_FOLDER}/settings"
echo "export KUBERNETES_BRANCH=\"$(python ${SCRIPT_ROOT}/constants.py KUBERNETES_BRANCH)\"" > $SETTING_FILE
echo "export CLIENT_VERSION=\"$(python ${SCRIPT_ROOT}/constants.py CLIENT_VERSION)\"" >> $SETTING_FILE
echo "export PACKAGE_NAME=\"client\"" >> $SETTING_FILE

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
fi

echo ">>> Running python generator from the gen repo"
"${GEN_ROOT}/openapi/python-asyncio.sh" "${CLIENT_ROOT}" "${SETTING_FILE}"
mv "${CLIENT_ROOT}/swagger.json" "${SCRIPT_ROOT}/swagger.json"

echo ">>> updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup-asyncio.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup-asyncio.py"
sed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup-asyncio.py"

echo ">>> fix generated api client for patching with strategic merge..."
patch "${CLIENT_ROOT}/client/api_client.py" "${SCRIPT_ROOT}/asyncio/api_client_strategic_merge_patch.diff"
echo ">>> fix generated api client by adding 'none' check..."
patch "${CLIENT_ROOT}/client/api_client.py" "${SCRIPT_ROOT}/asyncio/api_client_response_types_map_patch.diff"
echo ">>> fix generated rest client by accepting application/apply-patch+yaml content type"
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/asyncio/rest_client_apply_patch_patch.diff"
echo ">>> fix generated rest client by increasing aiohttp read buffer to 2MiB..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/asyncio/rest_client_patch_read_bufsize.diff"
echo ">>> fix generated rest client and configuration to support customer server hostname TLS verification..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/asyncio/rest_client_server_hostname_patch.diff"
patch "${CLIENT_ROOT}/client/configuration.py" "${SCRIPT_ROOT}/asyncio/client_configuration_tls_server_name_patch.diff"
echo ">>> fix generated rest client and configuration to support disabling strict TLS verification..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/asyncio/rest_client_disable_ssl_strict_verification_patch.diff"
patch "${CLIENT_ROOT}/client/configuration.py" "${SCRIPT_ROOT}/asyncio/client_configuration_disable_ssl_strict_verification_patch.diff"
echo ">>> fix generated rest client by handling timeout correctly..."
patch -R "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/asyncio/rest_client_timeout.diff"

echo ">>> don't deep-copy configuration for local_vars_configuration in models"
patch "${CLIENT_ROOT}/client/configuration.py" "${SCRIPT_ROOT}/asyncio/client_configuration_get_default_patch.diff"
find "${CLIENT_ROOT}/client/models/" -type f -print0 | xargs -0 sed -i 's/local_vars_configuration = Configuration.get_default_copy()/local_vars_configuration = Configuration.get_default()/g'

echo ">>> fix generated api client and configuration for async token refreshing..."
patch "${CLIENT_ROOT}/client/api_client.py" "${SCRIPT_ROOT}/asyncio/api_client_async_refresh_api_key_hook.diff"
patch "${CLIENT_ROOT}/client/configuration.py" "${SCRIPT_ROOT}/asyncio/client_configuration_async_refresh_api_key_hook.diff"

echo ">>> Remove invalid tests (workaround https://github.com/OpenAPITools/openapi-generator/issues/5377)"
grep -r make_instance "${CLIENT_ROOT}/test/" | awk '{ gsub(":", ""); print $1}' | sort | uniq | xargs rm

echo ">>> Fix API tests (https://github.com/aio-libs/aiohttp/issues/8555)"
find "${CLIENT_ROOT}/test/" -type f -print0 | xargs -0 sed -i -e 's/unittest.TestCase/unittest.IsolatedAsyncioTestCase/g' -e 's/def setUp(self):/async def asyncSetUp(self):/g'

echo ">>> Done."
