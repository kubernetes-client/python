#!/usr/bin/env bash
# add_patch_import.sh - Ensure monkey-patch loader is added to client/__init__.py

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null
CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes"
CONFIG_PATH="$CLIENT_ROOT/client"
CONFIG_FILE="$CONFIG_PATH/__init__.py"
# Normalize Windows-style backslashes to Unix-style forward slashes
CONFIG_FILE="$(echo "$CONFIG_FILE" | sed 's|\\|/|g')"

# Ensure file exists
if [ ! -f "$CONFIG_FILE" ]; then
  echo "Error: $CONFIG_FILE does not exist." >&2
  exit 1
fi

PATCH_SNIPPET='try:
    import kubernetes.client.helpers.patch as _patch
    _patch.apply_patch()
except ImportError:
    pass'

# Check if snippet already exists
if grep -q "your_project.k8s_helpers.patch" "$CONFIG_FILE"; then
  echo "Patch snippet already present in $CONFIG_FILE, skipping."
else
  echo "" >> "$CONFIG_FILE"
  echo "$PATCH_SNIPPET" >> "$CONFIG_FILE"
  echo "Patch snippet added to $CONFIG_FILE."
fi
