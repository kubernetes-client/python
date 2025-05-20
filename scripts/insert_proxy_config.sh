#!/usr/bin/env bash
# insert_proxy_config.sh - run this after openapi-generator release.sh
CONFIG_PATH="../python_kubernetes/kubernetes/client"

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

# --- Step 2: Insert proxy & no_proxy environment code (idempotent) ---
if ! grep -q 'os.getenv("HTTPS_PROXY"' "$CONFIG_FILE"; then
  LINE=$(grep -n "self.proxy = None" "$CONFIG_FILE" | cut -d: -f1)
  if [ -n "$LINE" ]; then
    INDENT=$(sed -n "${LINE}s/^\( *\).*/\1/p" "$CONFIG_FILE")

    # Build the insertion block with correct indentation
    
    BLOCK+="${INDENT}# Load proxy from environment variables (if set)\n"
    BLOCK+="${INDENT}if os.getenv(\"HTTPS_PROXY\"): self.proxy = os.getenv(\"HTTPS_PROXY\")\n"
    BLOCK+="${INDENT}if os.getenv(\"https_proxy\"): self.proxy = os.getenv(\"https_proxy\")\n"
    BLOCK+="${INDENT}if os.getenv(\"HTTP_PROXY\"): self.proxy = os.getenv(\"HTTP_PROXY\")\n"
    BLOCK+="${INDENT}if os.getenv(\"http_proxy\"): self.proxy = os.getenv(\"http_proxy\")\n"
    BLOCK+="${INDENT}self.no_proxy = None\n"
    BLOCK+="${INDENT}# Load no_proxy from environment variables (if set)\n"
    BLOCK+="${INDENT}if os.getenv(\"NO_PROXY\"): self.no_proxy = os.getenv(\"NO_PROXY\")\n"
    BLOCK+="${INDENT}if os.getenv(\"no_proxy\"): self.no_proxy = os.getenv(\"no_proxy\")"

    # Insert the block after the proxy default line
    sed -i "${LINE}a $BLOCK" "$CONFIG_FILE"
    echo "Proxy and no_proxy environment code inserted into $CONFIG_FILE."
  else
    echo "Warning: 'self.proxy = None' not found in $CONFIG_FILE. No proxy code inserted."
  fi
else
  echo "Proxy environment code already present; no changes made."
fi