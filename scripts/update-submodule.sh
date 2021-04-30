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


# Update python-base submodule and collect release notes.
# Usage:
#
#   $ scripts/update-submodule.sh
#
#   # To update the release notes for a specific release (e.g. v18.17.0a1):
#   $ TARGET_RELEASE="v18.17.0a1" scripts/update-submodule.sh
#
# After the script finishes, please create a commit "generated python-base update"
# and send a PR to this repository.
# TODO(roycaihw): make the script send a PR

set -o errexit
set -o nounset
set -o pipefail

repo_root="$(git rev-parse --show-toplevel)"
declare -r repo_root
cd "${repo_root}"

source scripts/util/changelog.sh
go get k8s.io/release/cmd/release-notes

TARGET_RELEASE=${TARGET_RELEASE:-"v$(grep "^CLIENT_VERSION = \"" scripts/constants.py | sed "s/CLIENT_VERSION = \"//g" | sed "s/\"//g")"}

# update submodule
git submodule update --remote

# download release notes
start_sha=$(git diff | grep "^-Subproject commit " | sed 's/-Subproject commit //g')
end_sha=$(git diff | grep "^+Subproject commit " | sed 's/+Subproject commit //g')
output="/tmp/python-base-relnote.md"
release-notes --dependencies=false --org kubernetes-client --repo python-base --start-sha $start_sha --end-sha $end_sha --output $output
sed -i 's/(\[\#/(\[kubernetes-client\/python-base\#/g' $output

# update changelog
IFS_backup=$IFS
IFS=$'\n'
sections=($(grep "^### " $output))
IFS=$IFS_backup
for section in "${sections[@]}"; do
  # ignore section titles and empty lines; replace newline with liternal "\n"
  release_notes=$(sed -n "/$section/,/###/{/###/!p}" $output | sed -n "{/^$/!p}" | sed ':a;N;$!ba;s/\n/\\n/g')
  util::changelog::write_changelog "$TARGET_RELEASE" "$section" "$release_notes"
done

rm -f $output
echo "Successfully updated CHANGELOG for submodule."
