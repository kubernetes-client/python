# Kubernetes Watch Examples

This directory contains examples demonstrating how to watch Kubernetes resources and handle real-time event streams using the Python client.

Kubernetes Watch provides a streaming HTTP connection that emits events (`ADDED`, `MODIFIED`, `DELETED`, `BOOKMARK`, and `ERROR`) as resources change in the cluster, eliminating the need for periodic polling.

## Setup & Prerequisites

These scripts require Python 3.10+ and the `kubernetes` Python package. Ensure your local `kubeconfig` (`~/.kube/config`) points to an accessible cluster:

```bash
pip install kubernetes
```

## Running an Example

Run any example from the root of the repository:

```bash
python examples/watch/pod_namespace_watch.py
```

## Available Examples & Guides

### Example Scripts

- [pod_namespace_watch.py](pod_namespace_watch.py) — Demonstrates basic resource watching with `CoreV1Api` and `kubernetes.watch.Watch`. Shows how to stream namespace and pod events, process event types and metadata, terminate the watch cleanly using `w.stop()`, and set server-side timeouts via `timeout_seconds`.
- [watch_recovery.py](watch_recovery.py) — Demonstrates resilient, fault-tolerant watching using `DynamicClient`. Illustrates bookmark support (`allow_watch_bookmarks=True`), tracking `resourceVersion` across reconnects, handling HTTP 410 (`ApiException` status 410 when a resource version expires in etcd), and recovering from network drops (`urllib3.exceptions.ProtocolError`).

### Configuration & Deep Dive Guides

- [timeout-settings.md](timeout-settings.md) — Comprehensive reference explaining the critical differences between server-side (`timeout_seconds`) and client-side (`_request_timeout`) timeouts, socket-level behavior during network partition or outages, and recommended timeout values for production watchers.

## Key Patterns & Best Practices

1. **Tracking `resourceVersion`:**
   Always record the latest `resourceVersion` from received events or bookmarks. When reconnecting after a network drop, pass `resource_version` to resume streaming without missing events or re-processing the entire cluster state.

2. **Enabling Bookmarks:**
   Set `allow_watch_bookmarks=True` so the API server sends periodic bookmark events containing the latest resource version even when no matching resources have changed. This prevents your recorded `resourceVersion` from becoming stale.

3. **Handling HTTP 410 (Gone):**
   When a watch stream encounters an HTTP 410 error, the recorded resource version has expired from the API server's history window. Catch `ApiException` with status 410, reset `resource_version = None` (or re-list the resource), and restart the watch.

4. **Socket & Connection Cleanup:**
   Always call `w.stop()` when exiting watch loops early to ensure underlying HTTP response connections and sockets are properly closed and returned to the connection pool.

## Related Documentation

- [Kubernetes Efficient Detection of Changes](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)
- [General Client Examples](../README.md)
