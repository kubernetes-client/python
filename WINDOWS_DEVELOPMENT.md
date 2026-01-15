# Windows Development Guide

This repository historically used Unix symbolic links inside the `kubernetes` package (e.g. `kubernetes/config` -> `kubernetes/base/config`). Windows clones without Developer Mode or elevated privileges could not create these links, breaking imports.

## What Changed

Shim Python modules replaced symlink placeholders (`config`, `dynamic`, `watch`, `stream`, `leaderelection`). They re-export from `kubernetes.base.*` so public APIs remain the same and no filesystem symlink is required.

## Getting Started

1. Ensure Python 3.9+ is installed and on PATH.
2. (Optional) Create virtual environment:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install requirements:

   ```powershell
   pip install -r requirements.txt -r test-requirements.txt
   ```

4. Run a quick import smoke test:

   ```powershell
   python - <<'PY'
   from kubernetes import config, watch, dynamic, stream, leaderelection
   print('Imported packages OK')
   PY
   ```

## Running Tests on Windows

`tox` can run most tests; some network / streaming tests are flaky under Windows due to timing. Recommended:

```powershell
pip install tox
tox -e py
```

If you see intermittent websocket or watch hangs, re-run that specific test module with pytest's `-k` to isolate.

## Permission Semantics

Windows has different file permission behavior than POSIX; tests expecting strict mode bits may fail. Adjust or skip such tests with `pytest.mark.skipif(sys.platform.startswith('win'), ...)` when encountered (none required yet after shims).

## Streaming / WebSocket Notes

If exec/port-forward tests hang:

- Ensure firewall allows local loopback connections.
- Set `PYTHONUNBUFFERED=1` to improve real-time logs.

## Troubleshooting

| Symptom | Fix |
| ------- | --- |
| `ModuleNotFoundError` for subpackages | Ensure shim files exist and you installed the package in editable mode `pip install -e .` |
| Watch stream stalls | Use smaller `timeout_seconds` and retry; Windows networking latency differs |
| PermissionError deleting temp files | Close file handles; Windows locks open files |

## Regenerating Client (Optional)

Regeneration scripts in `scripts/` assume a Unix-like environment. Use WSL2 or a Linux container when running `update-client.sh`.

## Contributing Windows Fixes

1. Create branch
2. Add / adjust tests using `sys.platform` guards
3. Run `ruff` or `flake8` (if adopted) and `tox`
4. Open PR referencing related issue (e.g. #2427 #2428)

---

Maintainers: Please keep this doc updated as additional Windows-specific adjustments are made.
