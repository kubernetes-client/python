#!/bin/bash

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

set -o errexit
set -o nounset
set -o pipefail

RUNNING_DIR=$(pwd)
TMP_DIR=$(mktemp -d)

function cleanup()
{
  cd "${RUNNING_DIR}"
}
trap cleanup EXIT SIGINT


SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

cd "${TMP_DIR}"
git clone https://github.com/kubernetes-client/python.git
cd python
git config user.email "kubernetes-client@k8s.com"
git config user.name "kubenetes client"
git rm -rf kubernetes/base
git commit -m "DO NOT MERGE, removing submodule for testing only"
mkdir kubernetes/base
cp -r "${SCRIPT_ROOT}/." kubernetes/base
rm -rf kubernetes/base/.git
rm -rf kubernetes/base/.tox
git add kubernetes/base
git commit -m "DO NOT MERGE, adding changes for testing."
git status

echo "Running tox from the main repo on $TOXENV environment"
# Run the user-provided command.
"${@}"
