#!/bin/bash

# Copyright 2021 The Kubernetes Authors.
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

# Workflow
# 1. [master branch] update existing snapshot (include API change for a new alpha/beta/GA
# release)
#   - add a new snapshot or reuse the existing snapshot, the latter means either
#     API change happened in a k8s patch release, or we want to include some new
#     python / python-base change in the release note
#   - API change w/ release notes
#   - master change w/ release notes
#   - submodule change w/ release notes
# 2. [master branch] create new snapshot (include API change for a new alpha release)
#   - add a new snapshot or reuse the existing snapshot, the latter means either
#     API change happened in a k8s patch release, or we want to include some new
#     python / python-base change in the release note
#   - API change w/ release notes
#   - master change w/ release notes
#   - submodule change w/ release notes
# 3. [release branch] create a new release
#   - pull master
#     - it's possible that master has new changes after the latest snaphost,
#       update CHANGELOG accordingly
#   - for generated file, resolve conflict by committing the master version
#   - abort if a snapshot doesn't exist
#   - generate client change, abort if API change is detected
#   - CHANGELOG: latest snapshot becomes the release, create a new snapshot
#     section that reflect the master branch state
#   - README: add the release to README
#   - an extra PR to update CHANGELOG and README in master in sync with this new
#     release
#
# Difference between 1&2: API change release notes
#
# TODO(roycaihw):
# - add user input validation
# - add function input validaiton (release/version strings start with 'v' or not)
# - automatically send a PR; provide useful links for review
#   - master branch diff: https://github.com/kubernetes-client/python/compare/commit1..commit2
#   - python base diff: https://github.com/kubernetes-client/python-base/compare/commit1..commit2
#   - Kubernetes changelog, e.g. https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.18.md
# - add debug log
# - add a sentence about "changes since {last release}". In most cases our
#   releases should be sequential. This script (the workflow above) is based on
#   this assumption, and we should make the release note clear about that.
# - update readme; if it's a real release (instead of a snapshot in master
#   branch), also create a PR to update changelog and readme in the master
#   branch
#
# Usage:
#   $ KUBERNETES_BRANCH=release-1.19 CLIENT_VERSION=19.0.0-snapshot DEVELOPMENT_STATUS="3 - Alpha" scripts/release.sh

set -o errexit
set -o nounset
set -o pipefail

# used by the client generator: https://github.com/kubernetes-client/gen/blob/729332ad08f0f4d98983b7beb027e2f657236ef9/openapi/openapi-generator/client-generator.sh#L52
export USERNAME=kubernetes

repo_root="$(git rev-parse --show-toplevel)"
declare -r repo_root
cd "${repo_root}"

source scripts/util/changelog.sh
source scripts/util/kube_changelog.sh

old_client_version=$(python3 "scripts/constants.py" CLIENT_VERSION)
old_k8s_api_version=$(util::changelog::get_k8s_api_version "v$old_client_version")
KUBERNETES_BRANCH=${KUBERNETES_BRANCH:-$(python3 "scripts/constants.py" KUBERNETES_BRANCH)}
CLIENT_VERSION=${CLIENT_VERSION:-$(python3 "scripts/constants.py" CLIENT_VERSION)}
DEVELOPMENT_STATUS=${DEVELOPMENT_STATUS:-$(python3 "scripts/constants.py" DEVELOPMENT_STATUS)}

# get Kubernetes API Version
new_k8s_api_version=$(util::kube_changelog::find_latest_patch_version $KUBERNETES_BRANCH)
echo "Old Kubernetes API Version: $old_k8s_api_version"
echo "New Kubernetes API Version: $new_k8s_api_version"

sed -i "s/^KUBERNETES_BRANCH =.*$/KUBERNETES_BRANCH = \"$KUBERNETES_BRANCH\"/g" scripts/constants.py
sed -i "s/^CLIENT_VERSION =.*$/CLIENT_VERSION = \"$CLIENT_VERSION\"/g" scripts/constants.py
sed -i "s/^DEVELOPMENT_STATUS =.*$/DEVELOPMENT_STATUS = \"$DEVELOPMENT_STATUS\"/g" scripts/constants.py
git commit -am "update version constants for $CLIENT_VERSION release"

util::changelog::update_release_api_version $CLIENT_VERSION $old_client_version $new_k8s_api_version

# get API change release notes since $old_k8s_api_version.
# NOTE: $old_k8s_api_version may be one-minor-version behind $KUBERNETES_BRANCH, e.g.
#   KUBERNETES_BRANCH=release-1.19
#   old_k8s_api_version=1.18.17
# when we bump the minor version for the snapshot in the master branch. We
# don't need to collect release notes in release-1.18, because any API
# change in 1.18.x (x > 17) must be a cherrypick that is already included in
# release-1.19.
# TODO(roycaihw): not all Kubernetes API changes modify the OpenAPI spec.
# Download the patch and skip if the spec is not modified. Also we want to
# look at other k/k sections like "deprecation"
release_notes=$(util::kube_changelog::get_api_changelog "$KUBERNETES_BRANCH" "$old_k8s_api_version")
if [[ -n "$release_notes" ]]; then
  util::changelog::write_changelog v$CLIENT_VERSION "### API Change" "$release_notes"
fi

git commit -am "update changelog"

# run client generator
scripts/update-client.sh

rm -r kubernetes/test/
git add .
git commit -m "temporary generated commit"
scripts/apply-hotfixes.sh
git reset HEAD~2
# custom object API is hosted in gen repo. Commit API change separately for
# easier review
if [[ -n "$(git diff kubernetes/client/api/custom_objects_api.py)" ]]; then
  git add kubernetes/client/api/custom_objects_api.py
  git commit -m "generated client change for custom_objects"
fi
git add kubernetes/docs kubernetes/client/api/ kubernetes/client/models/ kubernetes/swagger.json.unprocessed scripts/swagger.json
# verify if there are staged changes, then commit
git diff-index --quiet --cached HEAD || git commit -m "generated API change"
git add .
git commit -m "generated client change"
echo "Release finished successfully."
