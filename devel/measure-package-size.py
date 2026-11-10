#!/usr/bin/env python3
# Copyright 2026 The Kubernetes Authors.
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

"""Measure release wheel sizes without installing it or its dependencies.

Run with a Python environment containing setuptools and wheel. Pass the same
interpreter and separate clean checkouts to compare revisions. Sizes count
file contents, not filesystem allocation; bytecode uses optimization level 0.
"""

import argparse
import compileall
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile


def measure(root):
    with tempfile.TemporaryDirectory(prefix="kubernetes-size-") as tmp:
        temp = Path(tmp)
        result = subprocess.run(
            [sys.executable, "setup-release.py", "bdist_wheel",
             "--dist-dir", str(temp / "dist"),
             "--bdist-dir", str(temp / "build")],
            cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True,
        )
        if result.returncode:
            sys.stderr.write(result.stdout)
            result.check_returncode()
        wheel = next((temp / "dist").glob("*.whl"))
        installed = temp / "installed"
        with zipfile.ZipFile(wheel) as archive:
            archive.extractall(installed)
            source_bytes = sum(
                entry.file_size for entry in archive.infolist()
                if entry.filename.endswith(".py")
            )
            installed_bytes = sum(
                entry.file_size for entry in archive.infolist()
            )
        if not compileall.compile_dir(
            installed, quiet=2, force=True, stripdir=str(installed), optimize=0,
        ):
            raise RuntimeError("Wheel bytecode compilation failed")
        bytecode_bytes = sum(
            path.stat().st_size for path in installed.rglob("*.pyc")
        )
        return {
            "python": sys.version.split()[0],
            "source_bytes": source_bytes,
            "wheel_bytes": wheel.stat().st_size,
            "installed_no_compile_bytes": installed_bytes,
            "bytecode_bytes": bytecode_bytes,
            "installed_with_bytecode_bytes": installed_bytes + bytecode_bytes,
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="Client repository root")
    args = parser.parse_args()
    print(json.dumps(measure(args.checkout.resolve()), indent=2))
