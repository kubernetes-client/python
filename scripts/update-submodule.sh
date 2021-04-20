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
#   scripts/update-submodule.sh
#
# Create a commit "generated python-base update" and send a PR to the main repo.
# NOTE: not all python-base changes are user-facing, and you may want to remove
# some of the non-user-facing release notes from CHANGELOG.md.

set -o errexit
set -o nounset
set -o pipefail

repo_root="$(git rev-parse --show-toplevel)"
declare -r repo_root
cd "${repo_root}"

source scripts/util/changelog.sh

# TODO(roycaihw): make the script send a PR by default (standalone mode), and
# have an option to make the script reusable by other release automations.
TARGET_RELEASE=${TARGET_RELEASE:-"v$(grep "^CLIENT_VERSION = \"" scripts/constants.py | sed "s/CLIENT_VERSION = \"//g" | sed "s/\"//g")"}
SUBMODULE_SECTION=${SUBMODULE_SECTION:-"\*\*Submodule Change:\*\*"}

# update submodule
git submodule update --remote
pulls=$(git diff --submodule | egrep -o "^  > Merge pull request #[0-9]+" | sed 's/  > Merge pull request #//g')

# download release notes
release_notes=""
submodule_repo="kubernetes-client/python-base"
echo "Downloading release notes from submodule repo."
for pull in ${pulls}; do
  pull_url="https://github.com/$submodule_repo/pull/${pull}"
  echo "+++ Downloading python-base patch to /tmp/${pull}.patch"
  curl -o "/tmp/${pull}.patch" -sSL "${pull_url}.patch"
  subject=$(grep -m 1 "^Subject" "/tmp/${pull}.patch" | sed -e 's/Subject: \[PATCH//g' | sed 's/.*] //')
  pull_uid="$submodule_repo#${pull}"
  release_note="- ${subject} [${pull_uid}](${pull_url})\n"
  release_notes+=${release_note}
  # remove the patch file from /tmp
  rm -f "/tmp/${pull}.patch"
done

# find the place in the changelog that we want to edit
line_to_edit="1"
if util::changelog::has_release $TARGET_RELEASE; then
  # the target release exists
  release_first_line=$(util::changelog::find_release_start $TARGET_RELEASE)
  release_last_line=$(util::changelog::find_release_end $TARGET_RELEASE)
  if util::changelog::has_section_in_range "$SUBMODULE_SECTION" "$release_first_line" "$release_last_line"; then
    # prepend to existing section
    line_to_edit=$(($(util::changelog::find_section_in_range "$SUBMODULE_SECTION" "$release_first_line" "$release_last_line")+1))
    release_notes=${release_notes::-2}
  else
    # add a new section
    line_to_edit=$(($(util::changelog::find_release_start $TARGET_RELEASE)+4))
    release_notes="$SUBMODULE_SECTION\n$release_notes"
  fi
else
  # add a new release
  # TODO(roycaihw): ideally a parent script updates the generated client and
  # fills in the Kubernetes API Version based on the OpenAPI spec.
  release_notes="# $TARGET_RELEASE\n\nKubernetes API Version: TBD\n\n$SUBMODULE_SECTION\n$release_notes"
fi

echo "Writing the following release notes to CHANGELOG line $line_to_edit:"
echo -e $release_notes

# update changelog
sed -i "${line_to_edit}i${release_notes}" CHANGELOG.md

echo "Successfully updated CHANGELOG for submodule."
