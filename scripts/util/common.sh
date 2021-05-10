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

# check_sed returns an error and suggests installing GNU sed, if OS X sed is
# detected.
function util::common::check_sed {
  # OS X sed doesn't support "--version". This way we can tell if OS X sed is
  # used.
  if ! sed --version &>/dev/null; then
    # OS X sed and GNU sed aren't compatible with backup flag "-i". Namely
    # sed -i ... - does not work on OS X
    # sed -i'' ... - does not work on certain OS X versions
    # sed -i '' ... - does not work on GNU
    echo ">>> OS X sed detected, which may be incompatible with this script. Please install and use GNU sed instead:
    $ brew install gnu-sed
    $ brew info gnu-sed
    # Find the path to the installed gnu-sed and add it to your PATH. The default
    # is:
    #   PATH=\"/Users/\$USER/homebrew/opt/gnu-sed/libexec/gnubin:\$PATH\""
    exit 1
  fi
}
