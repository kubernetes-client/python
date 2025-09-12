#!/usr/bin/env bash
# insert_proxy_config.sh - run this after openapi-generator release.sh
SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null
CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes"
CONFIG_PATH="$CLIENT_ROOT/client"

# Compute the full file path
CONFIG_FILE="$CONFIG_PATH/configuration.py"

# --- Normalize Windows-style backslashes to Unix forward slashes ---
CONFIG_FILE="$(echo "$CONFIG_FILE" | sed 's|\\|/|g')"

# --- Ensure the target file exists and is writable ---
if [ ! -f "$CONFIG_FILE" ] || [ ! -w "$CONFIG_FILE" ]; then
  echo "Error: $CONFIG_FILE does not exist or is not writable." >&2
  exit 1
fi

# --- Step 1: Ensure 'import os' follows existing imports (idempotent) ---
if ! grep -qE '^import os$' "$CONFIG_FILE"; then
  LAST_IMPORT=$(grep -nE '^(import |from )' "$CONFIG_FILE" | tail -n1 | cut -d: -f1)
  if [ -n "$LAST_IMPORT" ]; then
    sed -i "$((LAST_IMPORT+1))i import os" "$CONFIG_FILE"
  else
    if head -n1 "$CONFIG_FILE" | grep -q '^#!'; then
      sed -i '2i import os' "$CONFIG_FILE"
    else
      sed -i '1i import os' "$CONFIG_FILE"
    fi
  fi
  echo "Inserted 'import os' after existing imports in $CONFIG_FILE."
else
  echo "'import os' already present; no changes made."
fi

# --- Step 2: Insert proxy & no_proxy environment code ---
if ! grep -q 'os.getenv("HTTPS_PROXY"' "$CONFIG_FILE"; then
  PROXY_LINE=$(grep -n "self.proxy = None" "$CONFIG_FILE" | cut -d: -f1)
  NO_PROXY_LINE=$(grep -n "^[[:space:]]*self\.no_proxy[[:space:]]*=[[:space:]]*None" "$CONFIG_FILE" | cut -d: -f1)

  if [ -n "$PROXY_LINE" ]; then
    INDENT=$(sed -n "${PROXY_LINE}s/^\( *\).*/\1/p" "$CONFIG_FILE")

    BLOCK=""

    if [ -z "$NO_PROXY_LINE" ]; then
      # self.no_proxy = None is not present → insert full block after self.proxy = None
      BLOCK+="${INDENT}# Load proxy from environment variables (if set)\n"
      BLOCK+="${INDENT}if os.getenv(\"HTTPS_PROXY\"): self.proxy = os.getenv(\"HTTPS_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"https_proxy\"): self.proxy = os.getenv(\"https_proxy\")\n"
      BLOCK+="${INDENT}if os.getenv(\"HTTP_PROXY\"): self.proxy = os.getenv(\"HTTP_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"http_proxy\"): self.proxy = os.getenv(\"http_proxy\")\n"
      BLOCK+="${INDENT}self.no_proxy = None\n"
      BLOCK+="${INDENT}# Load no_proxy from environment variables (if set)\n"
      BLOCK+="${INDENT}if os.getenv(\"NO_PROXY\"): self.no_proxy = os.getenv(\"NO_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"no_proxy\"): self.no_proxy = os.getenv(\"no_proxy\")"

      sed -i "${PROXY_LINE}a $BLOCK" "$CONFIG_FILE"
      echo "Inserted full proxy + no_proxy block after 'self.proxy = None'."
    else
      # self.no_proxy = None exists → insert only env logic after that
      BLOCK+="${INDENT}# Load proxy from environment variables (if set)\n"
      BLOCK+="${INDENT}if os.getenv(\"HTTPS_PROXY\"): self.proxy = os.getenv(\"HTTPS_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"https_proxy\"): self.proxy = os.getenv(\"https_proxy\")\n"
      BLOCK+="${INDENT}if os.getenv(\"HTTP_PROXY\"): self.proxy = os.getenv(\"HTTP_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"http_proxy\"): self.proxy = os.getenv(\"http_proxy\")\n"
      BLOCK+="${INDENT}# Load no_proxy from environment variables (if set)\n"
      BLOCK+="${INDENT}if os.getenv(\"NO_PROXY\"): self.no_proxy = os.getenv(\"NO_PROXY\")\n"
      BLOCK+="${INDENT}if os.getenv(\"no_proxy\"): self.no_proxy = os.getenv(\"no_proxy\")"

      sed -i "${NO_PROXY_LINE}a $BLOCK" "$CONFIG_FILE"
      echo "Inserted environment block after 'self.no_proxy = None'."
    fi
  else
    echo "Warning: 'self.proxy = None' not found in $CONFIG_FILE. No proxy code inserted."
  fi
else
  echo "Proxy environment code already present; no changes made."
fi