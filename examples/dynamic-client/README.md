# Kubernetes Dynamic Client Examples

This directory contains examples demonstrating how to use the Kubernetes **Dynamic Client** (`kubernetes.dynamic.DynamicClient`).

Unlike the statically typed client (`CoreV1Api`, `AppsV1Api`), the dynamic client discovers resource definitions (APIs and schemas) dynamically at runtime from the Kubernetes API server. This makes it ideal for:
- Interacting with **Custom Resource Definitions (CRDs)** without generating code or static model classes.
- Working with resources whose schemas vary across cluster versions.
- Writing generic controllers, operators, or CLI utilities that consume arbitrary YAML/JSON manifests.

## Setup & Prerequisites

These scripts require Python 3.10+ and the `kubernetes` Python package. Ensure your local `kubeconfig` (`~/.kube/config`) points to an accessible cluster (e.g. `minikube`, `kind`, or a remote cluster):

```bash
pip install kubernetes
```

## Running an Example

Run any example from the root of the repository:

```bash
python examples/dynamic-client/configmap.py
```

## Available Examples

### Core & Workload Resources

- [configmap.py](configmap.py) — Create, list, patch (update), and delete a `ConfigMap` using dynamic manifests.
- [deployment_rolling_restart.py](deployment_rolling_restart.py) — Create a `Deployment`, trigger a zero-downtime rolling restart by updating `kubectl.kubernetes.io/restartedAt` annotations, and delete the deployment.
- [service.py](service.py) — Lifecycle management for a Kubernetes `Service` (create, list, patch, delete).
- [node.py](node.py) — Discover and list cluster `Node` resources dynamically.
- [replication_controller.py](replication_controller.py) — Create, list, and delete namespaced `ReplicationController` resources.

### Custom Resources & CRDs

- [namespaced_custom_resource.py](namespaced_custom_resource.py) — Define a namespaced CustomResourceDefinition (`CRD`), instantiate Custom Resources (`CRs`), list, patch, and clean up.
- [cluster_scoped_custom_resource.py](cluster_scoped_custom_resource.py) — Define a cluster-scoped `CRD`, create cluster-level `CRs`, list, patch, and delete resources and definitions.

### Client Tuning & Headers

- [request_timeout.py](request_timeout.py) — Configure client-side timeouts (`_request_timeout` parameter in seconds) on dynamic client operations to prevent stalled connections.
- [accept_header.py](accept_header.py) — Pass custom `Accept` HTTP headers (such as `application/json;as=Table;v=v1`) to retrieve raw tabular data directly from the API server.

## Related Documentation

- [Dynamic Client Documentation](https://github.com/kubernetes-client/python/blob/master/kubernetes/dynamic/README.md)
- [General Client Examples](../README.md)
