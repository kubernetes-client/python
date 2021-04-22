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


# Utilities for parsing/writing the Python client's changelog.

changelog="$(git rev-parse --show-toplevel)/CHANGELOG.md"

function util::changelog::has_release {
  local release=$1
  return $(grep -q "^# $release$" $changelog)
}

# find_release_start returns the number of the first line of the given release
function util::changelog::find_release_start {
  local release=$1
  echo $(grep -n "^# $release$" $changelog | head -1 | cut -d: -f1)
}

# find_release_end returns the number of the last line of the given release
function util::changelog::find_release_end {
  local release=$1

  local release_start=$(util::changelog::find_release_start $release)
  local next_release_index=0
  local releases=($(grep -n "^# " $changelog | cut -d: -f1))
  for i in "${!releases[@]}"; do
     if [[ "${releases[$i]}" = "$release_start" ]]; then
       next_release_index=$((i+1))
       break
     fi
  done
  # return the line before the next release
  echo $((${releases[${next_release_index}]}-1))
}

# has_section_in_range returns if the given section exists between start and end
function util::changelog::has_section_in_range {
  local section="$1"
  local start=$2
  local end=$3

  local lines=($(grep -n "$section" "$changelog" | cut -d: -f1))
  for i in "${!lines[@]}"; do
    if [[ ${lines[$i]} -ge $start && ${lines[$i]} -le $end ]]; then
      return 0
    fi
  done
  return 1
}

# find_section_in_range returns the number of the first line of the given section
function util::changelog::find_section_in_range {
  local section="$1"
  local start=$2
  local end=$3

  local line="0"
  local lines=($(grep -n "$section" "$changelog" | cut -d: -f1))
  for i in "${!lines[@]}"; do
    if [[ ${lines[$i]} -ge $start && ${lines[$i]} -le $end ]]; then
      line=${lines[$i]}
      break
    fi
  done
  echo $line
}

# write_changelog writes release_notes to section in target_release
function util::changelog::write_changelog {
  local target_release="$1"
  local section="$2"
  local release_notes="$3"

  # find the place in the changelog that we want to edit
  local line_to_edit="1"
  if util::changelog::has_release $target_release; then
    # the target release exists
    release_first_line=$(util::changelog::find_release_start $target_release)
    release_last_line=$(util::changelog::find_release_end $target_release)
    if util::changelog::has_section_in_range "$section" "$release_first_line" "$release_last_line"; then
      # prepend to existing section
      line_to_edit=$(($(util::changelog::find_section_in_range "$section" "$release_first_line" "$release_last_line")+1))
    else
      # add a new section; plus 4 so that the section is placed below "Kubernetes API Version"
      line_to_edit=$(($(util::changelog::find_release_start $target_release)+4))
      release_notes="$section\n$release_notes\n"
    fi
  else
    # add a new release
    release_notes="# $target_release\n\nKubernetes API Version: To Be Updated\n\n$section\n$release_notes\n"
  fi

  echo "Writing the following release notes to CHANGELOG line $line_to_edit:"
  echo -e $release_notes

  # update changelog
  sed -i "${line_to_edit}i${release_notes}" $changelog
}

# get_api_version returns the Kubernetes API Version for the given client
# version in the changelog.
function util::changelog::get_k8s_api_version {
  local client_version="$1"

  local api_version_section="Kubernetes API Version: "
  # by default, find the first API version in the first 100 lines if the given
  # client version isn't found
  local start=0
  local end=100
  if util::changelog::has_release "$client_version"; then
    start=$(util::changelog::find_release_start "$client_version")
    end=$(util::changelog::find_release_end "$client_version")
  fi
  if ! util::changelog::has_section_in_range "$api_version_section" "$start" "$end"; then
    echo "error: api version for release $client_version not found"
    exit 1
  fi

  local api_version_line=$(util::changelog::find_section_in_range "$api_version_section" "$start" "$end")
  echo $(sed -n ${api_version_line}p $changelog | sed "s/$api_version_section//g")
}

function util::changelog::update_release_api_version {
  local release="$1"
  local old_release="$2"
  local k8s_api_version="$3"

  echo "New release: $release"
  echo "Old release: $old_release"

  if ! util::changelog::has_release v$old_release; then
    sed -i "1i# v$release\n\nKubernetes API Version: $k8s_api_version\n\n" $changelog
    return 0
  fi
  start=$(util::changelog::find_release_start v$old_release)
  sed -i "${start}s/# v$old_release/# v$release/" $changelog
  echo "$start"
  echo "$((${start}+2))"
  sed -i "$((${start}+2))s/^Kubernetes API Version: .*$/Kubernetes API Version: $k8s_api_version/" $changelog
}
