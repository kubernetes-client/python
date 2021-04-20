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

# has_section returns if the given section exists between start and end
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

# find_section returns the number of the first line of the given section
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
