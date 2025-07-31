#!/usr/bin/env python3
"""
Windows Development Setup Script for Kubernetes Python Client

This script helps Windows developers set up the repository by handling
symlink directories that don't work properly on Windows.
"""

import os
import shutil
import sys
import subprocess

def is_windows():
    return sys.platform.startswith('win')

def setup_windows_directories():
    """Replace symlink directories with actual directories for Windows development."""
    if not is_windows():
        print("This script is only needed on Windows systems.")
        return
    
    symlink_dirs = [
        ('kubernetes/config', 'kubernetes/base/config'),
        ('kubernetes/watch', 'kubernetes/base/watch')
    ]
    
    for symlink_path, target_path in symlink_dirs:
        if os.path.exists(symlink_path):
            # Check if it's a symlink or text file (broken symlink on Windows)
            if os.path.isfile(symlink_path):
                print(f"Removing broken symlink file: {symlink_path}")
                os.remove(symlink_path)
            elif os.path.islink(symlink_path):
                print(f"Removing symlink: {symlink_path}")
                os.unlink(symlink_path)
        
        if os.path.exists(target_path):
            print(f"Creating directory copy: {symlink_path} -> {target_path}")
            shutil.copytree(target_path, symlink_path)
        else:
            print(f"Warning: Target directory not found: {target_path}")

def main():
    print("Setting up Kubernetes Python Client for Windows development...")
    setup_windows_directories()
    print("Setup complete! You can now run 'pip install -e .' and tests.")

if __name__ == "__main__":
    main()
